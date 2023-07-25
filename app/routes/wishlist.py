from flask import Blueprint, request, jsonify, render_template, redirect, url_for
from app.services.wishlist_services import WishlistServices
from app.services.product_services import ProductService
from datetime import date

bp = Blueprint('wishlist', __name__)

@bp.route('/list/', methods=['GET'])
def wishlist_list():
    user_id = request.args.get('user')
    wishlist = WishlistServices.wishlist(user_id)
    products = ProductService().get_product_list()
    return render_template('wishlist/wishlist_list.html', products=products, wishlist=wishlist)

@bp.route('/add/<string:product_id>/', methods=['GET', 'POST'])
def add_product_by_id(product_id):
    user_id = request.args.get('user')
    date_added = date.today().strftime("%Y-%m-%d")
    if request.method == 'POST':
        wishlist_item = WishlistServices().add_to_wishlist(user_id, product_id, date_added)
        return wishlist_item, "200"
    WishlistServices().add_to_wishlist(user_id, product_id, date_added)
    return redirect(url_for('inventory.inventory_list'))
