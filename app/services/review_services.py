from app.models.product import Product
from app.models.reviews import Reviews

class ReviewService:

    #Function for selecting all reviews
    def review_list():
        return Reviews.select()

    #Function for selecting all reviews by product id
    def get_product_reviews_by_id(product_id):

        try:
            product_reviews = Reviews.select().where(Reviews.product_id == product_id)

            if product_reviews:

                return product_reviews
            else:
                return {'message': 'No product reviews found in the inventory'}, 404

        except Exception as e:
            return {'error': str(e)}, 500

    #Function for selecting all reviews by product name
    def get_product_reviews_by_name(product_name):

        try:
            product_id = Product.get(Product.product_name == product_name).product_id
            product_reviews = Reviews.select().where(Reviews.product_id == product_id)

            if product_reviews:

                return product_reviews
            else:
                return {'message' : 'No product reviews found for product name'}, 404

        except Exception as e:
            return {'error': str(e)}, 500

    #Function for selecting all reviews by user name
    def get_product_reviews_by_user(user_id):

        try:
            user_reviews = Reviews.select().where(Reviews.user_id == user_id)

            if user_reviews:

                return user_reviews
            else:
                return {'message' : 'No product reviews found for product name'}, 404

        except Exception as e:
            return {'error': str(e)}, 500

