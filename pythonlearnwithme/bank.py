import os

class Bank:
    def __init__(self, balance=0):
        self.balance = balance
        self.logged_in = False   # 🔐 Track login status

    # ---------------- SIGNUP ----------------
    def signup(self):
        f_name = input("Enter Your First Name: ")
        l_name = input("Enter Your Last Name: ")
        dob = input("Enter Your Date of Birth: ")
        address = input("Enter Your Address: ")
        phone = input("Enter Your Phone Number: ")
        email = input("Enter Your Email Address: ")
        password = input("Enter Password: ")

        file_exists = os.path.isfile("bankrecord.csv")

        with open("bankrecord.csv", "a") as f:
            if not file_exists:
                f.write("First Name,Last Name,Date of Birth,Address,Phone,Email,Password\n")

            f.write(f"{f_name},{l_name},{dob},{address},{phone},{email},{password}\n")

        print("Signup successful!\n")

    # ---------------- LOGIN ----------------
    def login(self):
        phone = input("Enter your phone number: ")
        password = input("Enter your password: ")

        try:
            with open("bankrecord.csv", "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    if len(data) >= 7:
                        if data[4] == phone and data[6] == password:
                            print("Login successful!\n")
                            self.logged_in = True   # ✅ User logged in
                            return
            print("Invalid phone number or password.\n")
        except FileNotFoundError:
            print("No records found.\n")

    # ---------------- DEPOSIT ----------------
    def deposit(self):
        if not self.logged_in:
            print("Please login first!\n")
            return

        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print("Deposit successful.\n")
        else:
            print("Amount must be positive.\n")

    # ---------------- WITHDRAW ----------------
    def withdraw(self):
        if not self.logged_in:
            print("Please login first!\n")
            return

        amount = float(input("Enter amount to withdraw: "))
        if amount > self.balance:
            print("Insufficient balance.\n")
        elif amount <= 0:
            print("Amount must be positive.\n")
        else:
            self.balance -= amount
            print("Withdrawal successful.\n")

    # ---------------- CHECK BALANCE ----------------
    def check_balance(self):
        if not self.logged_in:
            print("Please login first!\n")
            return

        print("Total Balance:", self.balance, "\n")

    # ---------------- DELETE ACCOUNT ----------------
    def delete_acc(self):
        if not self.logged_in:
            print("Please login first!\n")
            return

        delete_phone = input("Enter phone number to delete: ")
        found = False

        try:
            with open("bankrecord.csv", "r") as f:
                lines = f.readlines()

            with open("bankrecord.csv", "w") as f:
                for line in lines:
                    if delete_phone in line:
                        found = True
                        continue
                    f.write(line)

            if found:
                print("Account deleted successfully.\n")
                self.logged_in = False  # Logout after delete
            else:
                print("No record found.\n")

        except FileNotFoundError:
            print("No records found.\n")


# Create object
b1 = Bank()

# ---------------- MENU ----------------
def menu():
    while True:
        print("===== BANK MENU =====")
        print("1. Sign Up")
        print("2. Login")
        print("3. Deposit")
        print("4. Withdraw")
        print("5. Check Balance")
        print("6. Delete Account")
        print("7. Exit\n")

        choice = input("Enter Your Choice: ")

        if choice == "1":
            b1.signup()
        elif choice == "2":
            b1.login()
        elif choice == "3":
            b1.deposit()
        elif choice == "4":
            b1.withdraw()
        elif choice == "5":
            b1.check_balance()
        elif choice == "6":
            b1.delete_acc()
        elif choice == "7":
            print("Thank you for using the Bank System!")
            break
        else:
            print("Invalid choice. Please try again.\n")


menu()
