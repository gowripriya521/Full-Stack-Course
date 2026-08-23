from flask import Flask,request,jsonify
from mydata import *
from test_1 import employee_data, salary_data, email_names,temp,add_user,update_user,delete_user
app = Flask(__name__)


@app.route("/users",methods=["POST"])
def post_user():
    data=request.get_json()
    name=data.get("name")
    email=data.get("email")
    return jsonify({
        "name":name,
        "email":email
    }),201


@app.route("/login",methods=["POST"])
def login_post_data():
    data=request.get_json()
    username=data.get("username")
    password=data.get("password")
    if not username or not password:
        return jsonify({
            "message":"username and password are required"
        }),400       
    return jsonify({
            "Message":"login successful"
    }),400

@app.route("/add",methods=["POST"])
def add_number_post():
    data=request.get_json()
    a=data.get("a")
    b=data.get("b")
    if a is None or b is None:
        return jsonify({
            "msg":"a and b are required"
        }),400
    result=a+b
    return jsonify({
        "result":result
    })

@app.route("/products",methods=["POST"])
def product_post():
    data=request.get_json()
    name=data.get("name")
    price=data.get("price")
    quantity=data.get("quantity")
    if name is None or price is None or quantity is None:
        return jsonify({
            "error":"required data is missing"
        }),400
    return jsonify({
        "msg":"Successfully created"
    }),201

@app.route("/cart",methods=["POST"])
def cart_post_data():
    data=request.get_json()
    price=data.get("price")
    quantity=data.get("quantity")
    if price is None or quantity is None:
        return jsonify({
            "error":"required value is missing"
        }),400
    total=price*quantity
    return jsonify({
        "price":price,
        "quantity":quantity,
        "total":total
    })

@app.route("/validate_email",methods=["POST"])
def validate_email_post():
    data=request.get_json()
    email=data.get("email")
    if "@" in email :
        return jsonify({
            "msg":"valid email"
        })
    return jsonify({
         "msg":"invalid email"
    }),400

@app.route("/register",methods=["POST"])
def register_post():
    data=request.get_json()
    username=data.get("username")
    email=data.get("email")
    password=data.get("password")
    if username is None or email is None or password is None:
        return jsonify({
            "error":"required field is missing"
        }),400
    return({
        "message":"registration successful"
    })

@app.route("/users/<int:user_id>",methods=["POST"])
def user_post_data(user_id):
    data=request.get_json()
    name=data.get("name")
    email=data.get("email")
    if not name or not email:
        return jsonify({
            "error":"required field is missing"
        }),400
    return jsonify({
        "user_id":user_id,
        "name":name,
        "email":email
    })

@app.route("/salary",methods=["POST"])
def salary_post():
    data=request.get_json()
    basic=data.get("basic")
    allowance=data.get("allowance")
    bonus=data.get("bonus")
    if basic is None or allowance is None or bonus is None:
        return jsonify({
            "error":"required value is missing"
        }),400
    total =basic+allowance+bonus
    return jsonify({
        "basic": basic,
        "allowance": allowance,
        "bonus": bonus,
        "total": total
    })

@app.route("/todos",methods=["POST"])
def todos_post():
    data=request.get_json()
    title=data.get("title")
    completed=data.get("completed")
    if title is None or completed is None:
        return jsonify({
            "error":"title is required"
        }),400
    todo=({
        "title":title,
        "completed":completed
    }),201
    return todo

@app.route("/all_users",methods=["GET"])
def allusers_get():
    return jsonify(get_users())

@app.route("/create_users",methods=["POST"])
def user_data_post():
    data=request.get_json()
    user=create_users(data)
    return jsonify({
        "user":user
    }),201

@app.route("/find_person",methods=["POST"])
def find_person_post():
    data=request.get_json()
    email=data.get("email")
    user=find_users(email)
    if user:
        return jsonify({
            "msg":"person is present",
            "user":user
        })
    return jsonify({
        "error":"required person is not present"
    }),404

