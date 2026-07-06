# with open("search.txt","w") as f:
#     f.write(" Name: Raj Maharjan" \
#     "\n Age:12" \
#     "\n Address:Dhapakhel")


# search_word=input("Enter a word for search ")
# found=False
# line_no=1
# try:
#     with open("search.txt","r") as f:
#         for line in f:
#             if search_word.lower() in line.lower():
#                 print(f"found in {line_no} : {line.strip()}")
#                 found=True
#             line_no+=1
#     if not found:
#         print("No record found \n")
# except:
#     print("No record!! Thankyou")    
            

    


def check():
  name=input("Enter your name:")
  age=int(input("Enter your age:"))
  add=input("Enter your address:")

  with open("search.txt","a") as f:
    f.write(f" Name:{name}\n Age:{age} \n Address:{add} \n")
    f.write("------------------------- \n")

check()


# search_word=input("Enter the word for the search: ")
# found=False
# line_no=1


# try:
#     with open("search.txt","r") as f:
#         for line in f:
#             if search_word.lower() in line.lower():
#                 print(f"found in {line_no} : {line.strip()}")
#             line_no+=1
#     if not found:
#         print("No record found!!")

# except FileNotFoundError:
#     print("Not Found !! Try Again!!")



delete_name=input("Enter the name to delete ")
found =False
skip=False

try:
    with open("search.txt","r") as f:
        lines =f.readlines()
    with open("search.txt","w") as f:
        for line in lines:
            if delete_name.lower() in line.lower() and "Name:" in line:
                found=True
                skip=True
                continue
            if skip:
                if "-------------" in line:
                    skip=False
                continue
            f.write(line)
             
        if found:
            print(f"Name {delete_name} record delete successfully")
        else:
            print(f"No record found for {delete_name}")
except FileNotFoundError:
    print("file not found")








































