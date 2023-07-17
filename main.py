from inventory import Inventory
from orderForm import OrderForm
from item import Item
import pandas as pd


def main():
    
    new_item = Item("xbox","1001",499.99,5)


    empty_item = Item("NES", "1007", 199.99, 0)
    product_orderform = OrderForm()
    product_orderform.add_to_order(empty_item, 6)
    #product_orderform.clear_order()



    product_inventory = Inventory("data.json")
    #product_inventory.clearInventory()
    #product_inventory.populateInventory()
    #product_inventory.addItem(new_item)
    #product_inventory.printInventory()
    #product_inventory.removeItem(new_item)

    return 0

if __name__ == "__main__":
    main()