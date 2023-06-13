# Session 3 Exercises

## Section A
# 1. Ask for the user's name, if they are called "Bob", print "Welcome Bob!".
# name = input("What is your name? ")
# if name == "Bob":
#   print("Welcome Bob!")


# 2. Ask for the user's name, if they are not called "Alice", print "You're not Alice!".
# if name != "Alice":
#   print("You're not Alice!")


# 3. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure".
# password = input("Password: ")
# if password == "qwerty123":
#   print("You have successfully logged in")
# else:
#   print("Password failure")

# 4. Ask the user to enter a number, if the number is even, print "Even", otherwise print "Odd".
# number = int(input("Enter a number: "))
# if number%2 == 0:
#   print("Even")
# else:
#   print("Odd")

# 5. Ask the user for 2 different numbers, if the total of the two numbers is over 21, print "Bust" otherwise print "Safe"
# number1 = int(input("Enter number 1: "))
# number2 = int(input("Enter number 2: "))
# if number1+number2 > 21:
#   print("Bust")
# else:
#   print("Safe")

# 6. Ask the user to enter the length and width of a shape and check if it is a square or not.
# length = int(input("Enter length: "))
# width = int(input("Enter width: "))
# if length == width:
#   print("The shape is square!")
# else:
#   print("The shape is not square!")

# 7. You have had a great year and are going to offer a bonus of 10% to any employee who has a service of over 3 years. 
#   Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
# service = int(input("How many years have you worked at the company?: "))
# salary = int(input("What is your salary?: "))

# if service >= 3:
#   print("You will receive a bonus of: £" + str(int(salary/10)))
# else:
#   print("No bonus")

# 8. Take a whole number input, if it's positive, print out the number cubed, if it is a negative, print out half its value.
# number = int(input("Enter a whole number: "))
# if number >= 0:
#   print(number**3)
# else:
#   print(number/2)

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask for the user's name, if they are called "Alice" print "Hello, Alice", if they are called "Bob", 
#   print "You're not Bob! I'm Bob", else print "You must be Charlie".
# name = input("Enter name: ")
# if name == "Alice":
#   print("Hello, Alice")
# elif name == "Bob":
#   print("You're not Bob! I'm Bob")
# else:
#   print("You must be Charlie")

# 2. Ask the user to enter their age:
#     1. If they are younger than 11, print "You're too young to go to this school"
#     2. If they are between 11 and 16, print "You can can come to this school"
#     3. If they are over 16, print 'You're too old for school"
#     4. If they are 0, print "You're not born yet!"
# age = int(input("Enter age: "))
# if age < 11:
#   print("You're too young to go to this school")
# elif age >= 11 and age <= 16:
#   print("You can can come to this school")
# elif age > 16:
#   print("You're too old for school")
# elif age == 0:
#   print("You're not born yet!")

# 3. Ask the user to enter the name of a month. If the user enters March/April/May: print "<month> is in Spring", otherwise print "I don't know".
#     1. Expand for the rest of the year, given that summer is June/July/August. Autumn is September/October/November. Winter is December/January/February.
#     2. Ensure that when an unknown month is given it prints "I don't know".
# month = input("Enter month: ")
# if month == "March" or month == "April" or month == "May":
#   print(month + " is in Spring")
# elif month == "June" or month == "July" or month == "August":
#   print(month + " is in Summer")
# elif month == "September" or month == "October" or month == "November":
#   print(month + " is in Autumn")
# elif month == "December" or month == "January" or month == "February":
#   print(month + " is in Winter")
# else:
#   print("I don't know")


# 4. Ask the user for two different numbers, if both numbers are even, print "Even", if both numbers are odd, print "Odd", else print the product of the two numbers.
# number1 = int(input("Enter number 1: "))
# number2 = int(input("Enter number 2: "))
# if number1%2 == 0 and number2%2 == 0:
#   print("Both are even!")
# elif number1%2 == 1 and number2%2 == 1:
#   print("Both are odd!")
# else:
#   print(number1*number2)
  
# 5. Ask the user to input two numbers. Decide which is the number of highest value and print this out.
# num1 = int(input("Enter number 1: "))
# num2 = int(input("Enter number 2: "))
# if num1 >= num2:
#   print("The highest value is " + str(num1))
# else:
#   print("The highest value is " + str(num2))
  
# 6. You have had a fantastic year and are now going to offer a bonus of 20% to any employee who has a service of over 7 years, 
#   a bonus of 15% to any employee who has a service of over 5 years and a bonus of 10% to any employee who has a service of 3 - 5 years. 
#    Ask the user to input their current salary and years of service and print out their salary and their bonus or "No bonus" if they are not receiving one.
# service = int(input("How many years have you worked at the company?: "))
# salary = int(input("What is your salary?: "))

# if service >= 7:
#   print("You will receive a bonus of: £" + str(int(salary/100*20)))
# elif service >= 5:
#   print("You will receive a bonus of: £" + str(int(salary/100*15)))
# elif service >= 3:
#   print("You will receive a bonus of: £" + str(int(salary/100*10)))
# else:
#   print("No bonus")


# 7. Take the age and name of three people and determine who is the oldest and youngest and print out the name and age of the oldest and youngest. 
#   If all three ages are the same, print that.
# name1 = input("Enter name 1: ")
# age1 = int(input("Enter age 1: "))
# name2 = input("Enter name 2: ")
# age2 = int(input("Enter age 2: "))
# name3 = input("Enter name 3: ")
# age3 = int(input("Enter age 3: "))

# if age1 == age2 and age2 == age3:
#   print("All the same age!")
# elif age1 < age2 and age1 > age3:
#   print(name2 + " is the oldest and " + name3 + " is the youngest")
# elif age1 > age2 and age1 < age3:
#   print(name3 + " is the oldest and " + name2 + " is the youngest")
# elif age2 < age1 and age2 > age3:
#   print(name1 + " is the oldest and " + name3 + " is the youngest")
# elif age2 > age1 and age2 < age3:
#   print(name3 + " is the oldest and " + name1 + " is the youngest")
# elif age3 < age1 and age3 > age2:
#   print(name1 + " is the oldest and " + name2 + " is the youngest")
# elif age3 > age1 and age3 < age2:
#   print(name2 + " is the oldest and " + name1 + " is the youngest")
# else:
#   print("error")

# 8. A school has following rules for their grading system:
#     a.	Above 80 – A
#     b.	60 to 80 – B
#     c.	50 to 60 – C
#     d.	45 to 50 – D
#     e.	25 to 45 – E
#     f.	Below 25 - F
#   Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.
lesson = input("Enter lesson: ")
grade1 = int(input("Enter grade 1: "))
grade2 = int(input("Enter grade 2: "))
grade3 = int(input("Enter grade 3: "))

finalGrade = (grade1+grade2+grade3)/3

if finalGrade > 80:
  print("A")
elif finalGrade >= 60:
  print("B")
elif finalGrade >= 50:
  print("C")
elif finalGrade >= 45:
  print("D")
elif finalGrade >= 25:
  print("E")
else:
  print("F")
