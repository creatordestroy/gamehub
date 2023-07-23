from app.models.product import Product

class ProductService:
    def get_product_list(self):
        return Product.select()
