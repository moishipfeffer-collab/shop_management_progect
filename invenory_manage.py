from inputs import get_max_stock
from products import get_product_by_id
import os

def show_inventory_menu():
    while True:
        print("""
---------- INVENTORY MANAGEMENT ----------
1. Show full inventory
2. Search product in stock 
3. add units to inventory
4. Reducing units to inventory
5. Show out-of-stock products
6. Show products with low stock.
""")
        choise = input("choose an option: ")
        if choise in ["1","2","3","4","5","6"]:
            return choise
        print("not valid choise")

# option 1 show all stock

def show_full_inventory(products):
    for product in products:
        if product["active"]:
            print(f"product: {product['name']}, stock: {product['stock']}")

# option 2 search product

def search_product_stock(products):
    product = get_product_by_id(products)            
    if product:
        print(f"product: {product['name']}: stock: {product['stock']}")
    else:
        print("product not found")

# option 3 add units and 4 reduce

def change_units_num(product,units):
    if product["stock"] + units < 0:
        return False
    product["stock"] += units
    return True

# option 5 Show out-of-stock products

def show_out_products(products):
    for product in products:
        if product["stock"] == 0:
            print(product["name"])
            return True
    return False

# option 6 Show products with low stock.

def show_low_products(products):
    stock_num = get_max_stock()
    for product in products:
        if product["stock"] <= stock_num:
            print(f"product: {product['name']}, stock: {product['stock']}")
            return True
    return False
