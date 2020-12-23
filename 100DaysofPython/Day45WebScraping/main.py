from bs4 import BeautifulSoup
import requests

response = requests.get(
    "https://www.empireonline.com/movies/features/best-movies-2/").text
stew = BeautifulSoup(response, "html.parser")

movie_title = [title.getText().split(") ")[-1]
               for title in stew.find_all(name="h3", class_="title")]
movie_rank = [(101 - int(rank.getText().split()[0]))
              for rank in stew.find_all(class_="static-image__primary-total")]
movie_title.reverse()
movie_rank.reverse()
movie_list = []
for index, item in enumerate(movie_rank):
    movie = {
        'Rank': item,
        'Title': movie_title[index],
        'Watched': False
    }
    movie_list.append(movie)

with open("movies.csv", mode="w") as file:
    file.write(f"Rank,Title,Watched\n")
    for movie in movie_list:
        file.write(f"{movie['Rank']},{movie['Title']},{movie['Watched']}\n")
