x="gaddam gowri priya"
def word():
    temp={}
    for i in x:
        if i in temp:
            temp[i]+=1
        else:
            temp[i]=1
    print(temp)
    print(temp["g"])
word()
# a=[10,20,30,40]
# b=[]
# for i in a:
#     if i%20==0:
#         b.append(i//10)
# print(b)        
        