class Car:
    def __init__(self, brand, model, year): 
        self.brand = brand
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f'Brand: {self.brand}, Model: {self.model}, Year: {self.year}') 

car1 = Car('Honda', 'NSX', '2017')
car2 = Car('Toyota', 'AE86', '1983')
car3 = Car('Dodge', 'Charger', '1969')

car1.display_info()
car2.display_info()
car3.display_info()