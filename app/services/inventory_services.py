from app.models.inventory import Inventory
from app.models.product import Product
from flask import jsonify
from app.database import db

class InventoryService:

    #Default method for returning all products in all inventories
    def get_inventory_list(self):
        return Inventory.select()

    #Creates an inventory product if one does not exist from outside inventory
    def create_inventory(self, product_id, store_id, product_quantity):
        inventory = Inventory(product_id=product_id, store_id=store_id, product_quantity=product_quantity)
        inventory.save()

    #Creates a new inventory product within inventory
    def add_inventory(self, product_id, store_id, product_cost, product_quantity):
        inventory = Inventory(product_id=product_id, store_id=store_id, product_cost=product_cost, product_quantity=product_quantity)
        inventory.save()

    #Updates quantity of a product in an inventory
    def update_product_quantity(self, product_id, store_id, shipment_quantity):
        inventory = self.get_inventory(product_id, store_id)
        inventory.product_quantity += int(shipment_quantity)
        inventory.save()

    #Gets the inventory of a specific store
    def get_inventory(self, product_id, store_id):
        inventory = Inventory().select().where(Inventory.product_id == product_id, Inventory.store_id == store_id).first()
        return inventory

    #searches all inventories by product name
    def search_by_product_name(product_name):
        try:
            product_id = Product.get(Product.product_name == product_name).product_id
            product_status = Inventory.select().where(Inventory.product_id == product_id)
            product_cost = Product.get(Product.product_id == product_id).product_cost
            
            if product_status:
                product_details = {
                    'details' : product_status,
                    'cost' : product_cost
                }
                return product_details
            else:
                return {'message' : 'No product found'}, 404

        except Exception as e:
            return {'error': str(e)}, 500

    #Searches all inventories by product id
    def search_by_product_id(product_id):
        try:
            product_status = Inventory.select().where(Inventory.product_id == product_id)
            product_cost = Product.get(Product.product_id == product_id).product_cost
            
            if product_status:
                product_details = {
                    'details' : product_status,
                    'cost' : product_cost
                }
                return product_details
            else:
                return {'message' : 'No product found'}, 404

        except Exception as e:
            return {'error': str(e)}, 500


    #Searches for a product by both product id and store id
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

