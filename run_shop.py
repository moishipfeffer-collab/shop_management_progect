from products import show_products_management_menu,add_product,display_products,get_product_by_id
from products import search_product_flow,update_product_flow,remove_product
from invenory_manage import show_inventory_menu,show_full_inventory,search_product_stock
from invenory_manage import change_units_num,show_low_products,show_out_products
from inputs import get_units_num

def show_menu():
    valid = False
    while not valid:
        print("""
===============================
    COMPUTER STORE SYSTEM
===============================

1. Products Management
2. Inventory Management
3. Sales Management
4. Reports
5. Exit
        """)
        choise = input("\nChoose an option: ")
        if choise in ["1","2","3","4","5"]:
            return choise
        print("\nnot valid choise")

# option 1 product management

def product_management_flow(products):
    choise = show_products_management_menu()
    if choise == "1":
        if add_product(products):
            print("the product added successfully")
    elif choise == "2":
        display_products(products)
    elif choise == "3":
        search_product_flow(products)
    elif choise == "4":
        if update_product_flow(products):
            print("the product updated successfully")
    elif choise == "5":
        if remove_product(products):
            print("the product removed successfully")
    elif choise == "6":
        return 

# option 2 inventory management

def inventory_management(products):
    choise = show_inventory_menu()
    if choise == "1":
        show_full_inventory(products)
    elif choise == "2":
        search_product_stock(products)
    elif choise == "3":
        units = get_units_num()
        product = get_product_by_id(products)
        units = get_units_num()
        if change_units_num(product,units):
            print("stock added successfully")
    elif choise == "4":
        product = get_product_by_id(products)
        units = get_units_num()
        if change_units_num(product,-units):
            print("stock reduced successfully")
        else:
            print("stock can not be under zero!")
    elif choise == "5":
        show_out_products(products)
    elif choise == "6":
        show_low_products(products)

# option 3 sale action 



        