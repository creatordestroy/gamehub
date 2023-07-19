from app.models.inventory import Inventory

class InventoryService:
    def add_inventory(title, platform, quantity):
        inventory = Inventory(title=title, platform=platform, quantity=quantity)
        inventory.save()

    def update_inventory(inventory_id, quantity):
        inventory = Inventory.get(Inventory.id == inventory_id)
        inventory.quantity += quantity
        inventory.save()

    def get_inventory(inventory_id):
        return Inventory.get(Inventory.id == inventory_id)

    def get_all_inventory():
        return Inventory.select()

    def get_low_stock_inventories(threshold):
        return Inventory.select().where(Inventory.quantity <= threshold)
