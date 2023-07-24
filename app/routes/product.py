from flask import Blueprint, render_template, request, redirect, url_for
from app.services.product_services import ProductService

bp = Blueprint('product', __name__)

@bp.route('/list/')
def product_list():
    product_service = ProductService()
    products = product_service.get_product_list()
    return render_template('product/product_list.html', products=products)

@bp.route('/detail/<int:product_id>/')
def product_detail(product_id):
    product_service = ProductService()
    product = product_service.get_product_by_id(product_id)

    if product:
        return render_template('product/product_detail.html', product=product)
    else:
        return render_template('product/product_not_found.html')

@bp.route('/discontinue/<int:product_id>/', methods=['GET', 'POST'])
def discontinue_product(product_id):
    if request.method == 'POST':
        try:
            product_service = ProductService()
            result = product_service.discontinue_product(product_id)

            if result:
                return redirect(url_for('product.product_list'))
            else:
                return render_template('product/product_not_found.html')

        except ValueError:
            return render_template('invalid_product_id.html')

    return redirect(url_for('product.product_list'))

@bp.route('/outofstock/<int:product_id>/', methods=['GET', 'POST'])
def out_of_stock_product(product_id):
    if request.method == 'POST':
        try:
            product_service = ProductService()
            result = product_service.out_of_stock_product(product_id)

            if result:
                return redirect(url_for('product.product_list'))
            else:
                return render_template('product/product_not_found.html')

        except ValueError:
            return render_template('invalid_product_id.html')

    return redirect(url_for('product.product_list'))

@bp.route('/updateprice/', methods=['GET','POST'])
def update_product_price():

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        product_cost = data['product_cost']
        product_id = data['product_id']

        updated_product = ProductService.update_price(product_id,product_cost)

        if updated_product:
            return redirect(url_for('product.product_list'))
        else:
            return "update failed"
        
    return render_template('product/update_price.html')
