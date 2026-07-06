x=(1,4,9,16,25,36,49,64,81,100)

# for num in val:
#     print(num)
y=int(input("enter an number:"))
idx=0
for num in x:
    if(num==y):
        print(" number found at",idx)
        break
    idx=+1   
else:
    print("not found")
