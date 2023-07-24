# inventory.py
from flask import Blueprint, request, jsonify, render_template
from app.services.inventory_services import InventoryService
from app.services.store_location_services import StoreLocationService
from app.services.product_services import ProductService
from flask import redirect, url_for

bp = Blueprint('inventory', __name__)

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
        inventory = InventoryService().add_inventory(data['product_id'], data['store_id'], data['product_cost'], data['product_quantity'])
        return "success", 201
    
    all_stores = StoreLocationService().get_store_location_list()
    all_products = ProductService().get_product_list()
    return render_template('inventory/add_inventory.html', store_locations = all_stores, products = all_products)


#Route for searching for a product by name in any store
@bp.route('/search/name/', methods=['GET', 'POST'])
def search_by_product_name():

    product_list = []

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        product_name = data['product_name']

        return redirect(url_for('inventory.display_search_id', product_name = product_name))

    return render_template('inventory/inv_search_name.html', product_list=product_list)


#Route for searching for a product by id in any store
@bp.route('/search/id/', methods=['GET','POST'])
def search_by_product_id():

    product_list = []

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        product_id = data['product_id']

        return redirect(url_for('inventory.display_search_id', product_id = product_id))

    return render_template('inventory/inv_search_id.html', product_list=product_list)


#Route for searching for a product in a specific store
@bp.route('/search/storeid/<int:product_id>+<int:store_id>/', methods=['GET'])
def search_product_by_id_in_store(product_id, store_id):

    if product_id and store_id:
        json_list, status_code = InventoryService.product_search_by_id_in_store(product_id, store_id)
        print(f'Product id: {product_id}, Store_id: {store_id}')
        print(json_list)
    #return jsonify(json_list), status_code
    return render_template('inventory/table_template.html', json_list=json_list), status_code

@bp.route('/search/results', methods=['GET'])
def display_search_id():
    # Retrieve the product_list from the request's query parameters
    
    product_name = request.args.get('product_name')

    product_list = InventoryService.search_by_product_name(product_name)
    product_cost = product_list['cost']
    product_list = product_list['details']
    
    return render_template('inventory/inv_search_results.html', product_list=product_list, product_cost=product_cost)