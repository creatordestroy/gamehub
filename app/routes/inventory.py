# inventory.py
from flask import Blueprint, request, jsonify, render_template
from app.services.inventory_services import InventoryService
from app.services.store_location_services import StoreLocationService
from app.services.product_services import ProductService

bp = Blueprint('inventory', __name__)

#Test method for inventory route
@bp.route('/test/', methods=['GET'])
def test():
    return jsonify({'message': 'Inventory test route'}), 200

#Route for display all current inventory objects in all stores
@bp.route('/list/', methods=['GET'])
def inventory_list():
    inventory = InventoryService().get_inventory_list()
    return render_template('inventory/inventory_list.html', inventory=inventory)

#Route to add a new product into inventory
@bp.route('/add/', methods=['GET','POST'])
def add_inventory():

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        print(data)
        inventory = InventoryService().add_inventory(data['product_id'], data['store_id'], data['product_cost'], data['product_quantity'])
        return "success", 201
    
    all_stores = StoreLocationService().get_store_location_list()
    all_products = ProductService().get_product_list()
    return render_template('inventory/add_inventory.html', store_locations = all_stores, products = all_products)

@bp.route('/<int:inventory_id>/', methods=['PUT'])
def update_inventory(inventory_id):
    data = request.form.to_dict(flat=True)
    inventory = InventoryService().update_inventory(inventory_id, data['count'])
    return jsonify(inventory), 200

@bp.route('/search/', methods=['GET'])
def search_product_by_name():

    product_name = request.args.get('name')
    if product_name:
        json_list, status_code = InventoryService.product_search_by_name(product_name)
        print(json_list)

    return render_template('inventory/table_template.html', json_list=json_list), status_code

@bp.route('/search/<string:product_id>/', methods=['GET'])
def search_product_by_id(product_id):

    if product_id:
        json_list, status_code = InventoryService.product_search_by_id(product_id)
        print(json_list)

    return render_template('inventory/table_template.html', json_list=json_list), status_code

@bp.route('/search/store/<string:store_id>/', methods=['GET'])
def search_product_by_store_id(store_id):

    if store_id:
        json_list, status_code = InventoryService.product_search_by_store_id(store_id)
        print(json_list)

    return render_template('inventory/table_template.html', json_list=json_list), status_code

@bp.route('/search/storeid/<int:product_id>+<int:store_id>/', methods=['GET'])
def search_product_by_id_in_store(product_id, store_id):

    if product_id and store_id:
        json_list, status_code = InventoryService.product_search_by_id_in_store(product_id, store_id)
        print(f'Product id: {product_id}, Store_id: {store_id}')
        print(json_list)
    #return jsonify(json_list), status_code
    return render_template('inventory/table_template.html', json_list=json_list), status_code