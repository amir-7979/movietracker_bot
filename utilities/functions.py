import asyncio
import re
import threading

from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.types import InputChannel, ChannelParticipantsRecent
from telethon.tl.types.channels import ChannelParticipants

import utilities.classes
import utilities.variables
from api_requests.movie_request import *
from model.movie_db import MovieDb
from view_model.view_model import show_low_data_item, show_search_data_item, get_movie_link, get_serial_seasons, \
    get_serial_episode, get_serial_link, show_low_data_updates_with_date


def get_keyboard_button(enum):
    if enum == utilities.classes.State.main:
        return utilities.variables.start_buttons
    elif enum == utilities.classes.State.news:
        return utilities.variables.news_button
    elif enum == utilities.classes.State.search:
        return utilities.variables.search_button
    elif enum == utilities.classes.State.searching:
        return utilities.variables.search_button[1]


def click_keyboard_button(searching, new_state):
    utilities.variables.is_searching = searching
    utilities.variables.state = new_state
    return get_keyboard_button(utilities.variables.state)


def func_list(i: int, user_id: int):
    page_number = utilities.variables.movie_db.get_page_db((user_id,))
    if i == 0:
        return get_news(user_id, page_number)
    elif i == 1:
        return get_updates(user_id, page_number)
    elif i == 2:
        return get_tops_by_likes(user_id, page_number)
    elif i == 3:
        return get_top_movies(user_id, page_number)
    elif i == 4:
        return get_top_series(user_id, page_number)
    elif i == 5:
        return get_coming_soon(user_id, page_number)
    elif i == 6:
        return get_in_theaters(user_id, page_number)
    elif i == 7:
        return get_box_office(user_id, page_number)
    elif i == 8:
        return get_anime_top_airing(user_id, page_number)
    elif i == 9:
        return get_anime_top_comingSoon(user_id, page_number)
    elif i == 10:
        return get_popular(user_id, page_number)
    elif i == 11:
        return get_search(utilities.variables.page.search_name, user_id, page_number)


async def check_user_sub(client, chat_id, event, first_use) -> bool:
    channel = await client.get_entity('t.me/movie_tracker1')
    result: ChannelParticipants = await client(
        GetParticipantsRequest(InputChannel(channel.id, channel.access_hash), filter=ChannelParticipantsRecent(),
                               limit=1000000, offset=0, hash=0))
    sender = event.original_update.message.peer_id.user_id
    subscribers = (o.user_id for o in result.participants)
    if sender in subscribers:
        if first_use:
            await client.send_message(chat_id, 'Welcome to MovieTracker bot',
                                      buttons=click_keyboard_button(False, utilities.classes.State.main))
        return True
    else:
        await client.send_message(chat_id, 'Hi!\nPlease join our channel to use bot',
                                  buttons=utilities.variables.channel_button)
        return False


def get_option_index(text):
    try:
        index = utilities.variables.option.index(text)
        return index
    except:
        return -1


async def find_method_name_in_list(bot, chat, user_id, message_text):
    index = get_option_index(message_text)
    if index == -1:
        return False
    utilities.variables.function_number = index
    response = await func_list(index, user_id)
    await show_low_data_item(bot, chat, response,
                             click_keyboard_button(False, utilities.classes.State.news))
    return True


