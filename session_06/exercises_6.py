# Session 6 Exercises

## Section A
# 1. Create the following dictionary for an apple: Type = "Bramley", Price = 0.39, Colour = "Green".
apple = {
  "type": "Bramley",
  "price": 0.39,
  "colour": "Green"
}


# 2. Add the best before date to the dictionary - print the dictionary.
apple["bestBefore"] = "10/07/2023"
# print(apple)

# 3. Change the price to 0.41 - print the dictionary.
apple["price"] = 0.41
# print(apple)

# 4. Set the apple to be on offer using a Boolean - print the dictionary.
apple["onOffer"] = True
# print(apple)

# 5. The offer has now expired, remove the key/value from the dictionary - print the dictionary.
del(apple["onOffer"])
print(apple)

# <---------------------------------------------------------------------------------------------->

## Section B
# 1. Ask the user to enter a persons name, if they enter a name, ask for the persons age. Store this information in a dictionary inside a list. 
#   Continue to ask for names until no name is given. Then print out all of the names and ages collected.
# list = []
# name = None
# while name != "":
#   name = input("Enter name: ")
#   age = input("Enter age: ")
#   if name and age:
#     list.append({
#       "name": name,
#       "age": int(age)
#     })

# print(list)

# 2. Create a restaurants menu with 5 items. Store this information in a dictionary inside a list. 
#   Each item in the menu should have the name of the item, the price and if it's vegetarian friendly (make at least one vegetarian friendly dish). 
#   Print out the entire menu. Print out the name of the vegetarian option(s).
menu = [
  {
    "name": "Burger",
    "price": 5.50,
    "v": False
  },
  {
    "name": "Chips",
    "price": 3,
    "v": True
  },
  {
    "name": "Hot Dog",
    "price": 6,
    "v": False
  },
  {
    "name": "Salad",
    "price": 5,
    "v": True
  },
  {
    "name": "Chicken",
    "price": 6,
    "v": False
  },
]

print(menu)
print("")
print("Vegetarian options:")
for item in menu:
  if item["v"] == True:
    print(item)


# 3. The beetle game is a dice game where depending on what you roll is how much of the beetle you can draw.
#   If you roll a 6, you can draw the body
#   If you roll a 5, you can draw the head
#   If you roll a 4, you can draw the legs (but remember, you cannot draw legs without a body)
#   If you roll a 3, you can draw the antenna (but remember, you cannot draw antenna without a head)
#   If you roll a 2, you can draw the eyes (but remember, you cannot draw eyes without a head)
#   If you roll a 1, you can draw the mouth (but remember, you cannot draw a mouth without a head)
#   You need 6 legs, 2 antenna, 2 eyes, 1 mouth.
#   The player to complete the beetle in the fewest rolls of the dice wins. Create the beetle game.

import random
randNum = random.randint(1,11)
beetle = {
  "legs": 0,
  "antenna": 0,
  "eyes": 0,
  "mouth": False,
  "body": False,
  "head": False
}
rollCount = 0

while beetle["legs"] < 6 or beetle["antenna"] < 2 or beetle["eyes"] < 2 or beetle["mouth"] == False:
  print("")
  rollCount += 1
  input("Press enter to roll the dice for the "+str(rollCount)+" time!")
  randNum = random.randint(1,6)
  print("")
  print("You rolled: "+str(randNum))
  print("")
  if randNum == 6:
    if beetle["body"] == True:
      print("The beetle already has a body!")
    else:
      beetle["body"] = True
      print("Your beetle now has a body!")
  if randNum == 5:
    if beetle["head"] == True:
      print("The beetle already has a head!")
    else:
      beetle["head"] = True
      print("Your beetle now has a head!")
  if randNum == 4:
    if beetle["body"] == True:
      if beetle["legs"] < 6:
        beetle["legs"] += 1
        print("Your beetle now has "+str(beetle["legs"])+" legs!")
      else:
        print("Your beetle already has all of it's legs!")  
    else:
      print("Your beetle needs a body before you can add legs!")
  if randNum == 3:
    if beetle["head"] == True:
      if beetle["antenna"] < 2:
        beetle["antenna"] += 1
        print("Your beetle now has "+str(beetle["antenna"])+" antenna!")
      else:
        print("Your beetle already has both of it's antenna!")  
    else:
      print("Your beetle needs a head before you can add antenna!")
  if randNum == 2:
    if beetle["head"] == True:
      if beetle["eyes"] < 2:
        beetle["eyes"] += 1
        print("Your beetle now has "+str(beetle["eyes"])+" eyes!")
      else:
        print("Your beetle already has both of it's eyes!")  
    else:
      print("Your beetle needs a head before you can add eyes!")
  if randNum == 1:
    if beetle["head"] == True:
      if beetle["mouth"] == False:
        beetle["mouth"] = True
        print("Your beetle now has a mouth!")
      else:
        print("Your beetle already has a mouth!")  
    else:
      print("Your beetle needs a head before you can add a mouth!")
  print("")
  print(beetle)

print("")
print("You win!")
print("Number of rolls: "+str(rollCount))
