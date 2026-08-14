# x={
#     1:{"name":"priya","class":7},
#     2:{"name":"gowri","class":8},
#     3:{"name":"sam","class":7},
#     4:{"name":"raju","class":9},
#     5:{"name":"ram","class":6},
#     6:{"name":"radha","class":10},
#     7:{"name":"ramesh","class":9},
#     8:{"name":"suresh","class":6},
#     9:{"name":"devi","class":8},
#     10:{"name":"sam","class":5},

# }

# def student_class(y):
#     temp=[]
#     for i in x:
#         if x[i]["class"]==y:
#             temp.append(x[i]["name"])
#     return temp
# print(student_class(9))

# def cal(*marks):
#     total=sum(marks)
#     percentage=total/len(marks)
#     print(total,percentage)
# cal(80,75,90,85)

# x="pomegranate"
# def word_fre():
#     temp={}
#     for i in x:
#         if i in temp:
#             temp[i]+=1
#         else:
#             temp[i]=1
#     print(temp)
# word_fre()

# def word_1():
#     inven={"apple":50,"banana":0,"orange":12,"pears":0}
#     for i in inven:
#         temp=inven[i]
#         if temp==0:
#             print(f"item{i} is out of stock!")
#         else:
#             print(f"{i}:{temp} units available")
# word_1()

# arr=[1,2,3,4,5]
# s=0
# e=len(arr)-1
# while s<e:
#     arr[s],arr[e]=arr[e],arr[s]
#     s+=1
#     e-=1
# print(arr)

# dupli=[1,2,2,3,1,4]
# x=[]
# for i in dupli:
#     if i not in x:
#         x.append(i)
# print(x)

# emp_names=["ramu","sam","anil","rani","priya","anil","priya","sam"]
# temp={}
# for i in emp_names:
#     if i not in temp:
#         temp[i]=0
# print(temp)    

# def group_name(names):
#     temp={}
#     for i in names:
#         first_letter=i[0]
#         if first_letter in temp:
#             temp[first_letter].append(i)
#         else:
#             temp[first_letter]=[i]
#     return temp
# names=["Ram","Raj","Sam","Sita","John","Jenny"]
# print(group_name(names))

# def all_student():
#     temp=[]
#     for i in x:
#         temp.append(x[i]["name"])
#     return temp
# print(all_student())

# PLAYERS = { 
#     101: {"username": "PixelSlayer", "game": "Valorant", "rank": "Diamond", "level": 45}, 
#     102: {"username": "ShadowNinja", "game": "Fortnite", "rank": "Unranked", "level": 12}, 
#     103: {"username": "CyberQueen",  "game": "Valorant", "rank": "Radiant",  "level": 88}
# }
# def get_player(player_id):
#     return PLAYERS.get(player_id)


# SNEAKERS={
#     1: {"brand": "Nike", "model": "Air Max", "size": 10, "price": 120},
#     2: {"brand": "Adidas", "model": "Ultraboost", "size": 9, "price": 180},
#     3: {"brand": "Nike", "model": "Dunk Low", "size": 10, "price": 110},
#     4: {"brand": "Puma", "model": "Suede", "size": 8, "price": 70}
# }
# def get_sneakers(brand=None, max_price=None):
#     temp={}
#     for key, value in SNEAKERS.items():
#         if brand and value["brand"] != brand:
#             continue
#         if max_price and value["price"] > max_price:
#             continue
#         temp[key] = value
#     return temp

# def get_sneakers(brand=None,max_price=None):
#     result = []
#     for i in SNEAKERS:
#         if brand and SNEAKERS[i]["brand"] != brand:
#             continue
#         if max_price and SNEAKERS[i]["price"] > max_price:
#             continue
#         result.append({
#             "id": i,
#             **SNEAKERS[i]
#         })
#     return result


# PLAYLIST = {
#     1: {"title": "Blinding Lights",  "artist": "The Weeknd", "genre": "Pop"},
#     2: {"title": "Starboy","artist": "The Weeknd", "genre": "Pop"},
#     3: {"title": "Levitating","artist": "Dua Lipa", "genre": "Pop"},  
#     4: {"title": "Bohemian Rhapsody","artist": "Queen", "genre": "Pop"}     
# }
# def search_song(q=None):
#     result = []
#     q=q.lower()
#     for i in PLAYLIST:
#         title=PLAYLIST[i]["title"].lower()
#         artist=PLAYLIST[i]["artist"].lower()
#         if q in title or q in artist:
#             result.append({
#                 "id":i,
#                 **PLAYLIST[i]
#             })
#     return result

