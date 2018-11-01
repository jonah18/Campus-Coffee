from flask import Flask
from config import env
import api

app = Flask(__name__)

app.register_blueprint(api.order_api)

if __name__ == '__main__':
    app.run(host=env['host'], port=env['port'], debug=True)
