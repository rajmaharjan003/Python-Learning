import os

class Contact:
    def __init__(self):
        self.logged_in = False

    # ---------------- CREATE ACCOUNT ----------------
    def create(self):
        name = input("Enter your name: ")
        phone_no = input("Enter your phone number: ")
        email = input("Enter your email: ")
        dob = input("Enter your date of birth: ")
        password = input("Enter password: ")

        file_exists = os.path.isfile("users.csv")

        with open("users.csv", "a") as f:
            if not file_exists:
                f.write("Name,Phone,Email,DOB,Password\n")
            f.write(f"{name},{phone_no},{email},{dob},{password}\n")

        print("Signup successful!\n")

    # ---------------- LOGIN ----------------
    def login(self):
        name = input("Enter username: ")
        password = input("Enter password: ")

        try:
            with open("users.csv", "r") as f:
                for line in f:
                    data = line.strip().split(",")
                    if data[0] == name and data[4] == password:
                        print("Login successful!\n")
                        self.logged_in = True
                        return
            print("Invalid username or password.\n")
        except FileNotFoundError:
            print("No records found.\n")

    # ---------------- ADD CONTACT ----------------
    def add_contact(self):
        if not self.logged_in:
            print("Please login first!\n")
            return

        name = input("Enter Name: ")
        email = input("Enter email address: ")
        phone = input("Enter phone number: ")
        address = input("Enter address: ")

        file_exists = os.path.isfile("contactbook.csv")

        with open("contactbook.csv", "a") as f:
            if not file_exists:
                f.write("Name,Email,Phone,Address\n")
            f.write(f"{name},{email},{phone},{address}\n")

        print("Contact added successfully!\n")

    # ---------------- VIEW CONTACT ----------------
    def view_contact(self):
        if not self.logged_in:
            print("Please login first!\n")
            return

        try:
            with open("contactbook.csv", "r") as f:
                print("\n----- Contact List -----")
                print(f.read())
        except FileNotFoundError:
            print("No contacts found.\n")

    # ---------------- DELETE CONTACT ----------------
    def delete(self):
        if not self.logged_in:
            print("Please login first!\n")
            return

        delete_name = input("Enter name to delete: ")
        found = False

        try:
            with open("contactbook.csv", "r") as f:
                lines = f.readlines()

            with open("contactbook.csv", "w") as f:
                for line in lines:
                    if delete_name not in line:
                        f.write(line)
                    else:
                        found = True

            if found:
                print("Contact deleted successfully!\n")
            else:
                print("No record found.\n")

        except FileNotFoundError:
            print("No contacts found.\n")


# ---------------- MENU ----------------
c1 = Contact()

def menu():
    while True:
        print("------ Contact Book App ------")
        print("1. Create Account")
        print("2. Login")
        print("3. Add Contact")
        print("4. View Contact")
        print("5. Delete Contact")
        print("6. Exit")

        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input.\n")
            continue

        if choice == 1:
            c1.create()
        elif choice == 2:
            c1.login()
        elif choice == 3:
            c1.add_contact()
        elif choice == 4:
            c1.view_contact()
        elif choice == 5:
            c1.delete()
        elif choice == 6:
            print("Thank you!")
            break
        else:
            print("Invalid choice.\n")

menu()
