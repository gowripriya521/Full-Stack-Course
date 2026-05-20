x=[1,2,3,8,9,4,5,6,7,10]
# k=19
# b=2
# for i in range(len(x)-b):
#     total=0
#     for j in range(b):
#         total+=x[i+j]
#     if total==k:
#         print(x[i],x[i+1])
#         break
# Tracker=False
# for i in x:
#     if Tracker:
#         break
#     for j in x:
#         if(i+j)==k:
#             print(i,j)
#             Tracker=True
#             break
# for i in x:
#     for j in x:
#         if(i+j)==k:
#             print(i,j)
#             break
# k=3
# z=18
# a=0
# b=k
# # print(x[a:b])
# while b<=len(x):
#     if sum(x[a:b])==z:
#         print(x[a:b])
#         break
#     a+=1
#     b+=1