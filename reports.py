def show_reports_menu():
    print("========== REPORTS ==========\n")
    while True:
        choise = input("""
1. Total Sales
2. Total Revenue
3. Best Selling Products
4. Average Sale
5. Sales History
6. Category Statistics
7. Back

Choose an option: """)
        if choise in ["1","2","3","4","5","6","7"]:
            return choise
        print("not valid choise")

def check_sales(sales):
    if not sales:
        print("no sales yet")
        return False
    return True

    
def show_total_sales(sales):
    if check_sales(sales):
        print(f"Total sales are: {len(sales)}")

def get_total_revenue(sales):
    if check_sales(sales):
        total = 0
        for sale in sales:
            total += sale["total"]
        return total

def create_item_list(sales):
    item_list = []
    for sale in sales:
        for item in sale["items"]:
            item_list.append(item)
    return item_list

def sort_items_by_quantity(item_list):
    sorted_list = sorted(item_list,key=lambda i: i["quantity"],reverse=True)
    return sorted_list

def show_best_selling(sales):
    if check_sales(sales):
        item_list = create_item_list(sales)
        sorted_list = sort_items_by_quantity(item_list)
        for item in sorted_list[:5]:
            print(item["name"])

def show_avg_sale(sales):
    if check_sales(sales):
        total = get_total_revenue(sales)
        print(f"The avg sale: {total / len(sales)}")

def show_sale_history(sales):
    if check_sales(sales):
        print("\n---- sales history ----\n")
        for sale in sales:
            print(f"{sale}\n")

def find_product_by_id(products,product_id):
    for product in products:
        if product["id"] == product_id:
            return product

def show_category_statistics(products,sales):
    if check_sales(sales):
        categories_sale = {}
        item_list = create_item_list(sales)
        for item in item_list:
            product = find_product_by_id(products,item["product_id"])
            category = product["category"]
            if category not in categories_sale:
                categories_sale[category] = item["quantity"]
            categories_sale[category] += item["quantity"]
    print(categories_sale)