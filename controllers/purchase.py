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
    order_url = config.api_base_url + '/api/order'
    options = {
        'admin_message': 'Your order has been made and you will '
                         'receive a confirmation text shortly.'
    }

    resp = requests.post(order_url, json=request_form).json()

    if resp['status'] == 'failure':
        options['admin_message'] = 'Sorry, there are no deliverers available' \
                                   'for this shop, please try again later.'

    return render_template('purchase.html', **options)
