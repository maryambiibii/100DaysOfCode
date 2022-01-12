#Day-3-1: Odd or Even/Modulo
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if number % 2 == 0:
  print("This is an even number.")
else:
  print("This is an odd number.")
  
#Day-3-2: BMI 2.0
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
BMI = round(weight / height ** 2)

if BMI < 18.5:
  print(f"Your BMI is {BMI}, you are underweight.")
elif BMI < 25:
  print(f"Your BMI is {BMI}, you have a normal weight.")
elif BMI < 30:
  print(f"Your BMI is {BMI}, you are slightly overweight.")
elif BMI < 35:
  print(f"Your BMI is {BMI}, you are obese.")
else:
  print(f"Your BMI is {BMI}, you are clinically obese.")
  
#Day-3-3: Leap Year
# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if year % 4 == 0:
  if year % 100 == 0:
    if year % 400 == 0:
      print("Leap year.")
    else:
      print("Not leap year.")
  else:
      print("Leap year.")
else:
  print("Not leap year.")
  
#Day-3-4: Pizza order Pratice
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0

#Tell size of the pizzza you want
if size == "S":
  bill = 15 

elif size == "M":
  bill = 20

else:
  bill = 25

#Do you wnat to add pepperoni
if add_pepperoni == "Y":
  if size == "S":
    bill += 2
  else:
    bill += 3

#Do you want to dd extra cheese
if extra_cheese == "Y":
  bill += 1

print(f"Your final bill is: ${bill}.")

#Day-3-5: Love Calculator
# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combined_string = name1 + name2
lower_case_string = combined_string.lower()

#Total true score
T = lower_case_string.count('t')
R = lower_case_string.count('r')
U = lower_case_string.count('u')
E = lower_case_string.count('e')

Total_True = T + R + U + E

#Total love score
L = lower_case_string.count('l')
O = lower_case_string.count('o')
V = lower_case_string.count('v')
LE = lower_case_string.count('e')

Total_Love = L + O + V + LE

love_score_combine = f"{Total_True}{Total_Love}"
love_score = int(love_score_combine)

if love_score < 10 or love_score >90:
  print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >40 and love_score < 50:
  print(f"Your score is {love_score}, you are alright together.")
else:
  print(f"Your score is {love_score}.")
