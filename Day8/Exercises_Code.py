#Day-8-1: Paint Area Calculator
import math
#Write your code below this line 👇
def paint_calc(height, width, cover):
    number_of_cans = math.ceil((height * width) / cover)
    print(f"You'll need {number_of_cans} cans of paint.")



#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

##Day-8-2: Prime Number Checker
# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)


#Write your code below this line 👇
def prime_checker(number):
    list_of_record = []
    for divider in range(2 , number):
        if number % divider == 0:
            list_of_record.append(0)
        else:
            list_of_record.append(1)

    if 0 in list_of_record:
        print("It's not a prime number.")
    else:
        print("It's a prime number.")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)
