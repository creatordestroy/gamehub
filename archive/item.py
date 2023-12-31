class Item(object):
    def __init__(self, name: str, sku: str, cost: float, stock: int):

        self.name = name
        self.sku = sku
        self.cost = cost
        self.stock = stock
        self.order_quantity = 0

    def updateCost(self, new_cost: float) -> None:

        self.cost = new_cost

    def incrementStock(self) -> None:

        self.stock += 1

    def decrementStock(self) -> None:
        
        self.stock -= 1

    def getStock(self) -> int:

        return self.stock
        
    def updateQuantity(self, quantity) -> None:

        self.order_quantity = quantity

    




        

