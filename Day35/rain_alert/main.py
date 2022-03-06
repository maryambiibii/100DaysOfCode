import requests
import os
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "eb154405fd86906197525d8e04846257"
account_sid = 'ACbebce805eaf06d5c909a37025f934dc4'
auth_token = '33a8330393810b482182db819e2701b1'

parameters = {
    "lat": 33.765968,
    "lon": 72.360878,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(OWM_Endpoint, params=parameters)
weather_data = response.json()

hourly_weather = weather_data["hourly"]
twelve_hours = hourly_weather[:12]

will_rain = False
for hour in twelve_hours:
    hour_weather = hour["weather"]
    hour_weather_id = hour_weather[0]["id"]
    if hour_weather_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️.",
        from_='+12407166391',
        to='+923329784005'
    )

    print(message.status)
