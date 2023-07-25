from flask import Flask, render_template, url_for
#from app.middlewares import JSONContentTypeMiddleware

from app.routes import inventory, product, returns, reviews, sales, shipment, user, productOrder


def create_app():
    app = Flask(__name__, template_folder='app/templates')

    # Register blueprints alpabetically
    app.register_blueprint(inventory.bp, url_prefix='/inventory')
    app.register_blueprint(product.bp, url_prefix='/product')
    app.register_blueprint(productOrder.bp, url_prefix='/orders')
    app.register_blueprint(returns.bp, url_prefix='/returns')
    app.register_blueprint(reviews.bp, url_prefix='/reviews')
    app.register_blueprint(shipment.bp, url_prefix='/shipments')
    app.register_blueprint(sales.bp, url_prefix='/sales')



    # Default route
    @app.route("/")
    def index():
        links = {
            "Inventory": url_for('inventory.inventory_list'),
            "Orders" : url_for('productOrder.order_list'),
            "Product": url_for('product.product_list'),
            "Returns": url_for('returns.returns_list'),
            "Reviews": url_for('reviews.review_list'),
            "Shipments": url_for('shipment.shipment_list'),
            "Sales": url_for('sales.sales_list')
        }
        return render_template("index.html", links=links, is_index_page=True)
    return app

app = create_app()

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)