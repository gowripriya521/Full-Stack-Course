# ==============08-0-2026==================#
# 1 : Even or Odd Function
# Create a function check_number()
# Ask the user to enter a number
# Use try-except to handle invalid input
# Use if statement to check:
# even
# odd
# Print the result
# def check_number():
#     user = int(input("enter a number:"))
#     try :
#         if user%2==0:
#             print("even number")
#         else:
#             print("odd numbers")
#     except Exception as e:
#         print("invalid error")
# check_number()
# 2 : Sum of Numbers Using Loop
# Ask the user how many numbers they want to enter
# Use a loop to take numbers
# Handle invalid input using try-except
# Find the total sum
# Print the result
# def sum_1():
#     total=0
#     try:
#         user = int(input("enter how many numbers:"))
#         for i in range(user):
#             n=int(input("enter a numbers:"))
#             total=total+n
#         print("total",total)
#     except Exception as e:
#         print("invalid input")
# sum_1()
# 3 : Multiplication Table
# Create a function table()
# Ask the user to enter a number
# Handle invalid input
# Use a for loop to print multiplication table from 1 to 10
# def function_1():
#     try:
#         user = int(input("enter a number:"))
#         for i in range(1,11):
#             # print(user,"x",i,"=",user*i)
#             print(f"{user} x{i}={user*i}")
#     except Exception as e:
#         print("invalid input",e)
# function_1()
# 4 : Positive Number Checker
# Create a function positive()
# Ask the user for a number
# Use if statement:
# if negative → raise exception
# Handle the error using except
# Print suitable message
# def function_1():
#     try:
#         user = int(input("enter a number:"))
#         if user<0:
#             raise ValueError("negative numbers not allowed")
#         print("positive number")
#     except Exception as e:
#         print("invalid input",e)
# function_1()
# 5 : Module Function
# Create a module mymodule.py
# Add a function add(a, b)
# Import the module in another file
# Ask the user for two numbers
# Handle invalid input using try-except
# Call the module function and print result
# import mymodule
# try:
#     a = int(input("enter a numbers:"))
#     b = int(input("enter a numbers:"))
#     print(mymodule.add_1(a,b))
# except Exception as e:
#     print("invalid valid",e)
# 6 : Login System
# Create a correct password variable
# Use a loop to allow 3 attempts
# Use if statement to check password
# Print:
# "Login successful"
# or "Wrong password"
# Use try-except if input causes error
# def corr_1():
#     password="Learn"
#     count =3
#     try:
#         while count>0:
#             user = input("enter the password:")
#             if user==password:
#                 print("login successful")
#                 break
#             else:
#                 count-=1
#                 print("wrong password")
#     except Exception as e:
#         print("invalid input",e)
# corr_1()
# 7 : List Average Program
# Create a function average()
# Use loop to take 5 numbers from user
# Store them in a list
# Handle invalid input
# Find average and print it   
# def function_ave():
#     n=[]
#     while len(n)<5:
#         try:
#             user=int(input("enter a number:"))
#             n.append(user)
#         except Exception as e:
#             print("invalid input",e)
#     total=sum(n)
#     avg=total/len(n)
#     print("average=",avg)
# function_ave()
# 8 : Student Marks Module
# Create a module student.py
# Add function to calculate total marks
# Import module into another file
# Ask user for marks using loop
# Handle invalid input
# Print total and average
# import mymodule
# marks = []
# try:
#     for i in range(3):
#         user= int(input("enter a marks:"))
#         marks.append(user)
#     total = mymodule.student_1(marks)
#     average = total/len(marks)
#     print("total:",total)
#     print("Average:",average)
# except Exception as e:
#     print("invalid input",e)
# 9.Odd and Even Counter
# Create a function count_numbers()
# Ask the user to enter 5 numbers using loop
# Use if statement to count:
# even numbers
# odd numbers
# Handle invalid input using try-except
# Print total even and odd numbers
# def count_number():
#     even=0
#     odd=0
#     try:
#         for i in range(5):
#             user=int(input("enter a number:"))
#             if user%2==0:
#                 even+=1
#             else:
#               odd+=1
#         print("even numbers:",even)
#         print("odd numbers:",odd)
#     except Exception as e:
#          print("invalid input",e)
# count_number()
# 10.Largest Number Finder
# Create a function largest()
# Ask user to enter 3 numbers
# Use if-elif to find largest number
# Handle invalid input
# Print the largest number
# def largest_1():
#     try:
#         big=0
#         for i in range(3):
#             num=int(input("enter a number:"))
#             if i==0:
#                 big=num
#             elif num>big:
#                 big=num
#         print("largest number :",big)
#     except Exception as e:
#         print("invalid input",e)
# largest_1()
# 11.Countdown Program
# Create a function countdown()
# Ask user for starting number
# Use while loop to count down to 1
# Handle invalid input
# Print "Time Over" at end
# def countdown():
#     try:
#         user = int(input("enter a number:"))
#         while user>=1:
#             print(user)
#             user-=1
#         print("Time over")
#     except Exception as e:
#         print("invalid input",e)
# countdown()
# 12.Simple Attendance System
# Create a list of student names
# Use loop to display names
# Ask user to search a student
# Use if statement to check availability
# Handle errors using try-except
# def system_1():
#     list_1=["priya","raju","rahul","rani"]
#     try:
#         for i in list_1:
#             user = input("enter a name:")
#             if user == i:
#                 print("its available")
#                 break
#             else:
#                 print("not available")
#     except Exception as e:
#         print("invalid input",e)    
# system_1()
# 13.Marks and Result
# Create a function result()
# Ask user for marks of 5 subjects using loop
# Find total and average
# Use if-elif for:
# Pass
# Fail
# Grade
# Handle invalid input
# def result_1():
#     total=0   
#     try:
#         for i in range(5):
#             marks=int(input("enter a number:"))
#             total+=marks
#         average=total/5
#         print("total:",total)
#         print("average:",average)
#         if average>=35:
#             print("pass")
#         elif average>=90:
#             print("grade:A")
#         else:
#             print("fail")
#     except Exception as e:
#         print("invalid input",e)
# result_1()
# 14.Number Guessing Game
# Import random module
# Generate random number from 1 to 20
# Use loop to guess number
# Print:
# Too high
# Too low
# Correct
# Handle invalid input
# import random
# num = random.randint(1,20)
# while True:
#     try:
#         user = int(input("guess the number:"))
#         if user>num:
#             print("too high")
#         elif user<num:
#             print("too low")
#         else:
#             print("correct")
#             break
#     except Exception as e:
#         print("invalid input",e)
# 15.Random Password Generator
# Import random module
# Create a function password()
# Generate random 4-digit password
# Use loop to allow 3 attempts
# Use if statement for correct/wrong password
# Handle invalid input
# import random
# def password():
#     return random.randint(1000,9999)
# pass_w=password()
# print(pass_w)
# for i in range(3):
#     try:
#         user = int(input("enter OTP:")) 
#         if user==pass_w:
#             print("correct password")
#             break
#         else:
#             print("wrong password")
#     except Exception as e:
#         print("invalid input",e)
#         break
# password()
# 16.Shopping Cart
# Create a function cart()
# Use loop to add item prices
# Stop loop when user enters "stop"
# Find total bill
# Handle invalid inputs
# def cart():
#     total=0
#     while True:
#         price=input("enter the price of the item:")
#         if price=="stop":
#             break
#         else:
#             try:
#                 total+=int(price)
#             except Exception as e:
#                 print("error",e)
#     print("total bill:",total)  
# cart()
#==============Mean, Median, Mode=================#
# num = [10,20,30,40]
# mean = sum(num)/len(num)
# print("mean:",mean)
# 1 : Mean Program
# Create a list of numbers
# Find total using sum()
# Find mean using formula
# Print mean
# x=[1,2,3,4,5,6,7,8,9,10]
# total = sum(x)
# mean=total/len(x)
# print("mean:",mean)
# 2 : User Input Mean
# Ask user to enter 5 numbers using loop
# Store them in list
# Find mean
# Handle invalid input
# def user_1():
#     list_1=[]
#     try:
#         for i in range(5):
#             n = int(input("enter a number:"))
#             list_1.append(n)
#         mean = sum(list_1)/len(list_1)
#         print("mean:",mean)
#     except Exception as e:
#         print("invalid input",e)
# user_1()
# 3 : Median Finder
# Create a list of numbers
# Sort the list
# Find middle value
# Print median
# def median_1():
#     x=[10,30,40,50,20]
#     x.sort()
#     medain = x[len(x)//2]
#     print("medain is:",medain)
# median_1()
# 4 : Mode Finder
# Create a list with repeated numbers
# Find most repeated number
# Print mode
# def mode_finder():
#     x=[10,20,30,10,20,30,40]
#     mode = max(x,key=x.count)
#     print("mode is :",mode)
# mode_finder()
# def mode_finder():
#     x=[10,20,30,10,20,30,40]
#     mode=0
#     count=0
#     for i in x:
#         if x.count(i)>count:
#             count=x.count(i)
#             mode=i
#     print("mode:",mode)
# mode_finder()
# 5 : Mean, Median, Mode Program
# Ask user to enter numbers
# Store them in list
# Find:
# Mean
# Median
# Mode
# Handle invalid input
# Print all results
# def finding_1():
#     x=[]
#     try:
#         for i in range(5):
#             user = int(input("enter a numbers:"))
#             x.append(user)
#         mean = sum(x)/len(x)
#         x.sort()
#         median =x[len(x)//2]
#         mode= max(x,key=x.count)
#         print("mean:",mean)
#         print("median:",median)
#         print("mode:",mode)
#     except Exception as e:
#         print("invalid input",e)
# finding_1()
# Final Challenge:
# Create a function statistics()
# Ask user for 10 numbers using loop
# Calculate:
# Mean
# Median
# Mode
# Use:
# loop
# if statement
# try-except
# Print all outputs properly 
# def statistics_1():
#     x=[]
#     try:
#         for i in range(10):
#             user=int(input("enter a numbers:"))
#             x.append(user)
#         mean = sum(x)/len(x)
#         x.sort()
#         median = (x[4]+x[5])/2
#         count=0
#         mode=0
#         for i in x:
#             if x.count(i)>count:
#                 count = x.count(i)
#                 mode=i
#         print("mean:",mean)
#         print("medain:",median)
#         print("mode:",mode)
#     except Exception as e:
#         print("invalid input",e)
# statistics_1()
#====================11-05-2026========================#
# 1. The Clean Registry (Lists & Sets)
# The Problem: You are given a list of employee names that contains several duplicates due to data entry errors.
# Requirements: Create a list with duplicates. 
# Use a set to automatically remove them. 
# Convert it back to a list and sort it alphabetically.
# Concepts: list(), set(), .sort().
# list_1=["ramu","anil","rani","priya","anil","priya"]
# print(list_1)
# list_1=list(set(list_1))
# print(list_1)
# list_1.sort()
# print(list_1)
# 2. Word Frequency Analyzer (Dictionaries)
# The Problem: Write a program that takes a paragraph of text and counts how many times each unique word appears.
# Requirements: Store the results in a dictionary where the key is the word and the value is the count.
# Concepts: dict, loop through string, .split(), if key in dict.
# def worfre():
#     text="hi hello"
#     word=text.split()
#     print(text)
#     count={}
#     for i in word:
#         if i in count:
#             count[i]+=1
#         else:
#             count[i]=1
#     print(count)
# worfre()
# 3. Modular Temperature Tool (Functions)
# The Problem: Build a utility that converts temperatures between Celsius and Fahrenheit.
# Requirements: Define two functions: to_celsius(f) and to_fahrenheit(c). 
# The user should be able to input a value and choose which conversion to perform.
# Concepts: def, return, function arguments, user input.
# def to_celsius(f):
#     return (f-32)*5/9
# def to_fahrenheit(c):
#     return (c*9/5)+32
# choice = input("enter c for celsius or f for fahrenheit:")
# if choice=="c":
#     c=int(input("enter celsius:"))
#     print("fahrenheit",to_fahrenheit(c))
# elif choice=="f":
#     f=int(input("enter fahrenheit:"))
#     print("celsius",to_celsius(f))
# else:
#     print("invalid choice")
# 5. Persistent Guestbook (File Handling - Append)
# The Problem: Create a program that allows users to sign a digital guestbook.
# Requirements: Ask the user for their name and a short message.
#  Open a file named guestbook.txt in append mode ('a') and save the entry so that the previous entries aren't deleted.
# Concepts: open(), .write(), file modes.
# name=input("enter a name:")
# msg=input("enter a short message:")
# with open("guestbook.txt","a") as f:
#     f.write(name + ":" + msg )
#     print("save the msg")
# 6. Filtered Log Reader (File Handling - Read)
# The Problem: Imagine a file named system.log exists with various lines of text. 
# Some lines start with "INFO", some with "WARNING", and some with "ERROR".
# Requirements: Write a script that reads the file and only prints lines that contain the word "ERROR".
# Concepts: open(..., 'r'), .readlines() or looping over file object.
# with open("system.log","a") as f:
#     print("file created")
#     f=open("system.log","r")
#     lines = f.readlines()
#     print(lines)
#     i=0
#     # for i in lines:
#     #     if "ERROR" in i:
#     #         print(i)
#     while i<len(lines):
#         if "ERROR" in lines[i]:
#             print(lines[i])
#         i+=1
# 7. The Math Wizard (Modules - random)
# The Problem: Create a simple multiplication game.
# Requirements: Use the random module to generate two numbers between 1 and 12. 
# Ask the user for the product. If they are wrong, show the correct answer.
# Concepts: import random, random.randint().
# import random
# num1=random.randint(1,12)
# num2=random.randint(1,12)
# user=int(input(f"{num1}*{num2}:"))
# check_1=num1*num2
# if user==check_1:
#     print("correct")
# else:
#     print("wrong")
# print("correct answers is:",check_1)
# 8. Nested Contact Directory (Dictionaries & Functions)
# The Problem: Build a contact manager that stores more than just a phone number.
# Requirements: Use a dictionary where the key is the person's name and the value is another dictionary containing their email and city. 
# Create a function find_contact(name) that retrieves this info.
# Concepts: Nested dictionaries, searching keys.
# contact={
#     "ramu":{
#         "email":"ramu@gmail.com",
#         "city":"Madanapalli"
#     },
#     "priya":{
#         "email":"priya@gmail.com",
#         "city":"chitoor"
#     }
# }
# def find_contact(name):
#     if name in contact:
#         print(contact[name])
#     else:
#         print("not found")
# find_contact("ramu")
# 9. Safe File Discovery (Modules - os & Exceptions)
# The Problem: Write a script that attempts to read a file provided by the user.
# Requirements: Use the os module to check if the file path exists before opening it. If it doesn't exist, 
# raise a custom FileNotFoundError or print a safe warning message.
# Concepts: import os, os.path.exists(), custom error messages.
# import os
# file = input("enter file name:")
# if os.path.exists(file):
#     with open(file,"r") as f:
#         print(f.read())
# else:
#     print("not found")
# 10. Club Intersection (Set Operations)
# The Problem: You have two lists: students_math_club and students_art_club.
# Requirements: Convert both to sets. Use set operators to find:
# Students who are in both clubs.
# Students who are in the Math club but not the Art club.
# Concepts: .intersection(), .difference(), Set logic.
# students_math_club=["ramu","sam","rani","priya"]
# students_art_club=["raju","rahul","sai","rani"]
# math_club_set=set(students_math_club)
# art_club_set=set(students_art_club)
# print("students who are in both clubs:")
# print(math_club_set.intersection(art_club_set))
# print("students who are in the math club:")
# print(math_club_set.difference(art_club_set))
# print("set logics")
# print(math_club_set & art_club_set)
# print(math_club_set - art_club_set)
