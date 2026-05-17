# 2. Word Frequency Analyzer (Dictionaries)
# The Problem: Write a program that takes a paragraph of text and counts how many times each unique word appears.
# Requirements: Store the results in a dictionary where the key is the word and the value is the count.
# Concepts: dict, loop through string, .split(), if key in dict.
text='''winter is my favorite season because it brings a sense of calm and beauty to the world.
The cool breeze, misty mornings, and cozy evenings make it special. 
I enjoy sipping hot tea while reading a book, wrapped in a warm blanket.
Winter also brings festivals and celebrations, making it a time of joy and togetherness.'''
word=text.split()
count={}
for i in word:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print("is=",count["is"])
