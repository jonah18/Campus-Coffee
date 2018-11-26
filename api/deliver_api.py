from flask import *
import config
from modules import Deliverer

deliver_api = Blueprint('deliver_api', __name__)

REGISTER_CONFIRMATION = 'Deliverer Registered.'


@deliver_api.route('/api/deliver/register', methods=['POST'])
def deliver_api_register():
    """Register deliverer."""
    deliverer = Deliverer(request.get_json())

    with config.db_table.batch_writer() as batch:
        batch.put_item(
            Item={"Name": deliverer.name,
                  "PhoneNumber": deliverer.number,
                  "Shop": deliverer.shop})

    return REGISTER_CONFIRMATION
