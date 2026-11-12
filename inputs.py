from validations import check_empty,check_num

def get_input(massage,input_type):
    valid = False
    while not valid:
        user_input = input(massage)
        if check_empty(user_input):
            return user_input
        print(f"{input_type} can not be empty")

def get_product_name():
        name = get_input("enter product name: ","product name")
        return name 

def get_category():
    while True:
        category = get_input("enter product category: ","category")
        return category

def get_product_price():
    while True:
        price = get_input("enter product price: ","price")
        if check_num(price,"float"):
            return price
        print("price must be a positive number")

def get_stock():
    while True:
        stock = get_input("enter beggining stock: ","stock")
        if check_num(stock):
            return stock
        print("stock must be a hole positive number")

def get_product_id():
    while True:
        product_id = get_input("enter product id: ","product id")
        if check_num(product_id):
            return int(product_id)
        print("id must be a positive number")

def get_remove_product():
    while True:
        insure = input("are you sure you want to remove this product?\n1 .yes\n2. no\n choose: ")
        if insure in ["1","2"]:
            return insure
        print("not valid input")

def get_units_num():
    units = get_input("enter units number: ","units number")
    if check_num(units):
        return int(units)
    print("units must be a positive number")

def get_max_stock():
    while True:
        max_stock = get_input("enter the max stock number to show: ", "stock number")
        if check_num(max_stock):
            return int(max_stock)
        print("stock must be a positive number")

