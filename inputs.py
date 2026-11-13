from validations import check_empty,check_num

def get_input(massage,input_type):
    valid = False
    while not valid:
        user_input = input(massage)
        if check_empty(user_input):
            return user_input
        print(f"{input_type} can not be empty")

def show_num_error_if_there_is(user_input,num):
    valid = False
    while not valid:
        if check_num(user_input):
            return int(user_input)
        print(f"{num} must be a positive number")
        

def get_product_name():
        get_input("enter product name: ","product name")

def get_category():
    get_input("enter product category: ","category")

def get_product_price():
    price = get_input("enter product price: ","price")
    show_num_error_if_there_is(price,"price")

def get_stock():
    stock = get_input("enter beggining stock: ","stock")
    show_num_error_if_there_is(stock,"stock")

def get_product_id():
    product_id = get_input("enter product id: ","product id")
    show_num_error_if_there_is(product_id,"id")

def get_remove_product():
    while True:
        insure = input("are you sure you want to remove this product?\n1 .yes\n2. no\n choose: ")
        if insure in ["1","2"]:
            return insure
        print("not valid input")

def get_units_num():
    units = get_input("enter units number: ","units number")
    show_num_error_if_there_is(units,"units")        

def get_max_stock():
    max_stock = get_input("enter the max stock number to show: ", "stock number")
    show_num_error_if_there_is(max_stock,"sotck nimber")

def get_quantity():
    quantity = get_input("enter_quantity: ","quantity")
    show_num_error_if_there_is(quantity,"quantity")
