# num1=int(input("Enter a number to convert USD into NPR. :"));

# def num(num1):
#     if(num1>0):
#         result=num1*152.55;
#         print("The exchange money is Rs.",result);
#     else:
#         print("please take number")
    

# num(num1);


# num=int(input("enter a number"));


# def fact(num):
#     fact=1;
#     if(num>0):
#         for i in range(1,num+1):
#             fact =i* fact;
#         print("the factorial value is :",fact);
#     else:
#         print("please enter a valid number");

# fact(num);



# n=int(input("Enter a number:"));

# def fact(n):
#     if(n==0 or n==1):
#         return 1;
#     else:
#         return n*fact(n-1);
# print(f"the factorial value of {n} is ",fact(n));

# n=int(input("Enter a number"))
# def num(n):
#     sum=0;
#     for i in range(0,n+1):
#        sum+=i;
#     return sum;
# print("the sum is ",num(n));

# def lit(list,idx=4):
#     if(idx==len(list)):
#         return
#     print(list[idx]);
#     print(list,idx+1);

# fruits=["apple","banana","mango","juice","sitamol"];
# lit(fruits)


# multiplication table
# n=int(input("Enter a number :"));
# def mul(n):
#     for i in range(1,11):
#         print(f"{n} X {i} = {i*n}");

# mul(n);

# n=int(input("Enter a number:"));
# def rev(n):
#     if n>0:
#         return n;
#     else:
#         return (n-1);
# print("rev",rev(n));


# Write a menu-driven program using functions:

# 1. Add
# 2. Subtract
# 3. Multiply
# 4. Divide
# 5. Factorial
# 6. Exit

print("..............MENU................")
print("1.Addition");
print("2.subtraction");
print("3.multiplication");
print("4.Division");
choice=int(input("Enter your choice :"));
a=int(input("Enter a first number :"));
b=int(input("Enter a second number :"));

def add(a,b):
    result1=a+b
    print("sum is ",result1)
def sub(a,b):
    sub1= a-b
    print("sub is ",sub1)
def mul(a,b):
    mul1= a*b
    print("multiplication",mul1)
def div(a,b):
    if b==0:
        print("cannot divide")
    elif a>b:
        div1=a/b
        print("division is ",div1);
    else:
        print("error")

if choice==1:
    add(a,b)
elif choice==2:
    sub(a,b)
elif choice==3:
    mul(a,b)
elif choice==4 :
    div(a,b)
else:
    print("please enter a number from 1-4");
    
    