# # Simple Inheritance
# # Create a class Animal with attributes name and age.
# # Add a method speak().
# # Create a child class Dog that inherits from Animal.
# # Create an object of Dog and access parent properties.

# class Animal:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
    
#     def speak(self):
#         print("animal make sound")

# class Dog(Animal):
#     def __init__(self,name,age):
#         super().__init__(name,age)

#     def speak(self):
#         print("Bark Bark")

# d1=Dog("Bhote kukur",10)
# print(d1.name)
# print(d1.age)
# d1.speak()




# Constructor Inheritance
# Create a class Vehicle with attributes brand and model.
# Create a child class Car that inherits from Vehicle.
# Use super() to initialize the parent constructor.


# class Vehicle:
#     def __init__(self,brand,model):
#         self.brand=brand
#         self.model=model

# class Car(Vehicle):
#     def __init__(self,brand,model):
#         super().__init__(brand,model)
        

# c1=Car("Tesla",2025)
# print("Brand :",c1.brand)
# print("Model :",c1.model)
# print("Thank You")






# Adding New Methods in Child Class

# Create a class Shape with method area().

# Create a child class Rectangle with additional attributes length and width.

# Override the area() method.


# class shape:
#     # @property
#     def area(self):
#         print("area method in class")

# class rectangle(shape):
#     def __init__(self,length,height):
#         self.length=length
#         self.height=height
    
#     def area(self):
#         return self.length *self.height

# r1=rectangle(12,12)

# r1.length=12
# r1.height=15
# print(r1.area())


# Create class Grandparent

# Inherit Parent from Grandparent

# Inherit Child from Parent

# Show how methods are accessed in multilevel inheritance.


class grandparent:
    @staticmethod
    def grand():
        print("I am the oldest member in the family.")

class parents(grandparent):
    def parent(self):
        print("I am the parents of child")

class child(parents):
    def __init__(self,member):
        self.member=member
    def chil(self):
        print("i am the youngest")

c1=child("grandparent")
c1.grand()
c1.parent()
c1.chil()


