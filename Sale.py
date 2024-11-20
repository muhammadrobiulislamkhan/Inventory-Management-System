class Sale:
    def __init__(self):
        self.sales_history = []

    def record_sale(self, product, quantity):
        if product.get_quantity() >= quantity:
            product.update_quantity(-quantity)
            self.sales_history.append((product, quantity))
            print(f"Sold {quantity} of {product.name}.")
        else:
            print(f"Insufficient stock for {product.name}.")

    def get_sales_history(self):
        return [(product.name, quantity) for product, quantity in self.sales_history]
