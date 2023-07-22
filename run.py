from flask import Flask, jsonify, render_template
#from app.middlewares import JSONContentTypeMiddleware
from app.routes import inventory, user, shipment

def create_app():
    app = Flask(__name__, template_folder='app/templates')

    # Register blueprints
    app.register_blueprint(inventory.bp)
    app.register_blueprint(shipment.bp, url_prefix='/shipments')

    # Default route
    @app.route("/")
    def index():
        # return jsonify({"message": "Hello, world!"})
        return render_template("shipment.html")

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
