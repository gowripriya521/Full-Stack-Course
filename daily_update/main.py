x="ramesh kumar"
temp={}
for i in x:
    if i in temp:
        temp[i]+=1
    else:
        temp[i]=1
print(temp)
print(temp['r'])