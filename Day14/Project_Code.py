#1. Import logo
from replit import clear
from game_data import data
import random
import art


#2. Display logo
print(art.logo)


#####3. for loop for generating two initial celebratory#####
compareA = random.choice(data)
AgainstB = random.choice(data)
if compareA == AgainstB:
    AgainstB = random.choice(data)

compareA_value = list(compareA.values())
AgainstB_value = list(AgainstB.values())

print(f"Compare A: {compareA_value[0]}, a {compareA_value[2]}, from {compareA_value[3]}.")
print(art.vs)
print(f"Against B: {AgainstB_value[0]}, a {AgainstB_value[2]}, from {AgainstB_value[3]}.")


#####4. Choose celebratory after first two celebratory#####
def more_celebratory(compareA, AgainstB):
    """Takes the first two user account and return next two accounts by shifting B to A """
    compareA = AgainstB
    AgainstB = random.choice(data)
    if compareA == AgainstB:
        AgainstB= random.choice(data)

    compareA_value = list(compareA.values())
    AgainstB_value = list(AgainstB.values())

    print(f"Compare A: {compareA_value[0]}, a {compareA_value[2]}, from {compareA_value[3]}.")
    print(art.vs)
    print(f"Against B: {AgainstB_value[0]}, a {AgainstB_value[2]}, from {AgainstB_value[3]}.")
    return compareA, AgainstB, compareA_value, AgainstB_value


#####5. Compare_function: to compare the values of both celabratory#####
def game(compareA, AgainstB, compareA_value, AgainstB_value):
    """Take account counts and compare either the user answer is correct or wrong."""
    current_score = 0    
    answer = True
    while answer:
        choose_celebratory = input("Who has more followers? Type 'A' or 'B':").lower()
        if choose_celebratory == 'a':
            if compareA_value[1] > AgainstB_value[1]:
                current_score += 1
                clear()
                print(art.logo)
                print(f"You're right! Current score: {current_score}")
                compareA, AgainstB, compareA_value, AgainstB_value = more_celebratory(compareA, AgainstB)
            else:
                clear()
                print(art.logo)
                print(f"Sorry that's wrong. Final score: {current_score}")
                answer = False
        elif choose_celebratory == 'b':
            if AgainstB_value[1] > compareA_value[1]:
                current_score += 1
                clear()
                print(art.logo)
                print(f"You're right! Current score: {current_score}")
                compareA, AgainstB, compareA_value, AgainstB_value = more_celebratory(compareA, AgainstB)
            else:
                clear()
                print(art.logo)
                print(f"Sorry that's wrong. Final score: {current_score}")
                answer = False


#####6. Call game() to start game
game(compareA, AgainstB, compareA_value, AgainstB_value)
