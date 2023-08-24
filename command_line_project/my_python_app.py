import random
all_attackers = {
    "arsenal_attackers": ["Saka", "Martinelli", "Jesus"],
    "chelsea_attackers": ["Sterling", "Nkunku", "Mudryk"],
    "liverpool_attackers": ["Salah", "Diaz", "Jota"],
    "manchester_city_attackers": ["Álvarez", "Haaland", "Grealish"],
    "manchester_united_attackers": ["Rashford", "Højlund", "Antony"],
    "tottenham_attackers": ["Son", "Richarlison", "Kulusevski"]
}

def check_duplicate(current_attack, attacker):
    for i in range(0, len(current_attack)):
        if current_attack[i] == attacker:
            return True
    return False

def get_random_attack():
    random_attack = []
    while len(random_attack) < 3:
        team = random.randint(0, 5)
        player = random.randint(0, 2)
        if team == 0:
            new_attacker = all_attackers["arsenal_attackers"][player]
            if check_duplicate(random_attack, new_attacker) == False:
                random_attack.append(new_attacker)
        elif team == 1:
            new_attacker = all_attackers["chelsea_attackers"][player]
            if check_duplicate(random_attack, new_attacker) == False:
                random_attack.append(new_attacker)
        elif team == 2:
            new_attacker = all_attackers["liverpool_attackers"][player]
            if check_duplicate(random_attack, new_attacker) == False:
                random_attack.append(new_attacker)
        elif team == 3:
            new_attacker = all_attackers["manchester_city_attackers"][player]
            if check_duplicate(random_attack, new_attacker) == False:
                random_attack.append(new_attacker)
        elif team == 4:
            new_attacker = all_attackers["manchester_united_attackers"][player]
            if check_duplicate(random_attack, new_attacker) == False:
                random_attack.append(new_attacker)
        elif team == 5:
            new_attacker = all_attackers["tottenham_attackers"][player]
            if check_duplicate(random_attack, new_attacker) == False:
                random_attack.append(new_attacker)
        else:
            print("ERROR")
    print("")
    print("LW: "+random_attack[0])
    print("ST: "+random_attack[1])
    print("RW: "+random_attack[2])
    print("")

def play_game():
    play = True
    f1 = open("ASCII_ball.txt", "r")
    print(f1.read())
    print("Welcome to random attack generator!")
    print("")
    print("")
    while play == True:
        print("")
        input("Press enter to generate a random attacking front 3 from the big 6!")
        get_random_attack()
        stop = input("Do you want to play again? Yes (0) or No (1): ")
        if stop == "1":
            play = False
    print("")
    print("Thanks for playing!")
    print("")

play_game()
