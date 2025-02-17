class Book:
    def __init__(self, title, author, ISBN, quantity):
        self.title = title
        self.author = author
        self.ISBN = ISBN
        self.quantity = quantity
        self.available = quantity > 0
    
    def borrow_book(self, item):
        self.quantity -= item
        print(f"You've successfully borrowed {item} copies of '{self.title}' with ISBN {self.ISBN}")
        if self.quantity == 0:
            self.available = False

    def return_book(self, item):
        self.quantity += item
        self.available = True
        print(f"{item} copies of '{self.title}' have been successfully returned.")

    def show_info(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.ISBN}, Quantity: {self.quantity}, Available: {'Yes' if self.available else 'No'}"

books = []

while True:
    print("\n-- Menu --")
    print("1. List Books")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Exit")
    
    menu = input("Select menu: ")

    if menu == "1":
        for index, book in enumerate(books):
            print(f"{index} - {book.show_info()}")

    elif menu == "2":
        title = input("Please input the book's title: ")
        author = input("Please input the book's author: ")
        ISBN = input("Please input the book's ISBN: ")
        quantity = int(input("How many copies of the book are there?: "))
        books.append(Book(title, author, ISBN, quantity))

    elif menu == "3":
        for index, book in enumerate(books):
            print(f"{index} - {book.show_info()}")
        index = int(input("Select the book index to borrow: "))
        item = int(input("How many copies do you want to borrow? "))
        books[index].borrow_book(item)

    elif menu == "4":
        for index, book in enumerate(books):
            print(f"{index} - {book.show_info()}")
        index = int(input("Select the book index to return: "))
        item = int(input("How many copies are you returning? "))
        books[index].return_book(item)

    elif menu == "5":
        break