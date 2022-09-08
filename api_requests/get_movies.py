import requests
from model.low_data_movie import LowDataItem


async def get_news(i: int) -> list[LowDataItem]:
    response = requests.get(
        f'https://downloader-node-api.herokuapp.com/movies/news/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true')
    return [LowDataItem.from_dict(y) for y in response.json()['data']]


async def get_coming_soon(i: int) -> list[LowDataItem]:
    response = requests.get(
        f'https://downloader-node-api.herokuapp.com/movies/sortedMovies/comingSoon/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true')
    return [LowDataItem.from_dict(y) for y in response.json()['data']]


async def get_in_theaters(i: int) -> list[LowDataItem]:
    response = requests.get(
        f'https://downloader-node-api.herokuapp.com/movies/sortedMovies/inTheaters/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true')
    return [LowDataItem.from_dict(y) for y in response.json()['data']]


async def get_box_office(i: int) -> list[LowDataItem]:
    response = requests.get(
        f'https://downloader-node-api.herokuapp.com/movies/sortedMovies/boxOffice/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true')
    return [LowDataItem.from_dict(y) for y in response.json()['data']]


async def get_anime_top_airing(i: int) -> list[LowDataItem]:
    response = requests.get(
        f'https://downloader-node-api.herokuapp.com/movies/sortedMovies/animeTopAiring/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true')
    return [LowDataItem.from_dict(y) for y in response.json()['data']]



async def get_anime_top_comingSoon(i: int) -> list[LowDataItem]:
    response = requests.get(
        f'https://downloader-node-api.herokuapp.com/movies/sortedMovies/animeTopComingSoon/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true')
    return [LowDataItem.from_dict(y) for y in response.json()['data']]


async def get_popular(i: int) -> list[LowDataItem]:
    response = requests.get(
        f'https://downloader-node-api.herokuapp.com/movies/sortedMovies/popular/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true')
    return [LowDataItem.from_dict(y) for y in response.json()['data']]


async def get_updates(i: int) -> list[LowDataItem]:
    response = requests.get(
        f'https://downloader-node-api.herokuapp.com/movies/updates/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}'
        '?testUser=true')
    return [LowDataItem.from_dict(y) for y in response.json()['data']]


async def get_tops_by_likes(i: int) -> list[LowDataItem]:
    response = requests.get(
        f'https://downloader-node-api.herokuapp.com/movies/topsByLikes/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}'
        '?testUser=true')
    return [LowDataItem.from_dict(y) for y in response.json()['data']]


async def get_top_movies(i: int) -> list[LowDataItem]:
    response = requests.get(
        f'https://downloader-node-api.herokuapp.com/movies/sortedMovies/top/movie/telbot/0-10/0-10/{i}'
        '?testUser=true')
    return [LowDataItem.from_dict(y) for y in response.json()['data']]


async def get_top_series(i: int) -> list[LowDataItem]:
    response = requests.get(
        f'https://downloader-node-api.herokuapp.com/movies/sortedMovies/top/serial/telbot/0-10/0-10/{i}'
        '?testUser=true')
    return [LowDataItem.from_dict(y) for y in response.json()['data']]


async def get_series_of_day(i: int) -> list[LowDataItem]:
    response = requests.get(
        f'https://downloader-node-api.herokuapp.com/movies/seriesOfDay/0/movie-serial-anime_movie-anime_serial/telbot'
        f'/0-10/0-10/{i} '
        '?testUser=true')
    return [LowDataItem.from_dict(y) for y in response.json()['data']]


async def get_search(text, i: int) -> list[LowDataItem]:
    response = requests.get(
        f'https://downloader-node-api.herokuapp.com/movies/searchMovie/telbot/{i}?title={text}&testUser=true')
    return [LowDataItem.from_dict(y) for y in response.json()['data']]


async def get_movie(title: str, types: str, imdb_scores: str, years: str) -> LowDataItem:
    params = {'title': title, 'years': '1900-'+years, 'types': types, 'imdbScores': '0-'+imdb_scores, 'testUser': 'true'}
    response = requests.get(
        f'https://downloader-node-api.herokuapp.com/movies/searchMovie/telbot/1', params=params)
    return LowDataItem.from_dict(response.json()['data'][0])
