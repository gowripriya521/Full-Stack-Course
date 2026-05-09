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
#     pword = "Test"
#     count = 3
#     try:
#         while True:
#             user = input("enter a password:")
#             if user==pword:
#                 print("correct password")
#                 break
#             elif count==0:
#                 print("your chances over")
#             else:
#                 print("wrong password")
#                 count-=1
#     except Exception as e:
#         print("invalid input",e)
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
#         try:
#             price=input("enter the price of the item:")
#             total+=price
#             if price=="stop":
#                 break
#             total+=price
#         except Exception as e:
#             print("invalid input",e)
#     print("total bill:",total)    
# cart()
