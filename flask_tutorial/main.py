# from flask import Flask, request
# from mydata import *

# app = Flask(__name__)

# @app.route("/studentdata/<int:rollno>")
# def student(rollno):
#     print(rollno)
#     return (x[rollno])

# @app.route("/allstudents")
# def student_get_alldata():
#     return x

# @app.route("/classnames/<int:classname>")
# def student_get_names(classname):
#     return {
#         "student names":student_class(classname)
#     }
# @app.route("/usernames")
# def student_names():
#     return {
#         "all_student": all_student()
#     }

# if __name__ == "__main__":
#     app.run(debug=True, host="0.0.0.0", port=8001)