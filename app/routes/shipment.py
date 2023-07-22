from flask import Blueprint, render_template, request, jsonify
from app.services.shipment_services import ShipmentService

bp = Blueprint('shipment', __name__)

@bp.route('/receive/', methods=['GET', 'POST'])
def add_shipment():
    if request.method == 'POST':
        data = request.get_json()
        shipment = ShipmentService().receive_shipment(data['product_id'], data['shipment_quantity'])
        return jsonify(shipment), 201

    return render_template("shipment/add_shipment.html")