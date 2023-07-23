# inventory.py
from flask import Blueprint, request, jsonify, render_template
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

@bp.route('/inventory/search', methods=['GET'])
def search_product_by_name():
    
    product_name = request.args.get('name')
    if product_name:
        json_list, status_code = InventoryService.product_search_by_name(product_name)
        print(json_list)

    return render_template('table_template.html', json_list=json_list), status_code

@bp.route('/inventory/search/<string:product_id>', methods=['GET'])
def search_product_by_id(product_id):

    if product_id:
        json_list, status_code = InventoryService.product_search_by_id(product_id)
        print(json_list)

    return render_template('table_template.html', json_list=json_list), status_code

@bp.route('/inventory/search/store/<int:product_id>+<int:store_id>', methods=['GET'])
def search_product_by_id_in_store(product_id, store_id):

    if product_id and store_id:
        json_list, status_code = InventoryService.product_search_by_id_in_store(product_id, store_id)
        print(f'Product id: {product_id}, Store_id: {store_id}')
        print(json_list)
    #return jsonify(json_list), status_code
    return render_template('table_template.html', json_list=json_list), status_code