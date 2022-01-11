#Day-2-1: Data Types
# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

digit1 = int(two_digit_number[0])
digit2 = int(two_digit_number[1])

sum = digit1 + digit2
print(two_digit_number[0] + " + " + two_digit_number[1] + " = " + str(sum))

#Day-2-2: BMI Calculator
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

height_as_float = float(height)
weight_as_int = int(weight)

BMI = weight_as_int / height_as_float ** 2
print(int(BMI))

#Day-2-3:Life in Weeks
# 🚨 Don't change the code below 👇
age = input("What is your current age?")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
age_as_int = int(age)

years_remaining = 90 - age_as_int
#your days left if you live 90 years 
days_left = years_remaining * 365
#print(days_left)

#your weeks left if you live 90 years 
weeks_left = years_remaining * 52
#print(weeks_left)

#your months left if you live 90 years 
months_left  = years_remaining * 12
#print(months_left)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left.")
