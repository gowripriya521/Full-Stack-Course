import json
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

def create_task(data):
    with open("tasks.json", "r") as f:
        tasks = json.load(f)
    task = {
        "id": len(tasks) + 101,
        "title": data.get("title"),
        "priority": data.get("priority")
    }
    tasks.append(task)
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)
    return task


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
