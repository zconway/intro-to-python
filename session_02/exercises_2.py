# Session 2 Exercises

## Section A
# 1. Create two variables that hold the width and height of a rectangle, work out and store the area in a third variable. 
# Print out the string: `Rectangle of width <x> and height <y> has an area of <area>`.
# width = 4
# length = 6
# area = width * length
# print(area)


# 2. Write code that prints the length of the string, 'python'.
# print(len('python'))


# 3. Print out the first and third letter of the word 'python'.
# word = "python"
# print(word[0] + word[2])


# 4. Ask the user to enter their name, and print out `Hello, <name>`.
# name = input("What is your name? ")
# print("Hello, " + name)

# 5. Ask the user to enter their age, tell them how old they will be in 15 years time.
# age = int(input("How old are you? "))
# print("In 15 years you will be " + str(age+15) + " years old!")


# 6. Combine the two input statements above and print out the message `Hello, <name>, you are currently <age> years old. 
#   In 15 years time you will be <age_in_15_years_time>`.
# print("Hello, " + name + ", In 15 years you will be " + str(age+15) + " years old!")


# 7. Ask the user to enter their hometown, print it out in uppercase letters.
# town = input("What is your hometown? ")
# print(town.upper())

# 8. Ask the user to enter their favourite colour and find out the length of the colour they input.
# colour = input("What is your favourite colour?")
# print(len(colour))


# 9. Ask the user to enter the weather and the month. Print out the string, `It is <month> and it is <weather> today`.
# month = input("What month is it? ")
# weather = input("What is the weather like today? ")
# print("It is " + month + " and it is " + weather + " today")

# 10. Ask the user to enter 5 different temperatures and the month. Work out the average temperature and print out the string: 
#   `It is <month> and the average temperature is <average_temperature> degrees celsius`.
# month = input("What month is it? ")
# temp1 = int(input("What is the temperature on day 1? "))
# temp2 = int(input("What is the temperature on day 2? "))
# temp3 = int(input("What is the temperature on day 3? "))
# temp4 = int(input("What is the temperature on day 4? "))
# temp5 = int(input("What is the temperature on day 5? "))
# avg_temp = (temp1 + temp2 + temp3 + temp4 + temp5) / 5
# print("It is " + month + " and the average temperature is " + str(avg_temp) + " degrees celsius")


# 11. Print out the above sentence but make the month upper case.
# print("It is " + month.upper() + " and the average temperature is " + str(avg_temp) + " degrees celsius")


# 12. Create a variable that holds your favourite animals and print it out. 
#    Make sure the animals are all on different lines and tabbed.
# fav_animals = "\tDog\n\tCat\n\tElephant"
# print(fav_animals)

# 13. Ask the user to enter their name as well as a number. 
#    Print out the uppercase character at that position in the string.
# name = input("What is your name? ")
# number = int(input("enter a number: "))
# print(name.upper()[number])


# 14. Slice the string with steps of 2, excluding the first and last characters of the string "WelcometoPython".
string = "WelcometoPython"
print(string[1:-1:2])