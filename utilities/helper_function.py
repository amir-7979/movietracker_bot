import utilities.variables

import utilities.classes
from api_requests.movie_request import get_news, get_updates, get_tops_by_likes, get_top_movies, get_top_series, \
    get_coming_soon, get_in_theaters, get_box_office, get_anime_top_airing, get_anime_top_comingSoon, get_popular, \
    get_search


def get_keyboard_button(enum):
    if enum == utilities.classes.State.main:
        return utilities.variables.start_buttons
    elif enum == utilities.classes.State.news:
        return utilities.variables.news_button
    elif enum == utilities.classes.State.search:
        return utilities.variables.search_button


def click_keyboard_button(searching, new_state):
    utilities.variables.is_searching = searching
    utilities.variables.state = new_state
    return get_keyboard_button(utilities.variables.state)


def func_list(i: int):
    if i == 0:
        return get_news(utilities.variables.page.page_number)
    elif i == 1:
        return get_updates(utilities.variables.page.page_number)
    elif i == 2:
        return get_tops_by_likes(utilities.variables.page.page_number)
    elif i == 3:
        return get_top_movies(utilities.variables.page.page_number)
    elif i == 4:
        return get_top_series(utilities.variables.page.page_number)
    elif i == 5:
        return get_coming_soon(utilities.variables.page.page_number)
    elif i == 6:
        return get_in_theaters(utilities.variables.page.page_number)
    elif i == 7:
        return get_box_office(utilities.variables.page.page_number)
    elif i == 8:
        return get_anime_top_airing(utilities.variables.page.page_number)
    elif i == 9:
        return get_anime_top_comingSoon(utilities.variables.page.page_number)
    elif i == 10:
        return get_popular(utilities.variables.page.page_number)
    elif i == 11:
        return get_search(utilities.variables.page.search_name, utilities.variables.page.page_number)
