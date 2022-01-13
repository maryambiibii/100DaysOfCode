#Rock Paper Scissors
import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
#User chose

game_images = [rock, paper, scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice == 0:
  print(rock)
elif user_choice == 1:
  print(paper)
elif user_choice == 2:
  print(scissors)

#Computer chose
print("Computer Chose:")
computer_choice = random.randint(0 , 2)
if computer_choice == 0:
  print(rock)
elif computer_choice == 1:
  print(paper)
elif computer_choice == 2:
  print(scissors)

#Rock, Paper, Scissor Game Rule
#Rock wins against scissors.
#Scissors win against paper.
#Paper wins against rock.
if user_choice == 0 and computer_choice == 2:
  print("you Win")
elif user_choice == 2 and computer_choice == 1:
  print("you Win")
elif user_choice == 1 and computer_choice == 0:
  print("You win")
elif computer_choice == 0 and user_choice == 2:
  print("you lose")
elif computer_choice == 2 and user_choice == 1:
  print("you lose")
elif computer_choice == 1 and user_choice == 0:
  print("You lose")
elif computer_choice == user_choice:
  print("Draw")
else:
  print("You typed an invalid number. You lose.")
  
#Output:
#What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.
#2

#    _______
#---'   ____)____
#          ______)
#       __________)
#      (____)
#---.__(___)

#Computer Chose:

#    _______
#---'   ____)
#      (_____)
#      (_____)
#      (____)
#---.__(___)

#you lose

