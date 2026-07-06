# seq=range(10)
# for i in seq:
#     print(i)


# for i in range(3,20):
#     print(i)

# for i in range(2,50,2):
#     print(i)

# for i in range(1,101):
#     print(i)

# for i in range(100,0,-1):
#     print(i)

# n=int(input("Enter a number:"))
# for i in range(1,11):
#     print(n,"X",i,"=",n*i)



# n=int(input("Enter a number:"))
# n=5
# sum=0
# for i in range(n):
# #     sum +=i
# #     print ("total sum :",sum)


# # n=int(input("Enter a number:"))
# # fact=1
# # for i in range(1,n+1):
# #  fact=fact*i

# # print("factorial is:",fact)

# # num=int(input("Enter a number:"))
# # fact=1
# # while num>=1:
# #     fact=fact*num
# #     num=num-1

# # print("factorial is :",fact)



# # n=int(input("Enter a number:"))

# # sum=0
# # while n>=0:
# #     sum+=n
# #     n=n-1

# # print("Total sum is:",sum)


# # Print the square of numbers from 1 to 10.

# for i in range(1,11):
#     print("square no is:",i*i)

# # Print each character of a string.
# name="python"

# for char in name:
#     print(char)


# for i in range(10,0,-1):
#     print(i)


# num=[1,2,3,4,5]

# sum=0
# for i in num:
#     sum+=num[i-1]

# print("total is :",sum)



a= float(input("Enter Number:"))
b= float(input("Enter Number:"))

choose=input("Enter operator: +,-,*,/")

if choose=="+":
    print("a+b=",a+b)
elif choose=="-":
    print("a-b=",a=b)
elif choose=="*":
    print("a*b=",a*b)
elif choose=="/":
    print("a/b=",a/b)
else:
    print("please enter correct oprator") 

print("............THANKYOU.............")   



# Print all numbers divisible by 5 between 1 and 100.
for i in range(1,101):
    if i%5==0:
        print(i)
