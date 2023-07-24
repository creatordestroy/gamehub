from flask import Blueprint, request
from app.services.review_services import ReviewService
from flask import render_template

bp = Blueprint('reviews', __name__)

#Default reviews route, returns list of all product reviews
@bp.route('/list/', methods=['GET'])
def review_list():
    reviews = ReviewService.review_list()
    return render_template('/reviews/review_list.html', reviews=reviews)

#Returns list of product reviews by product_id
@bp.route('/id/', methods=['GET','POST'])
def get_product_reviews_by_id():

    reviews = []

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        reviews = ReviewService.get_product_reviews_by_id(data['product_id'])
    
    return render_template('/reviews/review_by_id.html', reviews=reviews)

#Returns list of product reviews by product name
@bp.route('/name/', methods=['GET', 'POST'])
def get_product_reviews_by_name():

    reviews = []

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        reviews = ReviewService.get_product_reviews_by_name(data['product_name'])
    
    return render_template('/reviews/review_by_name.html', reviews=reviews)

#Returns list of product reviews by user name
@bp.route('/user/', methods=['GET', 'POST'])
def get_product_reviews_by_user():
    reviews = []

    if request.method == 'POST':
        data = request.form.to_dict(flat=True)
        reviews = ReviewService.get_product_reviews_by_user(data['user_id'])
    
    return render_template('/reviews/review_by_user.html', reviews=reviews)

