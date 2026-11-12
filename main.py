from run_shop import show_menu,product_management_flow,inventory_management

def main():
    products = [{"id": 1,"name":"Gaming Mouse","category": "Gaming","price": 150.0,"stock": 20,"active": True},
{"id": 2,"name": "Mechanical Keyboard","category": "Accessories","price": 350.0,"stock": 10,"active": True }]
    while True:
        choise = show_menu()
        if choise == "1":
            product_management_flow(products)
        elif choise == "2":
            inventory_management(products)
        elif choise == "5":
            break

if __name__ == "__main__":
    main()