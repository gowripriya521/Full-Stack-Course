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
#     temp=[]
#     for i in books:
#         if i['author']==author:
#             temp.append(i)
#     return temp
   
# if __name__=="__main__":
#     app.run(host='0.0.0.0',port=8001, debug=True)

#1.write a fizzbuzz program
# from flask import Flask
# app=Flask(__name__)
# @app.route("/fizzbuzz/<int:n>")
# def fizz_buzz(n):
#     temp=[]
#     for i in range(1,n+1):
#         if i%3==0 and i%5==0:
#             temp.append("fizz buzz")
#         elif i%3==0:
#             temp.append("fizz" )
#         elif i%5==0:
#             temp.append("buzz")
#         else:
#             temp.append(i)
#     return temp
# if __name__=="__main__":
#     app.run(host='0.0.0.0',port=8001,debug=True)

#2.table
# from flask import Flask
# app=Flask(__name__)
# @app.route("/table/<int:num>")
# def table_1(num):
#     temp=[]
#     for i in range(1,11):
#         temp.append(f"{num} x {i} = {num*i}")
#     return temp
# if __name__=="__main__":
#     app.run(host='0.0.0.0',port=8001,debug=True)

#3.guess the game
# from flask import Flask
# app=Flask(__name__)
# @app.route("/guessgame/<int:num>/<int:target>")
# def guess(num,target):
#     if num>target:
#         return "high"
#     elif num<target:
#         return "low"
#     elif num==target:
#         return "you win"
#     else:
#         return "error"
# if __name__=="__main__":
#     app.run(host='0.0.0.0',port=8001,debug=True)

#4. frequency count program
# from flask import Flask
# app=Flask(__name__)
# @app.route("/budget")
# def number():
#     num=[1,2,3,4,4,5,6,7,4,0,0,5]
#     temp={}
#     for i in num:
#         if i not in temp:
#             temp[i]=1
#         else:
#             temp[i]+=1
#     return temp 
# if __name__=="__main__":
#     app.run(host='0.0.0.0',port=8001,debug=True)
from flask import request
from flask import Flask
app=Flask(__name__)
@app.route("/",methods=['POST'])
def hello_world_post():
    if request.method=='POST':
        data=request.get_json()
        for i in data:
            my_dict[i]=data[i]
    return "200"