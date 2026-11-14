from validations import check_empty,check_num

def get_input(message,input_type):
    valid = False
    while not valid:
        user_input = input(message)
        if check_empty(user_input):
            return user_input
        print(f"{input_type} can not be empty")

def get_num(message,num):
    valid = False
    while not valid:
        user_input = get_input(message,num)
        if num == "price":
            if check_num(user_input,"float"):
                return float(user_input)
        else:
            if check_num(user_input):
                return int(user_input)
        print(f"{num} must be a positive number")
        

def get_product_name():
    return get_input("enter product name: ","product name")

def get_category():
    return get_input("enter product category: ","category")

def get_product_price():
    return get_num("ter product price: ","price")

def get_stock():
    return get_num("enter beggining stock: ","stock")

def get_product_id():
    return get_num("enter product id: ","product id")

def get_remove_product():
    while True:
        insure = input("are you sure you want to remove this product?\n1 .yes\n2. no\n choose: ")
        if insure in ["1","2"]:
            return insure
        print("not valid input")

def get_units_num():
    return get_num("enter units number: ","units number")

def get_max_stock():
    return get_num("enter the max stock number to show: ", "stock number")

def get_quantity():
    return get_num("enter_quantity: ","quantity")

def get_enter():
    return input("\nEnter to return: ")