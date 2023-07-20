from flask import Flask, jsonify
from app.middlewares import JSONContentTypeMiddleware
from app.routes import inventory, user

def create_app():
    app = Flask(__name__)

    app.wsgi_app = JSONContentTypeMiddleware(app.wsgi_app)
    # Register blueprints
    app.register_blueprint(inventory.bp)
    app.register_blueprint(user.bp)

    # Default route
    @app.route("/")
    def index():
        return jsonify({"message": "Hello, world!"})

    return app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
