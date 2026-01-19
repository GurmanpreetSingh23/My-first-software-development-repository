# Unit 4: Simple Inventory Management
product_name = "Widget" # String
quantity = 10           # Integer
price = 19.99           # Float

# Functionality to display and update
def show_inventory(name, qnty, prc):
    print(f"Product: {name} | Quantity: {qnty} | Price: ${prc}")

# File handling to store data
with open("inventory.txt", "w") as file:
    file.write(f"{product_name},{quantity},{price}")

show_inventory(product_name, quantity, price)