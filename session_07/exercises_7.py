# Session 7 Exercises

## Section A
# 1. Write a function that prints your name
# def print_name():
#   print("Hello Zac!")

# print_name()

# 2. Write a function that accepts a name as a parameter and prints "Hello, <name>".
def print_name(name):
  print("Hello "+name)

# print_name("Zac")
# 3. Loop through the list ["Alice", "Bob", "Charlie"] and call the function you just wrote.
# names = ["Alice", "Bob", "Charlie"]
# for name in names:
#   print_name(name)

# 4. Write a function that prints the area of two passed in parameters.
def area(x, y):
  print("Area: "+str(x*y))

# area(5,6)
# 5. Write a function called 'print_list' that accepts a list as a parameter and then prints out each item of the list.
def print_list(list):
  for item in list:
    print(item)

names = ["Alice", "Bob", "Charlie"]
# print_list(names)

# 6. Put the following into a function that accepts age as a parameter:
#     1. If they are younger than 11, print "You're too young to go to this school".
#     2. If they are between 11 and 16, print "You can can come to this school".
#     3. If they are over 16, print 'You're too old for school".
#     4. If they are 0, print "You're not born yet!".
def school_age(age):
  if int(age) < 11:
    print("You're too young to go to this school")
  elif int(age) >= 11 and int(age) <= 16:
    print("You can can come to this school")
  elif int(age) > 16:
    print("You're too old for school")
  elif int(age) == 0:
    print("You're not born yet!")

# school_age(2)

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Write a function called is_odd that will return True or False if the integer passed as a parameter is odd (hint: x % 2 will return true for all odd numbers).
def is_odd(num):
  return num % 2

# if is_odd(2):
#   print(True)
# else:
#   print(False)

# 2. Write a function that accepts a word and returns it backwards, e.g. 'hello' -> 'olleh'.
def backwards(word):
  backwards = ""
  for i in reversed(word):
    backwards += i
  return backwards

# print(backwards("hello"))

# 3. Write a recursive function that accepts a number and prints that number of stars, followed by ever decreasing stars on each line, E.g:
# ```
# *****
# ****
# ***
# **
# *
# ```

def print_stars(x):
    star = ""
    for y in range(0, x):
        star = star + "*"
    print(star)
    if x > 1:
        print_stars(x-1)


# print_stars(10)

# 4. Create a padlock function. You need to be able to pass in a passcode and if its correct it should return "Unlock", else "Locked".
def lock(passcode):
  if passcode == "Hello":
    return "Unlock"
  else:
    return "Locked"


# 5. Write a function that returns the sum of multiples of 3 and 5 between 0 and limit (parameter). 
#   For example, if limit is 20, it should return the sum of 3, 5, 6, 9, 10, 12, 15, 18, 20.
def next_number(current):
  multiplyBy = 1
  nextNumber = 0
  while nextNumber < current:
    if 3*multiplyBy > current:
      return 3*multiplyBy
    elif 5*multiplyBy > current:
      return 5*multiplyBy
    multiplyBy += 1
    
def multiply(limit):
  current = 3
  while current < limit:
    print(current)
    current = next_number(current)
  return

# multiply(20)

# 6. Write a function called is_prime() that accepts a number and return True or False if the number of prime or not.
def is_prime(number):
  count = 0
  i = number
  while i > 0:
    if number % i == 0:
      count += 1
    i = i-1
  if count == 2:
    return True
  else:
    return False

# print(is_prime(8)) 

# 7. Write a function that checks to see if a string is a pallindrome, if it is, it will return True and False if it is not.
def is_pallindrome(word):
  reverse_word = word[::-1]
  if reverse_word == word:
    return True
  else:
    return False

# print(is_pallindrome("hey"))

# 8. Write a function that checks to see if a sentence is a pallindrome, if it is, it will return True and False if it is not. 
#   Tip - you may want to format your sentence so it is all lower case, and .replace() to get rid of white spaces.
def is_sentence_pallindrome(sentence):
  formatted_sen = sentence.lower()
  new_sentence = formatted_sen.replace(' ', '')
  rev_sentence = new_sentence[::-1]
  if rev_sentence == sentence:
    return True
  else:
    return False

print(is_sentence_pallindrome("he h"))