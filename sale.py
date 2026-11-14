from inputs import get_quantity
from products import get_product_by_id
from validations import show_valid_activity,show_valid_quantity


def create_new_sale(sales):
    sale = {"id":len(sales)+1,"items":[]}
    return sale

def show_products(products):
    print("--- The products are: --- \n")
    for product in products:
        print(product)

def get_sale_data(products):
    print()
    product = get_product_by_id(products)
    if not product:
        print("product not found")
        return False
    quantity = get_quantity()
    if not show_valid_activity(product) or not show_valid_quantity(quantity,product):
        return False
    return {"product_id":product["id"],"name":product["name"],
"quantity":quantity,"unit_price":product["price"],"total":product["price"] * quantity}


def add_to_items(items: list,item):
    items.append(item)

def add_subtotal_to_sale(sale):
    sale["subtotal"] = 0
    for item in sale["items"]:
        sale["subtotal"] += item["total"]

def calc_discount(subtotal):
    if subtotal >= 1500:
        return subtotal - subtotal / 100 * 15
    elif subtotal >= 800:
        return subtotal - subtotal / 100 * 10
    else:
        return subtotal

def add_discount_and_total(sale,total):
    try:
        sale["discount"] = sale["subtotal"] / (sale["subtotal"] - total)
    except ZeroDivisionError:
        sale["discount"] = 0
    sale["total"] = total 

def show_sale(sale):
    subtotal = 0
    print("\n========== NEW SALE ==========\n")
    for item in sale["items"]:
        print(f"Product id: {item['product_id']}\nQuantity: {item['quantity']}\n\n\
Added to cart!\n")
        subtotal += item["total"]
    print(f"Subtotal: {subtotal}")
    print(f"Total: {calc_discount(subtotal)}\n\n")


def check_continue_sale():
    while True:
        choise = input("1. Continue Shppping\n2. Complete Sale\n3. Cancel Sale\n4. Update or remove a product\n\nChoose: ")
        if choise in ["1","2","3","4"]:
            return choise
        print("not valid choise")

def show_compleate_sale(sale):
    print("========== SALE SUMMARY ==========\n")
    for item in sale["items"]:
        print(f"{item['name']}: {item['quantity']} X {item['unit_price']} = {item['total']}")
    print("\n---------------------------------\n")
    print(f"Subtotal: {sale['subtotal']}\nDicount: {sale['discount']} %\n\
Total: {sale['total']}")
    print("===================================\n\nSale completed successfully!")


def update_stock_after_sale(products,item):
    for product in products:
        if product["id"] == item["product_id"]:
            product["stock"] -= item["quantity"]


def show_updating_menu():
    while True:
        print("What would you like to change?\n ")
        choise = input("1. Remove\n2. Change\nChoose: ")
        if choise in ["1","2"]:
            return choise
        print("Not valid choise")

def remove_or_update_product(products,items:list,remove:str | None = None):
    product = get_product_by_id(products)
    if not product:
        return False
    for item in items:
        if item["product_id"] == product["id"]:
            if remove:
                items.remove(item)
            else:
                quantity = get_quantity()
                item["quantity"] = quantity
            return True
    return False



