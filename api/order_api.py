from flask import *
import config
from boto3.dynamodb.conditions import Key
import time
from modules import Order, Deliverer

order_api = Blueprint('order_api', __name__)

DELIVERER_CONFIRMATION = 'Your customer has been notified.'


@order_api.route('/api/order', methods=['POST'])
def order_api_route():
    """Receive user order and forward to deliverer."""
    order = Order(request.get_json())
    # Deliverer must respond with customer phone number in order to properly
    # notify customer of deliverer contact info.
    body = f'{order}\n' \
           f'Please respond with the customer\'s number'

    deliverer = retrieve_deliverer(order)

    if not deliverer:
        data = {'status': 'failure', 'message': 'no deliverers'}
        return jsonify(data)

    # Send order to deliverer
    config.twilio_client.messages.create(
        to=deliverer.number,
        from_=config.TWILIO_NUMBER,
        body=body)

    data = {'status': 'success', 'message': 'order placed'}
    return jsonify(data)


def retrieve_deliverer(order):
    """Retrieves appropriate deliverer based on order details."""

    # Wait for DB to backfill.
    while True:
        if not config.db_table.global_secondary_indexes or \
                config.db_table.global_secondary_indexes[0][
                    'IndexStatus'] != 'ACTIVE':
            print('Waiting for index to backfill...')
            time.sleep(5)
            config.db_table.reload()
        else:
            break

    resp = config.db_table.query(
        IndexName="ShopIndex",
        KeyConditionExpression=Key('Shop').eq(order.shop),
    )

    if len(resp['Items']) == 0:
        # No deliverers available from this shop.
        return None

    return Deliverer(resp['Items'][0])


@order_api.route('/sms', methods=['POST'])
def confirm_deliverer():
    """
    Receive response message from deliverer and notify customer of
    deliverer contact info.
    """
    deliverer_number = request.form['From']
    customer_number = request.form['Body']
    resp = config.db_table.get_item(
        Key={"PhoneNumber": deliverer_number})

    deliverer = Deliverer(resp)

    body = f'Your order has been received ' \
           f'by {deliverer.name}, ' \
           f'who can be reached at {deliverer.number}'

    # Send customer message containing deliverer contact info.
    config.twilio_client.messages.create(
        to=customer_number,
        from_=config.TWILIO_NUMBER,
        body=body)

    return DELIVERER_CONFIRMATION
