import json
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

data1 = {}

def create_user_core(email,name,age):
    if email in data1:
        return False, "email already exist"
    data1[email] = {
        "name":name,
        "age":age
    }
    with open("./sample.json","w") as f:
        json.dump(data1,f,indent=4)
    return True,"user created successfully"

def read_data():
    with open("./sample.json","r") as f:
        res = json.load(f)
    return res

def update_user_core(email,name,age):
    if email not in data1:
        return False,"email not found"
    data1[email] = {
        "name": name,
        "age": age
    }
    with open("./sample.json", "w") as f:
        json.dump(data1, f, indent=4)
    return True,"user updated successfully"

def delete_user_core(email):
    if email not in data1:
        return False,"email not found"
    del data1[email]
    with open("./sample.json", "w") as f:
        json.dump(data1, f, indent=4)
    return True, "user deleted successfully"

# Student Management:
# Create a dictionary using roll_no as the key.
# Store name, age, and course.
# Write the data to students.json.
# Read and display all students.
def create_user(roll_no,name,age,course):
    if roll_no in data1:
        return False,"this roll no already exist"
    data1[roll_no]={
        "name":name,
        "age":age,
        "course":course
    }
    with open("./student.json","w") as f:
        json.dump(data1,f,indent=4)
    return True,"user created Successfull"
# create_user(101,"suresh",27,"sql")
# print(data)

# Employee Management:Use email as the key.
# Store name, age, and salary.
# Implement:Create,Read,Update,Delete
def create_user1(email,name,age,salary):
    if email not in data1:
        return False,"this mail already exist"
    data1[email]={
        "name":name,
        "age":age,
        "salary":salary
    }
    with open("./sample.json","w") as f:
        json.dump(data1,f,indent=4)
    return True

def contact_book(contact_id,name,phone_no,email):
    if contact_id in data1:
        return False,"already exist"
    data1[contact_id]={
        "name":name,
        "phone_no":phone_no,
        "email":email
    }
    with open("./contacts.json","w") as f:
        json.dump(data1,f,indent=4)
    return True,"user create successfully"
# contact_book(1,"ram",73835728252,"ram@gmail.com")
# print(data)

def all_contact():
    with open("./contacts.json","r") as f:
        res = json.load(f)
    return res

def update_contact(contact_id,name,phone_no,email):
    if contact_id not in data1:
        return False,"contact_id not found"
    data1[contact_id] = {
        "name": name,
        "phone_no":phone_no,
        "email":email
    }
    with open("./contacts.json", "w") as f:
        json.dump(data1, f, indent=4)
    return True,"user updated successfully"

def delete_contact(contact_id):
    if contact_id not in data1:
        return False,"contact_id not found"
    del data1[contact_id]
    with open("./contacts.json", "w") as f:
        json.dump(data1, f, indent=4)
    return True, "user deleted successfully"

#1. Persistent Page Visitor Counter API
# Build a endpoint that tracks page hits. The API should read the current integer counter from a text file named 
# counter.txt using open('counter.txt', 'r+') (or read/write mode), increment the integer value by 1, save the
# new count back to the file, and return the updated count. 
# Endpoint & Method
# Headers
# File Handled
# POST /api/v1/counter/increment
# Accept: application/json
# counter.txt (Mode: r+ or r followed by w)

def visitor_counter():
    with open("counter.txt", "r+") as f:
        previous_count = int(f.read())
        current_count = previous_count + 1
        f.seek(0)
        f.write(str(current_count))
    return current_count, previous_count

#2. Implement two endpoints for a visitor guestbook. A POST endpoint receives a guest's name and message, formatted as a
# single line, and appends it to guestbook.txt using open('guestbook.txt', 'a'). A GET endpoint reads all
# entries using open('guestbook.txt', 'r') and returns them as a JSON list. 
# Endpoints:POST /api/v1/guestbook | GET /api/v1/guestbook
# File Handled:guestbook.txt (Modes: a for append, r for read)

def add_guest(name, message):
    with open("guestbook.txt", "a") as f:
        f.write(name + ": " + message + "\n")

def get_guests():
    with open("guestbook.txt", "r") as f:
        entries = f.read().splitlines()
    return entries

#  4: Plaintext Dynamic Settings Manager API
# BEGINNER
# Build an API endpoint that updates application runtime settings stored in a flat config.txt file in KEY=VALUE format.
# The endpoint should accept new config key-values, write/overwrite them to config.txt using open('config.txt',
# 'w'), and provide a GET route to read and parse the settings into JSON. 
# Endpoints
# File Handled
# PUT /api/v1/config | GET /api/v1/config
# config.txt (Modes: w for overwrite, r for read)
def create_config(data):
    with open("config.txt","w") as f:
        for key,value in data.items():
            f.write(f"{key}={value}\n")
    return data

