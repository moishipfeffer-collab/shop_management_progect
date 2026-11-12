from inputs import get_product_name,get_category,get_product_price,get_stock
from inputs import get_product_id,get_remove_product

def show_products_management_menu():
    while True:
        print("""
----------- PRODUCTS MANAGEMENT -----------
1. Add Product
2. Display All Products
3. Search Product
4. Update Product
5. Delete Product
6. Back to Main Menu 
        """)
        choise = input("\nChoose an option: ")
        if choise in ["1","2","3","4","5","6"]:
            return choise
        print("\nnot valid choise")

# option 1 add product 

def create_product(counter,name,category,price,stock):
    product = {"id":counter,"name":name,"category":category,
    "price":price,"stock":stock,"active":True}
    return product

def add_product(products:list):
    product_name = get_product_name()
    category = get_category()
    price = get_product_price()
    beggining_stock = get_stock()
    product = create_product(len(products)+1,product_name,category,price,beggining_stock)
    products.append(product)
    return True

# option 2 display all products

def display_products(products):
    active = []
    for product in products:
        if product["active"]:
            active.append(product)
    if active:
        print(active)
    else:
        print("no active products!")

# option 3 search product 

def show_search_menu():
    while True: 
        choise = input("search by:\n1. product id\n2. product name\n3. category\nChoose an option: ")
        if choise in ["1","2","3"]:
            return choise
        print("not valid choise")

def search_product(products,search_by,search_value):
    found_products = []
    for product in products:
        if search_by == "name":
            if search_value.lower() in product[search_by].lower(): 
                found_products.append(product)
        else:
            if product[search_by] == search_value:
                found_products.append(product)
    print(found_products) if found_products else print("product not found")


def search_product_flow(products):
    choise = show_search_menu()
    if choise == "1":
        product_id = get_product_id()
        found_products = search_product(products,"id",product_id)
    elif choise == "2":
        product_name = get_product_name()
        found_products = search_product(products,"name",product_name)
    else:
        categoty = get_category()
        found_products = search_product(products,"category",categoty)
    return found_products

# option 4 update product

def show_update_menu():
    while True:
        choise = input("what would you like to update?\n1. product name\n2. category\n3. price\n4. active\nchoose an opetion: ")
        if choise in ["1","2","3","4"]:
            return choise
        print("not valid choise")

def get_product_by_id(products):
    product_id = get_product_id()
    for product in products:
        if product["id"] == product_id:
            return product

def update_product(product,update_type):
    if update_type == "1":
        product["name"] = get_product_name()
    elif update_type == "2":
        product["category"] = get_category()
    elif update_type == "3":
        product["price"] = get_product_price()
    else:
        product["active"] = not product["active"]

def update_product_flow(products):
    product = get_product_by_id(products)
    if product:
        choise = show_update_menu()
        update_product(product,choise)
        return True
    else:
        print("no product found")

# option 5 del product 

def remove_product(products:list):
    product = get_product_by_id(products)
    if product:
        check = get_remove_product()
        if check == "1":
            products.remove(product)
            return True
        else:
            return False
    else:
        print("no product found")
