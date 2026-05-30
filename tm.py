# class Sub:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b
#     def add_1(self):
#         return self.a+self.b
#     def mul(self):
#         return self.a*self.b
#     def __isvalid(self):
#         if (self.a+self.b)>10:
#             return True
#         return False
#     def greet_a(self):
#         if self.__isvalid():
#             print("its valid")
#         else:
#             print("invalid")
# s=Sub(8,3)
# print(s.add_1())
# print(s.mul())
# #print(s.__isvalid())
# print(s.greet_a())

# print(dir(int))
# class Demo:
#     def __new__(cls):
#         print("Creating object")
#         return super().__new__(cls)

#     def __init__(self):
#         print("Initializing object")

# d = Demo()
# class Number:
#     def __init__(self, value):
#         self.v = value

#     def __mod__(self, other):
#         return self.v % other.v

# n1 = Number(10)
# n2 = Number(3)

# print(n1 % n2)