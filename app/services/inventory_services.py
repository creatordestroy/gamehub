from app.models.inventory import Inventory
from flask import jsonify
from app.database import db

class InventoryService:
    def add_inventory(product_id, product_name, product_cost, product_stock):
        inventory = Inventory(product_id=product_id, product_name=product_name, product_cost=product_cost, product_stock=product_stock)
        inventory.save()

    def update_product_stock(product_id, quantity):
        inventory = Inventory.get(Inventory.product_id == product_id)
        if quantity > 0:
            inventory.product_stock += quantity
        else:
            inventory.product_stock -= quantity
        inventory.save()

    def get_test_product():
        try:
            product = Inventory.select().first()

            if product:
                product_data = {
                    'product_id': product.product_id,
                    'name': product.product_name,
                    'cost': str(product.product_cost),
                    'stock': product.product_stock
                }
                return {'message': 'Successfully retrieved test product', 'product_data': product_data}, 200
            else:
                return {'message': 'No products found in the inventory'}, 404

        except Exception as e:
            return {'error': str(e)}, 500
        
