from utilities.consts import *
from api_requests.movie_request import *


def get_keyboard_button(enum):
    if enum == State.main:
        return start_buttons
    elif enum == State.news:
        return news_button
    elif enum == State.search:
        return search_button


def click_keyboard_button(searching, new_state):
    state = new_state
    is_searching = searching
    return get_keyboard_button(state)


def func_list(i: int):
    if i == 0:
        return get_news(page.page_number)
    elif i == 1:
        return get_updates(page.page_number)
    elif i == 2:
        return get_tops_by_likes(page.page_number)
    elif i == 3:
        return get_top_movies(page.page_number)
    elif i == 4:
        return get_top_series(page.page_number)
    elif i == 5:
        return get_coming_soon(page.page_number)
    elif i == 6:
        return get_in_theaters(page.page_number)
    elif i == 7:
        return get_box_office(page.page_number)
    elif i == 8:
        return get_anime_top_airing(page.page_number)
    elif i == 9:
        return get_anime_top_comingSoon(page.page_number)
    elif i == 10:
        return get_popular(page.page_number)
    elif i == 11:
        return get_search(page.search_name, page.page_number)
