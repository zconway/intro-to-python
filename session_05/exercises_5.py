# Session 5 Exercises

## Section A
# 1. Print 10 random numbers.
import random
# randomList = []
# for i in range(0,10):
#   print(random.randint(0,10000))



# 2. Keep asking the user to enter a number until they enter the number 7, then print "Wow lucky number 7!".
#     - Rewrite so that the number being guessed is a random value from 1 to 10 instead of number 7 .
import random
# randNum = random.randint(1,11)
# guessed = False
# while guessed == False:
#   guess = int(input("Guess the number between 1-10: "))
#   if guess == randNum:
#     guessed = True
#     print("Wow lucky number "+str(randNum)+"!")

# 3. The area of a rectangle is width multiplied by height. Ask the user to enter a width and height in cm, then print the area to the whole square metre. 
#   E.g. 240cm x 80cm = 19200cm2 = 2m2.
from math import floor
# width = int(input("Enter height in cm: "))
# height = int(input("Enter height in cm: "))
# area = floor(width/10*height/10)
# print("Area is "+str(area)+"m squared.")

# 4. Ask the user for a password, if they enter the password "qwerty123", print "You have successfully logged in". 
#   If they get it wrong, print "Password failure" and then ask them to enter it again. 
#   Only allow them to enter the password wrong 3 times before printing "System Locked!".
# count = 0
# password = "qwerty123"
# while True:
#   count += 1
#   e = input("Enter Password: ")
#   if e == password:
#     print("Correct!")
#     break
#   else:
#     print("Password failure")
#     if count >= 3:
#       print("System Locked!")
#       break

# 5. Add up all the numbers from 1 to 500 and print the answer.
# total = 0
# count = 0
# while count <= 500:
#   total += count
#   count += 1
# print(total)

# 6. Create a blank list. Ask the user to input 10 numbers (one should be the number 99) into the list. 
#   Find the index at which the user entered the number 99.
# list = []
# for i in range(10):
#   list.append(int(input("Enter number: ")))
# print(list)
# for i in range(10):
#   if list[i] == 99:
#     print("Index is "+str(i))
#     break

# 7. Print a multiplication table for the number 18 up to 15. E.g.
#     1 x 18 = 18
#     2 x 18 = 36
# for i in range(16):
#   print(str(18*i))


# 8. Print the numbers 1 to 100 (including the number 100) using a while loop.
# count = 1
# while count < 101:
#   print(count)
#   count += 1


# 9. Rewrite question B8 from session 3 using a while loop
#     - A school has following rules for their grading system:
#         a.	Above 80 – A
#         b.	60 to 80 – B
#         c.	50 to 60 – C
#         d.	45 to 50 – D
#         e.	25 to 45 – E
#         f.	Below 25 - F
#     Ask user to enter the lesson and the marks for three lessons and print out the corresponding grades for the lesson.
# lesson = input("Enter lesson: ")
# grade1 = int(input("Enter grade 1: "))
# grade2 = int(input("Enter grade 2: "))
# grade3 = int(input("Enter grade 3: "))

# finalGrade = (grade1+grade2+grade3)/3

# if finalGrade > 80:
#   print("A")
# elif finalGrade >= 60:
#   print("B")
# elif finalGrade >= 50:
#   print("C")
# elif finalGrade >= 45:
#   print("D")
# elif finalGrade >= 25:
#   print("E")
# else:
#   print("F")


# 10. Ask the user to enter the names of people who entered a prize draw. Select a random winner and print their name
# names = []

# for i in range(3):
#   names.append(input("Enter name: "))

# num = random.randint(0,2)
# print("The winner is: "+names[num])

# 11. Create a rock, paper, scissors game which is run against computer. 
#    This is a game where you select either rock/paper/scissors and you compare it to your opponents choice. 
#    Rock beats scissors, paper beats rock, scissors beats paper. If both choose the same, then you play again.
#       + Expand this so that its best of 3 games
type = ["Rock", "Paper", "Scissor"]

while True:
  comp = type[random.randint(0,2)]
  choice = input("Rock, Paper, Scissors: ")
  print("The computer chose "+comp)
  if choice == comp:
    print("It's a tie!")
  elif choice == "Rock":
    if comp == "Paper":
      print("You lose!")
    else:
      print("You win!")
  elif choice == "Paper":
    if comp == "Scissors":
      print("You lose!")
    else:
      print("You win!")
  elif choice == "Scissors":
    if comp == "Rock":
      print("You lose!")
    else:
      print("You win!")
  else:
    print("Error!")