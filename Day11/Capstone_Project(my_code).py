from replit import clear
from art import logo
import random
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.✔️

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
game_direction = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()

def add(your_cards):
    current_score = 0
    for card in your_cards:
        current_score += card
    return current_score

def your_side_game():
    print(logo)
    your_cards = []
    computer_cards = []
    add_more_cards_computer = [True , False]

    your_item1 = random.choice(cards)
    your_item2 = random.choice(cards)
    your_cards.append(your_item1)
    your_cards.append(your_item2)
    your_current_score = add(your_cards)
    print(f"    Your cards: {your_cards}, current score: {your_current_score}")

    computer_item1 = random.choice(cards)
    computer_item2 = random.choice(cards)
    computer_cards.append(computer_item1)
    computer_cards.append(computer_item2)
    #print(computer_cards)
    computer_current_score = add(computer_cards)
    #print(computer_current_score)
    print(f"    Computer's first card: {computer_cards[0]}")

    if (your_item1 == 10 and your_item2 == 11) or (your_item1 == 11 and your_item2 == 10):
        print(f"    Your final hand: {your_cards}, final score: 0")
        print(f"    Computer's final hand: {computer_cards}, final score: {computer_current_score}")
        print("Win with a Blackjack \N{smiling face with sunglasses}")
        game_direction = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if game_direction == 'y':
            clear()
            your_side_game()
        else:
            return
        return
    elif (computer_item1 == 10 and computer_item2 == 11) or (computer_item1 == 11 and computer_item2 == 10):
        print(f"    Your final hand: {your_cards}, final score: {your_current_score}")
        print(f"    Computer's final hand: {computer_cards}, final score: 0")
        print("Lose, opponent has a Blackjack \N{face with open mouth}")
        game_direction = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
        if game_direction == 'y':
            clear()
            your_side_game()
        else:
            return
        return

    your_score_flag = True
    your_card_flag = True
    computer_score_flag = True
    computer_card_flag = True

    while (your_score_flag and your_card_flag) and (computer_score_flag and computer_card_flag):
        if your_current_score <= 21:
            more_cards = input(f"Type 'y' to get another card, type 'n' to pass: ")
            if more_cards == "y":
                item = random.choice(cards)
                your_cards.append(item)
                for your_card in your_cards:
                    if your_card == 11:
                        your_current_score = add(your_cards)
                        if your_current_score > 21:
                            Ace_1 = your_current_score - 11
                            your_current_score = Ace_1 + 1
                            index_11 = your_cards.index(your_card)
                            your_cards[index_11] = 1                          
                    else:
                        your_current_score = add(your_cards)

                print(f"    Your cards: {your_cards}, current score: {your_current_score}")
                print(f"    Computer's first card: {computer_cards[0]}")
            else:
                your_card_flag = False
                print(f"    Your final hand: {your_cards}, final score: {your_current_score}")
        else:
            your_score_flag = False
            print(f"    Your final hand: {your_cards}, final score: {your_current_score}")

    
    while computer_score_flag and computer_card_flag:
        if computer_current_score <= 21:
            computer_choice = random.choice(add_more_cards_computer) 
            if computer_choice == True:
                item = random.choice(cards)
                computer_cards.append(item)
                for computer_card in computer_cards:
                    if computer_card == 11:
                        computer_scores = add(computer_cards)
                        computer_current_score = computer_scores
                        if computer_current_score > 21:
                            Ace_1 = computer_current_score - 11
                            computer_current_score = Ace_1 + 1
                            index_11 = computer_cards.index(computer_card)
                            computer_cards[index_11] = 1                          
                    else:
                        computer_scores = add(computer_cards)
                        computer_current_score = computer_scores

            else:
                computer_card_flag = False
        else:
            computer_score_flag = False
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_current_score}")


    if your_current_score == computer_current_score:
        print("Draw \N{upside-down face}")
    elif 21 >= computer_current_score > your_current_score:
        print("You Loose \N{loudly crying face}")
    elif 21 >= your_current_score > computer_current_score:
        print("You win \N{grinning face with smiling eyes}")
    elif your_current_score > computer_current_score >= 21:
        print("You went over. You loose \N{loudly crying face}")
    elif computer_current_score > your_current_score >= 21:
        print("Opponent went over. You win \N{grinning face with smiling eyes}")
    elif your_current_score > 21 >= computer_current_score:
        print("You went over. You loose \N{loudly crying face}")
    elif computer_current_score > 21 >= your_current_score:
        print("Opponent went over. You win \N{grinning face with smiling eyes}")

    game_direction = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if game_direction == 'y':
        clear()
        your_side_game()
    else:
        return

if game_direction == 'y':
    clear()
    your_side_game()
