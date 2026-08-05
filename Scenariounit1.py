class Vehicle:
    def __init__(self, number, brand, price):
        self.number = number
        self.brand = brand
        self.price = price

    def category(self):
        if self.price >= 1500000:
            return "Luxury"
        return "Economy"

    def display(self):
        print("Vehicle No. :", self.number)
        print("Brand       :", self.brand)
        print("Price       :", self.price)
        print("Category    :", self.category())


class Showroom:
    def __init__(self):
        self.vehicles = []

    def add_vehicle(self, vehicle):
        self.vehicles.append(vehicle)

    def display_all(self):
        for vehicle in self.vehicles:
            vehicle.display()
            print()


s = Showroom()

s.add_vehicle(Vehicle("MH12AB1234", "Toyota", 1800000))
s.add_vehicle(Vehicle("MH14CD5678", "Maruti", 750000))

print("Vehicle Details")
s.display_all()
