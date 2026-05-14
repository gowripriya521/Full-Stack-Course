# 14.Number Guessing Game
# Import random module
# Generate random number from 1 to 20
# Use loop to guess number
# Print:
# Too high
# Too low
# Correct
# Handle invalid input.
def guess():
    x=10
    while True:        
        try:
            user = int(input("enter a number:"))
            if user>x:
                print("too high")
            elif user<x:
                print("too low")
            else:
                print("correct")
                break
        except Exception as e:
            print("invalid",e)
guess()
# import random
# def password():
#     return random.randint(1000,9999)
# pass_w=password()
# print(pass_w)
# for i in range(3):
#     try:
#         user = int(input("enter OTP:")) 
#         if user==pass_w:
#             print("correct password")
#             break
#         else:
#             print("wrong password")
#     except Exception as e:
#         print("invalid input",e)
#         break
# password()