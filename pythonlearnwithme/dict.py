# student={
#     "name":"Raj Maharjan",
#     "age":18,
#     "Address":"Dhapakhel",
#     "subjects":["Nepali","English","Math","Science"],
#     "phone":980000000
# }
# print(student["Address"]) 

# info={
#     "name":"Shyam Thapa",
#     "course":{
#         "physic":44,
#         "Nepali":33,
#         "math":55,
#         "Biology":77
#     }
# }

# info["course"]["math"]=77
# print(info.keys())
# print(info.values())
# print(info.items())
# print(info.get("name"))
# print(info.get("course"))


# sts={
#     "name":"suhan Maharjan",
#     "age ":5,
#     "address":"sanogau",
#     "school":"LA",
#     "course":{
#         "math":1000,
#         "science":800,
#         "social":500
#     }
# }


# sts["course"]["Nepali"]=500

# print(sts.keys())
# print(sts.values())
# print(sts.items())
# print(sts.get("school"))
# print(sts.get("course"))
# print(list(sts.values()))

# tup=list(sts.items())
# print(tup[0])




# new_info={
#     "Mother's name": "hema Maharjan",
#     "Father's name":"Sudon Maharjan"
# }
# sts.update(new_info)
# print(sts)

# # print(list(sts.get("course")))
# print("............THANKYOU............")


st={
    "name":"shyam ",
    "age":22,
    "course":
{
        "math":88,
        "science":77,
        "social":66
}}

print(st.values())
print(st.items())
print(st.get("course"))
print(st.update({"address":"Lalitpur"}))
print(st),