# # class car:
# #     def __init__(self,type):
# #         self.type=type


# #     @staticmethod
# #     def start():
# #         print("car statrted...")

# #     @staticmethod
# #     def stop():
# #         print("car stop...")


# # class toyota(car):
# #     def __init__(self,brand,type):
# #         super().__init__(type)
# #         self.brand=brand
# #         super().start()

# # car1=toyota("royal","electic")
# # print(car1.brand)
# # print(car1.type) 
# # print(car1.stop())      

# # class furtuner(toyota):
# #     def __init__(self,name):
# #         self.name=name

# # car1=furtuner("petrol")
    



# # class A:
# #     varA="welcome to class A"

# # class B:
# #     varB="welcome to class B"

# # class C(A,B):
# #     varC="welcome to class C"

# # c1=C()
# # print(c1.varA)
# # print(c1.varB)
# # print(c1.varC)


# class student:
#     name="hello world"
#     # def changename(self,name):
#     #     # student.name=name
#     #     self. __class__.name="Raj"

#     @classmethod
#     def changeName(self,name):
#         self.name=name

# s1=student()
# s1.changeName("shyam Lal")
# print(s1.name)
# print(student.name)



#  property decirator

class marks:
    def __init__(self,phy,chem,bio,math):
        self.phy=phy
        self.chem=chem
        self.bio=bio
        self.math=math

    @property
    def percentage(self):
        return str((self.phy+self.chem+self.bio+self.math)/4)
    
m1=marks(66,88,87,44)
m1.phy=88
m1.math=90
print(m1.percentage)
