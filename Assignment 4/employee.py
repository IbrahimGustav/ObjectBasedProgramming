class Employee:
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def calculate_salary(self):
        return self.salary

    def show_details(self):
        return f"Name: {self.name}, ID: {self.id}, Salary: {self.calculate_salary()}"

class Manager(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id, salary)

    def calculate_salary(self):
        return self.salary * 1.2

class Engineer(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id, salary)

    def calculate_salary(self):
        return self.salary * 1.1

class Intern(Employee):
    def __init__(self, name, id, salary):
        super().__init__(name, id, salary)
        self.bonus = 0

    def calculate_salary(self):
        return self.salary

# Demonstration
employees = [
    Manager("John", 1, 1000),
    Engineer("Doe", 2, 1000),
    Intern("Jane", 3, 1000)
]

for emp in employees:
    print(emp.show_details())