def get_config():
    config={}
    with open("config.txt","r") as f:
        lines=f.readlines()
        for i in lines:
            data=i.split("=")
            key=data[0]
            value=data[1]
            config[key]=value
    return config

#  6: CSV Contact Manager with Manual File Parsing
# INTERMEDIATE
# Create an API for managing contacts without using the csv module. Write a POST /api/v1/contacts route that opens 
# contacts.csv in append mode ('a') and writes formatted rows (quoting fields if necessary). Build a GET /api/v1/
# contacts route that opens the CSV using open('contacts.csv', 'r'), manually parses the rows line-by-line, and
# converts them into structured JSON. 
# Endpoints
# File Handled
# POST /api/v1/contacts | GET /api/v1/contacts
# contacts.csv (Modes: a for write, r for read)
def create_contact(data):
    name = data.get("name")
    email = data.get("email")
    phone = data.get("phone")
    with open("contacts.csv", "a") as f:
        f.write(f"{name},{email},{phone}\n")
    return {
        "name": name,
        "email": email,
        "phone": phone
    }
def get_contacts():
    contacts = []
    with open("contacts.csv", "r") as f:
        lines = f.readlines()
    for i in range(len(lines)):
        line = lines[i].strip()
        data = line.split(",")
        contact = {
            "id": i + 1,
            "name": data[0],
            "email": data[1],
            "phone": data[2]
        }
        contacts.append(contact)
    return contacts

#  7: Flat-File JSON Database CRUD API
# INTERMEDIATE
# Build a full CRUD API for managing a Task List using a single tasks.json file as a flat-file database. Implement GET, 
# POST, and DELETE endpoints. Each route must explicitly open the file using open('tasks.json', 'r') to read
# current state and open('tasks.json', 'w') combined with json.dump() to persist state changes. 
# Endpoints
# File Handled
# GET /api/v1/tasks | POST /api/v1/tasks | DELETE /api/v1/tasks/<id>
# tasks.json (Modes: r and w)
def get_tasks():
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
    return tasks

# def create_task(data):
#     with open("tasks.json", "r") as f:
#         tasks = json.load(f)
#         print(type(tasks))
#     task = {
#         "id": len(tasks) + 101,
#         "title": data.get("title"),
#         "priority": data.get("priority")
#     }
#     tasks.append(task)
#     with open("tasks.json", "w") as f:
#         json.dump(tasks, f, indent=4)
#     return task
# create_task({"id":101,"title":"flask","priority":"high"})
# # print(type({"id":101,"title":"flask","priority":"high"}))

def create_task(data):
    with open("tasks.json","r") as f:
        print(json.load(f))
        tasks=json.load(f)  
    new_id=len(tasks)+101
    tasks[new_id]={
        "title":data.get("title"),
        "priority":data.get("priority")
    }
    with open("tasks.json","w") as f:
        json.dump(tasks,f,indent=4)
    return True
# create_task({"id":101,"title":"flask","priority":"high"})


def delete_task(task_id):
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            with open("tasks.json", "w") as f:
                json.dump(tasks, f, indent=4)
            return True, len(tasks)
    return False, len(tasks)

# 8: Log Tail & Seeking API
# INTERMEDIATE
# Build a log tailing API endpoint GET /api/v1/logs/tail?lines=N that returns only the last N lines of a large system
# log file (server.log). To make it performant, open the file using open('server.log', 'r') and utilize file pointer
# seeking (f.seek() and f.tell()) or buffer reading from the end of the file rather than reading the whole file into
# memory. 
# Endpoint & Method
# File Handled
# EXPECTED API INPUT
# GET /api/v1/logs/tail?lines=5
# server.log (Mode: rb or r with f.seek())
def get_last_lines(number):
    with open("server.log", "r") as f:
        lines = f.readlines()
    return lines[-number:]

#  9: File-Based User Auth & Credentials Store API
# INTERMEDIATE
# Build a lightweight user authentication API using a flat users.txt file to store user records formatted as 
# username:hashed_password . Implement POST /api/v1/auth/register to append new records with 
# open('users.txt', 'a') (checking duplicates first), and POST /api/v1/auth/login to scan lines with 
# open('users.txt', 'r') and verify credentials. 
# Endpoints
# File Handled
# POST /api/v1/auth/register | POST /api/v1/auth/login
# users.txt (Modes: a for sign-up, r for verification)

