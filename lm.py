# ==============08-04-2026==================#
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
#or
# list_1=["ramu","anil","rani","priya","anil","priya"]
# set_1={}
# for i in list_1:
#     if i not in set_1:
#         set_1[i]=0
# list_1=[]
# for i in set_1:
#     list_1.append(i)
# list_1.sort(reverse=True)
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
# 1. Library Book Tracker (Lists & Sets)
# Problem:A library has duplicate book entries.
# Requirements:Create a list with duplicate book names.
# Remove duplicates using a set.
# Convert back to list and sort the books.
# Concepts
# list()
# set()
# .sort()
# list_1=["python","pandas","numpy","python","numpy"]
# print(list_1)
# list_1=list(set(list_1))
# print(list_1)
# list_1.sort()
# print(list_1)
# 1. Sentence Word Counter (Dictionaries)
# Problem:Count how many times each word appears in a sentence.
# Requirements:Store words as keys and counts as values in a dictionary.
# Concepts
# dict
# split()
# loop
# if key in dict
# text = "small steps every day lead to big results"
# word=text.split()
# count={}
# for i in word:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1
# print(count)
# 1. Distance Converter Tool (Functions)
# Problem:Convert kilometers to meters and meters to kilometers.
# Requirements:Create:
# to_meters()
# to_kilometers()
# Take user input and perform conversion.
# Concepts
# functions
# return
# arguments
# input
# def to_meters(km):
#     return km*1000
# def to_kilometers(m):
#     return m/1000
# choice=input("enter km for kilometers or m for meters:")
# if choice=="km":
#     km=int(input("enter kilometers:"))
#     print("meters:",to_meters(km))
# elif choice=="m":
#     m=int(input("enter meters:"))
#     print("kilometer:",to_kilometers(m))
# else:
#     print("invalid choice")
# 4. Student Marks Saver (File Handling - Write)
# Problem:Save student marks into a file.
# Requirements:Ask user for name and marks.
# Store them in marks.txt.
# Concepts
# open()
# write()
# file modes
# name = input("Enter student name: ")
# marks = input("Enter marks: ")
# file = open("marks.txt", "w")
# file.write(name + " : " + marks)
# file.close()
# print("Data Saved")
# 5. Important Notes Reader (File Handling - Read)
# Problem:Read a file and print only lines containing "IMPORTANT".
# Requirements:Open file in read mode and filter lines.
# Concepts
# open(..., "r")
# readlines()
# loop
# file = open("notes.txt", "r")
# lines = file.readlines()
# for i in lines:
#     if "IMPORTANT" in i:
#         print(i)
# file.close()
# 6. Random Addition Game (Modules - random)
# Problem:Generate two random numbers and ask user for addition result.
# Requirements:Check whether answer is correct.
# Concepts
# import random
# randint()
# import random
# num1 = random.randint(1, 10)
# num2 = random.randint(1, 10)
# answer = int(input(f"What is {num1} + {num2}: "))
# if answer == num1 + num2:
#     print("Correct")
# else:
#     print("Wrong")
# 7. Employee Directory (Nested Dictionaries)
# Problem
# Store employee details like salary and department.
# Requirements
# Use nested dictionaries and create:
# find_employee(name)
# Concepts
# nested dictionary
# functions
# key searching
# employees = {
#     "Ravi": {
#         "salary": 25000,
#         "department": "IT"
#     },
#     "Priya": {
#         "salary": 30000,
#         "department": "HR"
#     }
# }
# def find_employee(name):
#     if name in employees:
#         print(employees[name])
#     else:
#         print("Employee not found")
# find_employee("Ravi")
# 8. Safe Password File Checker (os & Exceptions)
# Problem
# Check whether a password file exists before opening it.
# Requirements
# Use:
# os.path.exists()
# Print safe message if file not found.
# Concepts
# os module
# exceptions
# file handling
# import os
# file_name = "password.txt"
# if os.path.exists(file_name):
#     file = open(file_name, "r")
#     print(file.read())
#     file.close()
# else:
#     print("File not found")
# 9. Sports Club Analyzer (Set Operations)
# Problem
# Find students playing both Cricket and Football.
# Requirements
# Use set operations to find:
# common students
# only cricket students
# Concepts
# set logic
# &
# cricket = {"Ravi", "Priya", "Anil"}
# football = {"Priya", "Sita", "Anil"}
# print(cricket & football)
# print(cricket - football)
# 10. Shopping Bill Calculator (Functions & Lists)
# Problem
# Store product prices in a list and calculate total bill.
# Requirements
# Create a function to calculate total.
# Concepts
# list
# loop
# function
# sum logic
# prices = [100, 200, 300]
# def total_bill(items):
#     total = 0
#     for i in items:
#         total += i
#     return total
# print("Total Bill:", total_bill(prices))
#=====================class===========================#
# class MyClass:
#     x=5
# p1=MyClass()
# print(p1.x)
# class Person:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def greet(self):
#         print("hello,my name is"+self.name)
# p1=Person("John",36)
# p1.greet()
# import pyjokes
# joke = pyjokes.get_joke()
# print(joke)
# import pyjokes
# print(pyjokes.get_joke(language='en',category='neutral'))
# import pywhatkit
# pywhatkit.playonyt("dheere dheere tu song")
# 1. Student Details Class
# The Problem:Create a class to store student information.
# Requirements: Create a class Student with: name, marks
# Create a method to display student details:Concepts,class,object,init(),self,methods
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def results(self):
#         print("my name is:",self.name)
#         print("my marks is:",self.marks)
# x=Student("sam",98)
# x.results()
# 2. Bank Account System
# The Problem:Create a simple bank account program.
# Requirements:Create a class BankAccount with:account holder name,balance
# Create methods:deposit(),withdraw()
# Concepts:classes,methods,objects,arithmetic operations
# class BankAccount:
#     def __init__(self,account_holder_name,balance):
#         self.account=account_holder_name
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#         print("balance after deposit:",self.balance)
#     def withdraw(self,amount):
#         self.balance-=amount
#         print("balance after withdraw:",self.balance)
# b=BankAccount("priya",10000)
# b.deposit(2000)
# b.withdraw(5000)
# 3. Employee Salary Calculator
# The Problem:Store employee details and calculate yearly salary.
# Requirements:Create:employee name,monthly salary
# Create method:yearly_salary()
# Concepts:class,methods,calculations
# class Employee:
#     def __init__(self,ename,msalary):
#         self.name=ename
#         self.salary=msalary
#     def yearly_salary(self):
#         self.salary=self.salary*12
#         print(self.name,"yearly salary:",self.salary)
# e=Employee("priya",50000)
# e.yearly_salary()
# 4. Rectangle Area Finder
# The Problem:Find area of rectangle using class.
# Requirements:
# Create:length,width
# Create method:area()
# Concepts,classes,methods,
# class RectangleArea:
#     def __init__(self,lenght,width):
#         self.l=lenght
#         self.w=width
#     def area(self):
#         print(self.l*self.w)
# r=RectangleArea(30,20)
# r.area()
# 5. Car Information System
# The Problem:Store car details.
# Requirements:
# Create class Car with:brand,model,price
# Create method to display details.
# Concepts:class,constructor,object creation
# class Car:
#     def __init__(self,brand,model,price):
#         self.b=brand
#         self.m=model
#         self.p=price
#     def display(self):
#         print(self.b,"is the most popular brand,model-",self.m,"and price is:",self.p)
# c=Car("Toyota","Fortuner",340000)
# c.display()
# 6. Simple Calculator Class
# The Problem:Create calculator using class.
# Requirements
# Create methods:
# add()
# subtract()
# multiply()
# divide()
# Concepts:methods,arguments,objects
# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print(self.a+self.b)
#     def subtraction(self):
#         print(self.a-self.b)
#     def multiply(self):
#         print(self.a*self.b)
#     def divide(self):
#         print(self.a/self.b)
# c=Calculator(20,10)
# c.add()
# c.subtraction()
# c.multiply()
# c.divide()
# 7. Attendance Manager
# The Problem:Store student attendance.
# Requirements
# Create methods:
# mark_present()
# show_attendance()
# Concepts:class,list inside class,methods
# class AttendanceManager:
#     def __init__(self):
#         self.student=[]
#     def marks_present(self,name):
#         self.student.append(name)
#     def show_attendance(self):
#         print(self.student)
# a=AttendanceManager()
# a.marks_present("sam")
# a.marks_present("ramu")
# a.show_attendance()
# 9. Shopping Cart Class
# The Problem:Create a shopping cart system.
# Requirements:Store products in list and calculate total price.
# Concepts:classes,lists,methods,loops
# class ShoppingCard:
#     def __init__(self):
#         self.product=[]
#     def add_products(self,price):
#         self.product.append(price)
#     def total_price(self):
#         total=0
#         for i in self.product:
#             total+=i
#         print("total bill:",total)
# c=ShoppingCard()
# c.add_products(100)
# c.add_products(200)
# c.add_products(200)
# c.total_price()
# 10. Login Verification Class
# The Problem:Create a login system using class.
# Requirements:Store username and password.
# Create method:login()
# Check whether login is successful.
# Concepts:classes,methods,conditions
# class LoginSystem:
#     def __init__(self):
#         self.username="Test"
#         self.password="1234"
#     def login(self):
#         user=input("enter name:")
#         pw=input("enter password:")
#         if user==self.username and pw==self.password:
#             print("Login successful")
#         else:
#             print("login failed")
# l=LoginSystem()
# l.login()
# 1. Student Record Creator (Create)
# Problem:Create a dictionary to store student name and marks.
# Requirements:Add:name,marks,grade,
# Concepts:dictionary creation,key-value pairs
# student={
#     "name":"priya",
#     "marks":90,
#     "grade":"A"
# }
# print(student)
# student={
#     "Ravi":{
#         "marks":60,
#         "grade":"B"
#     },
#     "priya":{
#         "marks":97,
#         "grade":"A"
#     },
#     "sam":{
#         "marks": 56,
#         "grade":"c"
#     },
# }
# print(student)
# 2. Employee Information Reader (Read)
# Problem:Read employee details from dictionary.
# Requirements:
# Print:employee name,salary
# Concepts:dictionary access,keys
# employee={
#     "ename":"priya",
#     "salary":5000
# }
# print("employee name:",employee["ename"])
# print("salary:",employee["salary"])
# 3. Product Price Updater (Update)
# Problem:Update the price of a product in dictionary.
# Requirements:Change old price to new price.
# Concepts
# updating dictionary values
# product={
#     "apples":50,
#     "banana":30,
#     "mango":70
# }
# product.update({"apples":70})
# print(product)
# 4. Contact Remover (Delete)
# Problem:Delete a contact from dictionary.
# Requirements
# Remove a person using:
# del
# Concepts
# deleting keys
# contact={
#     "n1":"sam",
#     "n2":"priya",
#     "n3":"suma",
#     "n4":"raju"
# }
# del contact["n3"]
# print(contact)
# 5. Favorite Movies Appender (Append)
# Problem:Create an empty list and add movie names.
# Requirements
# Use:
# append()
# Concepts
# list
# append
# mname=[]
# m1=input("enter a movie name:")
# mname.append(m1)
# m2=input("enter a movie name:")
# mname.append(m2)
# m3=input("enter a movie name:")
# mname.append(m3)
# print(mname)
# 6. Number Slice Viewer (Slicing)
# Problem:Create a list of numbers from 1 to 10.
# Requirements:
# Print:
# first 3 numbers
# middle numbers
# last 2 numbers
# Concepts
# list slicing# 
# print(x[:3])
# print(x[1:10])
# print(x[-2:])
# 7. Shopping List Manager
# Problem:
# Store shopping items in list.
# Requirements
# Add new item and remove one item.
# Concepts
# append()
# remove()
# x=["milk","curd","eggs","soap"]
# x.append("choclate")
# print(x)
# x.remove("eggs")
# print(x)
# Tuple Code Challenges
# 8. Student Data Reader
# Problem
# Store student details in tuple.
# Requirements
# Print:
# name
# age
# course
# Concepts
# tuple
# indexing
# student=("ramu",21,"python")
# print("name:",student[0])
# print("age:",student[1])
# print("course:",student[2])
#=================18-05-2026=====================#
# x=[1,2,3,4,5,6,7,8,9,10]
# start=0
# end=len(x)-1
# while start<end:
#     # print(x[start],x[end])
#     x[start],x[end]=x[end],x[start]
#     start+=1
#     end-=1
# print(x)
# 1. Reverse a List Without Built-in Functions
# Given a list of integers, reverse the list manually without using:
# - reverse()
# - slicing ([::-1])
# - any built-in reverse utility
# You must solve it using loops or two pointers.
# Example:
# Input:[1, 2, 3, 4, 5]
# Output:[5, 4, 3, 2, 1]
# Constraints:
# - List length >= 1
# - Do not create another list if possible
#x=[1,2,3,4,5,6,7,8,9,10]
# start=0
# end=len(x)-1
# while start<end:
#     x[start],x[end]=x[end],x[start]
#     start+=1
#     end-=1
# print(x)
#=========or=============#
# i=len(x)-1
# while i>=0:
#     print(x[i])
#     i-=1
# 2. Find Duplicate Elements in a List
# Given a list of integers, print all elements that appear more than once.
# Each duplicate should appear only once in the output.
# Example:
# Input:[1, 2, 3, 2, 4, 1, 5]
# Output:[1, 2]
# Constraints:
# - Input may contain multiple duplicates
# - Order of output does not matter
# Expected Concept:
# - Set
# - Hashing
# x=[1,2,3,2,4,1,5]
# y=[]
# z=[]
# for i in x:
#     if i in y:
#         if i not in z:
#             z=z+[i]
#     else:
#         y=y+[i]
# print(z)

