import datetime

import requests
from requests_cache import CachedSession
from model.dlink_model import DLinkItem
from model.telbot_model import TelBotItem
import utilities

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



def api_handler(url):
    response = session.get(url)
    return [TelBotItem.from_dict(y) for y in response.json()['data']]


async def get_news(i: int) -> list[TelBotItem]:
    return api_handler(
        f'{utilities.variables.server_address}/movies/news/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true', )


async def get_coming_soon(i: int) -> list[TelBotItem]:
    return api_handler(
        f'{utilities.variables.server_address}/movies/sortedMovies/comingSoon/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true',
    )


async def get_in_theaters(i: int) -> list[TelBotItem]:
    return api_handler(
        f'{utilities.variables.server_address}/movies/sortedMovies/inTheaters/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true',
    )


async def get_box_office(i: int) -> list[TelBotItem]:
    return api_handler(
        f'{utilities.variables.server_address}/movies/sortedMovies/boxOffice/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true',
    )


async def get_anime_top_airing(i: int) -> list[TelBotItem]:
    return api_handler(
        f'{utilities.variables.server_address}/movies/sortedMovies/animeTopAiring/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true',
    )


async def get_anime_top_comingSoon(i: int) -> list[TelBotItem]:
    return api_handler(
        f'{utilities.variables.server_address}/movies/sortedMovies/animeTopComingSoon/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true',
    )


async def get_popular(i: int) -> list[TelBotItem]:
    return api_handler(
        f'{utilities.variables.server_address}/movies/sortedMovies/popular/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}?testUser=true',
    )


async def get_updates(i: int) -> list[TelBotItem]:
    return api_handler(
        f'{utilities.variables.server_address}/movies/updates/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}'
        '?testUser=true')


async def get_tops_by_likes(i: int) -> list[TelBotItem]:
    return api_handler(
        f'{utilities.variables.server_address}/movies/topsByLikes/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10/{i}'
        '?testUser=true')


async def get_top_movies(i: int) -> list[TelBotItem]:
    return api_handler(
        f'{utilities.variables.server_address}/movies/sortedMovies/top/movie/telbot/0-10/0-10/{i}'
        '?testUser=true')


async def get_top_series(i: int) -> list[TelBotItem]:
    return api_handler(
        f'{utilities.variables.server_address}/movies/sortedMovies/top/serial/telbot/0-10/0-10/{i}'
        '?testUser=true')


async def get_search(text, i: int) -> list[TelBotItem]:
    return api_handler(
        f'{utilities.variables.server_address}/movies/searchMovie/telbot/{i}?title={text}&testUser=true')


async def get_search_by_id(item_id) -> TelBotItem:
    response = session.get(
        f'{utilities.variables.server_address}/movies/searchByID/{item_id}/telbot?testUser=true')
    return TelBotItem.from_dict(response.json()['data'])


async def get_movie(title: str, types: str, imdb_scores: str, years: str) -> TelBotItem:
    imdb_scores = imdb_scores.replace(' |', '')
    params = {'title': title, 'types': types, 'imdbScores': '0-' + imdb_scores,
              'testUser': 'true'}
    if len(years) != 0:
        params['years'] = '1900-' + years
    response = session.get(
        f'{utilities.variables.server_address}/movies/searchMovie/telbot/1', params=params)
    return TelBotItem.from_dict(response.json()['data'][0])


async def get_movie_download_links(movie_id: str) -> DLinkItem:
    response = session.get(
        f'{utilities.variables.server_address}/movies/searchByID/{movie_id}/dlink?testUser=true')
    return DLinkItem.from_dict(response.json()['data'])


async def get_serial_links(movie_id: str, season, episode) -> DLinkItem:
    params = {'seasons': season, 'episodes': episode, 'testUser': 'true'}
    response = session.get(
        f'{utilities.variables.server_address}/movies/searchByID/{movie_id}/dlink?', params=params)
    return DLinkItem.from_dict(response.json()['data'])


async def get_data_for_channel(bot_id):
    response = requests.get(
        f'{utilities.variables.server_address}/movies/bots/{bot_id}/newsAndUpdates/movie-serial-anime_movie-anime_serial/telbot/0-10/0-10')
    return [TelBotItem.from_dict(y) for y in response.json()['data']]
