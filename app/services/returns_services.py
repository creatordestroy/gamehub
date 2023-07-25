from app.models.returns import Returns
from app.models.inventory import Inventory

class ReturnsService:
    def get_returns_list(self):
        return Returns.select()

    def create_returns(self, product_id, store_id, return_date, return_reason):
        return_quantity = 1

        returns = Returns(product_id=product_id, store_id=store_id, return_quantity=return_quantity, return_date=return_date, return_reason=return_reason)

        inventory = Inventory.get(Inventory.product_id == product_id, Inventory.store_id == store_id)

        inventory.product_quantity += return_quantity

        returns.save()
        inventory.save()

    def get_returns_by_id(self, return_id):
        try:
            return Returns.get(Returns.return_id == return_id)
        except Returns.DoesNotExist:
            return None