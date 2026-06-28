# from datetime import datetime 
# from time import sleep
# print(datetime.now().time())
# sleep(5)
# print(datetime.now().time())

# def test_dec(func):
#     def wrapper(*args,**kwargs):
#         print("function started")
#         result = func(*args,**kwargs)

#         print("function ended")
#         return result
#     return wrapper





# @test_dec
# def greet():
#     print("hello")
# greet()
x="Gaddam gowri priya"
temp={}
for i in x:
    if i in temp:
        temp[i]+=1
    else:
        temp[i]=1
print(temp["i"])

# C:\Users\kr418\AppData\Local\Python\pythoncore-3.14-64