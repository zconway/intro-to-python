# Session 4 Exercises

## Section A
# 1. Create the following list of items: Apples, Cherries, Pears, Pineapple, Peaches, Mango. Then print the list.
items = ["Apples", "Cherries", "Pears", "Pineapple", "Peaches", "Mango"]
print(items)

# 2. Add "Grapes" to the list and print the list.
items.append("Grapes")
print(items)

# 3. Change "Pears" to "Strawberries" and print the list.
items[2] = "Strawberries"
print(items)

# 4. Remove "Apples" from the list and print the list.
del(items[0])
print(items)

# 5. Print out the current length of the list.
print(len(items))


# 6. Order the list alphabetically.
items.sort()


# 7. Print out the list again.
print(items)



# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Loop through the list you created in section A and print each item out.
for item in items:
  print(item)


# 2. Print the numbers 1 to 100 (including the number 100).
for num in range(1,101):
  print(num)


# 3. Print all odd numbers from 1 to 100.
for num in range(1,101):
  if num%2 == 1:
    print(num)


# 4. The modern olympics started in 1896, print the years they have been held (bonus points to skip the years it has not been held 1916, 1940, 1944, 2020).
for year in range(1896, 2024, 4):
  if year != 1916 and year != 1940 and year != 1944 and year != 2020:
    print(year)


# 5. Create a list of ten random numbers. Loop through your list and count the number of even numbers and the number of odd numbers.
import random
randomList = []
for i in range(0,10):
  n = random.randint(1,30)
  randomList.append(n)
print(randomList)
odd = 0
even = 0
for i in randomList:
  if i%2 == 0:
    even = even+1
  else:
    odd = odd + 1
print("Even: "+ str(even))
print("Odd: "+ str(odd))
# 6. Create a list of five names. Write a loop that will print "Hello" plus each name in the list.
names = ["Zac", "Bob", "John", "Meg", "Alex"]
for name in names:
  print("Hello " + name)

# 7. Create a loop to go through each letter of the word "supercalifragilisticexpialidocious".
word = "supercalifragilisticexpialidocious"
for i in word:
  print(i)

# 8. Create a list of 5 numbers. Write a for loop which appends the square of each number to the new list.
nums = [1,2,3,4,5]
nums2 = []
for i in nums:
  nums2.append(i**2)
print(nums2)


# 9. Create a list with five names in. Write a for loop which appends  Dr. to each name in the new list.
names = ["Zac", "Bob", "John", "Meg", "Alex"]
names2 = []
for name in names:
  names2.append("Dr. " + name)
print(names2)

# 10. FizzBuzz – Write a program that prints the numbers from 1 to 100. For multiples of three, print "Fizz" instead of the number and for multiples of five, print "Buzz". 
#    For numbers which are multiples of both three and five, print "FizzBuzz".

#     ```
#     1
#     2
#     Fizz
#     4
#     Buzz
#     Fizz
#     7
#     8
#     Fizz
#     Buzz
#     11
#     Fizz
#     13
#     14
#     FizzBuzz
#     ```
for num in range(1,101):
  if num%3 == 0 and num%5 == 0:
    print("FizzBuzz")
  elif num%3 == 0:
    print("Fizz")
  elif num%5 == 0:
    print("Buzz")
  else:
    print(num)

