EMPLOYEE_DATA = {
    "Ramesh@gmail.com": {
        "dep": "IT",
        "salary": 50000,
        "location": "ODC1"
    },
    "Suresh@gmail.com": {
        "dep": "HR",
        "salary": 45000,
        "location": "ODC2"
    },
    "Mahesh@gmail.com": {
        "dep": "Finance",
        "salary": 60000,
        "location": "ODC1"
    },
    "Priya@gmail.com": {
        "dep": "IT",
        "salary": 55000,
        "location": "ODC3"
    },
    "Anitha@gmail.com": {
        "dep": "Marketing",
        "salary": 48000,
        "location": "ODC2"
    },
    "Kiran@gmail.com": {
        "dep": "IT",
        "salary": 65000,
        "location": "ODC1"
    },
    "Swathi@gmail.com": {
        "dep": "HR",
        "salary": 47000,
        "location": "ODC3"
    },
    "Ravi@gmail.com": {
        "dep": "Finance",
        "salary": 58000,
        "location": "ODC2"
    },
    "Deepika@gmail.com": {
        "dep": "Marketing",
        "salary": 52000,
        "location": "ODC1"
    },
    "Arjun@gmail.com": {
        "dep": "IT",
        "salary": 70000,
        "location": "ODC3"
    },
    "Pooja@gmail.com": {
        "dep": "Finance",
        "salary": 62000,
        "location": "ODC1"
    },
    "Vijay@gmail.com": {
        "dep": "HR",
        "salary": 49000,
        "location": "ODC2"
    },
    "Naveen@gmail.com": {
        "dep": "IT",
        "salary": 58000,
        "location": "ODC2"
    },
    "Lakshmi@gmail.com": {
        "dep": "Marketing",
        "salary": 51000,
        "location": "ODC3"
    },
    "Manoj@gmail.com": {
        "dep": "Finance",
        "salary": 67000,
        "location": "ODC2"
    }
}
def employee_data(department):
    temp=[]
    for email,employee in EMPLOYEE_DATA.items():
        if employee["dep"]==department:
            temp.append(email)
    return temp
#print(employee_data("IT"))

def salary_data(salary):
    result={}
    for email,employee in EMPLOYEE_DATA.items():
        if employee["salary"]<salary:
            result[email]={
                "dep":employee["dep"],
                "location":employee["location"]
            }
    return result
#print(salary_data(50000))

def email_names(email):
    res={}
    for mail,employee in EMPLOYEE_DATA.items():
        res[mail]={
            "dep":employee["dep"],
            "location":employee["location"],
            "name":mail.split("@")[0]
            }
    return res
# print(email_names("Lakshmi@gmail.com"))

x = {
    1: {'Name': 'Ramesh',
        'Email': 'Ramesh@gmail.com',
        'Dep': 'IT', 
        'Location':'ODC1'
        }
} 


t_data = {

        "Name":"Ramesh",
        "Email":"Ramesh@gmail.com",
        "Dep":"IT",
        "Location":"ODC1"
    }



temp = {}

#C -> Create    #Create a user ✅
#R -> Read      #Read all users ✅  & read user by ID 
#U -> Update    #update user by ID✅ 
#D -> Delete    #delete based on user ID

def add_user(**data): #to create user
    id = len(temp)+1
    temp[id] = data
    return id

def update_user(id,field,new_data):
    if id in temp:
        temp[id][field]= new_data
        return True
    return False

def delete_user(id):
    if id in temp:
        del temp[id]
        return True
    return False



    