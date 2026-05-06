from lm import num_1
while True:
    try:
        user = int(input("enter a number:"))
        print(num_1(user))
    except ValueError as e:
        print("invalid input=",e)
