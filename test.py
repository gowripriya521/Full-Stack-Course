# s = [1,2,3,4,5,6]
# print(s[::-1])
# print(s[2:])
# print(s[:2])
# #===============================
# x = 10
# if x > 5:
#     pass
# else:
#     print("less than 5")
# #======================================
# age = 20
# id1 = True
# if age>=18:
#     if id1:
#         print("you can enter")
# #===============================================
# for i in range(1,6):
#     if i == 3 :
#         continue
#     print(i)
# #================================================
# i = 1
# while i<=5:
#     print(i)
#     i+=1
#================================================
# def add_1(a,b,c):
#     return a+b+c
# result=add_1(2,3,5)
# #===================================
# def check_1(a):
#     if a==0:
#         return None
#     if a<0:
#         return False
#     else:
#         return True
# #=====================================
# def rev_1(n):
#    while n>0:    
#        n-=1
# rev_1(10)
# #=======================
# def num_1(m):
#     i=1
#     while i<=m:
#         #print(i)
#         if i%2 == 0:
#             print(i)
#         i+=1
# print(num_1(10))
# #=========================================
# def vote_1(age):
#     if type(age)==str:
#         return "invalid input"    
#     elif age<=0:
#         return "invalid"
#     elif age>=18:
#         return "eligible for vote"
#     else:
#         return "not eligible for vote"
# print(vote_1("A"))
# # ========================
# def marks(*sub):
#     sub = ((a,b,c,d,e,f)/6)
#     return (sub)
# marks(50,50,50,50,50,50)
# #============================================
# x = str("s1")
# y = str(4.8)
# z = str(3.0)
# print(x,y,z)
# #==========================================
# x = int(1)
# a = float(x)
# b = str(x)
# print(type(a),type(b))
# print(a,b)
# #=========================================
# list_1 = ["41","two"]
# print(list_1)
# #==========================================
# x = (1)
# y = ("hi")
# z = (2.4)
# print(type(x),type(y),type(z))
# print(x,y,z)
# #=========================================
# x = [1,3,4,5]
# x[0] = 10
# print(x)
# x.index(1,4)
# print(x)
# #============================================
# my_ls= [1,2,3,4,2,2,3]
# my_ls.sort()
# print(my_ls)
# #===========================================
# colors = {"red","green","blue"}
# print(colors)
# colors.add("yellow")
# colors.discard("green")
# print(colors)
# print(len(colors))
# #===============================
# 1. The "Stop" Command
# The Goal: Keep asking the user to type a word.
# If the word is "stop" (in any casing, like "STOP" or "stop"), 
# end the loop. Otherwise, tell them "I will keep going..." and ask again.
# def user_1():
#     while True:
#         word = input("enter a word:")
#         if word.lower()=="stop":
#             print("stopping.....")
#             break
#         else:
#             print("i will keep going....")
# user_1()
# 2. The Positive Inputter
# The Goal: Ask the user for a number. 
# If the number is negative, 
# print "Error: Negative number" and ask again.
# If the number is positive, 
# print "Thank you!" and end the loop.
# def positive_1():
#     while True:
#         num = int(input("enter a number:"))
#         if num<0:
#             print("Error:negative number")
#         else:
#             print("Thank you!")
#             break
# positive_1()
# 3. Vowel Hunter
# The Goal: Ask the user for a single word. 
# Loop through every letter in that word. 
# If the letter is a vowel (a, e, i, o, u), print "Found a vowel!". 
# If not, print the letter itself.
# def vowel_1(word):
#     for i in word:
#         if i.lower() in "aeiou":
#             print("Found a vowel!")
#         else:
#             print(i)
# vowel_1("CAT")
# 4. The Even Sum
# The Goal: Use a loop to check every number from 1 to 50. 
# If the number is even, add it to a "total" variable. 
# After the loop finished, print the final sum.
# def even_1():
#     total=0
#     num=1
#     while (num<=50):
#         if num%2==0:
#             total+=num
#         num+=1
#     print("sum of even numbers:",total)
# even_1()
# 5. Lucky 7s
# The Goal: Print numbers from 1 to 30. 
# If a number is divisible by 7, 
# print "Lucky!" instead of the number. 
# If it is not divisible by 7, just print the number.
# def lucky_1(num):
#     i=0
#     #while i<=30:
#     for i in range(1,31):
#         if i%7==0:
#             print("Lucky!")
#         else:
#             print("number:",i)
# lucky_1(7)
# 6. The Budget Tracker
# The Goal: Start with a variable balance = 100. 
# Ask the user for the price of an item. 
# If they have enough money, subtract the price from the balance. 
# If they don't, print "Insufficient funds!" and end the loop.
# def budget_1():
#     bala=100
#     while True:
#         price=int(input("enter item price:"))
#         if price<=bala:
#                 bala-=price
#                 print(bala)
#         else:
#                 print("insufficient fund!") 
#                 break
# budget_1()
# 7. The Password Lockout
# The Goal: Set a secret password. 
# Allow the user to try and guess it. 
# If they get it wrong, tell them "Try again." 
# If they fail 3 times in a row, print "Account Locked" and stop the loop.
# def password_1():
#     p = "Test123"
#     count = 3
#     while True:
#         users = input("enter password:")
#         if users == p:
#             print("correct")
#             break
#         elif count == 0:
#             print("Accountlocked")
#         else:
#             print("try again")
#             count-=1
# password_1()
#new=========================new===============================new
#1.The “Exit Word” Loop
# Goal:
# Keep asking the user to enter a word.
# If the user types "exit" (any case), stop the loop.
# Otherwise, print "Still running...".
# def word_1():
#     while True:
#         user= input("enter a word:")
#         if user.lower() == "exit":
#             print("stop")
#             break
#         else:
#             print("still running..")
# word_1()
# 2. Only Odd Numbers
# Goal:
# Ask the user for a number.
# If it is even → print "Even not allowed" and ask again
# If it is odd → print "Good choice!" and stop.
# def odd_1():
#     while True:
#         user = int(input("enter a number:"))
#         if user%2==0:
#             print("even not allowed")
#         else:
#             print("good chocie!")
#             break
# odd_1()
# 3. Letter Checker
# Goal:
# Ask the user for a word.
# Loop through each letter:
# If the letter is uppercase → print "Uppercase found"
# Otherwise → print the letter
# def checker_1():
#     user = input("enter a word:")
#     i=0
#     while i<len(user):
#         if user[i].isupper():
#             print("uppercase found")
#             break
#         i+=1
#     print(user)      
# checker_1()
# 4. Sum of Multiples of 3
# Goal:
# Loop from 1 to 40
# If number is divisible by 3 → add to total
# After loop → print total
# def sum_1():
#     total=0
#     for i in range(1,41):
#         if i%3==0:
#             total=total+i
#     print("total",total)
# sum_1()
# 5. Fizz Instead of 5
# Goal:
# Print numbers from 1 to 25
# If divisible by 5 → print "Fizz"
# Otherwise → print number
# def fizz_1():
#     for i in range(1,26):
#         if i%5==0:
#             print("Fizz")
#         else:
#             print(i)
# fizz_1()
# 6. Wallet Checker
# Goal:
# Start with balance = 200
# Ask user for amount:
# If amount ≤ balance → subtract and show remaining
# If amount > balance → print "Not enough money" and stop
# def wallet_1():
#     bala=200
#     user=int(input("enter a amount:"))
#     if user<=bala:
#         user=bala-user
#         print(user)
#     else:
#         print("not enough money")
# wallet_1()
# 7. PIN Checker
# Goal:
# Set a PIN (e.g., "1234")
# Ask user to enter PIN
# If correct → print "Access Granted"
# If wrong → print "Wrong PIN"
# After 3 wrong attempts → print "Card Blocked"
# def pin_1():
#     p="T123"
#     count=3
#     while True:
#         use=input("enter a pin:")
#         if use==p:
#             print("access Granted")
#             break
#         elif count==0:
#             print("card block")
#         else:
#             print("wrong pin")
#             count-=1
# pin_1()
# 8. Count Down Game
# Goal:
# Start from 10 and count down to 1
# When it reaches 0 → print "Boom!"
# def game_1():
#     for i in range(10,0,-1):
#         print(i)
#     print("boom!")
# game_1()
# 9. Reverse Printer
# Goal:
# Ask user for a word
# Print each letter in reverse order using a loop
# def rev_1():
#     use = input("enter a word:")
#     i=len(use)-1
#     while i>=0:
#         print(use[i])
#         i-=1
# rev_1()
# 10. Divide Until Valid
# Goal:
# Ask user for a number
# If number is 0 → print "Cannot divide by zero" and ask again
# Otherwise → print 100 / number and stop
# def valid_1():
#     while True:
#         user=int(input("enter a number:"))
#         if user == 0:
#             print("cannot divide by zero")
#         else:
#             print(100/user)
#             break
# valid_1()
# def exa_1(name):
#     print("Hello", name)
# car1={
#     "model":2001,
#     "company":"audi",
#     "price" : 10.20,
#     "color":"Blue"
# }
# x = [1,2,3,5,6,7,2,3]
# small=x[0]
# for i in x:
#     if i<small:
#         small=i
# print("smallest",small)
# import lm as mx
# a=mx.car1["color"]
# print(a)
# import math
# print(math.sqrt(36))
# def math_1():
#     n=36
#     i=0
#     while i*i<=n:
#         if i*i==n:
#             print("sqr:",i)
#             break
#         i+=1
# math_1()
# 1. The Inventory Manager (Dict + Loop + If)
# Scenario: You have a dictionary representing a store's inventory.
# inventory = {"apples": 50, "bananas": 0, "oranges": 12, "pears": 0}
# Task: Loop through the dictionary.
# If an item's count is 0, 
# print "Item [name] is out of stock!" Otherwise, 
# print "[name]: [count] units available."
# def man_1():
#     inventory = {"apples":50, "bananas":0,"oranges":12,"pears":0}
#     for i in inventory:
#         count = inventory[i]
#         if count==0:
#             print(f"items{i} is out of stock!")
#         else:
#             print(f"{i}:{count}units available")
# man_1()
# def man_1():
#     inventory = {"apples":50, "bananas":0,"oranges":12,"pears":0}
#     items=list(inventory)
#     i=0
#     while i<len(items):
#         name = items[i]
#         if inventory[name]==0:
#             print(f"{ name}is out of stock!")
#         else:
#             print(f"{name}:{inventory[name]},units available.")
#         i+=1
# man_1()
# 2. Character Frequency Counter (Dict + String/Loop)
# Scenario: You want to see which letters appear most often in a word.
# Task: Take a word like "pomegranate". Create an empty dictionary. Loop through each letter in the word:
# If the letter is already in the dictionary, increase its value by 1.
# If it isn't, add it to the dictionary with a value of 1.
# Result: You should end up with {'p': 1, 'o': 1, 'm': 1, ...}
# x="pomegranate"
# def cou_1():
#     i ={}
#     for letter in x:
#         if letter in i:
#             i[letter]+=1
#         else:
#             i[letter]=1
#     print(i)
# cou_1()
# x="pomegranate"
# def cou_1():
#     f={}
#     i=0
#     while i<len(x):
#         letter =x[i]
#         if letter in f:
#             f[letter]+=1
#         else:
#             f[letter]=1
#         i+=1
#     print(f)
# cou_1()
# 3. Nested Data Extraction (List of Dicts + Loop)
# Scenario: This is how data usually looks when it comes from the internet (JSON style).
# users = [{"name": "Alice", "role": "Admin"}, {"name": "Bob", "role": "User"}, {"name": "Charlie", "role": "User"}]
# * Task: Loop through the users list. Inside the loop, 
# use an if statement to check if the user's "role" is "Admin". If it is, print their name.
# users =[
#     {
#         "name": "Alice",
#         "role": "Admin"
#     }, 
#     {
#         "name": "Bob",
#         "role": "User"
#     }, 
#     {
#         "name": "Charlie",
#         "role": "User"
#     }
# ]
# def use_1():
#     for i in users:
#         if i["role"]=="Admin":
#             print(i["name"])
# use_1()
# def num_1(num):
#     if num>0:
#         return "positive number"
#     else:
#         return "negative"
#print(num_1(5))
# import random
# print(random.randint(1, 10))
# x = min(5,10,25)
# y = max(5,10,25)
# print("minimum value:",x)
# print("maximum value:",y)/
# x = abs(-7.25)
# print(x)
# x = pow(4,3)
# print(x)
# x=min(5,10)
# print("minimum values:",x)
# y=max(5,10)
# print("maximum value:",y)
# z=abs(-7.25)
# print(z)
# i=pow(4,3)
# print(i)
# try:
#     print (x)
# except:
#     print("an error occurred")
# finally:
#     print("Execution complete")
# try:
#     print("hello")
# except:
#     print("something went wrong")
# else: 
#     print("nothing went wrong")
# x=-1
# if x<0:
#     raise Exception("sorry,no numbers below zero")
# x="hello"
# if not type(x) is int:
#     raise TypeError("only integers are allowed")
# 1 : Basic try-except
# Instructions
# Write a program to divide 10 by 0
# Handle the error using except
# Print "Error handled"
# x = 10
# y=0
# try:
#     print(x/y)
# except:
#     print("Error handled")
# 2 : ValueError
# Instructions
# Ask the user to enter a number
# Convert input into integer
# Handle invalid input using except
# Print "Invalid number" if error occurs
# try:
#     num =int(input("enter a number:"))
#     print(num)
# except:
#     print("invalid number")
# Code Challenge 3 : NameError
# Instructions
# Print a variable that is not defined
# Handle the error using except
# Print a custom message
# try:
#     print(x)
# except:
#     print("variable is not defined")
# Code Challenge 4 : else Block
# 📝 Instructions
# Write a program to divide two numbers
# Use try and except
# Use else to print "Division successful" when no error occurs
# try:
#     num=int(input("enter a number:"))
#     print(10/num)
# except:
#     print("zero error")
# else:
#     print("division successful")
# 5 : finally Block
# 📝 Instructions
# Write a program using try and except
# Add a finally block
# Print "Program ended" inside finally
# x = "abs"
# try:
#     print(x)
# except:
#     print("value error")
# finally:
#     print("program ended")
# 6 : Multiple Exceptions
# 📝 Instructions
# Write code that may cause:
# ValueError
# ZeroDivisionError
# Handle both errors separately
# Print different messages for each error
# try:
#     x=int(input("enter a number:"))
#     print(10/x)
# except ValueError:
#     print("invalid number")
# except ZeroDivisionError:
#     print("Cannot divided by zero")
# 7 : raise Keyword
# 📝 Instructions
# Create a variable x = -5
# Check if number is less than 0
# Raise an exception with message:
# "Negative numbers not allowed"
# x=-5
# if x<0:
#     raise TypeError("negative numbers not allowed")
# 8 : TypeError
# Instructions
# Create a variable with string value "hello"
# Check if it is integer or not
# Raise TypeError if not integer
# x = "Hello"
# if not type(x) is int:
#     raise TypeError("not a integer")
# 9.Instructions
# Ask the user to enter two numbers
# Perform division
# Handle:
# invalid number input
# divide by zero
# Use:
# try
# except
# else
# finally
# Print suitable messages for each block
# try:
#     x = int(input("enter a number of s1:"))
#     y = int(input("enter a number s2:"))
#     result= x/y
# except ValueError:
#     print("invalid number input")
# except ZeroDivisionError:
#     print("cannot divide by zero")
# else:
#     print("Division result:",result)
# finally:
#     print("completed")

# def add_1(a,b):
#     return a+b
# num=[1,2,4,4,5,6,7,4,5,0,0]
# temp={}
# for i in num:
#     if i not in temp:
#         temp[i]=1
#     else:
#         temp[i]+=1
# print(temp)