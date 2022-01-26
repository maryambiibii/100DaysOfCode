#Number Guessing Game Objectives:
import random
#1. Import ASCII logo
from art import logo
print(logo)

#2. Welcome Title and Guessing from 1 to 100
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

#3. Random number to guess
def answer():
    number_to_guess = random.randint(2,100)
    return number_to_guess

#4. Choose a difficulty level
def level():
    choosed_level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    #5. Show the number of attempts based on choosed difficulty level
    number_of_attempts = 0
    if choosed_level == "easy":
        number_of_attempts = 10
    else:
        number_of_attempts = 5
    return number_of_attempts

def game():
    answer_to_guess = answer()
    game_level = level()
    for _ in range(game_level):
        print(f"You have {game_level} attempts remaining to guess the number.")
        #6. Make a guess
        number_guessed = int(input("Make a guess: "))
        #  If number greater than actual number: Too High
        if number_guessed > answer_to_guess:
            print("Too High")
            print("Guess again.")
        #  If number less than actual number: Too low
        elif number_guessed < answer_to_guess:
            print("Too low")
            print("Guess again.")
        #  If number guessed right: You got it! The answer was 74.
        elif number_guessed == answer_to_guess:
            print(f"You got it! The answer was {answer_to_guess}.")
            break
        #  If out of attempts without guessing right number: You've run out of guesses, 
        game_level -= 1
        if game_level == 0:
            print("You've run out of guesses, you lose.")

game()
        
