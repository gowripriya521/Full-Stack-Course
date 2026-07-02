# from datetime import datetime 
# from time import sleep
# print(datetime.now().time())
# sleep(5)
# print(datetime.now().time())

# def test_dec(func):
#     def wrapper(*args,**kwargs):
#         print("function started")
#         result = func(*args,**kwargs)

#         print("function ended")
#         return result
#     return wrapper

# @test_dec
# def greet():
#     print("hello")
# greet()
# x="Gaddam gowri priya"
# temp={}
# for i in x:
#     if i in temp:
#         temp[i]+=1
#     else:
#         temp[i]=1
# print(temp["i"])
# 1. The "Stop" Command
# The Goal: Keep asking the user to type a word.
# If the word is "stop" (in any casing, like "STOP" or "stop"), 
# end the loop. Otherwise, tell them "I will keep going..." and ask again.
# def word_1():
#     while True:
#         user = input("enter a word:")
#         if user.lower() =="stop":
#             print("done")
#             break
#         else:
#             print("i will keep going...")
# word_1()   
# 2. The Positive Inputter
# The Goal: Ask the user for a number.
#  If the number is negative, print "Error: Negative number" and ask again. 
# If the number is positive, print "Thank you!" and end the loop.
# def positivenum(func):
#     def wrapper(*args,**kwargs):
#         while True:
#             user = int(input("enter a number:"))
#             if user<0:
#                 print("error:Negative number")
#             else:
#                 print("Thank you!")
#                 break
#     return wrapper
# @positivenum
# def greet():
#     ...
# greet()
# 3. Vowel Hunter
# The Goal: Ask the user for a single word. 
# Loop through every letter in that word. 
# If the letter is a vowel (a, e, i, o, u), print "Found a vowel!".
# If not, print the letter itself.
# def hunt(func):
#     def wrapper(*args,**kwargs):
#         word=args[0]
#         for i in word:
#             if i.lower() in "aeiou":
#                 print("found")
#             else:
#                 print(i)
#         func(*args,**kwargs)
#     return wrapper
# @hunt
# def greet(word):
#     ... 
# greet("cat")  
# 1. Create a decorator that prints "Function Started" before executing the function and "Function Ended" after execution.
# Concepts Tested:
# Basic decorator
# Wrapper function
# def test_dec(func):
#     def wrapper(*args,**kwargs):
#         print("function started")
#         result = func(*args,**kwargs)

#         print("function ended")
#         return result
#     return wrapper

# @test_dec
# def greet():
#     print("hello")
# greet()
# 2. Create a decorator that counts how many times a function has been called.
# Concepts Tested:
# Variables
# Closures
# Decorators
# def dectimes(func):
#     func.count=0
#     def wrapper(*args,**kwargs):
#         func.count+=1
#         print("function called:",func.count," time(s)")
#         func()
#     return wrapper
# @dectimes
# def greet():
#     print("hello")
# greet()
# greet()
# 3. Create a decorator that measures the execution time of a function.
# import time
# def timer(func):
#     def wrapper():
#         start = time.time()
#         func()
#         end = time.time()
#         print("Execution Time:", end - start)
#     return wrapper
# @timer
# def display():
#     print("Learning Python Decorators")
# display()
# 4. Create a decorator that logs the function name whenever it is executed.
# def logger(func):
#     def wrapper():
#         print("Calling function:", func.__name__)
#         func()
#     return wrapper
# @logger
# def add():
#     print(10 + 20)
# add()
# 5. Create a decorator that repeats a function 5 times.
# def repeat(func):
#     def wrapper():
#         for i in range(5):
#             func()
#     return wrapper
# @repeat
# def hello():
#     print("Hello")
# hello()
# 6. Create a decorator that accepts any number of positional arguments (*args).
# def display_args(func):
#     def wrapper(*args):
#         print("Arguments:", args)
#         func(*args)
#     return wrapper
# @display_args
# def add(a, b):
#     print("Sum =", a + b)
# @display_args
# def multiply(a, b):
#     print("Product =", a * b)
# add(10, 20)
# multiply(5, 4)
# 7. Create a decorator that accepts keyword arguments (**kwargs).
# def display_kwargs(func):
#     def wrapper(**kwargs):
#         print(kwargs)
#         func(**kwargs)
#     return wrapper
# @display_kwargs
# def student(name, age):
#     print("Name:", name)
#     print("Age:", age)
# student(name="Priya", age=22)
# 8. Create a decorator that prints all arguments passed to a function before execution.
# def show_arguments(func):
#     def wrapper(*args):
#         print("Arguments:")
#         for i in args:
#             print(i)
#         func(*args)
#     return wrapper
# @show_arguments
# def numbers(a, b, c):
#     print("Function Executed")
# numbers(10, 20, 30)
# 9. Create a decorator that validates whether all arguments are integers.
# def validate(func):
#     def wrapper(*args):
#         for i in args:
#             if type(i) != int:
#                 print("Invalid Input")
#                 return
#         func(*args)
#     return wrapper
# @validate
# def add(a, b):
#     print("Sum =", a + b)
# add(10, 20)
# add(10, "20")
# 10. Create a decorator that doubles the returned value.
# def double_result(func):
#     def wrapper():
#         result = func()
#         print("Return Value:", result)
#         print("Decorator Output:", result * 2)
#     return wrapper
# @double_result
# def number():
#     return 20
# number()