#Day-4-1: Heads or Tails
#Write your code below this line 👇
#Hint: Remember to import the random module first. 🎲
import random

heads_tails = random.randint(0,1)
print(heads_tails)

if heads_tails == 1:
  print("Heads")
else:
  print("Tails")


#Day-4-2: Banker Roulette - Who will pay the bill?
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
#Get the length of the list
list_len = len(names)

#Generate the random index number
randam_name_index  = random.randint(0, list_len-1)
name_for_bill = names[randam_name_index]

#Print
print(f"{name_for_bill} is going to buy the meal today!")

#Day-4-3: Treasure Map
# 🚨 Don't change the code below 👇
row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
col = int(position[0])
row = int(position[1])

map[row-1][col-1] = 'X'

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")

