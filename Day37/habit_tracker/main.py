import requests
from datetime import datetime

USER_NAME = "your_user_name"
TOKEN = "your_private_token"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

# POST request
user_params = {
    "token": TOKEN,
    "username": USER_NAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

#response = requests.post(url= pixela_endpoint, json=user_params)
#print(response.text)

# POST request
graph_endpoint = f"{pixela_endpoint}/{USER_NAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "sora",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
#print(response.text)

# POST request
post_pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()

pixel_value = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometers you have cycle today? "),
}
response = requests.post(url=post_pixel_endpoint, json=pixel_value, headers=headers)
print(response.text)

# PUT request
yesterday = datetime(year=2022, month=3, day=9)
yesterday = yesterday.strftime("%Y%m%d")

update_pixel_endpoint = f"{post_pixel_endpoint}/{yesterday}"

update_pixel_value = {
    "quantity": "15",
}
#response = requests.put(url=update_pixel_endpoint, json=update_pixel_value, headers=headers)
#print(response.text)

# DELETE request
delete_endpoint = f"{post_pixel_endpoint}/{yesterday}"
#response = requests.delete(url=delete_endpoint, headers=headers)
#print(response.text)