def register_user(data):
    username = data.get("username")
    password = data.get("password")
    password = generate_password_hash(password)
    with open("./users.txt", "a") as f:
        f.write(username + ":" + password + "\n")
    return username

def login_user(data):
    username = data.get("username")
    password = data.get("password")
    with open("users.txt", "r") as f:
        lines = f.readlines()
    for line in lines:
        user = line.split(":")
        if user[0] == username:
            if check_password_hash(user[1][:-1], password):
                return True
    return False

# 3: Raw Text Note File Reader API
# BEGINNER
# Create an API endpoint GET /api/v1/notes/<filename> that reads text document files stored inside a server folder
# named storage/notes/ using open(). The endpoint should safely open the file in read mode, fetch its raw contents,
# and return it. Catch FileNotFoundError and return a structured 404 JSON response. 
# Endpoint & Method
# File Handled
# EXPECTED API INPUT
# GET /api/v1/notes/meeting_notes.txt
# storage/notes/meeting_notes.txt (Mode: r)
def read_note(filename):
    filepath = "storage/notes/" + filename
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        return content
    except FileNotFoundError:
        return None
    
# 5: Server Activity Logger Middleware API
# BEGINNER
# Implement a Flask @app.before_request or @app.after_request hook that intercepts every incoming HTTP
# request and appends request details to activity.log using open('activity.log', 'a'). Include a diagnostic
# endpoint GET /api/v1/analytics/summary that reads the log file using open() and returns total request counts. 
# Endpoint & Method
# File Handled
# GET /api/v1/analytics/summary
# activity.log (Modes: a for logging, r for analysis)

def save_log(method, path, ip):
    time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("activity.log", "a") as f:
        f.write(
            time + " | METHOD: " + method +
            " | PATH: " + path +
            " | IP: " + ip + "\n"
        )

def get_summary():
    with open("activity.log", "r") as f:
        lines = f.readlines()
    if len(lines) == 0:
        last_time = None
    else:
        last_time = lines[-1].split(" | ")[0]
    return len(lines), last_time


# x="gaddam gowri priya"
# temp={}
# for i in x:
#     if i in temp:
#         temp[i]+=1
#     else:
#         temp[i]=1
# print(temp["g"])

# x={i for i in range(1,100000000)}
# if 99999999 in x:
#     print("found")


# school={
#     "student1": {"name": "Alice", "total_marks": 450},
#     "student2": {"name": "Bob", "total_marks": 420},
#     "student3": {"name": "Charlie", "total_marks": 475},
#     "student4": {"name": "David", "total_marks": 390},
#     "student5": {"name": "Emma", "total_marks": 440},
#     "teacher1": {"name": "Mr. John"},
#     "teacher2": {"name": "Ms. Sarah"}
# }
# #avg=sum of students marks/total number of students 
# temp=0
# count=0
# for key,values in school.items():
#     if "total_marks" in values:
#         temp=temp+values["total_marks"]
#         count+=1
# average=temp/count
# print(average)


#1. Static Student Profile JSON Endpoint
# You are building a backend for a school portal. Define an in-memory dictionary storing the profile of a single student
# as follows:
# student_profile = {
#     "student_id": 101,
#     "name": "Sarah Connor",
#     "grade_level": 10,
#     "gpa": 3.8
# }
# Write a Flask route matching GET /student that returns this dictionary as a JSON response using Flask's
# jsonify() utility.
student_profile = {
    "student_id": 101,
    "name": "Sarah Connor",
    "grade_level": 10,
    "gpa": 3.8
}
def students_static():
    return student_profile

#2. Dynamic Teacher Lookup by ID with Error Handling
# A school administrative system maintains a dictionary of faculty members indexed by integer IDs:
# teachers = {
#     1: {"name": "Mr. Davis", "subject": "Mathematics", "office": "Room 102"},
#     2: {"name": "Ms. Vance", "subject": "English Literature", "office": "Room 204"}
# }
# Write a dynamic Flask route with an integer converter, GET /teachers/<int:teacher_id> , that looks up the teacher by key.
# REQUIREMENTS & CONSTRAINTS
# • If teacher_id exists in the teachers dictionary: return the teacher object as JSON with HTTP status code 200.
# • If teacher_id does NOT exist: return JSON {"error": "Teacher not found"} with HTTP status code 404.
teachers={
    1: {"name": "Mr. Davis", "subject": "Mathematics", "office": "Room 102"},
    2: {"name": "Ms. Vance", "subject": "English Literature", "office": "Room 204"}
}
def get_teacher(teacher_id):
    if teacher_id in teachers:
        return teachers[teacher_id]
    return None

