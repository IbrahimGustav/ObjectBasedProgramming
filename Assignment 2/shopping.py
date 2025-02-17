class CartItem:
    def __init__(self, item_name, price, quantity=1):
        self.item_name = item_name
        self.price = price
        self.quantity = quantity
    
    def add_item(self, quantity):
        self.quantity += quantity
        print(f"Added {quantity} more {self.item_name}(s). Total quantity: {self.quantity}")

    def remove_item(self, quantity):
        self.quantity -= quantity
        print(f"Removed {quantity} {self.item_name}(s). Remaining quantity: {self.quantity}")

    def calculate_total(self):
        total = self.price * self.quantity
        print(f"Total price for {self.quantity} {self.item_name}(s): ${total}")
        return total

cart = []

while True:
    print("-- Menu --")
    print("1. View Cart")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Calculate Total")
    print("5. Exit")

    menu = input("Select menu: ")

    if menu == "1":
        for index, item in enumerate(cart):
            print(f"{index} - {item.item_name}, Price: ${item.price}, Quantity: {item.quantity}")

    elif menu == "2":
        item_name = input("Enter item name: ")
        price = float(input("Enter price: "))
        quantity = int(input("Enter quantity: "))
        cart.append(CartItem(item_name, price, quantity))

    elif menu == "3":
        for index, item in enumerate(cart):
            print(f"{index} - {item.item_name}, Price: ${item.price}, Quantity: {item.quantity}")
        index = int(input("Select the item index to remove quantity from: "))
        quantity = int(input("Enter quantity to remove: "))
        cart[index].remove_item(quantity)

    elif menu == "4":
        total = sum(item.calculate_total() for item in cart)
        print(f"Total cart value: ${total}")

    elif menu == "5":
        break
