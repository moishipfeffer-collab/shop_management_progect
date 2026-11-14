from run_shop import show_menu,product_management_flow,inventory_management
from run_shop import run_sale,run_reports
import os 

def main():
    products = [{"id": 1,"name":"Gaming Mouse","category": "Gaming","price": 150.0,"stock": 20,"active": True},
{"id": 2,"name": "Mechanical Keyboard","category": "Accessories","price": 350.0,"stock": 10,"active": True }]
    sales = []
    while True:
        os.system("clear")
        choise = show_menu()
        if choise == "1":
            os.system("clear")
            product_management_flow(products)
        elif choise == "2":
            os.system("clear")
            inventory_management(products)
        elif choise == "3":
            os.system("clear")
            run_sale(products,sales)
        elif choise == "4":
            os.system("clear")
            run_reports(products,sales)
        elif choise == "5":
            break

if __name__ == "__main__":
    main()