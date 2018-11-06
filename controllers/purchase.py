from flask import *
import config
import requests

purchase = Blueprint('purchase', __name__, template_folder='templates')


@purchase.route('/purchase', methods=['GET', 'POST'])
def purchase_route():
    """Render purchase page.

    POST requests forward orders to Order API.
    """
    if request.method == 'POST':
        return send_order(request.form)
    return render_template('purchase.html')


def send_order(request_form):
    """Send order to Order API."""
    order_url = config.api_base_url + "/api/order"
    r = requests.post(order_url, json=request_form)

    options = {
        'admin_message': 'Your order has been made and you will '
                         'receive a confirmation text shortly.'
    }

    return render_template('purchase.html', **options)
