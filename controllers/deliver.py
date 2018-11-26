from flask import *
import config
import requests

deliver = Blueprint('deliver', __name__, template_folder='templates')


@deliver.route('/deliver', methods=['GET', 'POST'])
def deliver_route():
    """Renders deliver page."""
    if request.method == 'POST':
        return register_deliverer(request.form)

    options = {
        'admin_message': 'Enter your information and the coffee shop you are'
                         ' delivering from.'
    }

    return render_template('deliver.html', **options)


def register_deliverer(request_form):
    """Register deliverer for given coffee shop."""
    register_url = config.api_base_url + '/api/deliver/register'
    r = requests.post(register_url, json=request_form)

    options = {
        'admin_message': 'You have successfully been registered.'
    }

    return render_template('deliver.html', **options)
