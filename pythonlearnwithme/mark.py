# print("Enter your name:")
# name=input()

# print("Enter your symbol number:")
# sym_number=int(input())

# print("enter your marks of physic:")
# physic=int(input())

# print("enter your marks of chemistry:")
# chemistry=int(input())
              
# print("enter your marks of Nepali:")
# # Nepali=int(input())

# print("enter your marks of english:")
# english=int(input())

# print("enter your marks of Biology:")
# biology=int(input())

# marks=(physic+chemistry+Nepali+english+biology)
# print("total marks obtained by",name,"is:",marks)


# percentage=(marks/500)*100
# if(percentage>=90):
#     print("CONGRATULATIONS",name,"you have secured A+ grade with",percentage,"% marks")
# elif(80<=percentage<90):
#      print("CONGRATULATIONS",name,"you have secured A grade with",percentage,"% marks")
# elif(70<=percentage<80):
#       print("CONGRATULATIONS",name,"you have secured B+ grade with",percentage,"% marks")
# elif(60<=percentage<70):
#       print("CONGRATULATIONS",name,"you have secured B grade with",percentage,"% marks")
# elif(50<=percentage<60):
#       print("CONGRATULATIONS",name,"you have secured C+ grade with",percentage,"% marks")
# elif(40<=percentage<50):
#       print("CONGRATULATIONS",name,"you have secured C+ grade with",percentage,"% marks")
# else:
#       print("INCOMPLETE!! THANKYOU ")



set={
    
}

x=int(input("enter a marks of nep"))
set.update({"nepali":x})

x=int(input("enter a marks of eng"))
set.update({"english":x})

x=int(input("enter a marks of math"))
set.update({"math":x})

x=int(input("enter a marks of science"))
set.update({"science":x})

x=int(input("enter a marks of social"))
set.update({"social":x})


print(set)