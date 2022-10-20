import datetime

from requests_cache import CachedSession

import utilities.variables
from model.dlink_model import DLinkItem
from model.telbot_model import TelBotItem

session = CachedSession(
    'demo_cache',
    use_cache_dir=True,  # Save files in the default user cache dir
    cache_control=True,  # Use Cache-Control headers for expiration, if available
    expire_after=datetime.timedelta(minutes=5),  # Otherwise expire responses after one day
    allowable_methods=['GET', 'POST'],  # Cache POST session to avoid sending the same data twice
    allowable_codes=[200, 400],  # Cache 400 responses as a solemn reminder of your failures
    ignored_parameters=['api_key'],  # Don't match this param or save it in the cache
    match_headers=True,  # Match all request headers
    stale_if_error=True,  # In case of request errors, use stale cache data if possible
)


async def get_news(user_id: int, i: int) -> list[TelBotItem]:
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/news/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true')
    utilities.variables.movie_db.insert_db((user_id, i))
    print('news', (user_id, i))

    return [TelBotItem.from_dict(y) for y in response.json()['data']]


async def get_coming_soon(user_id: int, i: int) -> list[TelBotItem]:
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/sortedMovies/comingSoon/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true')
    utilities.variables.movie_db.insert_db((user_id, i))
    return [TelBotItem.from_dict(y) for y in response.json()['data']]


async def get_in_theaters(user_id: int, i: int) -> list[TelBotItem]:
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/sortedMovies/inTheaters/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true')
    utilities.variables.movie_db.insert_db((user_id, i))
    return [TelBotItem.from_dict(y) for y in response.json()['data']]


async def get_box_office(user_id: int, i: int) -> list[TelBotItem]:
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/sortedMovies/boxOffice/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true')
    utilities.variables.movie_db.insert_db((user_id, i))
    return [TelBotItem.from_dict(y) for y in response.json()['data']]


async def get_anime_top_airing(user_id: int, i: int) -> list[TelBotItem]:
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/sortedMovies/animeTopAiring/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true')
    utilities.variables.movie_db.insert_db((user_id, i))
    return [TelBotItem.from_dict(y) for y in response.json()['data']]


async def get_anime_top_comingSoon(user_id: int, i: int) -> list[TelBotItem]:
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/sortedMovies/animeTopComingSoon/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true')
    utilities.variables.movie_db.insert_db((user_id, i))
    return [TelBotItem.from_dict(y) for y in response.json()['data']]


async def get_popular(user_id: int, i: int) -> list[TelBotItem]:
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/sortedMovies/popular/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true')
    utilities.variables.movie_db.insert_db((user_id, i))
    return [TelBotItem.from_dict(y) for y in response.json()['data']]


async def get_updates(user_id: int, i: int) -> list[TelBotItem]:
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/updates/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}'
        '?testUser=true')
    utilities.variables.movie_db.insert_db((user_id, i))
    return [TelBotItem.from_dict(y) for y in response.json()['data']]


async def get_tops_by_likes(user_id: int, i: int) -> list[TelBotItem]:
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/topsByLikes/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}'
        '?testUser=true')
    utilities.variables.movie_db.insert_db((user_id, i))
    return [TelBotItem.from_dict(y) for y in response.json()['data']]


async def get_top_movies(user_id: int, i: int) -> list[TelBotItem]:
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/sortedMovies/top/movie/telbot/0-10/0-10/{i}'
        '?testUser=true')

    utilities.variables.movie_db.insert_db((user_id, i))
    return [TelBotItem.from_dict(y) for y in response.json()['data']]


async def get_top_series(user_id: int, i: int) -> list[TelBotItem]:
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/sortedMovies/top/serial/telbot/0-10/0-10/{i}'
        '?testUser=true')
    utilities.variables.movie_db.insert_db((user_id, i))
    return [TelBotItem.from_dict(y) for y in response.json()['data']]

async def get_search(text, user_id: int, i: int) -> list[TelBotItem]:
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/searchMovie/telbot/{i}?title={text}&testUser=true')
    utilities.variables.movie_db.insert_db((user_id, i))
    return [TelBotItem.from_dict(y) for y in response.json()['data']]


async def get_search_by_id(item_id) -> TelBotItem:
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/searchByID/{item_id}/telbot?testUser=true')
    return TelBotItem.from_dict(response.json()['data'])


async def get_movie(title: str, types: str, imdb_scores: str, years: str) -> TelBotItem:
    params = {'title': title, 'years': '1900-' + years, 'types': types, 'imdbScores': '0-' + imdb_scores,
              'testUser': 'true'}
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/searchMovie/telbot/1', params=params)
    return TelBotItem.from_dict(response.json()['data'][0])


async def get_news_with_date(i: int) -> list[TelBotItem]:
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/newsWithDate/{datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")}/movie-serial-anime_serial-anime_movie/telbot/0-10/0-10/{i}?testUser=true')
    print(response)
    print(response.url)
    return [TelBotItem.from_dict(y) for y in response.json()['data']]


async def get_updates_with_date(i: int) -> list[TelBotItem]:
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/updatesWithDate/{datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%SZ")}/movie-serial-anime_serial-anime_movie/telbot/0-10/0-10/{i}?testUser=true')
    print(response)
    print(response.url)
    return [TelBotItem.from_dict(y) for y in response.json()['data']]


async def get_movie_download_links(movie_id: str) -> DLinkItem:
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/searchByID/{movie_id}/dlink?testUser=true')
    return DLinkItem.from_dict(response.json()['data'])


async def get_serial_links(movie_id: str, season, episode) -> DLinkItem:
    params = {'seasons': season, 'episodes': episode, 'testUser': 'true'}
    response = session.get(
        f'https://downloader-node-api.herokuapp.com/movies/searchByID/{movie_id}/dlink?', params=params)
    return DLinkItem.from_dict(response.json()['data'])
