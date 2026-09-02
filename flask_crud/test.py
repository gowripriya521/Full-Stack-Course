import json
data = {}

# def create_user_core(email,name,age):
#     if email in data:
#         return False, "email already exist"
#     data[email] = {
#         "name":name,
#         "age":age
#     }
#     with open("./sample.json","w") as f:
#         json.dump(data,f,indent=4)
#     return True,"user created successfully"

# def read_data():
#     with open("./sample.json","r") as f:
#         res = json.load(f)
#     return res

# def update_user_core(email,name,age):
#     if email not in data:
#         return False,"email not found"
#     data[email] = {
#         "name": name,
#         "age": age
#     }
#     with open("./sample.json", "w") as f:
#         json.dump(data, f, indent=4)
#     return True,"user updated successfully"

# def delete_user_core(email):
#     if email not in data:
#         return False,"email not found"
#     del data[email]
#     with open("./sample.json", "w") as f:
#         json.dump(data, f, indent=4)
#     return True, "user deleted successfully"

# Student Management:
# Create a dictionary using roll_no as the key.
# Store name, age, and course.
# Write the data to students.json.
# Read and display all students.
# def create_user(roll_no,name,age,course):
#     if roll_no in data:
#         return False,"this roll no already exist"
#     data[roll_no]={
#         "name":name,
#         "age":age,
#         "course":course
#     }
#     with open("./student.json","w") as f:
#         json.dump(data,f,indent=4)
#     return True,"user created Successfull"
# create_user(101,"suresh",27,"sql")
# print(data)

# Employee Management:Use email as the key.
# Store name, age, and salary.
# Implement:Create,Read,Update,Delete
def create_user(email,name,age,salary):
    if email not in data:
        return False,"this mail already exist"
    data[email]={
        "name":name,
        "age":age,
        "salary":salary
    }
    with open("./sample.json","w") as f:
        json.dump(data,f,indent=4)
    return True