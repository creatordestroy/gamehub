from app.models.inventory import Inventory
from app.models.product import Product
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

    def product_search_by_name(product_name):
        try:
            product_id = Product.get(Product.product_name == product_name).product_id
            product_status = Inventory.select().where(Inventory.product_id == product_id)

            if product_status:
                product_details = [info.__data__ for info in product_status]

                return product_details, 200
            else:
                return {'message' : 'No product found'}, 404
            
        except Exception as e:
            return {'error': str(e)}, 500
        
    def product_search_by_id():
        pass

    def product_search_by_id_in_store():
        pass
        
        