#3. Course Seating Capacity Checker
# The registrar needs a simple API to check maximum student capacities for course codes. Given the dictionary:
# course_capacities = {
#     "MATH101": 30,
#     "BIO201": 25,
#     "HIST110": 40
# }
# Create a Flask route GET /courses/<course_code>/capacity that takes a string course code parameter.
# REQUIREMENTS & CONSTRAINTS
# • Convert string path variable to uppercase before looking up the key to handle case-insensitive requests.
# • On key match: return JSON {"course": course_code, "capacity": capacity_value} with HTTP status 200 .
# • On missing key: return JSON {"error": "Course not offered"} with HTTP status 404.
course_capacities = {
    "MATH101": 30,
    "BIO201": 25,
    "HIST110": 40
}
def get_course(course_code):
    course_code=course_code.upper()
    if course_code in course_capacities:
        return course_capacities[course_code]
    return None 

#4. Capturing URL Query Parameters into a Dictionary
# School administrators want to filter student records using arbitrary query strings in the request URL (e.g., 
# students/search?grade=11&house=Gryffindor&status=active ).
# Write a Flask route GET /students/search that extracts all incoming URL query parameters using Flask's 
# request.args object and converts them into a standard Python dictionary.
# REQUIREMENTS & CONSTRAINTS
# • Use request.args.to_dict() to convert incoming query parameters to a dictionary.
# • Return JSON structured as: {"filters_applied": <extracted_dict>, "count": <number_of_filters>} . 
def get_filters(args):
    filters = args.to_dict()
    return {
        "filters_applied": filters,
        "count": len(filters)
    }

# 5.New Student Enrollment with In-Memory Auto-Increment
# Create a POST route to register new students into an initially empty global dictionary students = {} with an auto-incrementing ID tracker next_student_id = 1001 .
# The route should accept a JSON body containing name and grade (e.g.,{"name": "Marcus Aurelius","grade": 9} ).
# REQUIREMENTS & CONSTRAINTS
# • Route: POST /students
# • Extract data using request.get_json() .
# • Store the record inside students[next_student_id] and increment next_student_id .
# • Return the newly created student record along with its assigned ID, with HTTP status code 201 Created .
students = {}
next_student_id = 1001
def create_student(data):
    global next_student_id
    student = {
        "name": data.get("name"),
        "grade": data.get("grade")
    }
    students[next_student_id] = student
    student_id = next_student_id
    next_student_id = next_student_id + 1
    return student_id, student

#6. In-Place Student Record & GPA Update
# Given an existing dictionary of student records:
# students = {
#     101: {"name": "Alex Smith", "gpa": 3.2, "grade_level": 11}
# }
# Write a route PUT /students/<int:student_id> that receives a JSON payload containing updated fields (e.g.,{"gpa": 3.55} or {"grade_level": 12, "gpa": 3.6} ) and updates the dictionary in-place.
# REQUIREMENTS & CONSTRAINTS
# • If student_id is missing from students : return JSON {"error": "Student record missing"} with HTTP 404.
# • If present: use Python dictionary update methods (e.g.,.update() ) to modify existing fields without replacing the entire record.
# • Return JSON {"message": "Student updated successfully", "student": <updated_record>} with HTTP 200 .
students = {
    101: {
        "name": "Alex Smith",
        "gpa": 3.2,
        "grade_level": 11
    }
}
def update_student(student_id, data):
    if student_id not in students:
        return None
    students[student_id].update(data)
    return students[student_id]

#7. Student Unenrollment / Record Deletion
# Given an in-memory dictionary of enrolled students:
# students = {
#     101: {"name": "Alex Smith", "status": "Active"},
#     102: {"name": "Jordan Lee", "status": "Active"}
# }
# Implement a Flask route DELETE /students/<int:student_id> that removes a student record completely from the dictionary when requested.
# REQUIREMENTS & CONSTRAINTS
# • Check if student_id exists in students.
# • If found: remove the key using pop() or del , and return JSON{"message": "Student 101 successfully  unenrolled"} with HTTP status 200.
# • If not found: return JSON {"error": "Student ID not found"} with HTTP status code 404 . 
student = {
    101: {
        "name": "Alex Smith",
        "status": "Active"
    },
    102: {
        "name": "Jordan Lee",
        "status": "Active"
    }
}
def delete_student(student_id):
    if student_id in student:
        student.pop(student_id)
        return True
    return False

