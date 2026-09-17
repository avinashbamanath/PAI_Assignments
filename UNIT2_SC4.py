class Mobile:
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price

        if price >= 50000:
            self.category = "Premium"
        elif price >= 20000:
            self.category = "Mid-range"
        else:
            self.category = "Budget"

    def display(self):
        print("Brand   :", self.brand)
        print("Model   :", self.model)
        print("Price   : Rs.", self.price)
        print("Category:", self.category)
        print("----------------------------")


class Store:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self, mobile):
        self.mobiles.append(mobile)
        print("Mobile added successfully!")

    def display_all(self):
        if len(self.mobiles) == 0:
            print("No mobiles available in the store.")
        else:
            print("\n===== Mobile Store =====")
            for mobile in self.mobiles:
                mobile.display()


store = Store()

while True:
    print("\n===== MOBILE STORE MANAGEMENT SYSTEM =====")
    print("1. Add Mobile")
    print("2. Display All Mobiles")
    print("3. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        brand = input("Enter brand: ")
        model = input("Enter model: ")
        price = float(input("Enter price: "))

        mobile = Mobile(brand, model, price)
        store.add_mobile(mobile)

    elif choice == 2:
        store.display_all()

    elif choice == 3:
        print("Exiting program...")
        break

    else:
        print("Invalid choice!")
