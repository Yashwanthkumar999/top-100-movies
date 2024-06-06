import requests
import _markupbase
import html
from bs4 import BeautifulSoup
import prettify
URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"


response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
heading = soup.find_all(name="h3", class_="title")
movie_titles = [movie.getText() for movie in heading]
movies = movie_titles[::-1]

print(movies)
with open("movies.txt", mode="w") as file:
    for movie in movies:
        movie1 = html.unescape(f"{movie}")
        print(movie1)
        file.write(f"{movie1}\n")







