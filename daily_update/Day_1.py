x="gaddam gowri priya"
y="priya gowri gaddam"
def data_1(x):
    print("--------->",x)
    temp={}
    for i in x:
        if i in temp:
            temp[i]+=1
        else:
            temp[i]=1
    return temp
for i in range(10):
    if i%2==0:
        print(data_1(x))
    else:
        print(data_1(y))

# 1 Find the largest number in a list without using max().
stu=[12,45,23,67,34,89,10]
s=stu[0]
e=stu[0]
for i in stu:
    if i>e:
        e=i
print("largest number :",e)    

# 2	Find the smallest number in a list without using min().
stu=[90,85,97,95,76,65]
s=stu[0]
e=stu[0]
for i in stu:
    if i<s:
        s=i
print("smallest number:",s)

# 3	Count how many even and odd numbers are present in a list.
roll_numbers = [12, 15, 18, 21, 24, 27, 30, 33]
even=0
odd=0
for i in roll_numbers:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(f"even numbers:{even} odd numbers:{odd}")

# 4	Find the sum of all positive numbers in a list.
numbers = [10, -5, 20, -15, 30, 0, 40, -8]
total=0
for i in numbers:
    if i>0:
        total=total+i    
print("sum of positive numbers:",total)


# 5	Separate positive, negative and zero values into three lists.
numbers = [10, -5, 0, 25, -15, 30, -2, 0]
pos=[]
negative=[]
zero=[]
for i in numbers:
    if i>0:
        pos.append(i)
    elif i<0:
        negative.append(i)
    elif i==0:
        zero.append(i)
print(pos,negative,zero)

# 6	Find duplicate elements in a list.
numbers = [10, 20, 30, 20, 40, 10, 50, 30, 60]
seen=set()
temp=[]
for i in numbers:
    if i in seen:
        temp.append(i)
    else:
        seen.add(i)
print(temp)

# 7	Remove duplicate elements without using set().
numbers = [10, 20, 10, 30, 40, 20, 50, 30]
temp=[]
for i in numbers:
    if i not in temp:
        temp.append(i)
print(temp)

# 8	Reverse a list without using reverse() or slicing.
numbers = [10, 20, 30, 40, 50]
s=0
e=len(numbers)-1
while s<e:
    numbers[s],numbers[e]=numbers[e],numbers[s]
    s+=1
    e-=1
print(numbers)

# 9	Find the second-largest number in a list.
stu=[12,45,23,67,34,89,10]
s=0
e=0
for i in stu:
    if i>s:
        e=s
        s=i
print("second largest number:",e)

# 10 Check whether all numbers in a list are positive.
numbers = [10, 20, 30, 40, 50]
count=0
for i in numbers:
    if i>0:
        count+=1
if count==len(numbers):
    print("all numbers are positive")
else:
    print("Not all numbers are positive")

