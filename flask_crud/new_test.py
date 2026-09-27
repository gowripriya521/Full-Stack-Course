# # x={
# #     "name":"gowri priya",
# #     "class":10,
# #     "address":"a-21-30,ammacheruvumitta",
# #     "photo":"C:/Users/kr418/OneDrive/Desktop/Full_Stack/flask_crud/contacts.csv",
# #     "aadhar_pic":"C:/Users/kr418/OneDrive/Desktop/Full_Stack/flask_crud/students.csv"
# # }

students_db = {} 

def get_all_students(): 
    return list(students_db.values())

def add_student(data):
    student_id = data["student_id"]
    students_db[student_id] = {
        "student_id": student_id,
        "name": data["name"],
        "email": data["email"],
        "department": data["department"],
        "photo_path": None
    }
    return students_db[student_id] 

def get_students(student_id):
    if student_id not in students_db:
        return None
    return students_db[student_id]


def update_students(student_id, data):
    if student_id not in students_db:
        return None
    students_db[student_id].update(data)
    return students_db[student_id]

def upload_photo(student_id, photo):
    if student_id not in students_db:
        return None
    path = "uploads/" + student_id + "_" + photo.filename
    photo.save(path)
    students_db[student_id]["photo_path"] = path
    return students_db[student_id]

def update_photos(student_id, photo):
    if student_id not in students_db:
        return None
    path = "uploads/" + student_id + "_" + photo.filename
    photo.save(path)
    students_db[student_id]["photo_path"] = path
    return students_db[student_id]

def delete_photo(student_id):
    if student_id not in students_db:
        return None
    students_db[student_id]["photo_path"] = None
    return students_db[student_id]


