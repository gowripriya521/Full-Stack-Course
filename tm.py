#1.Concepts: Attributes, methods, updating state.
# Create a class named ⁠BankAccount⁠ that simulates basic banking operations.
#  Attributes: ⁠account_holder⁠ (string) and ⁠balance⁠ (float, defaults to ⁠0.0⁠).
#  Methods:
#  ⁠deposit(amount)⁠: Adds the amount to the balance.
#  ⁠withdraw(amount)⁠: Deducts the amount from the balance if there are sufficient funds. If not, print ⁠"Insufficient funds!"⁠.
#  ⁠display_balance()⁠: Prints a message showing the current balance.
# class BankAccount:
#     def __init__(self,account_holder,balance=0.0):
#         self.a=account_holder
#         self.b=balance
#     def deposit(self,amount):
#         self.b+=amount
#         print("deposit amount",amount)
#     def withdraw(self,amount):
#         if amount<self.b:
#             self.b-=amount
#             print("withdraw amount",amount)
#         else:
#             print("insufficient funds!")
#     def display_balance(self):
#         print("current balance",self.b)
# a=BankAccount("sam")
# a.deposit(50000)
# a.withdraw(40000)
# a.display_balance()



# 2. Real-World Modeling: The ⁠Library⁠ and ⁠Book⁠ Classes
# Concepts: Object interaction (objects holding other objects).
# Create two classes: ⁠Book⁠ and ⁠Library⁠.
#  ⁠Book⁠ Class:
#  Attributes: ⁠title⁠, ⁠author⁠, and ⁠is_loaned⁠ (boolean, defaults to ⁠False⁠).
#  ⁠Library⁠ Class:
#  Attributes: ⁠name⁠ and ⁠books⁠ (a list that starts empty).
#  Methods:
#  ⁠add_book(book)⁠: Takes a ⁠Book⁠ object and adds it to the library's collection.
#  ⁠borrow_book(title)⁠: Looks for a book by its title. If found and not loaned out, change ⁠is_loaned⁠ to ⁠True⁠. If already borrowed or not found, print an appropriate message.
#  ⁠return_book(title)⁠: Looks for a book by title and marks ⁠is_loaned⁠ as ⁠False⁠.
# class Book:
#     def __init__(self,title,author,is_loaned=False):
#         self.title=title
#         self.author=author
#         self.is_loaned=is_loaned
# class Library:
#     def __init__(self):
#         self.name=None
#         self.books=[]
#     def add_book(self,book):
#         self.books.append(book)
#     def borrow_book(self,title):
#         for book in self.books:
#             if book.title == title:
#                 if not book.is_loaned:
#                     print("thank you for visiting")
#                     book.is_loaned=True
#                     return True
#                 if book.is_loaned:
#                     print("some one take the book")
#                     return False
#         print("title not found")
#     def return_book(self,title):
#         for book in self.books:
#             if book.title == title:
#                 book.is_loaned=False
#                 print("book return")
#                 return True
#         print("the title not found")
# l=Library()
# l.add_book(Book("class","sam"))
# l.add_book(Book("python","ram"))
# l.add_book(Book("API","raju"))
# l.borrow_book("python")
# l.borrow_book("python")
# l.return_book("python")
# l.return_book("python")


# 3.The Upgrade: The ⁠ElectricVehicle⁠ Class
# Concepts: Inheritance and overriding methods.
# Start with a base ⁠Vehicle⁠ class and build a specific child class.
#  Base Class ⁠Vehicle⁠:
#  Attributes: ⁠make⁠, ⁠model⁠, and ⁠fuel_level⁠ (percentage, e.g., ⁠100⁠).
#  Method: ⁠drive()⁠: Prints ⁠"Driving the [make] [model]!"⁠ and reduces ⁠fuel_level⁠ by ⁠10⁠.
#  Child Class ⁠ElectricVehicle⁠:
#  Inherits from ⁠Vehicle⁠.
#  Override ⁠fuel_level⁠ to be named ⁠battery_level⁠ (or just treat ⁠fuel_level⁠ as the battery capacity).
#  Override the ⁠drive()⁠ method: Print ⁠"Quietly cruising in the electric [make] [model]!"⁠ and reduce the battery by ⁠5⁠.
#  Add a new method ⁠charge()⁠: Restores the battery to ⁠100⁠.
class Vechicle:
    def __init__(self,make,model,fuel_level):
        self.make=make
        self.model=model
        self.fuel_level="%"
    def drive(self):
