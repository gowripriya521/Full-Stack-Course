x="gaddam gowri priya"
y="priya gowri gaddam"
def data_1(x):
    print("--------->",x)
    temp={}
    for i in x:
        if i in temp:
            temp[i]+=1
        else:
            temp[i]=1
    return temp
for i in range(10):
    if i%2==0:
        print(data_1(x))
    else:
        print(data_1(y))

# 1.	count_even_odd
# 	•	Input: [1, 2, 3, 4, 5, 6, 7]
# 	•	Output: (3, 4)
# 	•	Logic: Loop through the list; if num % 2 == 0 increment even, else increment odd.
num=[1,2,3,4,5,6,7]
even=0
odd=0
for i in num:
    if i%2==0:
        even+=1
    else:
        odd+=1
print(even,odd)


# 	2.	fizzbuzz
# 	•	Input: fizzbuzz(15)
# 	•	Output: 1, 2, Fizz, 4, Buzz, Fizz, 7, 8, Fizz, Buzz, 11, Fizz, 13, 14, FizzBuzz (one per line)
# 	•	Logic: Loop 1 to n; check divisible by both 3 and 5 first, then 3, then 5, else print the number.
def fizzbuzz_1(num):
    for i in range(1,num):
        if i%3==0 and i%5==0:
            print("Fizzbuzz")
        elif i%3==0:
            print("fizz")
        elif i%5==0:
            print("buzz")
        else:
            print(i)
fizzbuzz_1(16)
    

# 	3.	is_prime
# 	•	Input: is_prime(7), is_prime(10)
# 	•	Output: True, False
# 	•	Loop output (1 to 50): 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47
# 	•	Logic: Return False if n < 2; loop from 2 to √n and return False if any divisor is found; otherwise True.
def is_prime(n):
    if n<2:
        return False 
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
print(is_prime(7))
print(is_prime(10))
  
# 	4.	get_grade
# 	•	Input: [95, 80, 60, 40]
# 	•	Output: A, B, C, Fail
# 	•	Logic: if/elif chain checking from highest threshold down.
num=[95,80,60,40]
def get_grade():
    for i in num:
        if i>=95:
            print("A")
        elif i<95 and i>=80:
            print("B")
        elif i<80 and i>=60:
            print("c")
        elif i<=40:
            print("fail")
get_grade()

# 	5.	factorial
# 	•	Input: factorial(5), factorial(0), factorial(-3)
# 	•	Output: 120, 1, "Error: negative number"
# 	•	Logic: If n < 0 return error; start result = 1 and multiply by each number from 1 to n.
def factorial_1(n):
    if n<0:
        print(f"error:negative number")
    else:
        result=1
        for i in range(1,n+1):
            result*=i
        print(result)
factorial_1(5)
factorial_1(0)
factorial_1(-3)

# 	6.	is_palindrome
# 	•	Input: is_palindrome("Race car"), filter on ["madam", "hello", "Nurses run", "python"]
# 	•	Output: True; filtered list: ["madam", "Nurses run"]
# 	•	Logic: Lowercase the text, remove spaces, compare it with its reverse.
def is_palindrome(n):
    s = ""
    for i in n:
        if i != " ":
            if i >= "A" and i <= "Z":
                i = chr(ord(i) + 32)
            s = s + i
    start = 0
    end = len(s) - 1
    while start < end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    return True
print(is_palindrome("Race car"))


# 	7.	digit_sum
# 	•	Input: digit_sum(1234), digit_sum(9)
# 	•	Output: 10, 9
# 	•	Logic: While n > 0, add n % 10 to total, then n //= 10.
def digit_sum(n):
    total = 0
    while n > 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    return total
print(digit_sum(1234))
print(digit_sum(9))

# 	8.	find_extremes
# 	•	Input: [4, 9, -2, 15, 7]
# 	•	Output: (15, -2) (largest, smallest)
# 	•	Logic: Set both to the first element; loop through the rest, updating when a bigger or smaller value is found.
def find_extremes(n):
    s=n[0]
    e=n[0]
    for i in n:
        if i>e:
            e=i
        elif i<s:
            s=i
    return e,s
print(find_extremes([4,9,-2,15,7]))

# 	9.	print_table
# 	•	Input: print_table(7), print_table(3, 10)
# 	•	Output for (3, 10): 3, 6, 9, 12, 15, 18, 24, 27, 30 (21 is skipped). For print_table(7), every result is divisible by 7, so nothing prints.
# 	•	Logic: Loop 1 to limit; compute n * i; if result % 7 == 0, continue; else print.
def print_table(n):
    for i in range(1, 11):
        result = n * i
        if result % 7 != 0:
            print(result)
print_table(3)

# 	10.	guess_game
# 	•	Input: guess_game(25) with user guesses 10, 40, 25
# 	•	Output: Prints Too low, Too high, Correct!; returns 3
# 	•	Logic: While loop with an attempts counter; compare each guess to secret using if/elif/else; break on correct.
def guess_game(secret):
    count = 0
    while True:
        guess = int(input("Enter guess: "))
        count = count + 1
        if guess < secret:
            print("Too low")
        elif guess > secret:
            print("Too high")
        else:
            print("Correct!")
            break
    return count
print(guess_game(25))

# 1. reverse_string
# - Input: reverse_string("python")
# - Output: "nohtyp"
# - Logic: Loop through the string in reverse order and build a new string.
def reverse_string(s):
    temp= ""
    for i in s:
        temp=i+temp
    return temp
print(reverse_string("python"))

# 2. count_vowels
# - Input: count_vowels("hello world")
# - Output: 3
# - Logic: Loop through each character and count vowels (a, e, i, o, u).
def count_vowels(s):
    count=0
    for i in s.lower():
        if i in "aeiou":
            count+=1
    return count
print(count_vowels("hello world"))

# 3. remove_duplicates
# - Input: [1, 2, 2, 3, 4, 4, 5]
# - Output: [1, 2, 3, 4, 5]
# - Logic: Create an empty list and append only elements that are not already present.
def remove_duplicates(n):
    temp=[]
    for i in n:
        if i not in temp:
            temp.append(i)
    return temp
print(remove_duplicates([1, 2, 2, 3, 4, 4, 5]))

# 4. sum_of_list
# - Input: [10, 20, 30, 40]
# - Output: 100
# - Logic: Loop through the list and add every element.
def sum_of_list(n):
    total=0
    for i in n:
        total+=i
    return total
print(sum_of_list([10, 20, 30, 40]))

# 5.group_even_odd
# - Input: [1, 2, 3, 4, 5, 6, 7, 8]
# - Output: {'even': [2, 4, 6, 8], 'odd': [1, 3, 5, 7]}
# - Logic: Create two lists and place numbers into them based on divisibility by 2.
def group_even_odd(n):
    temp={
        "even":[],
        "odd":[]
    }
    for i in n:
        if i%2==0:
            temp["even"].append(i)
        else:
            temp["odd"].append(i)
    return temp
print(group_even_odd([1, 2, 3, 4, 5, 6, 7, 8]))
