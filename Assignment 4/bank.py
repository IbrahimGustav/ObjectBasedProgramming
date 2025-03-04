class BankAccount:
    def __init__(self, account_id, account_holder, balance, pin):
        self.account_holder = account_holder
        self.account_id = account_id
        self._balance = balance
        self.__pin = pin

    def get_balance(self):
        return self._balance

    def set_balance(self, amount):
        if amount <= 0:
            print("Invalid balance, please input the correct balance!")
        else:
            self._balance = amount
            print(f"{self.account_holder} set their balance to ${amount}. New balance: ${self._balance}")

    def verify_pin(self, input_pin):
        return input_pin == self.__pin

    def deposit(self, amount):
        if amount <= 0:
            print("Please input a correct deposit amount!")
        else:
            self._balance += amount
            print(f"{self.account_holder} deposited ${amount}. New balance: ${self._balance}")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"{self.account_holder} withdrew ${amount}. New balance: ${self._balance}")
        else:
            print("Insufficient funds!")

    def showInfo(self):
        return f"Account ID: {self.account_id}, Name: {self.account_holder}, Balance: ${self._balance}"



class SavingsAccount(BankAccount):
    def __init__(self, account_id, account_holder, balance, pin):
        super().__init__(account_id, account_holder, balance, pin)
        self.withdraw_limit = 500

    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print("Withdrawal limit cannot exceed $500")
        else:
            super().withdraw(amount)


class PremiumSavingsAccount(SavingsAccount):
    def __init__(self, account_id, account_holder, balance, pin):
        super().__init__(account_id, account_holder, balance, pin)
        self.withdraw_limit = 2000

    def withdraw(self, amount):
        if amount > self.withdraw_limit:
            print("Withdrawal limit cannot exceed $2000")
        else:
            super().withdraw(amount)

accounts = []
account_ids = set()


while True:
    print("\n--Menu--")
    print("1. List Accounts")
    print("2. Create Account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Set balance")
    print("6. Exit")

    menu = input("Select menu: ")

    if menu == "1":
        if not accounts:
            print("No accounts available.")
        else:
            for account in accounts:
                print(account.showInfo())

    elif menu == "2":
        status = input("Which account do you want to create? (1. Savings 2. PremiumSavings): ")
        account_holder = input("Please input your name: ")
        
        while True:
            account_id = input("Please input a unique account ID: ")
            if account_id in account_ids:
                print("This ID is already taken. Please choose another one.")
            else:
                account_ids.add(account_id)
                break
        
        balance = int(input("Insert balance: "))
        pin = int(input("Please input your PIN: "))

        if status == "1":
            accounts.append(SavingsAccount(account_id, account_holder, balance, pin))
        elif status == "2":
            accounts.append(PremiumSavingsAccount(account_id, account_holder, balance, pin))
        else:
            print("Invalid selection!")

    elif menu in ["3", "4", "5"]:
        account_id = input("Please input your account ID: ")
        account = next((acc for acc in accounts if acc.account_id == account_id), None)

        if not account:
            print("Invalid account ID!")
            continue

        input_pin = int(input("Please input your PIN: "))
        if not account.verify_pin(input_pin):
            print("Invalid PIN!")
            continue

        if menu == "3":
            amount = int(input("Insert deposit amount: "))
            account.deposit(amount)

        elif menu == "4":
            amount = int(input("Insert your withdraw amount: "))
            account.withdraw(amount)

        elif menu == "5":
            amount = int(input("Insert your new balance: "))
            account.set_balance(amount)

    elif menu == "6":
        print("Exiting the system...")
        break

    else:
        print("Invalid selection! Please try again.")