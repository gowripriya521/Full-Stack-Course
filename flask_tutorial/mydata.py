# x="gaddam gowri priya"
# def word():
#     temp={}
#     for i in x:
#         if i in temp:
#             temp[i]+=1
#         else:
#             temp[i]=1
#     print(temp)
#     print(temp["g"])
# word()
# a=[10,20,30,40]
# b=[]
# for i in a:
#     if i%20==0:
#         b.append(i//10)
# print(b)        


temp={}
def get_users():
    return temp

def create_users(data):
    name=data.get("name")
    user={
        "name":name,
        "email":data.get("email"),
        "phone_no":data.get("phone_no"),
        "address":data.get("address")
    }
    temp[name]=user
    return user

def find_users(email):
    for user in temp.values():
        if user["email"]==email:
            return user

def create_emp(data):
    name=data.get("name")
    department=data.get("department")
    salary=data.get("salary")
    users={
        "name":name,
        "department":department,
        "salary":salary
    }
   
    if name is None or department is None or salary is None:
        return None
    return users

def student_registration(data):
    name=data.get("name")
    age=data.get("age")
    course=data.get("course")
    reg={
        "name":name,
        "age":age,
        "course":course
    }
    if name is None or age is None or course is None:
        return None
    return reg


def contact_form(data):
    name=data.get("name")
    email=data.get("email")
    msg=data.get("msg")
    if not name or not email or not msg:
        return None
    return {
        "name":name,
        "email":email,
        "msg":msg
    }

def feedback_api(data):
    name=data.get("name")
    rating=data.get("rating")
    comment=data.get("comment")
    if name is None or rating is None or comment is None:
        return None
    if type(rating)!=int or rating <1 or rating>5:
        return None
    return {
        "name":name,
        "rating":rating,
        "comment":comment
    }

admin=1234
def simple_login(data):
    username=data.get("username")
    password=data.get("password")
    if username is None or password is None:
        return None
    if password!=admin:
        return None
    return {
        "username":username,
        "password":password
    }

def age_validation(data):
    name=data.get("name")
    age=data.get("age")
    if type(age)!=int or age<17:
        return None
    if name is None or age is None:
        return None
    return {
        "name":name,
        "age":age
    }
def email_validation(data):
    name=data.get("name")
    email=data.get("email")
    if name is None or email is None:
        return None
    if "@" in email and "." in email:
        return {
            "name":name,
            "email":email
        }
    return None
    
def password_len(data):
    username=data.get("username")
    password=data.get("password")
    if username is None or password is None:
        return None
    if len(password)<8:
        return None
    return {
        "username":username
    }

def check_user(data):
    errors = []
    name = data.get("name")
    email = data.get("email")
    age = data.get("age")
    if not name:
        errors.append("name is required")
    if not email:
        errors.append("email is required")
    if age is None or age < 18:
        errors.append("age must be 18 or older")
    return errors

def get_user(data):
    name = data.get("name")
    email = data.get("email")
    return {
        "name": name,
        "email": email
    }

temp={}
def create_task(data):
    title=data.get("title")
    task={
        "title":title
    }
    temp[title]=task
    return task

products = {}
def create_product(data):
    name = data.get("name")
    price = data.get("price")
    id = len(products) + 1
    product = {
        "id": id,
        "name": name,
        "price": price
    }
    products[id] = product
    return product


# temp={}
# def duplicate_email(data):
#     name=data.get(name)
#     email=data.get(email)
#     for i in temp:
#         if


    




