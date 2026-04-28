def add_1(a,b,c):
    return a+b+c
result=add_1(2,3,5)
#===================================
def check_1(a):
    if a==0:
        return None
    if a<0:
        return False
    else:
        return True
#=====================================
def rev_1(n):
   while n>0:
    
       n-=1
rev_1(10)
#=======================
def num_1(m):
    i=1
    while i<=m:
        #print(i)
        if i%2 == 0:
            print(i)
        i+=1
print(num_1(10))
#=========================================
def vote_1(age):
    if type(age)==str:
        return "invalid input"    
    elif age<=0:
        return "invalid"
    elif age>=18:
        return "eligible for vote"
    else:
        return "not eligible for vote"
print(vote_1("A"))
# ========================
def marks(*sub):
    sub = ((a,b,c,d,e,f)/6)
    return (sub)
marks(50,50,50,50,50,50)
#============================================
x = str("s1")
y = str(4.8)
z = str(3.0)
print(x,y,z)
#==========================================
x = int(1)
a = float(x)
b = str(x)
print(type(a),type(b))
print(a,b)
#=========================================
list_1 = ["41","two"]
print(list_1)
#==========================================
x = (1)
y = ("hi")
z = (2.4)
print(type(x),type(y),type(z))
print(x,y,z)
#=========================================
x = [1,3,4,5]
x[0] = 10
print(x)
x.index(1,4)
print(x)
#============================================
my_ls= [1,2,3,4,2,2,3]
my_ls.sort()
print(my_ls)
#===========================================
colors = {"red","green","blue"}
print(colors)
colors.add("yellow")
colors.discard("green")
print(colors)
print(len(colors))

#================================
set_name = {1,2,3,20,40}
print(del(set_name))

