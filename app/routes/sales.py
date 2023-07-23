from flask import Blueprint, render_template, request, redirect, url_for
from app.services.sales_services import SalesService

bp = Blueprint('sales', __name__)

@bp.route('/list/')
def sales_list():
    sales_service = SalesService()
    sales = sales_service.get_sales_list()
    return render_template('sales/sales_list.html', sales=sales)

@bp.route('/detail/<int:sale_id>/')
def sales_detail(sale_id):
    sales_service = SalesService()
    sale = sales_service.get_sales_by_id(sale_id)

    if sale:
        return render_template('sales/sales_detail.html', sale=sale)
    else:
        return render_template('sales/sales_not_found.html')

@bp.route('/date/<sale_date>/')
def sales_by_date(sale_date):
    sales_service = SalesService()
    sales = sales_service.get_sales_by_date(sale_date)

    if sales:
        return render_template('sales/sales_by_date.html', sales=sales)
    else:
        return render_template('sales/sales_not_found.html')