# name=input("enter a name:")
# print(len(name))

#conditional statements

print("enter your name:")
name=input()
print("enter your age:")
age=int(int(input()))

if(age<18):
    print("Your are minior !! Not eligible for chunab voting")
elif (age<=18 or age<=50):
    print("your are young and eligible for voting")
else:
    print("your are seniour citizen ")

 