# 1	Find the largest element in a tuple.
numbers = (12, 45, 23, 67, 34, 89, 10)
largest=numbers[0]
for i in numbers:
    if i>largest:
        largest=i
print("The largest number :",largest)

# 2	Count how many times a particular element appears in a tuple.
numbers = (10, 20, 30, 10, 40, 10, 50, 20)
target=10
count=0
for i in numbers:
    if i==target:
        count+=1
print(target,"appears",count,"times")

# 3	Find the sum of all tuple elements without using sum().
numbers=(10, 20, 30, 40, 50)
count=0
for i in numbers:
    count+=i
print("total sum :",count)

# 4	Convert a tuple into a list and remove a particular element.
numbers = (10, 20, 30, 40, 50)
remove_element = 30
temp=[]
for i in numbers:
    if i!=remove_element:
        temp.append(i)
num=tuple(temp)
print("updated tuple:",num)

# 5	Find common elements between two tuples.
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 50, 60, 70)
for i in tuple1:
    if i in tuple2:
        print(i)

# 6	Check whether a tuple is a palindrome.
numbers = (10, 20, 30, 20, 10)
if numbers==numbers[::-1]:
    print("The tuple is a palindrome")
else:
    print("The tuple is not a palindrome")

# 7	Find the second-smallest number in a tuple.
numbers = (50, 20, 10, 40, 30, 10)
s=numbers[0]
e=numbers[0]
for i in numbers:
    if i<s:
        e=s
        s=i
    elif i<e and i!=s:
        e=i
print("Second smallest number:",e)

# 8	Count positive and negative numbers in a tuple.
numbers = (10, -5, 20, -15, 0, 30, -8, 0)
pos=0
neg=0
ze=0
for i in numbers:
    if i>0:
        pos+=1
    elif i<0:
        neg+=1
    elif i==0:
        ze+=1
print("positive number:",pos)
print("negative numbers:",neg)
print("zeros:",ze)

# 9	Print all tuple elements using a while loop.
numbers = (10, 20, 30, 40, 50)
i=0
while i<len(numbers):
    print(numbers[i])
    i+=1

# 10 Find the unique elements from two tuples.
tuple1 = (10, 20, 30, 40, 50)
tuple2 = (30, 40, 60, 70, 80)
temp=[]
for i in tuple1:
    if i not in tuple2:
        temp.append(i)
for i in tuple2:
    if i not in tuple1:
        temp.append(i)
result=tuple(temp)
print("Unique elements:",result)