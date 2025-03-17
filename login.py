class Email:
    def login(self):
        email = input("Input your email address: ")
        password = input("Input your password: ")
        print(f"Logged in as {email}")
        return email, password


class Google:
    def login(self):
        print("Please login via Google")
        google_account = input("Enter your Google email: ")
        print(f"Logged in with Google account: {google_account}")
        return google_account


class Fingerprint:
    def login(self):
        print("Please authenticate using your fingerprint...")
        print("Fingerprint authenticated successfully!")


class LoginMenu:
    def __init__(self):
        self.methods = {
            "1": Email(),
            "2": Google(),
            "3": Fingerprint()
        }

    def run(self):
        while True:
            # Simplified menu
            print("\nSelect login method:")
            print("1. Email Login")
            print("2. Google Login")
            print("3. Fingerprint Authentication")
            print("0. Exit")
            
            choice = input("Enter choice (1/2/3/0): ")

            if choice == "0":
                print("Exiting...")
                break
            elif choice in self.methods:
                self.methods[choice].login()
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu = LoginMenu()
    menu.run()
