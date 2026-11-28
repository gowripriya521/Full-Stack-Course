# Question 1: Count the frequency of each character
# Question: Given a string, count how many times each character appears. Store each character and its count in a dictionary.
# Given data:
# text = "python programming"
# Expected output:
# {    'p': 2,    'y': 1,    't': 1,    'h': 1,    'o': 2,    'n': 2,    ' ': 1,    'r': 2,    'g': 2,    'a': 1,    'm': 2,    'i': 1}
# Rules:
# - Use a dictionary.
# - Use a for loop.
# - If the character already exists, increase its count.
# - Otherwise, add it with count 1.

x="python programming"
temp={}
for i in x:
    if i in temp:
        temp[i]+=1
    else:
        temp[i]=1
print(temp)

# Question 2: Find the student with the highest marks
# Question: Given a dictionary containing student names and their marks, find the student who scored the highest marks.
# Given data:
# students = {    "Rahul": 85,    "Priya": 92,    "Sam": 78,    "Anil": 95,    "Ravi": 88}
# Expected output:
# Highest marks: 95
# Student name: Anil
# Rules:
# - Use a for loop.
# - Compare the marks of each student.
# - Do not use max().
students = {"Rahul": 85,"Priya": 92,"Sam": 78,"Anil": 95,"Ravi": 88}
s=0
e=0
for key,value in students.items():
    if value>e:
        e=value
        s=key
print(f"Highest marks:{e} Student name:{s}")

# Question 3: Find the student with the lowest marks
# Question: Given a dictionary of student names and marks, find the student who scored the lowest marks.
# Given data:
# students = {"Rahul": 85,"Priya": 92,"Sam": 38,"Anil": 95,"Ravi": 45}
# Expected output:
# Lowest marks: 38
# Student name: Sam
# Rules:
# - Use a for loop.
# - Compare each student's marks.
# - Do not use min().
students = {"Rahul": 85,"Priya": 92,"Sam": 38,"Anil": 95,"Ravi": 45}
s=0
e=0
for key,value in students.items():
    if e==0 or value<e:
        e=value
        s=key
print(f"lowest marks:{e} Student name:{s}")

# Question 4: Count employees in each department
# Question: Given a list of employees and their departments, count how many employees belong to each department.
# Given data:
# employees = [{"name":"Rahul","department":"IT"},{"name":"Priya","department":"HR"},{"name":"Sam","department":"IT"},{"name":"Anil","department":"Finance"},{"name":"Ravi","department":"HR"},{"name": "Kiran","department": "IT"}]
# Expected output:
# {    "IT": 3,    "HR": 2,    "Finance": 1}
# Rules:
# - Use a dictionary to store department counts.
# - Use a for loop.
# - Check whether the department already exists.
# employees = [{"name":"Rahul","department":"IT"},{"name":"Priya","department":"HR"},{"name":"Sam","department":"IT"},{"name":"Anil","department":"Finance"},{"name":"Ravi","department":"HR"},{"name": "Kiran","department": "IT"}]



# Question 5: Find duplicate values in a dictionary
# Question: Given a dictionary containing employee names and their salaries, find the salary values that appear more than once.
# Given data:
# employees = {"Rahul": 30000,"Priya": 40000,"Sam": 30000,"Anil": 50000,"Ravi": 40000,"Kiran": 60000}
# Expected output:
# Duplicate salaries: [30000, 40000]
# Rules:
# - Use a for loop.
# - Use a list or another dictionary to track values.
# - Do not print the same duplicate salary multiple times.
# employees = {"Rahul": 30000,"Priya": 40000,"Sam": 30000,"Anil": 50000,"Ravi": 40000,"Kiran": 60000}

        
# Question 6: Merge two dictionaries without using update()
# Question: Given two dictionaries, combine them into a new dictionary without using the update() method.
# Given data:
# dict1 = {    "name": "Rahul",    "age": 22,    "city": "Madanapalle"}dict2 = {    "course": "Python",    "marks": 85}
# Expected output:
# {    "name": "Rahul",    "age": 22,    "city": "Madanapalle",    "course": "Python",    "marks": 85}
# Rules:
# - Create a new empty dictionary.
# - Use for loops.
# - Copy the key-value pairs from both dictionaries.
# - Do not use update().

# Question 7: Filter students based on marks
# Question: Given a dictionary of student names and marks, create a new dictionary containing only students who scored above 75.
# Given data:
# students = {    "Rahul": 85,    "Priya": 72,    "Sam": 90,    "Anil": 65,    "Ravi": 80,    "Kiran": 50}
# Expected output:
# {    "Rahul": 85,    "Sam": 90,    "Ravi": 80}
# Rules:
# - Create a new dictionary.
# - Use a for loop.
# - Use if marks > 75.
# - Keep both the student name and marks.

# Question 8: Calculate the total shopping cart price
# Question: Given a shopping cart dictionary containing product names and their prices, calculate the total price of all products.
# Given data:
# cart = {    "Laptop": 50000,    "Mouse": 500,    "Keyboard": 1500,    "Monitor": 10000}
# Expected output:
# Total shopping cart price: 62000
# Rules:
# - Use a for loop.
# - Access dictionary values.
# - Use a variable called total.
# - Do not use sum().

# Question 9: Find the key with the maximum value
# Question: Given a dictionary containing product names and their sales amounts, find the product that generated the highest sales.
# Given data:
# sales = {    "Laptop": 50000,    "Mobile": 30000,    "Tablet": 20000,    "Monitor": 60000,    "Keyboard": 15000}
# Expected output:
# Highest selling product: Monitor
# Sales amount: 60000
# Rules:
# - Use a for loop.
# - Compare dictionary values.
# - Store both the product name and sales amount.
# - Do not use max().

# Question 10: Count word frequency in a sentence
# Question: Given a sentence, count how many times each word appears and store the results in a dictionary.
# Given data:
# sentence = "python is easy and python is powerful"
# Expected output:
# {    "python": 2,    "is": 2,    "easy": 1,    "and": 1,    "powerful": 1}
# Rules:
# - Use split() to separate words.
# - Use a dictionary.
# - Use a for loop.
# - If a word already exists, increase its count.

# Real-world challenge: Student Grade Management
# Question: You are developing a student result management system. You have a dictionary containing student names and their marks.
# Your task is to check each student's marks and assign a grade.
# Given data:
# students = {    "Rahul": 95,    "Priya": 82,    "Sam": 65,    "Anil": 35,    "Ravi": 90,    "Kiran": 40}
# Grade conditions:
# Marks	Grade
# 90 and above	A Grade
# 75–89	B Grade
# 40–74	C Grade
# Below 40	Fail
# Expected output:
# Rahul: A Grade
# Priya: B Grade
# Sam: C Grade
# Anil: Fail
# Ravi: A Grade
# Kiran: C Grade
# Rules:
# 1. Use a dictionary.
# 2. Use a for loop.
# 3. Use if, elif, and else.
# 4. Check every student's marks.
# 5. Print the student name and corresponding grade.