async def find_method(bot, chat, message_text, user_id):
    if not await find_method_name_in_list(bot, chat, user_id, message_text):
        if message_text == '🏠 Home':
            utilities.variables.function_number = -1
            utilities.variables.movie_db.reset_page_db((user_id,))
            utilities.variables.page.format()
            utilities.variables.is_searching = False
            await bot.send_message(chat.id, 'Choose one of the options below',
                                   buttons=click_keyboard_button(False, utilities.classes.State.main))
        elif message_text == 'More ...':
            utilities.variables.movie_db.inc_page_db((int(user_id),))
            response = await func_list(utilities.variables.function_number, user_id)
            if utilities.variables.function_number == 11:
                await show_search_data_item(bot, chat, user_id, response, click_keyboard_button(False,
                                                                                       utilities.classes.State.search))
            else:
                await show_low_data_item(bot, chat, response,
                                         click_keyboard_button(False, utilities.classes.State.news))
        elif message_text == '🔙':
            utilities.variables.movie_db.dec_page_db((user_id,))
            response = await func_list(utilities.variables.function_number, user_id)
            if utilities.variables.function_number == 11:
                await show_search_data_item(bot, chat, response, click_keyboard_button(False,
                                                                                       utilities.classes.State.search))
            else:
                await show_low_data_item(bot, chat, response,
                                         click_keyboard_button(False, utilities.classes.State.news))
        elif re.findall("\|", message_text):
            split = message_text.split(' | ')
            response = await get_movie(split[0], split[1], split[2], split[3])
            await bot.send_message(chat.id, response.to_string(), file=response.get_url(), link_preview=False,
                                   buttons=click_keyboard_button(False, utilities.classes.State.main))
        elif message_text == '🔍 Search':
            await bot.send_message(chat.id, 'type your movie or serial name',
                                   buttons=click_keyboard_button(True, utilities.classes.State.searching))
            click_keyboard_button(True, utilities.classes.State.main)
        elif utilities.variables.is_searching:
            await bot.send_message(chat.id, 'searching...')
            utilities.variables.function_number = 11
            utilities.variables.page.set_search_name(message_text)
            response = await func_list(11, user_id)
            await show_search_data_item(bot, chat, user_id, response,
                                        click_keyboard_button(False, utilities.classes.State.search))


async def set_download_button(bot, chat, split):
    movie_id, movie_type = split[1].split('-')
    if movie_type == 'movie' or movie_type == 'anime_movie':
        response = await get_movie_download_links(movie_id)
        await get_movie_link(chat, bot, response)
    elif movie_type == 'serial' or movie_type == 'anime_serial':
        response = await get_search_by_id(movie_id)
        await get_serial_seasons(chat, bot, response)


async def download_handler_type(bot, chat, data, event):
    data = re.findall(r"'([^']*)'", data)[0]
    split_list = data.split('-')
    if len(split_list) == 3:
        response = await get_search_by_id(split_list[0])
        await get_serial_episode(bot, chat.id, event.original_update.msg_id, response, split_list[2])
    elif len(split_list) == 4:
        response = await get_serial_links(split_list[0], int(split_list[2]) + 1, int(split_list[3]) + 1)
        await get_serial_link(bot, chat.id, event.original_update.msg_id, response, split_list[2], split_list[3])


async def user_start(bot, chat, event):
    await check_user_sub(bot, chat.id, event, True)
    if utilities.variables.first_run:
        utilities.variables.first_run = False
        utilities.variables.movie_db = MovieDb()
        utilities.variables.channel = await bot(ResolveUsernameRequest('movie_tracker1'))
        channel_data(bot)


def channel_data(bot):
    threading.Timer(utilities.variables.wait_seconds, news_with_date2, (bot,)).start()
    threading.Timer(utilities.variables.wait_seconds, updates_with_date2, (bot,)).start()


def news_with_date2(bot):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(news_with_date(bot=bot))
    loop.close()


def updates_with_date2(bot):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(updates_with_date(bot=bot))
    loop.close()


async def news_with_date(bot):
    i = 1
    while True:
        print('amir')
        response = await get_news_with_date(i)
        print(response)
        await show_low_data_updates_with_date(bot, utilities.variables.channel, response)
        if len(response) != 12:
            return
        i = i + 1


async def updates_with_date(bot):
    i = 1
    while True:
        response = await get_updates_with_date(i)
        await show_low_data_updates_with_date(bot, utilities.variables.channel, response)
        if len(response) != 12:
            return
        i = i + 1
