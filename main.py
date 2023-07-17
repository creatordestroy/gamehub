from inventory import Inventory
from item import Item
import pandas as pd


def main():
    
    new_item = Item("xbox","1001",499.99,5)
    product_inventory = Inventory("data.json")
    #product_inventory.clearInventory()
    #product_inventory.populateInventory()
    #product_inventory.addItem(new_item)
    #product_inventory.printInventory()
    #product_inventory.removeItem(new_item)

    return 0

if __name__ == "__main__":
    main()