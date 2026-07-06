# print(".........................................................")
# print("                STUDENT MANAGEMENT SYSTEM                ")
# print(".........................................................")



# with open("management.txt","a+") as f:
#   f.read()
# def add_student():
#        f_name= input("Enter First Name: ")
#        l_name=input("Enter Last Name: ")
#        address=input("Enter your address: ")
#        phone=int(input("Enter your phone no: "))
#        email=input("Enter your Email-Address: ")
#        f.write("First Name: "+f_name+"\n")
#        f.write("Last Name: "+l_name+"\n")
#        f.write("Address: "+address+"\n")
#        f.write("phone No: "+str(phone)+"\n")
#        f.write("email: "+email+"\n")
    
# def view():
#      print("...............Student Information............... ")
#      print(add_student())

# def search():
#      search_word=input(" Enter word to search")
#      with open("management.txt","r") as f:
#           found=False
#           line_no=1
#           for line in f:
#                 if search_word.lower() in line.lower():  # case-insensitive search
#                    print(f"Found on line {line_no}: {line.strip()}")
#                    found = True
#                 line_no += 1
#           if not found:
#               print("No matching Found Result")
              
# def delete_record():
#     delete_name=input("Enter the student Name to delete")
#     with open("management.txt","r") as f:
#         f.readline()
#     with open("management.txt","w") as f:
#         found=False
#         skip=False
#         for line in lines:
#             if delete_name.lower() in line.lower() and "First Name: " in line:
#                 found= True
#                 skip = True
#                 continue
#             if skip:
#                 if all in line:
#                     skip= False
#                 continue 
#             f.write(line)
#         if found:
#             print(f"student {delete_name} record delete sucessfully" )
#         else:
#             print(f"No record found for {delete_name}")


# def menu():
#  while True:
#   print("1. Add Student")
#   print("2. View Student")
#   print("3. Search Student")
#   print("4. Delete Student")
#   print("5. Exit")
# # print(int(input("Enter Your choice : ")))
#   choice= int(input("Enter Your choice : "))

#   if(choice==1):
#       add_student()
#   elif(choice==2):
#       view()
#   elif(choice==3):
#       search()
#   elif(choice==4):
#       delete_record()
#   else:
#       print("Invalid choice. Thank you")
      

# menu()
print(".........................................................")
print("                STUDENT MANAGEMENT SYSTEM                ")
print(".........................................................\n")

# Function to add student
def add_student():
    with open("management.txt", "a") as f:
        f_name = input("Enter First Name: ")
        l_name = input("Enter Last Name: ")
        address = input("Enter your address: ")
        phone = input("Enter your phone no: ")
        email = input("Enter your Email Address: ")

        f.write("First Name: " + f_name + "\n")
        f.write("Last Name: " + l_name + "\n")
        f.write("Address: " + address + "\n")
        f.write("Phone No: " + phone + "\n")
        f.write("Email: " + email + "\n")
        f.write("---------------------------\n")

    print("Student information saved successfully.\n")


# Function to view all students
def view_students():
    print("\n...............Student Information...............\n")
    try:
        with open("management.txt", "r") as f:
            data = f.read()
            if data.strip() == "":
                print("No student records found.\n")
            else:
                print(data)
    except FileNotFoundError:
        print("No student records found.\n")


# Function to search student
def search_student():
    search_word = input("Enter the word to search: ")
    found = False
    line_no = 1
    try:
        with open("management.txt", "r") as f:
            for line in f:
                if search_word.lower() in line.lower():
                    print(f"Found on line {line_no}: {line.strip()}")
                    found = True
                line_no += 1
        if not found:
            print("No matching record found.\n")
    except FileNotFoundError:
        print("No student records found.\n")


# Function to delete student record
def delete_student():
    delete_name = input("Enter the Student First Name to delete: ")
    try:
        with open("management.txt", "r") as f:
            lines = f.readlines()

        with open("management.txt", "w") as f:
            skip = False
            found = False
            for line in lines:
                if delete_name.lower() in line.lower() and "First Name:" in line:
                    found = True
                    skip = True
                    continue
                if skip:
                    if "----------------" in line:
                        skip = False
                    continue
                f.write(line)

        if found:
            print(f"Student '{delete_name}' record deleted successfully.\n")
        else:
            print(f"No record found for '{delete_name}'.\n")
    except FileNotFoundError:
        print("No student records found.\n")


# Menu function
def menu():
    while True:
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit\n")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            add_student()
        elif choice == 2:
            view_students()
        elif choice == 3:
            search_student()
        elif choice == 4:
            delete_student()
        elif choice == 5:
            print("Thank you for using the Student Management System!")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the menu
menu()
