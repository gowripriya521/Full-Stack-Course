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
# def user_1():
#     while True:
#         word = input("enter a word:")
#         if word.lower()=="stop":
#             print("stopping.....")
#             break
#         else:
#             print("i will keep going....")
# user_1()
# def positive_1():
#     while True:
#         num = int(input("enter a number:"))
#         if num<0:
#             print("Error:negative number")
#         else:
#             print("Thank you!")
#             break
# positive_1()
# def vowel_1(word):
#     for i in word:
#         if i.lower() in "aeiou":
#             print("Found a vowel!")
#         else:
#             print(i)
# vowel_1("CAT")
# def even_1():
#     total=0
#     num=1
#     while (num<=50):
#         if num%2==0:
#             total+=num
#         i+=1
#     print("sum of even numbers:",total)
# even_1()
# def lucky_1(num):
#     i=0
#     #while i<=30:
#     for i in range(1,31):
#         if i%7==0:
#             print("Lucky!")
#         else:
#             print("number:",i)
# lucky_1(7)
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
# def password_1():
#     p = "Test123"
#     count = 3
#     while True:
#         users = input("enter password:")
#         if users == p:
#             print("correct")
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
car1={
    "model":2001,
    "company":"audi",
    "price" : 10.20,
    "color":"Blue"
}
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