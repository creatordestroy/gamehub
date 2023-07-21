# inventory.py
from flask import Blueprint, request, jsonify
from app.services.inventory_services import InventoryService

bp = Blueprint('inventory', __name__)

@bp.route('/inventory/test', methods=['GET'])
def test():
    return jsonify({'message': 'Inventory test route'}), 200

@bp.route('/inventory', methods=['POST'])
def add_inventory():
    data = request.get_json()
    inventory = InventoryService().add_inventory(data['title'], data['platform'], data['count'])
    return jsonify(inventory), 201

@bp.route('/inventory/<int:inventory_id>', methods=['PUT'])
def update_inventory(inventory_id):
    data = request.get_json()
    inventory = InventoryService().update_inventory(inventory_id, data['count'])
    return jsonify(inventory), 200

@bp.route('/inventory/all', methods=['GET'])
def get_all_products():
    inventory_data, status_code = InventoryService.get_test_product()
    return jsonify(inventory_data), status_code

@bp.route('/inventory/ratings/all', methods=['GET'])
def get_all_product_ratings():
    inventory_data, status_code = InventoryService.get_all_product_ratings()
    return jsonify(inventory_data), status_code