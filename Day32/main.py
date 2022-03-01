##################### Extra Hard Starting Project ######################
import datetime as dt
import pandas
import random
import smtplib
import os

MY_EMAIL = "emailsender618@gmail.com"
PASSWORD = "Pass123word"
#PASSWORD = "oearamruvzclkvnb"

# 1. Update the birthdays.csv
# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_month = now.month
current_day = now.day

pd = pandas.read_csv("birthdays.csv")
pd = pd.to_dict(orient="records")

for birthday in pd:
    if birthday["month"] == current_month and birthday["day"] == current_day:
        # 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's
        # actual name from birthdays.csv
        letters = [f for f in os.listdir('./letter_templates/')]
        random_letters = random.choice(letters)
        print(random_letters)

        with open("letter_templates/"+random_letters) as letter_file:
            contents = letter_file.read()
            contents = contents.replace("[NAME]", birthday["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="emailsender618@gmail.com",
                                msg=f"Subject:Happy Birthday\n\n{contents}."
                                )
