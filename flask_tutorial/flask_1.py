# from flask import Flask
# app=Flask(__name__)

# @app.route("/")
# def word_1():
#     return "hello world"

# @app.route("/get_name/<name>")
# def user_1(name):
#     return  f'hi {name}'

# @app.route("/<int:a>/<int:b>")
# def addition_1(a,b):
#     return str(a+b)

# @app.route("/<int:a>")
# def list_num(a):
#     temp=[]
#     for i in range(1,a+1):
#         temp.append(i)
#     return temp
# @app.route("/eligible_checker/<int:age>")
# def eligible(age):
#     if age>=18:
#         return "eligible for vote"
#     else:
#         return "not eligible for vote"
# @app.route("/number_checker/<int:num>")
# def factors_1(num):
#     temp=[]
#     for i in range(1,num+1):
#         if num%i==0:
#             temp.append(i)
#     return temp

# if __name__=="__main__":
#     app.run(host='0.0.0.0',port=8001,debug=True)
# 1. The Greeter Endpoint
#  Write a GET API ⁠/api/welcome⁠ that accepts a ⁠user⁠ query parameter.
#  If ⁠user⁠ is provided, return ⁠"Welcome, <user>!"⁠.
#  If ⁠user⁠ is not provided, default to ⁠"Welcome, Guest!"⁠.
# from flask import Flask
# app = Flask(__name__)

# @app.route("/api/welcome")
# def guest():
#     return "Welcome, Guest!"

# @app.route("/api/welcome/<user>")
# def welcome(user):
#     return f"Welcome, {user}!"

# if __name__ == "__main__":
#     app.run(host="0.0.0.0", port=8001, debug=True)
# 2. Simple Calculator
#  Create an endpoint ⁠/api/add⁠ that accepts two query parameters: ⁠num1⁠ and ⁠num2⁠.
#  Parse them as integers, calculate their sum, and return the result in JSON format: ⁠{"result": 15}⁠.
# from flask import Flask
# app=Flask(__name__)

# @app.route("/add/<int:num1>/<int:num2>")
# def calculator(num1,num2):
#     return f"result : {str(num1+num2)}"
# if __name__=="__main__":
#     app.run(host="0.0.0.0", port=8001, debug=True)

# 1. Age Checker / Eligibility API
#  Create an endpoint ⁠/api/check-eligibility⁠ that takes an ⁠age⁠ query parameter.
#  Make sure ⁠age⁠ is automatically cast to an integer using Flask's ⁠type=int⁠.
#  Return ⁠{"eligible": true}⁠ if age is 18 or older, otherwise ⁠{"eligible": false}⁠.
# from flask import Flask
# app=Flask(__name__)

# @app.route("/api/check/<int:age>")
# def eligibility(age):
#     if age>=18:
#         return f"eligible:true"
#     else:
#         return f"eligible:false"
# if __name__=="__main__":
#     app.run(host='0.0.0.0',port=8001, debug=True)

# 2. Filtering a Static List
#  Given a list of books in Python (each book having ⁠title⁠, ⁠author⁠, and ⁠year⁠), write a GET API ⁠/api/books⁠ that accepts an ⁠author⁠ query parameter.
#  If ⁠author⁠ is provided, return only the books written by that author.
#  If ⁠author⁠ is omitted, return all books.
# from flask import Flask
# app=Flask(__name__)
# books=[
#     {'title':'python','author':'sam','year':1998},
#     {'title':'flask','author':'priya','year':1999},
#     {'title':'sql','author':'ram','year':2000}]
# @app.route("/api/books")
# def book_1():
#     return books
# @app.route("/api/books/<author>")
# def filt_book(author):
#     if author:
#         temp=[]
#         for i in books:
#             if i['author']==author:
#                 temp.append(i)
#         return temp
# if __name__=="__main__":
#     app.run(host='0.0.0.0',port=8001, debug=True)
    