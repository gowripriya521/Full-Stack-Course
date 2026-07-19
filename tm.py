# 4. More Magic Methods: The ⁠Playlist⁠ Class
# Concept: Customizing container behavior using ⁠__len__⁠ and ⁠__getitem__⁠.
# Create a class called ⁠Playlist⁠ that holds a list of song titles.
#  Attributes: ⁠name⁠ (string) and ⁠songs⁠ (list of strings).
#  Magic Methods:
#  ⁠__len__(self)⁠: Allow the user to use the built-in ⁠len()⁠ function on your playlist object to see how many songs are in it.
#  ⁠__getitem__(self, index)⁠: Allow the user to access songs using index bracket notation (e.g., ⁠my_playlist[0]⁠ should return the first song).
#  Methods: ⁠add_song(song_title)⁠: Appends a song to the list.
# Which one of these looks like a fun next step? Write out your code for any of them and let's check it!
# class PlayList:
#     def __init__(self,name):
#         self.name=name
#         self.songs=[]
#     def add_song(self,song_title):
#         self.songs.append(song_title)
#     def __len__(self):
#         return len(self.songs)
#     def __getitem__(self,index):
#         return self.songs[index]
# p=PlayList.add_song("lenin")
# p=PlayList.add_song("rubaroo")
# p=PlayList.add_song("dheer dheer")
# print(len(p))
# print(p[0])
# The Multiplier: The ⁠__mul__⁠ Magic Method
# Concept: Overloading the multiplication (⁠*⁠) operator.
# You already mastered ⁠__add__⁠ earlier. Now let's see how to multiply an object by a number! Create a class called ⁠Item⁠.
#  Attributes: ⁠name⁠ (string) and ⁠price⁠ (float).
#  Magic Method ⁠__mul__(self, quantity)⁠: Overload the ⁠*⁠ operator so that if you multiply an item object by an integer quantity (e.g., ⁠item * 3⁠), it returns the total cost as a number.
#  Challenge: Create an item ⁠"Coffee"⁠ for ⁠3.50⁠ and print ⁠coffee * 4⁠. It should output ⁠14.0⁠.
# class Item:
#     def __init__(self,name,price):
#         self.name=name
#         self.price=price
#     def __mul__(self,quantity):
#         return self.price*quantity
# i=Item("coffee",3.50)
# print(i*4)
# 2. The Clean-Up: The ⁠__del__⁠ Destructor
# Concept: Running code automatically when an object is destroyed or deleted.
# Python has a dunder method called ⁠__del__⁠ that runs right before an object is removed from memory.
#  Attributes: ⁠username⁠ (string).
#  Constructor (⁠__init__⁠): Print ⁠"[username] has logged in."⁠
#  Destructor (⁠__del__⁠): Print ⁠"[username] has logged out."⁠
#  Challenge: Create a user instance ⁠user1 = User("Alice")⁠.
#  Then, manually delete it using the Python command ⁠del user1⁠ and watch the logout message trigger automatically!
# class CleanUp:
#     def __init__(self,username):
#         self.username=username
#         print(f"{self.username} has logged in.")
#     def __del__(self):
#         print(f"{self.username} has logged out.")
# user1=CleanUp("alice")
# del user1
# 3. Custom Iterators: The ⁠__iter__⁠ and ⁠__next__⁠ Methods
# Concept: Making your object loopable with a standard ⁠for⁠ loop.
# Right now, your ⁠Playlist⁠ class allows bracket indexing (⁠p1[0]⁠). But what if you want to loop through an object directly using ⁠for song in playlist:⁠? 
# Let's build a simple counter to see how looping works under the hood. Create a class called ⁠Countdown⁠.
#  Attributes: ⁠start⁠ (integer).
#  Magic Method ⁠__iter__(self)⁠: Simply ⁠return self⁠. This tells Python the object is iterable.
#  Magic Method ⁠__next__(self)⁠:
#  If ⁠self.start⁠ is greater than ⁠0⁠, save the current value, decrease ⁠self.start⁠ by ⁠1⁠, and return the saved value.
#  If ⁠self.start⁠ reaches ⁠0⁠, raise ⁠StopIteration⁠ (this is a special Python signal that safely tells a ⁠for⁠ loop to stop spinning).
#  Challenge: Create ⁠counter = Countdown(3)⁠ and run ⁠for num in counter: print(num)⁠. It should print ⁠3⁠, ⁠2⁠, ⁠1⁠, and stop beautifully.
# class CountDown:
#     def __init__(self,start):
#         self.start=start
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.start>0:
#             current=self.start
#             self.start-=1
#             return current
#         elif self.start==0:
#             raise StopIteration("this is a special python signal that safely tells a for loop to stop spinning")
# counter=CountDown(3)
# for num in counter:
#     print(num)
    