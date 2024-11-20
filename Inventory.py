from Product import Product, Electronics, Clothing, Grocery
from Supplier import Supplier
from Stock import Stock
from Sale import Sale

class Inventory:
    def __init__(self):
        self.stock = Stock()
        self.sales = Sale()
        self.suppliers = []

    def add_supplier(self, supplier):
        self.suppliers.append(supplier)

    def add_product_to_inventory(self, product):
        self.stock.add_product(product)

    def record_sale(self, product_name, quantity):
        if product_name in self.stock.inventory:
            self.sales.record_sale(self.stock.inventory[product_name], quantity)
        else:
            print(f"{product_name} not found in inventory.")

    def display_stock(self):
        for name, product in self.stock.inventory.items():
            print(product)

    def display_sales_history(self):
        for record in self.sales.get_sales_history():
            print(f"Product: {record[0]}, Quantity Sold: {record[1]}")
