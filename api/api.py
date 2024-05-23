import requests
from config_data.config import RAPID_API_KEY

url = "https://imdb-top-100-movies.p.rapidapi.com/"

headers = {
    "X-RapidAPI-Key": RAPID_API_KEY,
    "X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

movies_list = response.json()
# print(len(movies_list))
