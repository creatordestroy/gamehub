from datetime import datetime
from app.models.shipments import Shipments

class ShipmentService:
    def receive_shipment(product_id, shipment_quantity):
        shipment_date = datetime.strptime(shipment_date, "%Y-%m-%d").date()
        shipment = Shipments(product_id=product_id, shipment_date=shipment_date, shipment_quantity=shipment_quantity)
        shipment.save()