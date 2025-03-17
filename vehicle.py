class Car:
    def move(self):
        return "Move with engine"

class Bicycles:
    def move(self):
        return "Move by pedaling"

class Boat:
    def move(self):
        return "Move by engine at water"
    
vehicles = [Car(), Bicycles(), Boat()]

for vehicle in vehicles:
    print(vehicle.move())