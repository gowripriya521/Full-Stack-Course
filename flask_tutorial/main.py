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



