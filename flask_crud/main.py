from flask import Flask,request,jsonify
from ex import add_cart,get_products,cal_total,check_out
from test import persons_data,create_user_core,read_data,update_user_core,delete_user_core

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


if __name__=="__main__":
    app.run(port=8001,host='0.0.0.0',debug=True)
