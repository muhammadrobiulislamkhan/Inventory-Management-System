class Stock:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product):
        if product.name in self.inventory:
            self.inventory[product.name].update_quantity(product.get_quantity())
        else:
            self.inventory[product.name] = product

    def update_stock(self, product_name, quantity):
        if product_name in self.inventory:
            self.inventory[product_name].update_quantity(quantity)

    def get_stock(self):
        return {name: product.get_quantity() for name, product in self.inventory.items()}
