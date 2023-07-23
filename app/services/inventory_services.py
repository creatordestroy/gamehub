from app.models.inventory import Inventory

class InventoryService:
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

    def get_all_product_ratings():
        try:
            products = Inventory.select(Inventory.product_rating)

            if products:
                product_data = [{
                    'product_id' : product.product_id,
                    'name' : product.product_name,
                    'rating' : str(product.product_rating),
                    'review' : product.product_review
                } for product in products]
                return {'message' : 'Successfully returned product ratings', 'product_data' : product_data}, 200
            else:
                return {'message': 'Error finding product ratings'}, 404

        except Exception as e:
            return {'error': str(e)}, 500

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