# 3. Rotate a List by K Positions
# Given a list and an integer k, rotate the list to the right by k positions.
# Example:
# Input:
# arr = [1, 2, 3, 4, 5]
# k = 2
# Output:
# [4, 5, 1, 2, 3]
# Additional Notes:
# - k may be greater than list length
# - Try solving in-place if possible
# Expected Concept:
# - List manipulation
# - Modulo operation
# arr=[1,2,3,4,5]
# k=2
# n=len(arr)
# new=[0]*n
# i=0
# while i<n:
#     new[(i+k)%n]=arr[i]
#     i+=1
# print(new)
# 4. Find Common Elements Between Two Lists
# Given two lists of integers, return all common elements.
# Example:
# Input:
# a = [1, 2, 3, 4]
# b = [3, 4, 5, 6]
# Output:
# [3, 4]
# Constraints:
# - Output should not contain duplicates
# - Order is not important
# Expected Concept:
# - Set intersection
# a=[1,2,3,4]
# b=[3,4,5,6]
# x=set(a)
# y=set(b)
# print(list(x&y))
# 5. Check Whether All Characters Are Unique
# Given a string, determine whether all characters in the string are unique.
# Example 1:
# Input:
# "python"
# Output:
# True
# Example 2:
# Input:
# "apple"
# Output:
# False
# Expected Concept:
# - Set
# - Character tracking
# inp="python"
# set_1=set()
# Tracker=True
# for i in inp:
#     if i in set_1:
#         Tracker=False
#     else:
#         set_1.add(i)
# print(Tracker)
# 6. Remove Duplicates While Maintaining Order
# Given a list, remove duplicate elements while preserving the original order.
# Example:
# Input:
# [1, 2, 2, 3, 1, 4]
# Output:
# [1, 2, 3, 4]
# Constraints:
# - Preserve first occurrence
# - Do not sort the list
# Expected Concept:
# - Set + List
# input=[1,2,2,3,1,4]
# x=set(input)
# print(list(x))
#=========or=============#
# y=[]
# for i in input:
#     if i not in y:
#         y.append(i)
# print(y)
# 7. Count Frequency of Characters in a String
# Given a string, count how many times each character appears.
# Example:
# Input:
# "banana"
# Output:
# {
#  'b': 1,
#  'a': 3,
#  'n': 2
# }
# Expected Concept:
# - Dictionary
# - Frequency counting
# input="banana"
# temp={}
# for i in input:
#     if i in temp:
#         temp[i]+=1
#     else:
#         temp[i]=1
# print(temp)
# 8. Count Frequency of Words in a Sentence
# Given a sentence, count occurrence of each word.
# Example:
# Input:
# "hi hello hi python"
# Output:
# {
#  'hi': 2,
#  'hello': 1,
#  'python': 1
# }
# Constraints:
# - Words are separated by spaces
# - Ignore punctuation for now
# Expected Concept:
# - Dictionary
# - String splitting
# input="hi hello hi python"
# word=input.split()
# count={}
# for i in word:
#     if i in count:
#         count[i]+=1
#     else:
#         count[i]=1
# print(count)

