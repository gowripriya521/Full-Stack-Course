x = 15
if x>10:
    print("x is greater than 10")
#=============================================
age = 18
if age >=18:
    print("eligible for vote")
#=============================================
y = 20
if y < 21:
    print("not eligible for marriage")
#=============================================
i = 5
if i in range(6):
    print("hi")
#=============================================
num = 4
if num%2 == 0:
    print("even number")
#=============================================
for i in range(1,5):
    print(i)
#=============================================
for i in range(5):
    pass
#==============================================
for ch in "python":
    print(ch)
#==============================================
count = 0
while(count<4):
    count+=1
    print(count)
#==============================================
ls = 4
while(ls>0):
    print(ls)
    ls-=1
#==============================================
def total(*num):
    print(num)
total(1,2,3,4,5)
#==============================================
def add(a,b):
    print(a+b)
add(3,2)
#==============================================
def t_1(*numb):
    print(sum(numb))
t_1(1,2,3)
#==============================================
def sub(c,d):
    print(c-d)
sub(3,5)
#==============================================
def detail(*info)-> int:
    print(info)
detail(1,3)
#==============================================
def find_odd(*args):
    for num in args:
        if num%2!=0:
            print(num)
find_odd(1,2,3,4,5,6,7)
#==============================================
def age_1(*args1):
    for num in args1:
        if num>=18:
            print("you can vote")
age_1(19)
#==============================================
for i in range(1,6):
    if i%2==0:
        print(i,"even numbers")
    else:
        print(i,"odd numbers")
i = 1
while i<=4:
    print(i)
    i+=1
#==============================================
def cal_marks(*marks):
    total = sum(marks)
    per = total/len(marks)
    print(total,per)
cal_marks(80,75,90,85)
#===============================================
def cricle_area(r):
    area = 3.14*r*r
    print(area)
cricle_area(2)
#===============================================
def triangle_area(b,h):
    area1 = (1/2*(b*h)) 
    print(area1)
triangle_area(5,4)