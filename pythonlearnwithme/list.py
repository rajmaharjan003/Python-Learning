# num=[48,38,28,12,3,45,65]
# print(sorted(num))

# print(num[1:4])
# print(min(num))
# print(max(num))
# print(num[-4:-1])   


# num1=[1,23,4,5,6,4,3,2,5,6,7,2,4,5,4,45,45,65]

# print(num1.append(122))

# print(num1.sort())


# print(num1.sort(reverse =True))

# print(num1.reverse())
# print(num1)


# movie=input("enter movie name:")
# movie1=input("enter second movie name:")
# movie2=input("enter third movie name:")
# movies=[movie,movie1,movie2]
# print("your favourite movies are :",movies)

num=[1,2,3,2,1]
palin=num.copy()
palin.reverse()

if(palin==num):
    print("it is palindrome")
else:
    printI("it is not  palindrome")

num2=[1,2,4,6,4,3]
palin1=num2.copy()
palin1.reverse()

if(num2==palin1):
    print("it is palindrome")
else:
    print("it is not palindrome")



tup=["A","B","C","A","D","E","A","F","G","A"]

# print(tup.count("A"))
# print(tup.index("D"))
print(tup.sort())
print(tup)

