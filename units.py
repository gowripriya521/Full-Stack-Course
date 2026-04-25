def greet_F():
    print("hello every one")
greet_F()
#===================================================
def add(a,b):
    return a+b
result = add(2,3)
print(result)
#=====================================================================================
def my_function(name1):
    print("hi"+name1)
my_function("ram")
my_function("priya")
#===========================================================
def greet_1(age="21"):
    print("my age is",age)
greet_1()
greet_1(20)
#========================================
def student(name,age1):
    print(name,age1)
student(age1=22,name="priya")
#===========================================
def add1(c,d):
    print(c+d)
add1(4,6)
#=============================================
def total(*numbers):
    print(numbers)
total(1,2,3,4)
#=============================================
def details(**info):
    print(info)
details(name="ram",age=21)
#===============================================
def my_fun(food):
    for x in food:
        print(x)
fruits = ["apple","banana","mango"]
my_fun(fruits)
#====================================================
def m_func():
    pass
m_func()
#====================================================
for i in range(5):
    pass
#=====================================================
x = 10
if x > 5:
    pass
else:
    print("less than 5")
#==============================================
marks = 75
if marks>=90:
    print("grade A")
elif marks>=70:
    print("grade B")
else:
    print("grade c")