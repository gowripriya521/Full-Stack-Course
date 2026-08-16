# from flask import Flask, request ,jsonify
# from mydata import *

# app = Flask(__name__)
# @app.route("/weather/<int:station_id>")
# def station_get(station_id):
#     result=get_weather(station_id)
#     if result:
#         return jsonify({"id":station_id,**result}),200
#     return jsonify({"error":"not found"}),404

# @app.route("/cricket/rankings")
# def get_players():
#     top=request.args.get("top",type=int)
#     result=get_player(top)
#     return jsonify(result),200

# @app.route("/player/<int:player_id>") 
# def player_get_data(player_id):
#     result=get_player(player_id)
#     if result:
#         return jsonify({"id":player_id,
#         **result}), 200
#     return jsonify({
#         "error":"player not found"
#     }),404

# @app.route("/sneakers")
# def sneakers_get_data():
#     brand=request.args.get("brand")
#     max_price=request.args.get("max_price",type=int)
#     result = get_sneakers(brand, max_price)
#     return jsonify({
#         "count":len(result),
#         "results":result}), 200

# @app.route("/songs/search")
# def get_playlist():
#     q=request.args.get("q")
#     if not q:
#         return jsonify({
#             "error":"query parameter 'q' is required"
#         }),404
#     result=search_song(q)
#     return jsonify({
#         "query":q,
#         "matches":result
#     }),200

# @app.route("/leaderboard")
# def leaderboard_get_data():
#     top = request.args.get("top", type=int)
#     result = get_leaderboard(top)
#     return jsonify({
#         "top_scores":result
#     }), 200

# @app.route("/students/stats")
# def students_get_data():
#     result = get_student_stats()
#     return jsonify(result), 200
    

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


# from flask import Flask,request,jsonify

# app = Flask(__name__)

# temp = {}

# @app.route("/signup",methods=['POST'])
# def signup():
#     data = request.get_json()
#     if data['email'] in temp:
#         return jsonify({"Satus":"Email already Exist"}), 409
#     temp[data['email']] = {"Name":data['Name'],"Pass":data['Pass']}
#     return jsonify({"Status":True}),201

# @app.route("/get_all_users") #For Admin
# def get_all_users():
#     res = temp.copy()
#     res['length'] = len(temp)
#     return jsonify(res)

# @app.route("/login",methods=['POST'])
# def login():
#     data = request.get_json()
#     if data['email'] in temp:
        
#         if data['Pass'] == temp[data['email']]['Pass']:
#             return f"Hi {temp[data['email']]['Name']}"
#         else:
#             return jsonify({"Status":"incorrect Pass"}),401
#     else:
#         return jsonify({"Status":"User Not Found"}),404

# @app.route("/updateprofilename",methods = ['PUT'])
# def update_profile():
#     data = request.get_json()
#     print(type(data))
#     if data['email']:
#         try:
#             if data['new_name'] :
#                 temp[data['email']]['Name'] = data['new_name']
#                 return jsonify({"status":"Updated"}),204
#         except KeyError:
#             # return 'sam'
#             return jsonify({"status":"invald Entity['newname']"}),422

# @app.route("/deactivteuser",methods=['DELETE'])
# def delete_user():
#     data = request.get_json()
#     try:
#         if data['email']:
#             del temp[data['email']]
#             return jsonify(),204
#     except KeyError:
#         return jsonify({"Status":"Invalid Entity['email']"}),422



# if __name__=="__main__":
#     app.run(host='0.0.0.0',port=8001,debug=True)


from flask import Flask,request,jsonify

app = Flask(__name__)

temp={}
@app.route("/users",methods=["POST"])
def post_user():
    data=request.get_json()
    if data["email"] in temp:
        return jsonify({"Satus":"invalid/missing input"}), 400
    temp[data['email']] = {"Name":data['Name']}
    return jsonify({"Status":True}),201


if __name__=="__main__":
    app.run(host='0.0.0.0',port=8001,debug=True)