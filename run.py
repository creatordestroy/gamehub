from flask import Flask, jsonify
#from app.middlewares import JSONContentTypeMiddleware
from app.database import db
from app.routes import inventory, reviews

def create_app():
    app = Flask(__name__)

    # Register blueprints

    app.register_blueprint(inventory.bp)
    app.register_blueprint(reviews.bp)

    # Default route
    @app.route("/")
    def index():
        return jsonify({"message": "Hello, world!"})

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
    
