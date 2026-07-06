# class complex:
#     def __init__(self,real,img):
#         self.real=real
#         self.img=img

#     def show(self):
#         print(self.real ,"i +",self.img,"j")
    
#     def __sub__(self,num2):
#         Newreal=self.real-num2.real
#         Newimg=self.img-num2.img
#         return complex(Newreal,Newimg)

# num1=complex(2,5)
# num1.show()
# num2=complex(4,5)
# num2.show()
# num3=num1-num2
# num3.show()
# # num3=num1.add(num2)



# class circle:
#     def __init__(self,radius):
#         self.radius=radius
    
#     def area(self):
#         newvalue=3.1414*self.radius*self.radius
#         return newvalue
#     def perimeter(self):
#         newperi=2*3.1414*self.radius
#         return newperi
    
# c1=circle(12)
# print("Area of circle is :",c1.area())
# print("The perimeter of circle is ",c1.perimeter())


# class employee:
#     def __init__(self,role,dept,salary):
#         self.role=role
#         self.dept=dept
#         self.salary=salary

#     def detail(self):
#         print("Role: ",self.role)
#         print("department: ",self.dept)
#         print("salary: ",self.salary)

# # e1=employee("accountant","finance",40000)

# class engineer(employee):
#     def __init__(self,name,age,role,dept,salary):
#         super().__init__(role,dept,salary)
#         self.name=name
#         self.age=age
        
#     def detail(self):
#         print("Name: ",self.name)
#         print("Age: ",self.age)
#         super().detail()

# e1=engineer("Ronak",18,"Data Analyst","IT manager",40000)
# e1.detail()


#  using tunder function we print True/False i.e if order1 is greater then print True otherwise print False

class order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
        
    def __gt__(self,ord2):                # using thunder function 
        return self.price>ord2.price


ord1=order("Potato",120)
ord2=order("sugar",100)

print(ord1<ord2)