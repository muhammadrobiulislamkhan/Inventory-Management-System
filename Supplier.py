class Supplier:
    def __init__(self, name, contact_info):
        self.name = name
        self.contact_info = contact_info
        self.products_supplied = []

    def add_product(self, product):
        self.products_supplied.append(product)

    def __str__(self):
        return f"Supplier: {self.name}, Contact: {self.contact_info}"
