from datetime import date
from flask import Blueprint, render_template, request, jsonify
from app.services.shipment_services import ShipmentService
from app.services.product_services import ProductService
from app.services.store_location_services import StoreLocationService

bp = Blueprint('shipment', __name__)

@bp.route('/receive/', methods=['GET', 'POST'])
def add_shipment():
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        shipment_date = date.today().strftime("%Y-%m-%d")
        shipment = ShipmentService().receive_shipment(data['product_id'], data['store_location'], data['shipment_quantity'], shipment_date)
        return "success", 201

    all_products = ProductService().get_product_list()
    all_store_locations = StoreLocationService().get_store_location_list()
    return render_template("shipment/add_shipment.html", products=all_products, store_locations=all_store_locations)

@bp.route('/list/', methods=['GET'])
def shipment_list():
    shipment_list = ShipmentService().get_shipment_list()
    return render_template("shipment/shipment_list.html", shipment_list=shipment_list)