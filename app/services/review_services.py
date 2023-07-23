from app.models.product import Product
from app.models.user import User
from app.models.reviews import Reviews
from flask import jsonify
from app.database import db
from peewee import JOIN

class ReviewService:

    def get_all_product_reviews():
        try:
            product_reviews = Reviews.select()

            if product_reviews:

                reviews_data = [review.__data__ for review in product_reviews]

                #return {'message': 'Successfully retrieved test product', 'product_data': reviews_data}, 200
                return reviews_data, 200
            else:
                return {'message': 'No products found in the inventory'}, 404

        except Exception as e:
            return {'error': str(e)}, 500

    def get_product_reviews_by_id(product_id):
        
        try:
            product_reviews = Reviews.select().where(Reviews.product_id == product_id)

            if product_reviews:
                
                reviews_data = [{
                    'rating' : review.product_rating,
                    'comment' : review.product_review
                } for review in product_reviews]
                #reviews_data = [review.product_review for review in product_reviews]

                return reviews_data, 200
            else:
                return {'message': 'No product reviews found in the inventory'}, 404

        except Exception as e:
            return {'error': str(e)}, 500

    def get_product_reviews_by_product_name(product_name):

        try:
            product_id = Product.get(Product.product_name == product_name).product_id
            product_reviews = Reviews.select().where(Reviews.product_id == product_id)

            if product_reviews:

                reviews_data = [{
                    'name' : product_name,
                    'rating' : review.product_rating,
                    'review' : review.product_review
                } for review in product_reviews]

                return reviews_data, 200
            else:
                return {'message' : 'No product reviews found for product name'}, 404

        except Exception as e:
            return {'error': str(e)}, 500

    def get_product_reviews_by_user_id(user_id):

        try:
            user_name = User.get(User.user_id == user_id).user_name
            user_reviews = Reviews.select().where(Reviews.user_id == user_id)

            if user_reviews:

                reviews_data = [{
                    'username' : user_name,
                    'rating' : review.product_rating,
                    'review' : review.product_review,
                    'date' : review.review_date
                }for review in user_reviews]

                return reviews_data, 200
            else:
                return {'message' : 'No product reviews found for product name'}, 404

        except Exception as e:
            return {'error': str(e)}, 500

