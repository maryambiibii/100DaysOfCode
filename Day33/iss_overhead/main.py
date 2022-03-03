from datetime import datetime
import requests
import smtplib
import time

MY_EMAIL = "emailsender618@gmail.com"
PASSWORD = "Pass123word"

MY_LAT = 33.684422
MY_LONG = 73.047882

my_position = (MY_LONG, MY_LAT)
print("My Position: ", my_position)


def is_iss_overhead():
    # ISS position
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()
    longitude = float(data["iss_position"]["longitude"])
    latitude = float(data["iss_position"]["latitude"])
    iss_position = (longitude, latitude)
    print("ISS Position: ", iss_position)

    # Your position is within +5 or -5 degrees of the ISS position
    # Latitude
    start_latitude = latitude - 5
    end_latitude = latitude + 5
    latitude_range = (start_latitude, end_latitude + 1)

    # longitude
    start_longitude = longitude - 5
    end_longitude = longitude + 5
    longitude_range = (start_longitude, end_longitude + 1)
    if MY_LAT in latitude_range and MY_LONG in longitude_range:
        return True


def is_dark():
    # Sunrise and sunset time at my position
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0
    }
    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    print("Sunrise at my position: ", sunrise)
    print("Sunset at my position: ", sunset)

    # Time now
    time_now = datetime.now()
    current_hour = time_now.hour
    print("Current Hour: ", current_hour)

    if (current_hour >= sunset) or (current_hour < sunrise):
        return True


start_time = time.time()
while True:
    time.sleep(60)
    if is_iss_overhead() == True and is_dark() == True:
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=MY_EMAIL,
                                msg=f"Subject:Look Up!\n\nISS is close to your position."
                                )
