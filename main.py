from Inventory import Inventory
from Product import Electronics, Clothing, Grocery
from Supplier import Supplier

#Set up inventory System
inventory = Inventory()

# Create suppliers
supplier1 = Supplier("ABC Electronics", "123-456-7890")
inventory.add_supplier(supplier1)

# Create and add Products
tv = Electronics("TV", 400, 10, warranty=2)
shirt = Clothing("Shirt", 20, 50, size="M")
milk = Grocery("Milk", 2, 100, expiration_date="2024-01-01")

# Add products to Inventory
inventory.add_product_to_inventory(tv)
inventory.add_product_to_inventory(shirt)
inventory.add_product_to_inventory(milk)

# Display initial Stock
print("Initial Stock:")
inventory.display_stock()

# Record a Sale
inventory.record_sale("TV", 2)

# Display stock after Sale
print("\nStock After Sale:")
inventory.display_stock()

# Display sales History
print("\nSales History:")
inventory.display_sales_history()
