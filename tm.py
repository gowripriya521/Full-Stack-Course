# x ="hello"
# i={}
# for letter in x:
#     if letter in i:
#         i[letter]+=1
#     else:
#         i[letter]=1
# print(i)
import lm
try:
    print(lm.add_1("a",5))
except Exception as e:
    print("invalid error",e)
    