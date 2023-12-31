from app.models.product import Product

class ProductService:
    def get_product_list(self):
        return Product.select()

    def get_product_by_id(self, product_id):
        try:
            return Product.get(Product.product_id == product_id)
        except Product.DoesNotExist:
            return None

    def discontinue_product(self, product_id):
        try:
            product = Product.get(Product.product_id == product_id)
            product.product_discontinued = True
            product.save()
            return True
        except Product.DoesNotExist:
            return False

    def out_of_stock_product(self, product_id):
        try:
            product = Product.get(Product.product_id == product_id)
            product.product_out_of_stock = True
            product.save()
            return True
        except Product.DoesNotExist:
            return False
        
    def update_price(product_id, product_cost):
        try:
            product = Product.get(Product.product_id==product_id)
            product.product_cost = product_cost
            product.save()

            return product
        except Product.DoesNotExist:

            return None

