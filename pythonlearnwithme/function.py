# num1=int(input("enter a first  number:"))
# num2=int(input("enter a second number:"))
# num3=int(input("enter a third number:"))
# # def num(num1,num2):
# #     num=num1+num2
# #     return num

# # result=num(num1,num2)
# # print("the sum is :",result)

# def avg():
#     num=(num1+num2+num3)/3
#     return num

# result=avg()
# print("The average of 3 number is :",result)



# num1=(1,2,3,4,5,6,7)

# def num():
#     value=len(num1)
#     return value

# result=num()
# print("length of list is :",result)

# num1=(1,2,3,4,5,6,7)

# def num():
#   print(num1)

# print(num())

#factorial

# num=int(input("enter a number"))
# def facto(n):
#    fact=1
#    if(n==1 or n==0):
#       return 1
#    for i in range(1,n+1):
#       fact=fact*i 
#    return fact
   
# result=facto(num)
# print("The factorial is:",result)


# num=[1,2,3,4,5,6,7]

# def sum_value(num):
#     sum=0
#     for i in num:
#         sum+=num[i-1]
    
# result=sum_value(num)
# print("the total sum is:",result)

# amt=int(input("enter a amount of dollor to convert it in NPR: "))

# def money():
#     Npr=143.93
#     doll=amt*Npr
#     return doll

# print("Rs:",money())

rate=143.93

print("enter your choice")
print("1. convert npr into dollor")
print("2. convert dollor into npr")

choice=int(input("enter your choice (1 or 2)"))

def money(choice):
    if choice==1:
        npr=float(input("enter amount"))
        usd=npr/rate
        return usd
    elif choice==2:
        usd=float(input("enter amount"))
        npr=usd*rate
        return npr
    else:
        print("invalid")

result=money(choice)
print("Amount:",result)