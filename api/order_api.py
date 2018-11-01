import config as conf
from flask import *
from modules import Order
from twilio.rest import Client

order_api = Blueprint('about', __name__)

twilio_client = Client(conf.twilio_sid, conf.twilio_auth_token)

DELIVERER_CONFIRMATION = 'Your customer has been notified.'


@order_api.route('/order', methods=['POST'])
def order_api_route():
    """Receive user order and forward to deliverer."""
    order = Order(request.get_json())
    # Deliverer must respond with customer phone number in order to properly
    # notify customer of deliverer contact info.
    body = f'{order}\n' \
           f'Please respond with the customer number beginning with +1'

    msg = twilio_client.messages.create(
        to=conf.NUMBER_BY_NAME['Jonah'],
        from_=conf.TWILIO_NUMBER,
        body=body)

    return msg.sid


@order_api.route('/sms', methods=['POST'])
def confirm_deliverer():
    """
    Receive response message from deliverer and notify customer of
    deliverer contact info.
    """
    deliverer_number = request.form['From']
    customer_number = request.form['Body']
    body = f'Your order has been received ' \
           f'by {conf.NAME_BY_NUMBER[deliverer_number]}, ' \
           f'who can be reached at {deliverer_number}'

    # Send customer message containing deliverer contact info.
    twilio_client.messages.create(
        to=customer_number,
        from_=conf.TWILIO_NUMBER,
        body=body)

    return DELIVERER_CONFIRMATION
