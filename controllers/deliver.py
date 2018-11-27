from flask import *
import config
import requests

deliver = Blueprint('deliver', __name__, template_folder='templates')


@deliver.route('/deliver', methods=['GET'])
def deliver_route():
    """Render deliverer landing page."""
    return render_template('deliver.html')


def register_deliverer(request_form):
    """Register deliverer for given coffee shop."""
    register_url = config.api_base_url + '/api/deliver/register'
    r = requests.post(register_url, json=request_form)

    options = {
        'admin_message': 'You have successfully been registered.'
    }

    return render_template('register.html', **options)


@deliver.route('/deliver/register', methods=['GET', 'POST'])
def deliver_register_route():
    """Render deliver registration page."""
    if request.method == 'POST':
        return register_deliverer(request.form)

    options = {
        'admin_message': 'Enter your information and the coffee shop you are'
                         ' delivering from.'
    }

    return render_template('register.html', **options)


def deregister_deliverer(request_form):
    """Deregister deliverer."""
    deregister_url = config.api_base_url + '/api/deliver/deregister'
    options = {
        'admin_message': 'You have successfully been deregistered.'
    }

    resp = requests.post(deregister_url, json=request_form).json()
    return render_template('deregister.html', **options)


@deliver.route('/deliver/deregister', methods=['GET', 'POST'])
def deliver_deregister_route():
    """Render deliverer deregistration page."""

    if request.method == 'POST':
        return deregister_deliverer(request.form)

    options = {
        'admin_message': 'Enter your information in order to deregister.'
    }

    return render_template('deregister.html', **options)
