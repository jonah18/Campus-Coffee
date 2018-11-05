from flask import *
import config
import requests

home = Blueprint('home', __name__, template_folder='templates')


@home.route('/', methods=['GET'])
def home_route():
    """Render Campus Coffee home page."""
    return render_template('home.html')


@home.route('/send', methods=['POST'])
def send_order():
    """Receive order and send to Order API."""
    order_url = config.api_base_url + "/order"
    r = requests.post(order_url, json=request.form)

    return 'Your order has been made and you will receive a confirmation' \
           ' text shortly.'
