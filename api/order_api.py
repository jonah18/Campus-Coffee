from config import twilio_auth_token, twilio_sid, NUMBERS, TWILIO_NUMBER
from flask import *
from modules import Order
from twilio.rest import Client

order_api = Blueprint('about', __name__)

twilio_client = Client(twilio_sid, twilio_auth_token)


@order_api.route('/order', methods=['POST'])
def order_api_route():
    """Receive user order and forward to deliverer."""
    order = Order(request.get_json())
    msg = twilio_client.messages.create(
        to=NUMBERS[0],
        from_=TWILIO_NUMBER,
        body=str(order))

    return msg.sid
