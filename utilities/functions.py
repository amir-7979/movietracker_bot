import asyncio
import re
import threading
import time

from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.types import InputChannel, ChannelParticipantsRecent
from telethon.tl.types.channels import ChannelParticipants

from utilities.variables import *
from api_requests.movie_request import *
from model.movie_db import MovieDb
from view_model.view_model import show_low_data_item, show_search_data_item, get_movie_link, get_serial_seasons, \
    get_serial_episode, get_serial_link, show_item_channel


def func_list(i: int, user_id: int):
    global movie_db
    page_number = movie_db.get_page_db((user_id,))
    if i == 0:
        return get_news(page_number)
    elif i == 1:
        return get_updates(page_number)
    elif i == 2:
        return get_tops_by_likes(page_number)
    elif i == 3:
        return get_top_movies(page_number)
    elif i == 4:
        return get_top_series(page_number)
    elif i == 5:
        return get_coming_soon(page_number)
    elif i == 6:
        return get_in_theaters(page_number)
    elif i == 7:
        return get_box_office(page_number)
    elif i == 8:
        return get_anime_top_airing(page_number)
    elif i == 9:
        return get_anime_top_comingSoon(page_number)
    elif i == 10:
        return get_popular(page_number)
    elif i == 11:
        return get_search(movie_db.get_search_name_db((user_id,)), page_number)


async def check_user_sub(client, chat_id, event, first_use) -> bool:
    global channel, start_buttons
    channel = await client.get_entity('t.me/movie_tracker1')
    result: ChannelParticipants = await client(
        GetParticipantsRequest(InputChannel(channel.id, channel.access_hash), filter=ChannelParticipantsRecent(),
                               limit=1000000, offset=0, hash=0))
    sender = event.original_update.message.peer_id.user_id
    subscribers = (o.user_id for o in result.participants)
    if sender in subscribers:
        if first_use:
            await client.send_message(chat_id, 'Welcome to MovieTracker bot',
                                      buttons=start_buttons)
        return True
    else:
        await client.send_message(chat_id, 'Hi!\nPlease join our channel to use bot',
                                  buttons=channel_button)
        return False


def get_option_index(text):
    global option
    try:
        index = option.index(text)
        return index
    except:
        return -1


async def find_method_name_in_list(bot, chat, user_id, message_text):
    global movie_db
    index = get_option_index(message_text)
    if index == -1:
        return False
    movie_db.insert_function_number_db((user_id, index))
    response = await func_list(index, user_id)
    await show_low_data_item(bot, chat, response)
    return True


async def find_method(bot, chat, message_text, user_id):
    global news_button, search_button, news_button, movie_db
    if not await find_method_name_in_list(bot, chat, user_id, message_text):
        if message_text == '🏠 Home':
            movie_db.reset_all((user_id,))
            await bot.send_message(chat.id, 'Choose one of the options below',
                                   buttons=start_buttons)
        elif message_text == 'More ...':
            movie_db.inc_page_db((user_id,))
            function_number = movie_db.get_function_number_db((user_id,))
            response = await func_list(function_number, user_id)
            if function_number == 11:
                await show_search_data_item(bot, chat, user_id, response, search_button, movie_db.get_page_db((user_id,)))
            else:
                await show_low_data_item(bot, chat, response)
        elif message_text == '🔙':
            movie_db.dec_page_db((user_id,))
            function_number = movie_db.get_function_number_db((user_id,))
            response = await func_list(function_number, user_id)
            if function_number == 11:
                await show_search_data_item(bot, chat, user_id, response, search_button, movie_db.get_page_db((user_id,)))
            else:
                await show_low_data_item(bot, chat, response)
        elif re.findall("\|", message_text):
            split = message_text.split(' | ')
            movie_db.get_search_name_db((user_id, ))
            response = await func_list(11, user_id)
            buttons = await show_search_data_item(bot, chat, user_id, response,
                                        search_button, movie_db.get_page_db((user_id,)))
            if len(split) == 3:
                response = await get_movie(split[0], split[1], split[2], '')
            else:
                response = await get_movie(split[0], split[1], split[2], split[3])
            print(response)
            await bot.send_message(chat.id, response.to_string(), file=response.get_url(), link_preview=False,
                                   buttons=buttons)
        elif message_text == '🔍 Search':
            await bot.send_message(chat.id, 'type your movie or serial name',
                                   buttons=Button.text('🏠 Home', resize=True))
        else:
            await bot.send_message(chat.id, 'searching...')
            movie_db.insert_function_number_db((user_id, 11))
            movie_db.insert_search_name_db((user_id, message_text))
            response = await func_list(11, user_id)
            await show_search_data_item(bot, chat, user_id, response,
                                        search_button, movie_db.get_page_db((user_id,)))



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
        response = await get_serial_links(split_list[0], int(split_list[2]), int(split_list[3]) + 1)
        await get_serial_link(bot, chat.id, event.original_update.msg_id, response, split_list[2], split_list[3])


async def user_start(bot, chat, event, bot_id):
    global first_run, movie_db, channel
    await check_user_sub(bot, chat.id, event, True)
    if first_run:
        first_run = False
        movie_db = MovieDb()
        channel = await bot(ResolveUsernameRequest('movie_tracker1'))
        await channel_data(bot, bot_id)
    movie_db.reset_all((event.original_update.message.peer_id.user_id,))


async def channel_data(bot, bot_id):
    global channel
    while True:
        response = await get_data_for_channel(bot_id)
        await show_item_channel(bot, channel, response)
        if len(response) == 0:
            break

    print('brake')
    threading.Timer(60, channel_data, (bot, bot_id)).start()


def news_with_date2(bot, bot_id):
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)
    # loop.run_until_complete(news_with_date(bot_id))
    # loop.close()
    print('timer')





def reset_db(user_id):
    global movie_db
    movie_db.reset_all((user_id,))
