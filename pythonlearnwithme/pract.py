# with open("practice.txt","r") as f:
#     data=f.read()
#     new_data=data.replace("Java","Python")
#     print(new_data)

# with open("practice.txt","a+") as f:
#     f.write(new_data)

# with open("practice.txt","r") as f:
#     data=f.read()
#     if(data.find("learning") != -1):
#         print("found")
#     else:
#         print("not found")


# def check_line():
#     word="Java"
#     data=True
#     line_no=1
#     with open("practice.txt","r") as f:
#         while data:
#             data= f.readline()
#             if(word in data):
#                 print(line_no)
#                 return
#             line_no += 1
#     return -1

# print(check_line())    
count=0   
with open("practice.txt","a+") as f:
    number=[1,3,4,2,5,6,7,8,9,22,21,32,31]
    data=f.write(" ,".join(map(str,number)))
    for val in number:
        if(int(val)%2==0):
            count+=1
print(count)

    