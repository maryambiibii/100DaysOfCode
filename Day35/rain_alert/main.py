import requests
import os
from twilio.rest import Client


OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "your_api_key"
account_sid = 'your_twilio account_sid'
auth_token = 'your_api_auth_token'

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
        from_='twilio_number_generated',
        to='your_number'
    )

    print(message.status)