# 9. Group Students Based on Marks
# You are given a list containing student names and marks.
# Group students having the same marks.
# Example:
# Input:
# [
#  ("ram", 90),
#  ("sam", 80),
#  ("raj", 90)
# ]
# Output:
# {
#  90: ["ram", "raj"],
#  80: ["sam"]
# }
# Expected Concept:
# - Dictionary of lists
# input=[
#  ("ram", 90),
#  ("sam", 80),
#  ("raj", 90)
# ]
# x={}
# for name,marks in input:
#     if marks in x:
#         x[marks]=x[marks]+[name]
#     else:
#         x[marks]=[name]
# print(x)
# 10. Two Sum in Sorted Array
# Given a sorted array and a target value, find two numbers whose sum equals the target.
# Example:
# Input:
# arr = [1, 2, 3, 4, 6]
# target = 6
# Output:
# (2, 4)
# Constraints:
# - Array is already sorted
# - Use two pointers
# - Avoid nested loops
# Expected Concept:
# - Two pointers
# arr = [1, 2, 3, 4, 6]
# target = 6
# s=0
# e=len(arr)-1
# while s<e:
#     i=arr[s]+arr[e]
#     if i==target:
#         print(arr[s],arr[e])
#         break
#     s+=1
#     e-=1
# 11. Check Palindrome Using Two Pointers
# Given a string, determine whether it is a palindrome.
# A palindrome reads the same forward and backward.
# Example:
# Input:
# "madam"
# Output:
# True
# Example:
# Input:
# "python"
# Output:
# False
# Expected Concept:
# - Two pointers
# input="madam"
# s=0
# e=len(input)-1
# Tracker=True
# while s<e:
#     if input[s]!=input[e]:
#         Tracker=False
#     s+=1
#     e-=1
# print(Tracker)
# 12. Move All Zeroes to End
# Given an array, move all zeroes to the end while maintaining the order of non-zero elements.
# Example:
# Input:
# [0, 1, 0, 3, 12]
# Output:
# [1, 3, 12, 0, 0]
# Constraints:
# - Try solving in-place
# - Minimize operations
# Expected Concept:
# - Two pointers
# input=[0, 1, 0, 3, 12]
# i=0
# j=0
# while i<len(input):
#     if input[i]!=0:
#         input[j],input[i]=input[i],input[j]
#         j+=1
#     i+=1
# print(input)
# 13. Maximum Sum Subarray of Size K
# Given an array of integers and a window size k, find the maximum sum of any contiguous subarray of size k.
# Example:
# Input:
# arr = [2, 1, 5, 1, 3, 2]
# k = 3
# Output:
# 9
# Explanation:
# Subarray:
# [5,1,3] = 9
# Expected Concept:
# - Sliding window
# arr = [2, 1, 5, 1, 3, 2]
# k=3
# z=9
# a=0
# b=k
# while b<len(arr):
#     if sum(arr[a:b])==z:
#         print(arr[a:b],"=",z)
#         break
#     a+=1
#     b+=1
# import pyjokes
# print(pyjokes.get_joke())
# import pyjokes
# print(pyjokes.get_joke("eu"))
# print(pyjokes.get_joke("es", "chuck"))
# import pyjokes
# for joke in pyjokes.get_jokes():
#     print(joke)
#import pywhatkit
#pywhatkit.start_server()
#pywhatkit.sendwhats_image("+916303055390", "Images/Hello.png", "Hello")
# 14. Longest Substring Without Repeating Characters
# Given a string, find the length of the longest substring without repeating characters.
# Example:
# Input:
# "abcabcbb"
# Output:
# 3
# Explanation:
# Longest substring:
# "abc"
# Expected Concept:
# - Sliding window
# - Set
# input="abcabcbb"
# s=0
# e=0
# longest=0
# while e<len(input):
#     temp=""
#     i=s
#     while i<e:
#         temp+=input[i]
#         i+=1
#     if input[e] in temp:
#             s+=1
#     else:
#         if(e-s+1)>longest:
#             longest=e-s+1
#         e+=1
# print(longest)
# 15. Maximum Number of Vowels in a Window
# Given a string and an integer k, find the maximum number of vowels present in any substring of size k.
# Example:
# Input:
# s = "abciiidef"
# k = 3
# Output:
# 3
# Explanation:
# Substring:
# "iii"
# contains 3 vowels
# Expected Concept:
# - Sliding window
# - Character checking
# s = "abciiidef"
# k=3
# x=0
# y=0
# for i in s:
#     if i in "aeiou":
#         y+=1
#         if y>=k:
#             k=y
#     else:
#         y=0
#         x+=1
# print(k)
# import smtplib
# print("SMTP imported successfully")
# 11. Find Missing Number in Array
# Question
# Given a list containing numbers from 1 to n with one number missing, find the missing number.
# Example
# Input
# [1, 2, 4, 5]
# Expected Output
# 3
# Expected Concepts
# Sum formula
# Loop
# Arithmetic logic
# input=[1,2,3,5]
# n=5
# exp=n*(n+1)//2
# act=0
# for i in input:
#     act+=i
# missing=exp-act
# print(missing)
# 12. Find Second Largest Element
# Question:Given a list of integers, find the second largest element without sorting.
# Example
# Input
# [10, 20, 4, 45, 99]
# Expected Output
# 45
# Expected Concepts
# Comparison
# Loop
# Maximum tracking
# input=[10,20,4,45,99]
# l=0
# s=0
# for i in input:
#     if i>l:
#         s=l
#         l=i
#     elif i>s and i!=l:
#         s=i
# print(s)
# 13. Check Anagram Strings
# Question:Given two strings, check whether they are anagrams.
# Two strings are anagrams if they contain the same characters with same frequency.
# Example
# Input
# "listen"
# "silent"
# Expected Output
# True
# Expected Concepts
# Dictionary
# Sorting logic
# Frequency counting
# s1 = "listen"
# s2 = "silent"
# count1 = {}
# count2 = {}
# for i in s1:
#     if i in count1:
#         count1[i] += 1
#     else:
#         count1[i] = 1
# for i in s2:
#     if i in count2:
#         count2[i] += 1
#     else:
#         count2[i] = 1
# print(count1 == count2)
# 14. Find All Pairs With Given Sum
# Question:Given a list and a target value, print all pairs whose sum equals the target.
# Example
# Input
# arr = [1, 2, 3, 4, 5]
# target = 5
# Expected Output
# (1, 4)
# (2, 3)
# Expected Concepts
# Set
# Pair checking
# Loop
# arr=[1,2,3,4,5]
# target=5
# s=0
# e=len(arr)-1
# while s<e:
#     i=arr[s]+arr[e]
#     if i==target:
#         print(arr[s],arr[e])
#         s+=1
#         e-=1
#     elif i<target:
#         s+=1
#     else:
#         e-=1
# 15. Count Vowels and Consonants
# Given a string, count vowels and consonants.
# Example:
# Input:
# Python
# "python"
# Output:
# Python
# Vowels = 1
# Consonants = 5
# Expected Concept:
# Character checking
# Loops
# input="python"
# c=0
# temp=0
# for i in input:
#     if i in "aeiou":
#         c+=1
#     else:
#         temp+=1
# print("vowels:",c)
# print("consonants:",temp)
#========================22-05-2026===========================#
# 1.Basic Class & Object Implementation:
# Problem: Create a Rectangle class with attributes length and width. 
# Implement methods to calculate the area() and perimeter().
# Goal: Tests your ability to define a class, 
# use the _init_ constructor, and understand the self keyword.
# class Rectangle:
#     def __init__(self,length,width):
#         self.l=length
#         self.w=width
#     def area(self):
#         return self.l*self.w
#     def perimiter(self):
#         return 2*(self.l+self.w)
# r=Rectangle(30,20)
# print(r.area())
# print(r.perimiter())
# 2.Inheritance & Method Overriding:
# Problem: Create a base class Animal with a method speak(). 
# Create child classes Dog and Cat that override speak() to print "Woof" and "Meow" respectively.
# Goal: Demonstrates understanding of how child classes inherit and modify parent behavior.
# class Animal:
#     def speak(self):
#        print("Animal sound")
# class Dog(Animal):
#     def speak(self):
#         print("woof")
# class Cat(Animal):
#     def speak(self):
#         print("meow")
# d1=Dog()
# c1=Cat()
# print(d1.speak())
# print(c1.speak())
# 3.Encapsulation (Private/Protected Members):
# Problem: Design a BankAccount class where the balance attribute is private. 
# Provide methods to deposit(), withdraw(), and a getter to view the current balance.
# Goal: Checks if you know how to use single underscores () or double underscores (_) to manage data access.
# class BankAccount:
#     def __init__(self,balance):
#         self.__b=balance
#     def deposit(self,amount):
#         self.__b+=amount
#         print("balance after deposit:",amount)
#     def withdraw(self,amount):
#         if amount<=self.__b:
#             self.__b-=amount
#             print("balance after withdraw:",amount)
#         else:
#             print("insufficient balance")
#     def get_b(self):
#         return self.__b
# b=BankAccount(5000)
# print(b.deposit(2000))
# print(b.withdraw(2000))
# print(b.get_b())
# 4.Constructor Overloading Simulation:
# Problem: In Python, you cannot have multiple _init_ methods.
# How would you create an Employee class that can be initialized either with just a name or with both a name and a salary?.
# Goal: Tests knowledge of default arguments or using args/*kwargs to handle flexible inputs.
# class Employee:
#     def __init__(self,name,salary=None):
#         self.n=name
#         self.s=salary
#     def greet(self):
#         print("name:",self.n)
#         print("salary:",self.s)
# e=Employee("priya",50000)
# e.greet()
# 5.Polymorphism with Functions:
# Problem: Write a function that takes a list of different objects 
# (e.g., Circle, Square) and calls their common draw() method.
# Goal: Demonstrates "duck typing" and the ability to use a single interface for different data types.
# Circle Class
# class Circle:
#     def draw(self):
#         print("Drawing Circle")
# class Square:
#     def draw(self):
#         print("Drawing Square")
# def draw_shapes(shapes):
#     for shape in shapes:
#         shape.draw()
# c1 = Circle()
# s1 = Square()
# shape_list = [c1, s1]
# draw_shapes(shape_list)
# 6. Student Details Class
# The Problem:Create a class to store student information.
# Requirements: Create a class Student with: name, marks
# Create a method to display student details:Concepts,class,object,init(),self,methods
# class Student:
#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks
#     def results(self):
#         print("my name is:",self.name)
#         print("my marks is:",self.marks)
# x=Student("sam",98)
# x.results()
# 7. Employee Salary Calculator
# The Problem:Store employee details and calculate yearly salary.
# Requirements:Create:employee name,monthly salary
# Create method:yearly_salary()
# Concepts:class,methods,calculations
# class Employee:
#     def __init__(self,ename,msalary):
#         self.name=ename
#         self.salary=msalary
#     def yearly_salary(self):
#         self.salary=self.salary*12
#         print(self.name,"yearly salary:",self.salary)
# e=Employee("priya",50000)
# e.yearly_salary()
# 8. Car Information System
# The Problem:Store car details.
# Requirements:
# Create class Car with:brand,model,price
# Create method to display details.
# Concepts:class,constructor,object creation
# class Car:
#     def __init__(self,brand,model,price):
#         self.b=brand
#         self.m=model
#         self.p=price
#     def display(self):
#         print(self.b,"is the most popular brand,model-",self.m,"and price is:",self.p)
# c=Car("Toyota","Fortuner",340000)
# c.display()
# 9. Simple Calculator Class
# The Problem:Create calculator using class.
# Requirements
# Create methods:
# add()
# subtract()
# multiply()
# divide()
# Concepts:methods,arguments,objects
# class Calculator:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add(self):
#         print(self.a+self.b)
#     def subtraction(self):
#         print(self.a-self.b)
#     def multiply(self):
#         print(self.a*self.b)
#     def divide(self):
#         print(self.a/self.b)
# c=Calculator(20,10)
# c.add()
# c.subtraction()
# c.multiply()
# c.divide()
# 10. Attendance Manager
# The Problem:Store student attendance.
# Requirements
# Create methods:
# mark_present()
# show_attendance()
# Concepts:class,list inside class,methods
# class AttendanceManager:
#     def __init__(self):
#         self.student=[]
#     def marks_present(self,name):
#         self.student.append(name)
#     def show_attendance(self):
#         print(self.student)
# a=AttendanceManager()
# a.marks_present("sam")
# a.marks_present("ramu")
# a.show_attendance()
# 11. Shopping Cart Class
# The Problem:Create a shopping cart system.
# Requirements:Store products in list and calculate total price.
# Concepts:classes,lists,methods,loops
# class ShoppingCard:
#     def __init__(self):
#         self.product=[]
#     def add_products(self,price):
#         self.product.append(price)
#     def total_price(self):
#         total=0
#         for i in self.product:
#             total+=i
#         print("total bill:",total)
# c=ShoppingCard()
# c.add_products(100)
# c.add_products(200)
# c.add_products(200)
# c.total_price()
# 12. Login Verification Class
# The Problem:Create a login system using class.
# Requirements:Store username and password.
# Create method:login()
# Check whether login is successful.
# Concepts:classes,methods,conditions
# class LoginSystem:
#     def __init__(self):
#         self.username="Test"
#         self.password="1234"
#     def login(self):
#         user=input("enter name:")
#         pw=input("enter password:")
#         if user==self.username and pw==self.password:
#             print("Login successful")
#         else:
#             print("login failed")
# l=LoginSystem()
# l.login()
# 13. Design a class as described below.
# class name : MyClass
# function: function name - display(), parameters - none, return type - void ,
# access modifier - public, function body - should print "Hello World"
# Note: The driver's code will call the display function of the MyClass
# Example:
# Input: None
# Output: "Hello World"
# class MyClass:
#     def display(self):
#         print("hello world")        
# c=MyClass()
# c.display()
#14.  Design a class as described below.
# class: User
# instance variable: name(String)
# constructor: parameter: none, task: initialize the instance variable to "Default"
# Note: The driver's code will print instance variable (name) of your designed class.
# Example:
# Input: None
# Output: Default
# class User:
#     def __init__(self):
#        self.name="Default"       
# c=User()
# print(c.name)
# 15. Your task is to create a Person class in Python that demonstrates encapsulation. 
# This class should have two "private" attributes:
# name (String) with a default value of "Geeks".
# age (int) with a default value of 10.
# The class should provide public methods to access and modify these private attributes:
# Getter Methods: get_name() and get_age()
# Setter Methods: set_name(name) and set_age(age)
# Example:
# Input: Funtion calls: [Person(), get_name(), set_name("John"), set_age(21), get_name(), get_age()] 
# Output: Geeks John 21
# class Person:
#     def __init__(self):
#         self.__name="Geeks"
#         self.__age=10
#     def get_name(self):
#         return self.__name
#     def get_age(self):
#         return self.__age
#     def set_name(self,name):
#         self.__name=name
#     def set_age(self,age):
#        self.__age=age
# p1=Person()
# print(p1.get_name())
# p1.set_name("john")
# p1.set_age(21)
# print(p1.get_name())
# print(p1.get_age())
# 16. Implement the following classes to understand abstraction in Python :
# Note: Driver code makes all the function calls and print statements
# Class Name: Shape (Abstract Class)
# Attributes: color (String)
# Constructor: Shape(c) -> assign value of c to color attribute
# Methods: get_color() -> returns value of color
#          get_area() -> abstract method with float return type
# Class Name: Square (extends Shape)
# Attributes: side (float)
# Constructor: Square(c, side) -> calls super(c) to initialize the color and assigns the value to side.
# Methods: get_area() -> returns the area of the square (side * side).
# Example:
# Input: color = "red", side = 5.0
# Output: 
# red 25.0
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     def __init__(self,c):
#         self.color=c
#     def get_c(self):
#         return self.color
#     @abstractmethod
#     def get_area(self):
#         ...
# class Square(Shape):
#     def __init__(self,c,side):
#         self.color=c
#         self.s=side
#     def get_area(self):
#         return self.s*self.s
# s=Square("red",5.0)
# print(s.get_c())
# print(s.get_area())
# 17. Design a class as described below:
# Class Name: Addition
# Method:
# Function Name: add
# Parameters: a (int), b (int)
# Return Type: int
# Static: Yes (Use the @staticmethod decorator)
# Task: Returns the sum of the values given as parameters.
# Examples
# Input: a = 3, b = 4
# Output: 7
# class Addition:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add_1(self):
#         return self.a+self.b
# a=Addition(3,4)
# print(a.add_1())
# ==============or=================
# class Addition:
#     @staticmethod
#     def add(a, b):
#         return a + b
# print(Addition.add(3, 4))
# 18.Vehicle Management System
# Create:
# Parent class → Vehicle
# Child classes → Car and Bike
# Requirements:
# Vehicle should contain common methods
# Car and Bike should inherit Vehicle features
# Add separate methods for child classes
# Concepts Tested:
# Inheritance
# Parent-child relationship
# class Vehicle:
#     def start(self):
#         print("Vehicle Started")
# class Car(Vehicle):
#     def drive(self):
#         print("Car Driving")
# class Bike(Vehicle):
#     def ride(self):
#         print("Bike Riding")
# c1 = Car()
# b1 = Bike()
# c1.start()
# c1.drive()
# b1.start()
# b1.ride()
# 19.Shape Area Calculator
# Create abstract class Shape.
# Requirements:
# Create abstract method:
# area()
# Create child classes:
# Circle
# Rectangle
# Triangle
# Calculate area differently for each shape
# Concepts Tested:
# Abstraction
# Polymorphism
# from abc import ABC, abstractmethod
# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(Shape):
#     def __init__(self, r):
#         self.r = r
#     def area(self):
#         print(3.14 * self.r * self.r)
# class Rectangle(Shape):
#     def __init__(self, l, b):
#         self.l = l
#         self.b = b
#     def area(self):
#         print(self.l * self.b)
# c1 = Circle(5)
# r1 = Rectangle(10, 5)
# c1.area()
# r1.area()
# 20.Library Management System
# Requirements:
# Add books
# Issue books
# Return books
# Display available books
# Need Classes:
# Book
# Library
# Student
# Concepts Tested:
# Object interaction
# Encapsulation
# class Library:
#     def __init__(self):
#         self.books = []
#     def add_book(self, book):
#         self.books.append(book)
#     def show_books(self):
#         print(self.books)
# l1 = Library()
# l1.add_book("Python")
# l1.add_book("Java")
# l1.show_books()
# 21.Payment Gateway System
# Requirements:
# Create payment methods:
# UPI
# Credit Card
# Net Banking
# Use same method:
# pay()
# Different implementation for each payment type
# Concepts Tested:
# Polymorphism
# Method overriding
# class Payment:
#     def pay(self):
#         print("Payment Done")
# class UPI(Payment):
#     def pay(self):
#         print("UPI Payment")
# class Card(Payment):
#     def pay(self):
#         print("Card Payment")
# u1 = UPI()
# c1 = Card()
# u1.pay()
# c1.pay()
# 22.Mobile Phone System
# Requirements:
# Call
# Message
# Camera
# Internet
# Need:
# Parent class → Mobile
# Child class → SmartPhone
# Concepts Tested:
# Inheritance
# Method overriding
# class Mobile:
#     def call(self):
#         print("Calling...")
#     def message(self):
#         print("Sending Message...")
# class SmartPhone(Mobile):
#     def camera(self):
#         print("Opening Camera...")
#     def internet(self):
#         print("Connecting Internet...")
#     def call(self):
#         print("Video Calling...")
# s1 = SmartPhone()
# s1.call()
# s1.message()
# s1.camera()
# s1.internet()
#===========practices Questions============================#
# 1.How do you write a program to check whether a character is a vowel or consonant?
# input="a"
# vowels="aeiou"
# for i in input:
#     if i.lower() in vowels:
#         print("its vowel")
#     else:
#         print("its consonant")
# 2.How do you check whether a character is an alphabet or not?
# x="-"
# y="alphabet"
# for i in x:
#     if i in y:
#         print("its a character")
#         break
#     else:
#         print("its not a character")
#3.How do you find the ASCII value of a character?
# x="A"
# print("the ascii value of '"+ x +"' is",ord(x))
