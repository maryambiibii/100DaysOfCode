import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

response = requests.get(URL)
Empire_text = response.text

soup = BeautifulSoup(Empire_text, "html.parser")

movies_title = soup.findAll(name="h3", class_="title")
movies_list = [movie.getText() for movie in movies_title]
movies_list.reverse()

with open("movies.txt", mode="w") as file:
    for movie in movies_list:
        file.write(movie+'\n')

