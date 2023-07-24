from app.models.inventory import Inventory
from app.models.product import Product
from app.models.storeLocation import StoreLocation
from app.models.productOrders import ProductOrders
from flask import jsonify
from app.database import db
from datetime import date

class OrderServices:

    def get_order(self):
        return ProductOrders.select()

    def add_order(self,product_id, store_id,order_status,order_date,order_quantity):

        order = ProductOrders(product_id=product_id,store_id=store_id,order_status=order_status,order_date=order_date,order_quantity=order_quantity)
        order.save()

    def auto_order(store_id):

        products_to_order = Product.select().join(Inventory).where((Inventory.store_id == store_id) & (Inventory.product_quantity < Product.threshold))

    # Add the products to the ProductOrders table with order_quantity set to the difference between the threshold and current quantity
        for product in products_to_order:
            order_date = date.today().strftime("%Y-%m-%d")
            order_status = 'processing'
            order_quantity = product.threshold - Inventory.get((Inventory.store_id == store_id) & (Inventory.product_id == product.product_id)).product_quantity
            ProductOrders.create(product_id=product.product_id, store_id=store_id, order_quantity=order_quantity, order_status=order_status, order_date=order_date)


        