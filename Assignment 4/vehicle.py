class Vehicle:
    def __init__(self, brand, model, rentalrate):
        self.brand = brand
        self.model = model
        self.rentalrate = rentalrate
    
    def calculate_rental(self, days):
        return self.rentalrate * days
    
    def show_info(self):
        return f"Brand: {self.brand}, Model: {self.model}, Rental rate: {self.rentalrate}"

class Car(Vehicle):
    def open_trunk(self):
        return "Trunk is now open."

class Bike(Vehicle):
    def kickstart(self):
        return "Bike is now kickstarted."

class LuxuryFeatures:
    def enable_gps(self):
        return "GPS is now enabled."

    def enable_heated_seats(self):
        return "Heated seats are now enabled."

class LuxuryCar(Car, LuxuryFeatures):
    def calculate_rental(self, days):
        base_rental = super().calculate_rental(days)
        luxury_charge = 50
        return base_rental + luxury_charge

cars = [LuxuryCar("Lexus", "SC300", 500)]

for car in cars:
    print(car.show_info())
    print(f"Rental cost for 3 days with all luxury features: ${car.calculate_rental(3)}")
    print(car.enable_gps())
    print(car.enable_heated_seats())
    print(car.open_trunk())