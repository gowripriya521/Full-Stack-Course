# 5 : Module Function
# Create a module mymodule.py
# Add a function add(a, b)
# Import the module in another file
# Ask the user for two numbers
# Handle invalid input using try-except
# Call the module function and print result
# def add_1(a,b):
#     return a+b
# 8 : Student Marks Module
# Create a module student.py
# Add function to calculate total marks
# Import module into another file
# Ask user for marks using loop
# Handle invalid input
# Print total and average
# def student_1(marks):
#     return sum(marks)
# import os
# os.remove("units.py")
# import os
# os.remove("student.txt")
# import os
# if os.path.exists("student.txt"):
#     os.remove("student.txt")
#     print("File deleted successfully")
# else:
#     print("File not found")
# file = open("student.txt", "w")
# file.close()
# import json
# print(json.dumps({"name": "John", "age": 30}))
# print(json.dumps(["apple", "bananas"]))
# print(json.dumps(("apple", "bananas")))
# print(json.dumps("hello"))
# print(json.dumps(42))
# print(json.dumps(31.76))
# print(json.dumps(True))
# print(json.dumps(False))
# print(json.dumps(None))
# import json
# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }
# json.dumps(x, indent=4, sort_keys=True)
#print(json.dumps(x, indent=4, separators=(". ", " = ")))
# print(json.dumps(x))
# print(json.dumps(x, indent=4))

# class Student:
#     def __init__(self, name):
#         self.name = name
# s1 = Student("Ram")
# print(s1.name)
# class Person:
#     def __init__(self, age):
#         self.__age = age
#     def set_age(self, age):
#         if age > 0:
#             self.__age = age
#         else:
#             print("Age must be positive")
#     def get_age(self):
#         return self.__age
# p1 = Person(25)
# p1.set_age(26)
# print(p1.get_age())
# print(dir(int))
# class Demo:
#     def __new__(cls):
#         print("Object is being created")
#         return super().__new__(cls)
#     def __init__(self):
#         print("Constructor called")
# d = Demo()


