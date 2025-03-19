class Product:
    def __init__(self, product_id, name, price, quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity


class StockMaintenanceSystem:
    def __init__(self):
        self.products = {}

    def add_product(self, product):
        if product.product_id not in self.products:
            self.products[product.product_id] = product
            print(f"Product {product.name} added successfully.")
        else:
            print("Product with the same ID already exists.")

    def display_inventory(self):
        print("\nCurrent Inventory:")
        if not self.products:
            print("Inventory is empty.")
            return
        for product_id, product in self.products.items():
            print(f"ID: {product_id}, Name: {product.name}, Quantity: {product.quantity}, Price: ${product.price}")

    def execute_transaction(self, product_id, quantity_change, transaction_type):
        if product_id in self.products:
            product = self.products[product_id]
            if transaction_type == "IN":
                product.quantity += quantity_change
                print(f"Added {quantity_change} units of {product.name}.")
            elif transaction_type == "OUT":
                if product.quantity >= quantity_change:
                    product.quantity -= quantity_change
                    print(f"Removed {quantity_change} units of {product.name}.")
                else:
                    print(f"Insufficient stock to remove {quantity_change} units of {product.name}.")
        else:
            print("Product not found in inventory.")
system = StockMaintenanceSystem()
p1 = Product(1, "Laptop", 800, 10)
p2 = Product(2, "Smartphone", 500, 20)
system.add_product(p1)
system.add_product(p2)
system.display_inventory()
system.execute_transaction(1, 5, "OUT") 
system.execute_transaction(2, 8, "IN") 
system.display_inventory()