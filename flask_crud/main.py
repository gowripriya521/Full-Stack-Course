from flask import Flask,request,jsonify
from ex import add_cart,get_products,cal_total,check_out
from test import create_user_core,read_data,update_user_core,delete_user_core,contact_book,all_contact,update_contact,delete_contact,visitor_counter,add_guest,get_guests,add_guest,get_guests,create_contact,get_contacts,get_tasks,create_task,delete_task,get_last_lines,create_config,get_config

app=Flask(__name__)

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

if __name__=="__main__":
    app.run(port=8001,host='0.0.0.0',debug=True)
