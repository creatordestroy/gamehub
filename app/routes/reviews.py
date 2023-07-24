from flask import Blueprint, request, jsonify
from app.services.review_services import ReviewService
from flask import render_template

bp = Blueprint('reviews', __name__)

@bp.route('/list/', methods=['GET'])
def review_list():
    reviews = ReviewService.review_list()
    return render_template('/reviews/review_list.html', reviews=reviews)

@bp.route('/all/', methods=['GET'])
def get_all_product_reviews():
    json_list, status_code = ReviewService.get_all_product_reviews()

    return render_template('base.html', json_list = json_list), status_code

@bp.route('/id/<int:product_id>/', methods=['GET'])
def get_product_reviews_by_id(product_id):
    json_list, status_code = ReviewService.get_product_reviews_by_id(product_id)
    #return jsonify(reviews_data), status_code

    return render_template('base.html', json_list = json_list), status_code

@bp.route('/product/', methods=['GET'])
def get_product_reviews_by_name():
    product_name = request.args.get('name')
    print(product_name)
    if product_name:
        json_list, status_code = ReviewService.get_product_reviews_by_product_name(product_name)
    #return jsonify(reviews_data), status_code
    return render_template('base.html', json_list = json_list), status_code

@bp.route('/user/', methods=['GET'])
def get_product_reviews_by_user_id():
    product_user = request.args.get('user')
    print(product_user)
    if product_user:
        json_list, status_code = ReviewService.get_product_reviews_by_user_id(product_user)
    #return jsonify(reviews_data), status_code
    return render_template('base.html', json_list = json_list), status_code