#8. Class Performance Analytics & Average Grade Calculation
# A teacher stores exam score percentages for a class in a Python dictionary:
# class_grades = {
#     "Alice": 88,
#     "Bob": 92,
#     "Charlie": 78,
#     "Diana": 95,
#     "Edward": 64
# }
# Write a Flask route GET /analytics/class-average that iterates through the dictionary values, calculates mathematical summary statistics, and returns them as JSON.
# REQUIREMENTS & CONSTRAINTS
# • Calculate total enrolled count, average grade (rounded to 2 decimal places), highest score, and lowest score.
# • Handle potential empty dictionary edge cases safely without causing division-by-zero errors.
# • Return JSON format:{"total_students": 5, "average_grade": 83.4, "highest_score": 95,"lowest_score": 64} . 
class_grades = {
    "Alice": 88,
    "Bob": 92,
    "Charlie": 78,
    "Diana": 95,
    "Edward": 64
}
def get_average():
    total=sum(class_grades.values())
    count=len(class_grades)
    average = total/count
    return {
        "total_students": count,
        "average": average,
        "highest": max(class_grades.values()),
        "lowest": min(class_grades.values())
    }

#9. Honor Roll Filtering via Query Parameters
# A school roster stores multiple student records in a dictionary structure:
# roster = {
#     101: {"name": "Alice", "gpa": 3.9, "grade": 11},
#     102: {"name": "Bob", "gpa": 2.8, "grade": 10},
#     103: {"name": "Charlie", "gpa": 3.6, "grade": 11},
#     104: {"name": "Diana", "gpa": 3.2, "grade": 12}
# }
# Create a Flask route GET /roster that returns all students by default. However, if the request includes query parameter honor_roll=true (e.g., GET /roster?honor_roll=true ), filter the output to include ONLY students with a gpa >= 3.5 .
# REQUIREMENTS & CONSTRAINTS
# • Inspect request.args.get('honor_roll') .
# • Use Python dictionary comprehensions to filter items cleanly.
# • Return filtered dictionary or full dictionary formatted as JSON with HTTP 200. 
roster={
    101:{"name":"Alice","gpa":3.9,"grade":11},
    102:{"name":"Bob","gpa":2.8,"grade":10},
    103:{"name":"Charlie","gpa":3.6,"grade":11},
    104:{"name":"Diana","gpa":3.2,"grade":12}
}
def get_roster(honor_roll):
    if honor_roll=="true":
        result={
            key:value
            for key,value in roster.items()
            if value["gpa"]>=3.5
        }
        return result
    return roster

#10. Nested Department & Faculty Structure Lookup
# Consider the following nested dictionary representing school department administration:
# school_structure = {
#     "science": {"head": "Dr. Stone", "teachers_count": 8, "budget": 45000},
#     "arts": {"head": "Mrs. Palette", "teachers_count": 4, "budget": 22000},
#     "sports": {"head": "Coach Carter", "teachers_count": 5, "budget": 30000}
# }
# Write a Flask route GET /department/<dept_name> that accepts a department name as a URL parameter and searches the nested structure.
# REQUIREMENTS & CONSTRAINTS
# • Convert parameter to lowercase to allow case-insensitive matching (e.g., "Science" vs "science").
# • If matched: return JSON containing the department key and its nested dictionary details.
# • If NOT matched: return JSON {"error": "Department 'xyz' does not exist",
# "available_departments": ["science", "arts", "sports"]} with HTTP status code 404.
school_structure={
    "science":{
        "head":"Dr. Stone",
        "teachers_count":8,
        "budget":45000
    },
    "arts":{
        "head":"Mrs. Palette",
        "teachers_count":4,
        "budget":22000
    },
    "sports":{
        "head":"Coach Carter",
        "teachers_count":5,
        "budget":30000
    }
}
def get_department(dept_name):
    dept_name = dept_name.lower()
    if dept_name in school_structure:
        return school_structure[dept_name]
    return None

def test_123():
    count=0
    for i in range(2):
        count+=1
    return count

# print(test_123())

students_1={
    1:{
        "stu_name":"sam",
        "stu_class":9,
        "total_marks":420
    },
    2:{
        "stu_name":"ram",
        "stu_class":10,
        "total_marks":560
    }
}
def creat_stu(data):
    student_id=len(students_1)+1
    students_1[student_id]={
        "stu_name":data["stu_name"],
        "stu_class":data["stu_class"],
        "total_marks":data["total_marks"]
    }
    return students_1[student_id]

def get_stu():
    return students_1

def update_stu(student_id,data):
    if student_id not in students_1:
        return None
    students_1[student_id].update(data)
    return students_1[student_id]

def delete_stu(student_id):
    if student_id not in students_1:
        return None
    students=students_1.pop(student_id)
    return students_1
   



