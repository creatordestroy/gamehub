from app.models.inventory import Inventory
from app.models.product import Product
from flask import jsonify
from app.database import db

class InventoryService:
    def get_inventory_list(self):
        return Inventory.select()

    def create_inventory(self, product_id, store_id, product_quantity):
        inventory = Inventory(product_id=product_id, store_id=store_id, product_quantity=product_quantity)
        inventory.save()

    def add_inventory(self, product_id, product_name, product_cost, product_quantity):
        inventory = Inventory(product_id=product_id, product_name=product_name, product_cost=product_cost, product_quantity=product_quantity)
        inventory.save()

    def update_product_quantity(self, product_id, store_id, shipment_quantity):
        inventory = self.get_inventory(product_id, store_id)
        inventory.product_quantity += int(shipment_quantity)
        inventory.save()

    def get_inventory(self, product_id, store_id):
        inventory = Inventory().select().where(Inventory.product_id == product_id, Inventory.store_id == store_id).first()
        return inventory

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

    def product_search_by_id(product_id):
        try:
            product_name = Product.get(Product.product_id == product_id).product_name
            product_cost = Product.get(Product.product_id == product_id).product_cost
            product_status = Inventory.select().where(Inventory.product_id == product_id)

            if product_status:

                product_details = [{
                    'name' : product_name,
                    'store' : product.store_id,
                    'id' : product.product_id,
                    'quantity' : product.product_quantity,
                    'cost' : product_cost
                } for product in product_status]

                return product_details, 200
            else:
                return {'message' : 'No product found'}, 404
        except Exception as e:
            return {'error' : str(e)}, 500

    def product_search_by_store_id(store_id):
        try:
            product_list = Inventory.select().where(Inventory.store_id == store_id)

            if product_list:

                product_details = [product.__data__ for product in product_list]

                return product_details, 200
            else:
                return [{'message' : 'No product found in store'}], 404
        except Exception as e:
            return {'error' : str(e)}, 500

    def product_search_by_id_in_store(product_id, store_id):
        try:

            product_list = Inventory.select().where((Inventory.product_id == product_id) & (Inventory.store_id == store_id))
            if product_list:

                product_details = [product.__data__ for product in product_list]

                return product_details, 200
            else:
                return [{'message' : 'No product found in store'}], 404
        except Exception as e:
            return {'error' : str(e)}, 500
