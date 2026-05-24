# 15. Maximum Number of Vowels in a Window
# Given a string and an integer k, find the maximum number of vowels present in any substring of size k.
# Example:
# Input:
# s = "abciiidef"
# k = 3
# Output:
# 3
# Explanation:
# Substring:
# "iii"
# contains 3 vowels
# Expected Concept:
# - Sliding window
# - Character checking
# s="abciiidef"
# k=3
# x=0
# c=0
# for i in s:
#     if i in "aeiou":
#         c+=1
#         if c>=k:
#             k=c
#     else:
#         c=0
#         x+=1
# print(k)


