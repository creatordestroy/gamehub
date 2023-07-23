from app.models.sales import Sales

class SalesService:
    def get_sales_list(self):
        return Sales.select()

    def get_sales_by_date(self, sale_date):
        sales = Sales.select().where(Sales.sale_date == sale_date)
        return sales

    def get_sales_by_id(self, sale_id):
        try:
            return Sales.get(Sales.sale_id == sale_id)
        except Sales.DoesNotExist:
            return None

