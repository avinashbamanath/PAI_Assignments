class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price

    def category(self):
        if self.price >= 5000:
            return "Expensive"
        return "Affordable"

    def display(self):
        print("Product ID   :", self.pid)
        print("Product Name :", self.name)
        print("Price        :", self.price)
        print("Category     :", self.category())


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def display_all(self):
        for product in self.products:
            product.display()
            print()


inv = Inventory()

inv.add_product(Product(101, "Headphones", 6500))
inv.add_product(Product(102, "Notebook", 120))

print("Product Inventory")
inv.display_all()
