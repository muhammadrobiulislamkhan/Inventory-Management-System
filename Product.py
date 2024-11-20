class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self._quantity = quantity  # Encapsulation: making quantity private

    def update_quantity(self, amount):
        self._quantity += amount

    def get_quantity(self):
        return self._quantity

    def __str__(self):
        return f"{self.name} - ${self.price}, Quantity: {self._quantity}"

class Electronics(Product):
    def __init__(self, name, price, quantity, warranty):
        super().__init__(name, price, quantity)
        self.warranty = warranty

class Clothing(Product):
    def __init__(self, name, price, quantity, size):
        super().__init__(name, price, quantity)
        self.size = size

class Grocery(Product):
    def __init__(self, name, price, quantity, expiration_date):
        super().__init__(name, price, quantity)
        self.expiration_date = expiration_date
