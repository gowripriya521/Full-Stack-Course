import os
from flask import Flask,request,jsonify,send_from_directory
from ex import add_cart,get_products,cal_total,check_out
from new_test import get_all_students,add_student,get_students,update_students,upload_photo,delete_photo,update_photos
from test import create_user_core,read_data,update_user_core,delete_user_core,contact_book,all_contact,update_contact,delete_contact,visitor_counter,add_guest,get_guests,add_guest,get_guests,create_contact,get_contacts,get_tasks,create_task,delete_task,get_last_lines,create_config,get_config,register_user,login_user,read_note,save_log,get_summary,students_static,get_teacher,get_course,get_filters,create_student,update_student,delete_student,get_average,get_roster,get_department,school_structure
#from new_test import students_static,get_teacher,get_course,get_filters,create_student,update_student,delete_student,get_average,get_roster,get_department,school_structure
from flask import Flask, flash, request, jsonify
from werkzeug.utils import secure_filename
from flask_cors import CORS


UPLOAD_FOLDER = 'uploads'

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
# CORS(app, resources={r"*": {"origins": "https://driveway-manicure-cattail.ngrok-free.dev"}})


@app.post("/add_to_cart")
def add_to_cart():
    data=request.get_json()
    product=add_cart(data)
    if not product:
        return jsonify({
            "error":"invalid email"
        }),400
    return jsonify({
        "msg":"product added",
        "product":product
    }),201

@app.get("/all_products")
def all_products():
    return jsonify (get_products()),200

@app.get("/total")
def total_items():
    email=request.args.get("email")
    result=cal_total(email)
    if not email:
        return jsonify({
            "error":"email not found"
        }),404
    return jsonify({
        "result":result
    }),200

@app.post("/createuser")
def create_user():
    data = request.get_json()
    email = data["email"]
    name = data["name"]
    age =data ["age"]
    result = create_user_core(email, name, age)
    return jsonify(result)

@app.get("/getuser")
def read_users():
    result = read_data()
    return jsonify(result)

@app.put("/users/<email>")
def update_user(email):
    data= request.get_json()
    name = data["name"]
    age =data ["age"]
    result = update_user_core(email, name, age)
    return jsonify(result)

@app.delete("/users/<email>")
def delete_user(email):
    result = delete_user_core(email)
    return jsonify(result)

@app.post("/contact_create")
def contact_create():
    data=request.get_json()
    contact_id=data["contact_id"]
    name=data["name"]
    phone_no=data["phone_no"]
    email=data["email"]
    result=contact_book(contact_id,name,phone_no,email)
    return jsonify(result)

@app.get("/all_contacts")
def all_contacts():
    return (all_contact())

@app.put('/update_contacts/<int:contact_id>')
def update_contacts(contact_id):
    data = request.get_json()
    name=data["name"]
    phone_no=data["phone_no"]
    email=data["email"]
    res=update_contact(contact_id,name,phone_no,email)
    return jsonify(res)

@app.delete('/delete_contacts/<int:contact_id>')
def delete_contacts(contact_id):
    res=delete_contact(contact_id)
    return jsonify(res)

@app.post("/api/v1/counter/increment")
def increment():
    current_count,previous_count=visitor_counter()
    return jsonify({
        "status": "success",
        "message": "Visitor count incremented",
        "current_count": current_count,
        "previous_count": previous_count
    })

@app.post("/api/v1/guestbook")
def add_entry():
    data = request.json
    add_guest(data["name"], data["message"])
    return jsonify({
        "message": "Guest added"
    }), 201


@app.get("/api/v1/guestbook")
def get_entries():
    entries = get_guests()
    return jsonify({
        "total_entries": len(entries),
        "entries": entries
    }), 200


@app.post("/api/v1/contacts")
def contacts_post():
    data = request.get_json()
    contact = create_contact(data)
    return jsonify({
        "contact": contact
    }), 201


@app.get("/api/v1/contacts")
def contacts_get():
    contacts = get_contacts()
    return jsonify({
        "count": len(contacts),
        "contacts": contacts
    })

@app.get("/api/v1/tasks")
def tasks_get():
    tasks = get_tasks()
    return jsonify(tasks)

@app.post("/api/v1/tasks")
def tasks_post():
    data = request.get_json()
    task = create_task(data)
    return jsonify(task), 201


@app.delete("/api/v1/tasks/<int:task_id>")
def tasks_delete(task_id):
    result, count = delete_task(task_id)
    if result:
        return jsonify({
            "status": "success",
            "message": f"Task with ID {task_id} successfully deleted from tasks.json",
            "remaining_count": count
        })
    return jsonify({
        "error": "Task not found"
    }), 404

@app.get("/api/v1/logs/tail")
def log_tail():
    number = int(request.args.get("lines"))
    lines = get_last_lines(number)
    result = []
    for line in lines:
        result.append(line.replace("\n", ""))
    return jsonify({
        "requested_lines": number,
        "returned_lines": len(result),
        "log_tail": result
    })

@app.put("/api/v1/config")
def config_put():
    data=request.get_json()
    config=create_config(data)
    return jsonify({
        "config":config
    })

@app.get("/api/v1/config")
def config_get():
    config=get_config()
    return jsonify({
        "status":"active",
        "config":config
    })

@app.post("/api/v1/auth/register")
def register():
    data = request.get_json()
    username = register_user(data)
    return jsonify({
        "message": "User registered successfully",
        "username": username
    }), 201


