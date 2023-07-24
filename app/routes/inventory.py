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

        return redirect(url_for('inventory.display_search_name', product_name = product_name))

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
@bp.route('/search/store/', methods=['GET', 'POST'])
def search_by_product_store():

    product_list = []

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        product_id = data['product_id']
        store_id = data['store_id']

        return redirect(url_for('inventory.display_search_store', product_id = product_id, store_id=store_id))

    return render_template('inventory/inv_search_store.html', product_list=product_list)

#Route to display results for search by name
@bp.route('/search/results/name', methods=['GET'])
def display_search_name():
    
    product_name = request.args.get('product_name')

    product_list = InventoryService.search_by_product_name(product_name)
    product_cost = product_list['cost']
    product_list = product_list['details']
    
    return render_template('inventory/inv_search_results.html', product_list=product_list, product_cost=product_cost)

#Route to display results for search by ID
@bp.route('/search/results/id', methods=['GET'])
def display_search_id():
    
    product_id = request.args.get('product_id')

    product_list = InventoryService.search_by_product_id(product_id)
    product_cost = product_list['cost']
    product_name = product_list['name']
    product_list = product_list['details']

    return render_template('inventory/inv_search_results.html', product_list=product_list, product_cost=product_cost, product_name=product_name)

#Route to display results for search by store and by ID
@bp.route('/search/results/store', methods=['GET'])
def display_search_store():
    
    product_id = request.args.get('product_id')
    store_id = request.args.get('store_id')

    product_list = InventoryService.search_by_product_store(product_id, store_id)
    product_cost = product_list['cost']
    product_name = product_list['name']
    product_list = product_list['details']

    return render_template('inventory/inv_search_results.html', product_list=product_list, product_cost=product_cost, product_name=product_name)