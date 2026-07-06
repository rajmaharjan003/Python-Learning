# class Student:
#     college_name="hilton"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         print("adding name")
    
# s1=Student("sita",23)
# print(Student.college_name)
# print(s1.name)
# print(s1.age)

# s2=Student("hari",22)
# print(Student.college_name)
# print(s2.name)
# print(s2.age)







# #     name="shyam"
# # S1=Student()
# # print(S1.name)

# # S2=Student()
# # print(S2.name)


# class person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age

# name=input("enter name:")
# age=int(input("enter age:"))

# s1=person(name,age)

# print("INFORMATION")
# print("Name :",s1.name)
# print("Age: ",s1.age)

# class car:
#     def __init__(self,brand,price):
#         self.brand=brand
#         self.price=price

# b1=car("Toyota" ,5000000)


# print(f"Car brand is {b1.brand} and price is {b1.price}")
# print("THANK YOU")


# class book:
#     def __init__(self,title,author):
#         self.title=title
#         self.author=author

# b1=book("the ship man","the man vs wild")
# a1=book("harry","rohan")

# print(f" the title is {b1.title} and the author is {a1.author}")
# print(f"the book title us {b1.title} and the author is {a1.author}")



# class student:
#     def __init__ (self,name,age,email):
#         self.name=name
#         self.age=age
#         self.email=email

# name=input("Enter your name :")
# age=int(input("Enter your age :"))
# email=input("Enter your email address :")

# s1=student(name,age,email)

# print(
#     "Information "
# )

# print(f"My name is {s1.name} and  i am {s1.age} years old. My email address is {s1.email} ")



class student:
    def __init__ (self,name,phy,chem,bio):
        self.name=name
        self.phy=phy
        self.chem=chem
        self.bio=bio
    
    def marks(self):
       return (self.phy+self.chem+self.bio)/3  

name=input("enter your name :")
phy=int(input("enter the marks of physic :"))
chem=int(input("enter the marks of chemistry :"))
bio=int(input("enter the marks of Biology :"))

s1=student(name,phy,chem,bio)
print(" Result")
print("Name:",s1.name)
print("the average marks is ",s1.marks())