@app.route("/employees",methods=["POST"])
def employees_post():
    data=request.get_json()
    users=create_emp(data)
    if users:
        return jsonify(users),201
    return jsonify({
        "error":"required all fields"
    }),400

@app.route("/students",methods=["POST"])
def student_data():
    data=request.get_json()
    reg=student_registration(data)
    if reg:
        return jsonify({
            "Msg":"student registered successfull",
            "reg":reg
        }),201
    return jsonify({
        "error":"required filed is missing"
    }),400

@app.route("/contact",methods=["POST"])
def contacts():
    data=request.get_json()
    result=contact_form(data)
    if result:
        return jsonify({
            "Msg":"message received successfull",
            "result":result
        }),201
    return jsonify({
        "error":"required filed is missing"
    }),400

@app.route("/feedback",methods=["POST"])
def feedback_post():
    data=request.get_json()
    temp=feedback_api(data)
    if temp:
        return jsonify({
            "Msg":"feedback received successfull",
            "feedback":temp
        }),201
    return jsonify({
        "error":"required filed is missing"
    }),400

@app.route("/login",methods=["POST"])
def login():
    data=request.get_json()
    result=simple_login(data)
    if result:
        return jsonify({
            "result":result
        }),201
    return jsonify({
        "error":"required filed is missing"
    }),400

@app.route("/userage",methods=["POST"])
def user_post():
    data=request.get_json()
    result=age_validation(data)
    if result:
        return jsonify({
            "result":result
        }),201
    return jsonify({
        "error":"pls enter the valid age"
    }),400

@app.route("/register_email",methods=["POST"])
def register_post1():
    data=request.get_json()
    res=email_validation(data)
    if res:
        return jsonify({
            "res":res
        }),201
    return jsonify({
        "error":"pls enter the valid email"
    }),400

@app.route("/registers",methods=["POST"])
def length_validation():
    data=request.get_json()
    res=password_len(data)
    if res:
        return jsonify({
            "res":res
        }),201
    return jsonify({
        "error":"pls enter the valid password"
    }),400

@app.route("/users1", methods=["POST"])
def users_post():
    data = request.get_json()
    errors = check_user(data)
    if errors:
        return jsonify({
            "errors": errors
        }), 400
    return jsonify({
        "message": "User registration successful"
    }), 201

@app.route("/users2", methods=["POST"])
def users_pos():
    if not request.is_json:
        return jsonify({
            "error": "JSON body is required"
        }), 400
    data = request.get_json()
    result = get_user(data)
    return jsonify(result), 201

@app.route("/tasks", methods=["POST"])
def tasks_post():
    data = request.get_json()
    task = create_task(data)
    return jsonify(task), 201

@app.route("/products1", methods=["POST"])
def products_post():
    data = request.get_json()
    product = create_product(data)
    return jsonify(product), 201

@app.route("/employee",methods=["POST"])
def employee():
    data=request.get_json()
    department=data.get("department")
    temp=employee_data(department)
    return jsonify(temp),200

@app.route("/salarys",methods=["POST"])
def salarys_post():
    data=request.get_json()
    salary=data.get("salary")
    result=salary_data(salary)
    return jsonify(result),200

@app.route("/emails",methods=["POST"])
def email_data_post():
    data=request.get_json()
    email=data.get("email")
    res=email_names(email)
    return jsonify(res),200

@app.get("/getuser")
def getuser():
    id=request.args.get("id",type=int)
    if id in temp:
        return jsonify (temp[id])
    return jsonify (temp)


@app.post("/createuser")
def create_user():
    data = request.get_json()
    id = add_user(**data)
    if id:
        return jsonify({"Status":"user added!","ID":id}),201

@app.put('/updateuser/<int:id>')
def updateuser(id):
    data = request.get_json()
    if update_user(id,data["field"],data["new_data"]):
        return jsonify({"Status":f"{id} updated!"}),200

@app.delete('/del_user/<int:id>')
def deluser(id):
    if delete_user(id):
        return jsonify({"Status":f"User {id} Deleted"}),200


if __name__=="__main__":
    app.run(host='0.0.0.0',port=8001,debug=True)