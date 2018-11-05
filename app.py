from flask import Flask
import api
import controllers

app = Flask(__name__, template_folder='templates')

app.register_blueprint(api.order_api)
app.register_blueprint(controllers.home)

if __name__ == '__main__':
    app.run(debug=True)
