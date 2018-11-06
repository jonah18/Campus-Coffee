from flask import *
import api
import controllers

app = Flask(__name__, template_folder='templates')

app.register_blueprint(api.order_api)
app.register_blueprint(controllers.purchase)


@app.route('/')
def app_route():
    """Render Campus Coffee home page."""
    return render_template('purchase.html')


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
