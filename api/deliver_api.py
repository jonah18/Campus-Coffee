from flask import *
import config
from modules import Deliverer
from botocore.exceptions import ClientError

deliver_api = Blueprint('deliver_api', __name__)


@deliver_api.route('/api/deliver/register', methods=['POST'])
def deliver_api_register():
    """Register deliverer."""
    deliverer = Deliverer(request.get_json())

    with config.db_table.batch_writer() as batch:
        batch.put_item(
            Item={"Name": deliverer.name,
                  "PhoneNumber": deliverer.number,
                  "Shop": deliverer.shop})

    data = {'status': 'success'}
    return jsonify(data)


@deliver_api.route('/api/deliver/deregister', methods=['POST'])
def deliver_api_deregister():
    """Deregister deliverer."""
    deliverer = Deliverer(request.get_json())

    try:
        config.db_table.delete_item(
            Key={"PhoneNumber": deliverer.number})
        data = {'status': 'success'}
    except ClientError:
        # Unable to delete deliverer
        data = {'status': 'failure'}

    return jsonify(data)