# SCORES = {
#     1: {"player": "Alex", "score": 4500},
#     2: {"player": "Sam", "score": 9200},
#     3: {"player": "Jordan", "score": 1200},
#     4: {"player": "Taylor", "score": 8100},
#     5: {"player": "Morgan", "score": 6700}
# }
# def get_leaderboard(top=None):
#     result =[] 
#     for i in SCORES:
#         result.append({
#             "id":i,
#             **SCORES[i]
#         })
#     result.sort(key=lambda x: x["score"], reverse=True)
#     if top:
#         result = result[:top]
#     return result

# STUDENTS = {
#     1: {"name": "Emma", "grade": 10, "passed": True},
#     2: {"name": "Liam", "grade": 10, "passed": False},
#     3: {"name": "Noah", "grade": 11, "passed": True},
#     4: {"name": "Olivia", "grade": 11, "passed": True},
#     5: {"name": "Ethan", "grade": 10, "passed": True}
# }
# def get_student_stats():
#     passed = 0
#     for i in STUDENTS:
#         if STUDENTS[i]["passed"]:
#             passed += 1
#     total=len(STUDENTS)
#     failed = total - passed
#     pass_rate=(passed/total)*100
#     return {
#         "total_students": total,
#         "passed_count": passed,
#         "failed_count": failed,
#         "pass_rate_percentage":pass_rate
#     }


# WEATHER = {
#     101: {"city": "Chennai", "temperature": 34, "condition": "Sunny"},
#     102: {"city": "Bangalore", "temperature": 27, "condition": "Cloudy"},
#     103: {"city": "Hyderabad", "temperature": 31, "condition": "Clear"},
#     104: {"city": "Mumbai", "temperature": 29, "condition": "Rainy"}
# }
# def get_weather(station_id):
#     return WEATHER.get(station_id)

# PLAYERS = {
#     1: {"name": "Rohit", "runs": 8500},
#     2: {"name": "Virat", "runs": 12500},
#     3: {"name": "Rahul", "runs": 7200},
#     4: {"name": "Gill", "runs": 6800},
#     5: {"name": "Pant", "runs": 5900}
# }
# def get_player(top=None):
#     result = sorted(PLAYERS.items(), key=lambda x: x[1]["runs"], reverse=True)
#     if top:
#         result = result[:top]
#     return dict(result)

# 1
# def list_operation():
#     matrix = [[1, 6, 9], [4, 12, 15], [7, 8, 21]]
#     temp=[]
#     for i in matrix:
#         for j in i:
#             if j%3==0:
#                 temp.append(j) 
#     print(temp)           
# list_operation()

# 2
# students = [("Alice", 88, 20), ("Bob", 95, 22), ("Charlie", 88, 19), ("David", 95, 20)]
# result=sorted(students,key=lambda x:(-x[1],x[2]))
# for i in result:
#     print(i)

# students = [
#     ("Alice", 88, 20),
#     ("Bob", 95, 22),
#     ("Charlie", 88, 19),
#     ("David", 95, 20)
# ]
# def sort_students(x):
#     return (-x[1], x[2])
# result = sorted(students, key=sort_students)
# print(result)


# 3.
# numbers = [1, 3, 4, 6, 7, 8, 9]
# temp=[]
# for i in numbers:
#     if i%2==0:
#         temp.append(i)
# print(temp)

# 4
# nums1 = [1, 2, 3, 4, 5]#; ref1 = nums1[1:4]; ref1[0] = 99
# nums2 = [1, 2, 3, 4, 5]#; nums2[1:4] = [99]
# print(nums1)
# print(nums2)

# 5
# data = [10, 20, 30, 40, 50, 60, 70]
# def chunk_list(size): 
#     temp=[]
#     for i in range(0,len(data),size):
#         result=data[i:i+size]
#         temp.append(result)
#     print(temp)
# chunk_list(3)

# 6
# user_roles = {"usr_1": "admin","usr_2": "editor","usr_3": "admin","usr_4": "viewer","usr_5": "editor"}
# temp = {}
# for user, role in user_roles.items():
#     if role in temp:
#         temp[role].append(user)
#     else:
#         temp[role] = [user]
# print(temp)

# 7
# d1 = {'a': 100, 'b': 200, 'c': 300}
# d2 = {'b': 150, 'c': 50, 'd': 400}
# temp={}
# for i in d1:
#     temp[i]=d1[i]
# for i in d2:
#     if i in temp:
#         temp[i]=temp[i]+d2[i]
#     else:
#         temp[i]=d2[i]
# print(temp)

# 8
# words = ["Apple", "apricot", "Banana", "blueberry", "Avocado", "Cherry"]
# temp={}
# for i in words:
#     first_word=i[0].lower()
#     if first_word in temp:
#         temp[first_word].append(i)
#     else:
#         temp[first_word]=[i]
# print(temp)



