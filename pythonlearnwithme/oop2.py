# class student:
#     def __init__(self,name,age,grade):
#         self.name=name
#         self.age=age
#         self.grade=grade

# name=input("enter your name :")
# age=int(input("enter your age:"))
# grade=int(input("enter your grade"))

# s1=student(name,age,grade)

# print("INFORMATION")

# print("Name:",s1.name)
# print("Age:",s1.age)
# print("Grade: ",s1.grade)



class bankaccount:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.balance=balance

def deposit(self,amount):
    if amount >0:
        self.balance+=amount
        print(f"deposited :{amount}")
    else:
        print("deposited amount must be positive")

def withdraw(self,amount):
    if amount>self.balance:
        print("insufficent balance")
    elif amount<=0:
        print("withdraw amount must be positive")
    else: 
        self.balance-=amount
        print(f"withdraw amount:{amount}")

def check_balance(self):
    print(f"current Balance:{self.balance}")

name = input("Enter account holder name: ")
balance = float(input("Enter initial balance: "))

# Creating object
a1 = bankaccount(name, balance)

amount = float(input("Enter amount to deposit: "))
a1.deposit(amount)

# Withdraw
amount = float(input("Enter amount to withdraw: "))
a1.withdraw(amount)

# Check balance
a1.check_balance()