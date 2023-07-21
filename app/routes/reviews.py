from flask import Blueprint, request, jsonify
from app.services.review_services import ReviewService

bp = Blueprint('Reviews', __name__)

@bp.route('/reviews/all', methods=['GET'])
def get_all_product_reviews():
    reviews_data, status_code = ReviewService.get_all_product_reviews()
    return jsonify(reviews_data), status_code

@bp.route('/reviews/id/<int:product_id>', methods=['GET'])
def get_product_review_by_id(product_id):
    reviews_data, status_code = ReviewService.get_product_review_by_id(product_id)
    return jsonify(reviews_data), status_code
    

