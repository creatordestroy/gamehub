from flask import Blueprint, request, jsonify, render_template
from app.services.order_services import OrderServices
from datetime import date
from app.services.product_services import ProductService
from app.services.store_location_services import StoreLocationService

bp = Blueprint('productOrder', __name__)

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
        return "success", 201
    
    return render_template('orders/auto_order.html')



