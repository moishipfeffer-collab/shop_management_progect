from products import show_products_management_menu,add_product,display_products,get_product_by_id
from products import search_product_flow,update_product_flow,remove_product
from invenory_manage import show_inventory_menu,show_full_inventory,search_product_stock
from invenory_manage import change_units_num,show_low_products,show_out_products
from inputs import get_units_num,get_enter
from sale import create_new_sale,get_sale_data,add_to_items,add_subtotal_to_sale
from sale import calc_discount,add_discount_and_total,show_sale,check_continue_sale
from sale import show_compleate_sale,update_stock_after_sale,show_products
from sale import show_updating_menu,remove_or_update_product
from reports import show_reports_menu,show_total_sales,get_total_revenue,show_best_selling
from reports import show_avg_sale,show_sale_history,show_category_statistics
import os

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
        os.system("clear")
        if add_product(products):
            print("---- the product added successfully ----")
        get_enter()
    elif choise == "2":
        os.system("clear")
        display_products(products)
        get_enter()
    elif choise == "3":
        os.system("clear")
        search_product_flow(products)
        get_enter()
    elif choise == "4":
        os.system("clear")
        if update_product_flow(products):
            print("the product updated successfully")
        get_enter()
    elif choise == "5":
        os.system("clear")
        if remove_product(products):
            print("the product removed successfully")
        get_enter()
    elif choise == "6":
        return 

# option 2 inventory management

def inventory_management(products):
    choise = show_inventory_menu()
    if choise == "1":
        show_full_inventory(products)
        get_enter()
    elif choise == "2":
        search_product_stock(products)
        get_enter()
    elif choise == "3":
        product = get_product_by_id(products)
        units = get_units_num()
        if change_units_num(product,units):
            print("stock added successfully")
        get_enter()
    elif choise == "4":
        product = get_product_by_id(products)
        units = get_units_num()
        if change_units_num(product,-units):
            print("stock reduced successfully")
        else:
            print("stock can not be under zero!")
        get_enter()
    elif choise == "5":
        if not show_out_products(products):
            print("no products")
        get_enter()
    elif choise == "6":
        if not show_low_products(products):
            print("no products")
        get_enter()

# option 3 sale action 

def run_sale(products,sales:list):
    sale = create_new_sale(sales)
    while True:
        os.system("clear")
        show_products(products)
        item = get_sale_data(products)
        if not item:
            get_enter()
            continue
        add_to_items(sale["items"],item)
        add_subtotal_to_sale(sale)
        total = calc_discount(sale["subtotal"])
        add_discount_and_total(sale,total)
        os.system("clear")
        show_sale(sale)
        choise = check_continue_sale()
        if choise == "2":
            if not sale["items"]:
                print("Can not conplete a sale with no items! ")
            else:
                os.system("clear")
                show_compleate_sale(sale)
                for item in sale["items"]:
                    update_stock_after_sale(products,item)
                sales.append(sale)
            get_enter()
            return 
        elif choise == "3":
            print("The sale cancaled successfully!")
            get_enter()
            return 
        elif choise == "4":
            os.system("clear")
            update = show_updating_menu()
            if update == "1":
                updated = remove_or_update_product(products,sale["items"],"remove")
            else:
                updated = remove_or_update_product(products,sale["items"])
            if updated:
                print("Updated successfully!")
            else:
                print("The product not found in cart")
            get_enter()


def run_reports(products,sales):
    choise = show_reports_menu()
    if choise == "1":
        show_total_sales(sales)
        get_enter()
    elif choise == "2":
        print(f"Total Revenue: {get_total_revenue(sales)}")
        get_enter()
    elif choise == "3":
        show_best_selling(sales)
        get_enter()
    elif choise == "4":
        show_avg_sale(sales)
        get_enter()
    elif choise == "5":
        show_sale_history(sales)
        get_enter()
    elif choise == "6":
        show_category_statistics(products,sales)
        get_enter()
    elif choise == "7":
        return 