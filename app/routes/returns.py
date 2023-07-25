from datetime import date
from flask import Blueprint, render_template, request, redirect, url_for
from app.services.returns_services import ReturnsService
from app.services.store_location_services import StoreLocationService
from app.services.product_services import ProductService

bp = Blueprint('returns', __name__)

@bp.route('/list/')
def returns_list():
    returns_service = ReturnsService()
    returns = returns_service.get_returns_list()
    return render_template('returns/returns_list.html', returns=returns)

@bp.route('/detail/<int:return_id>/')
def returns_detail(return_id):
    returns_service = ReturnsService()
    returns = returns_service.get_returns_by_id(return_id)

    if returns:
        return render_template('returns/returns_detail.html', returns=returns)
    else:
        return render_template('returns/returns_not_found.html')

@bp.route('/create/', methods=['GET', 'POST'])
def create_return():
    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        return_date = date.today().strftime("%Y-%m-%d")
        returns = ReturnsService().create_returns(data['product_id'], data['store_id'], return_date, data['return_reason'])

        return redirect(url_for('returns.returns_list'))

    all_stores = StoreLocationService().get_store_location_list()
    all_products = ProductService().get_product_list()
    return render_template('returns/create_return.html', stores = all_stores, products = all_products)
