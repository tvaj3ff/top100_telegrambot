import requests
from config_data.config import RAPID_API_KEY


def get_movies_list(api_key):
    url = "https://imdb-top-100-movies.p.rapidapi.com/"

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return response.status_code


def get_series_list(api_key):
    url = "https://imdb-top-100-movies.p.rapidapi.com/series/"

    headers = {
        "X-RapidAPI-Key": api_key,
        "X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    return response.status_code


movies_list = get_movies_list(RAPID_API_KEY)
series_list = get_series_list(RAPID_API_KEY)
