class BankAccount:
    def __init__(self, account_holder, balance, pin):
        self.account_holder = account_holder
        self._balance = balance
        self.__pin = pin
    
    def get_balance(self):
        return self._balance
    
    def set_balance(self, amount):
        if amount <= 0:
            raise ValueError("Invalid balance, please input the correct balance!")
        else:
            self._balance = amount
            print(f"{self.account_holder} set their balance to ${amount}. New balance: ${self._balance}")

    
    def verify_pin(self, input_pin):
        return input_pin == self.__pin
    
    def deposit(self,amount):
        if amount >= 0:
            self._balance+= amount
            print(f"{self.account_holder} deposited ${amount}. New balance: ${self._balance}")
        else:
            print("Please input a correct amount!")

    def withdraw(self,amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"{self.account_holder} withdrawed ${amount}, new balance: ${self._balance}")
        else:
            print("Insufficient funds!")
    
    def showInfo(self):
        return f"{self.account_holder} balance:{self._balance}" 

# Demonstration
account = BankAccount("Alice", 1000, 1234)
print(account.account_holder)  # Public
print(account._balance)  # Protected
# print(account.__pin)  # Private, commented out because the code will give error
accounts=[]

while True:
    print("--Menu--")
    print("1. List Accounts")
    print("2. Create Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Set balance")
    print("6. Exit")
    
    menu = input("Select menu: ")

    if menu == "1":
        for index, account in enumerate(accounts):
            print(f"{index} - {account.showInfo()}")
    
    elif menu == "2":
        account_holder = input("Please input your name: ")
        balance = int(input("Insert balance: "))
        pin = int(input("Please input your PIN: "))
        accounts.append(BankAccount(account_holder, balance, pin))
    
    elif menu == "3":
        index = int(input("Please choose your account index: "))
        amount = int(input("Insert deposit amount: "))
        input_pin = int(input("Please input your PIN: "))
        if accounts[index].verify_pin(input_pin):
            accounts[index].deposit(amount)
        else:
            print("Invalid PIN!")
    
    elif menu == "4":
        index = int(input("Please input your account index: "))
        amount = int(input("Insert your withdraw amount: "))
        input_pin = int(input("Please input your PIN: "))
        if accounts[index].verify_pin(input_pin):
            accounts[index].withdraw(amount)
        else:
            print("Invalid PIN!")
    
    elif menu == "5":
        index = int(input("Please input your account index: "))
        amount = int(input("Insert your withdraw amount: "))
        input_pin = int(input("Please input your PIN: "))
        if accounts[index].verify_pin(input_pin):
            accounts[index].set_balance(amount)
        else:
            print("Invalid PIN!")

    elif menu == "6":
        break