@app.post("/api/v1/auth/login")
def login():
    data = request.get_json()
    result = login_user(data)
    if result:
        return jsonify({
            "message": "Login successful",
            "username": data.get("username")
        })
    return jsonify({
        "message": "Invalid username or password"
    }), 401

@app.get("/api/v1/notes/<filename>")
def get_note(filename):
    content = read_note(filename)
    if content is None:
        return jsonify({
            "error": "File not found"
        }), 404
    return jsonify({
        "filename": filename,
        "content": content,
        "size_bytes": len(content.encode())
    })

@app.before_request
def log_request():
    save_log(
        request.method,
        request.path,
        request.remote_addr
    )

@app.get("/api/v1/analytics/summary")
def summary():
    total, last_time = get_summary()
    return jsonify({
        "total_logged_requests": total,
        "last_logged_time": last_time,
        "logfile_path": "activity.log"
    })

@app.get("/student")
def student_data():
    return jsonify(students_static())

@app.get("/teachers/<int:teacher_id>")
def dynamic_teacher(teacher_id):
    data=get_teacher(teacher_id)
    if data:
        return jsonify(data),200
    return jsonify({
        "error":"teacher not found"
    }),404


@app.get("/courses/<course_code>/capacity")
def courses(course_code):
    capacity=get_course(course_code)
    if capacity:
        return jsonify({
            "course":course_code.upper(),
            "capacity":capacity
        }),200
    return jsonify({
        "error": "Course not offered"
    })

@app.route("/students/search", methods=["GET"])
def search_students():
    result = get_filters(request.args)
    return jsonify(result), 200

@app.post("/students")
def students_post():
    data = request.get_json()
    student_id, student = create_student(data)
    return jsonify({
        "id": student_id,
        "student": student
    }), 201

@app.put("/students/<int:student_id>")
def students_put(student_id):
    data=request.get_json()
    student=update_student(student_id, data)
    if student:
        return jsonify({
            "message":"Student updated successfully",
            "student": student
        }), 200
    return jsonify({
        "error":"Student record missing"
    }), 404

@app.delete("/students/<int:student_id>")
def students_delete(student_id):
    result=delete_student(student_id)
    if result:
        return jsonify({
            "message": f"Student {student_id} successfully unenrolled"
        }), 200
    return jsonify({
        "error": "Student ID not found"
    }), 404

@app.get("/analytics/class-average")
def average_get():
    result=get_average()
    return jsonify(result)   

@app.get("/roster")
def roster_get():
    honor_roll=request.args.get("honor_roll")
    result=get_roster(honor_roll)
    return jsonify(result), 200

@app.get("/department/<dept_name>")
def department_get(dept_name):
    department=get_department(dept_name)
    if department:
        return jsonify({
            "department":dept_name.lower(),
            "details":department
        }),200
    return jsonify({
        "error":f"Department '{dept_name}' does not exist",
        "available_departments":list(school_structure.keys())
    }), 404 

UPLOAD_FOLDER = 'uploads'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return jsonify({'status':'no file given'}),400
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return jsonify({'status':'file name not given'}),400
        if file.name:
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'file uploaded'
    return ['True']


@app.route("/upload",methods=['GET','POST'])
def standard_file():
    if request.method == 'POST':
        if 'doc' not in request.files:
            flash('No file part')
            return jsonify({'status':'no file given'}),400
        file = request.files['doc']

        if file.filename == '':
            flash('No selected file')
            return jsonify({'status':'file name not given'}),400
        if file.name:
            filename = secure_filename(file.filename)
            # file.save(f'./uploads/{file.filename}')
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return 'file uploaded'
    return ['True']

@app.post("/api/stu")
def crate_api():
    data=request.get_json()
    student=add_student(data)
    return jsonify({
        "status":"success",
        "data":student
    }),201

@app.get("/api/stu")
def api_stu():
    data=get_all_students()
    return jsonify(data),200

@app.get("/api/students/<student_id>")
def get_one_student(student_id):
    student = get_students(student_id)
    if student is None:
        return jsonify({"message": "Student not found"}), 404
    return jsonify(student), 200

@app.put("/api/students/<student_id>")
def update(student_id):
    data = request.get_json()
    student = update_students(student_id, data)
    if student is None:
        return jsonify({"message": "Student not found"}), 404
    return jsonify({
        "message": "Student updated",
        "data": student
    }), 200

@app.post("/api/students/<student_id>/photo")
def upload(student_id):
    photo = request.files["photo"]
    student = upload_photo(student_id, photo)
    if student is None:
        return jsonify({"message": "Student not found"}), 404
    return jsonify({
        "message": "Photo uploaded successfully",
        "photo_path": student["photo_path"],
        "student_id": student_id
    }), 201


@app.put("/api/students/<student_id>/photo1")
def update_1(student_id):
    photo = request.files["photo1"]
    student = update_photos(student_id, photo)
    if student is None:
        return jsonify({"message": "Student not found"}), 404
    return jsonify({
        "message": "Photo updated successfully",
        "photo_path": student["photo_path"],
        "student_id": student_id
    }), 200

@app.delete("/api/students/<student_id>/photo2")
def delete(student_id):
    student = delete_photo(student_id)
    if student is None:
        return jsonify({"message": "Student not found"}), 404
    return jsonify({
        "message": "Photo removed successfully",
        "student_id": student_id,
        "photo_path": None
    }), 200

@app.route("/uploads/<path:name>")
def download_file(name):
    return send_from_directory(
        app.config['UPLOAD_FOLDER'], name, as_attachment=True
    )


if __name__=="__main__":
    app.run(port=8001,host='0.0.0.0',debug=True)
