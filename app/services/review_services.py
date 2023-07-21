from app.models.inventory import Inventory
from app.models.user import User
from app.models.reviews import Reviews
from flask import jsonify
from app.database import db

class ReviewService:

    def get_all_product_reviews():
        try:
            product_reviews = Reviews.select()

            if product_reviews:

                reviews_data = [review.__data__ for review in product_reviews]

                return {'message': 'Successfully retrieved test product', 'product_data': reviews_data}, 200
            else:
                return {'message': 'No products found in the inventory'}, 404

        except Exception as e:
            return {'error': str(e)}, 500

    def get_product_review_by_id(product_id):
        
        try:
            product_review = Reviews.select(Inventory.product_id == product_id)

            if product_review:
                
                reviews_data = {
                                'product_id' : Inventory.product_id,
                                'name' : Inventory.product_name,
                                'rating' : Reviews.product_rating,
                                'review' : Reviews.product_review,
                                'date' : Reviews.review_date
                }

                return {'message': 'Successfully retrieved product reviews', 'product_data': reviews_data}, 200
            else:
                return {'message': 'No product found in the inventory'}, 404

        except Exception as e:
            return {'error': str(e)}, 500