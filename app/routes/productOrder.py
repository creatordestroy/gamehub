from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app.services.order_services import OrderServices
from datetime import date
from app.services.product_services import ProductService
from app.services.store_location_services import StoreLocationService

bp = Blueprint('productOrder', __name__)

#Route for display all current inventory objects in all stores
@bp.route('/list/', methods=['GET'])
def order_list():
    orders = OrderServices().get_order()
    return render_template('orders/order_list.html', orders=orders)

@bp.route('/add', methods=['GET','POST'])
def add_productOrder():
    
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        order_date = date.today().strftime("%Y-%m-%d")
        order = OrderServices().add_order(data['product_id'], data['store_id'], data['order_status'], order_date, data['order_quantity'])
        return "success", 201
    
    return render_template('orders/add_order.html')

@bp.route('/auto', methods=['GET','POST'])
def auto_order():

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        order = OrderServices.auto_order(data['store_id'])
        return redirect(url_for('productOrder.order_list', order=order))
    
    return render_template('orders/auto_order.html')



