# # n=int(input("enter a number"))

# # def factorial(n):
# #     fact=1
# #     if(n==0 or n==1):
# #         return 1
# #     return n *factorial(n-1)

# # print("factorial",factorial(n))


# n=int(input("enter a number:"))

# def sum(n):
#     if(n==1):
#         return 1
#     return n+ sum(n-1)

# print("sum is:",sum(n))
    


#  tower of hanoi



# def tower_of_hanoi(n,source,helper,destination):
#     if(n==1):
#         print(f"disk from form {source} to {destination}")
#         return 
#     tower_of_hanoi(n-1,source,destination,helper)
#     print(f"disk move {n} from {source} to {destination}")

#     tower_of_hanoi(n-1,helper,source,destination)

# n=3
# tower_of_hanoi(n,"A","B","C")




def tower_of_hanoi(n,source,helper,destination):
    if(n==1):
        print(f"disk move from {source} to {destination}")
        return
    tower_of_hanoi(n-1,source,destination,helper)
    print(f"disk move {n} form {source } to {destination}")

    tower_of_hanoi(n-1,helper,source,destination)

n=3
print(tower_of_hanoi(n,"A","B","C"))
    