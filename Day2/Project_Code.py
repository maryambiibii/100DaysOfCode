#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
print("Welcome to the tip calculator!")
total_bill = input("What was the total bill? $")
tip_percentage = input("How much tip would you like to give? 10, 12, or 15? ")
number_of_people = input("How many people to split the bill? ")

tip_to_bill = (float(tip_percentage) / 100) * float(total_bill)
total_bill_after_tip = tip_to_bill + float(total_bill)

final_amount = round(total_bill_after_tip / float(number_of_people),2)
each_person_payment = "{:.2f}".format(final_amount)

amount = f"Each person should pay: ${each_person_payment}"
print(amount)

#Welcome to the tip calculator!
#What was the total bill? $150
#How much tip would you like to give? 10, 12, or 15? 12
#How many people to split the bill? 5
#Each person should pay: $33.60
