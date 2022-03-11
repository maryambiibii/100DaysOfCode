import requests
import os
from datetime import datetime

APP_ID = os.getenv('APP_ID')
API_KEY = os.getenv('API_KEY')
SHEETY_ENDPOINT = os.getenv('SHEETY_ENDPOINT')
BEARER_TOKEN = os.getenv('BEARER_TOKEN')


GENDER = 'your_gender'
WEIGHT_KG = your_weight
HEIGHT_CM = your_height
AGE = your_age

EXERCISE_ENDPOINT = 'https://trackapi.nutritionix.com/v2/natural/exercise'

headers = {
    'x-app-id': APP_ID,
    'x-app-key': API_KEY
}

params = {
    'query': input("Tell me which exercise you did: "),
    'gender': GENDER,
    'weight_kg': WEIGHT_KG,
    'height_cm': HEIGHT_CM,
    'age': AGE
}
response = requests.post(url=EXERCISE_ENDPOINT, json=params, headers=headers)
result = response.json()

################### Start of Step 4 Solution ######################
user_exercises = result['exercises']
print(user_exercises)

for exercise in user_exercises:
    today = datetime.now()
    date = today.strftime("%d/%m/%Y")
    time = today.strftime("%H:%M:%S")
    exercise_by_user = exercise["user_input"]
    exercise_minutes = exercise["duration_min"]
    exercise_calories = exercise["nf_calories"]

    data = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise_by_user.title(),
            "duration": exercise_minutes,
            "calories": exercise_calories,
        }
    }

    headers = {
        "Authorization": BEARER_TOKEN
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=data, headers=headers)
    print(response.text)
