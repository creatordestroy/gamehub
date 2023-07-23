from app.models.shipments import Shipments
from app.services.inventory_services import InventoryService

class ShipmentService:
    def receive_shipment(self, product_id, store_id, shipment_quantity, shipment_date):
        # Create a row for shipments table
        quantity_shipped = int(shipment_quantity)
        shipment = Shipments(product_id=product_id, shipment_date=shipment_date, quantity_shipped=quantity_shipped, store_id=store_id)
        shipment.save()

        # Check if the product exists in the inventory
        inventory = InventoryService().get_inventory(product_id, store_id)

        if inventory is None:
            # Create a row for inventory table
            inventory = InventoryService().create_inventory(product_id=product_id, store_id=store_id, product_quantity=shipment_quantity)
        else:
            # Update the inventory table quantity
            inventory = InventoryService().update_product_quantity(product_id, store_id, shipment_quantity)

        return shipment