# collect = set()
# # collect.add("apple")
# # print(collect.remove("apple"))
# print(collect.add("pinepapple"))

# collect.clear()

# collect={1,2,5,6,4,6}
# collect.pop()

# collect.remove(4)
# collect.add(777)
# collect.clear()
# print(collect)
# print(type(collect))

# A={1,2,3,5,6,4,3,2}
# B={2,3,5,3,2,3,4,6,7,8}
# print(A.union(B))
# print(A.intersection(B))

# fruits={"apple","banana","mango","apple","banana","pineapple"}
# fruit={"banana","dragonfruit","apple","mango","naspati"}

# print(fruits.union(fruit))
# print(fruit.intersection(fruits))


# sub={"python","java","c++","python","javascript","java","python","java","c++","c"}
# print(len(sub))



sub={

}

# sub["nepali"]=20
# sub["english"]=25
# sub["math"]=20


x=int(input("enter a marks of nepali"))
sub.update({"nepali":x})

x=int(input("enter a marks of english"))
sub.update({"english":x})

x=int(input("enter a marks of math"))
sub.update({"math":x})
print(sub)

