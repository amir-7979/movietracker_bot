import os
import re
import threading
import time

#from dotenv import load_dotenv
from telethon.sync import TelegramClient, events
from telethon.tl.functions.contacts import ResolveUsernameRequest

from api_requests.get_movies import get_news, get_updates, get_tops_by_likes, get_top_movies, get_top_series, \
    get_search, get_coming_soon, get_in_theaters, get_box_office, get_anime_top_airing, get_anime_top_comingSoon, \
    get_popular, get_movie
from consts import State, get_keyboard_button
from view_model.view_model import show_low_data_item, show_search_data_item

#load_dotenv('scratch.env')
api_id = 19110656
api_hash = "4dc18fd5f2a138e06cb6c6979d1c21df"
bot_token = "5394497257:AAGC6mmWGDs4vv4mn0sPp8ZJeJfrrsnbY34"
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)
is_searching = False
state = State.main
glob_text = -1
WAIT_SECONDS = 240


def foo():
    print(time.ctime())
    threading.Timer(WAIT_SECONDS, foo).start()


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


def click_keyboard_button(searching, new_state):
    global state, is_searching
    state = new_state
    is_searching = searching
    return get_keyboard_button(state)


@client.on(events.Raw())
async def rec_commands(event):
    foo()


@client.on(events.NewMessage(pattern="/"))
async def rec_commands(event):
    global is_searching, glob_text, func_list
    message = event.message
    text = message.text
    chat = await event.get_chat()
    channel = await client(ResolveUsernameRequest('movie_tracker1'))
    await client.send_message(channel, message='amir')

    #await client(JoinChannelRequest(channel))
    if text == '/start':
        await client.send_message(chat.id, 'Welcome to MovieTracker bot',
                                  buttons=click_keyboard_button(False, State.main))
    elif text == '/news':
        glob_text = 0
        response = await func_list[0]
        await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif text == '/updates':
        glob_text = 1
        response = await func_list[1]
        await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif text == '/tops_by_likes':
        glob_text = 2
        response = await func_list[2]
        await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif text == '/top_movies':
        glob_text = 3
        response = await func_list[3]
        await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif text == '/top_series':
        glob_text = 4
        response = await func_list[4]
        await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif text == '/search':
        await message.reply('type your movie or serial name')
        click_keyboard_button(True, State.main)
    elif text == '/main':
        await client.send_message(chat.id, message='-', buttons=click_keyboard_button(False, State.main))
    else:
        print('here')



@client.on(events.NewMessage(pattern=""))
async def rec_commands(event):
    global is_searching, glob_text, func_list, page
    message = event.message
    text = message.text
    chat = await event.get_chat()
    if text == '🔥 News':
        glob_text = 0
        response = await func_list(0)
        await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif text == '💢 Updates':
        glob_text = 1
        response = await func_list(1)
        await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif text == 'Top by likes':
        glob_text = 2
        response = await func_list(2)
        await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif text == 'Top movies':
        glob_text = 3
        response = await func_list(3)
        await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif text == 'Top series':
        glob_text = 4
        response = await func_list(4)
        await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif text == 'Coming soon':
        glob_text = 5
        response = await func_list(5)
        await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif text == 'In theaters':
        glob_text = 6
        response = await func_list(6)
        await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif text == 'Box office':
        glob_text = 7
        response = await func_list(7)
        await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif text == 'Anime airing':
        glob_text = 8
        response = await func_list(8)
        await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif text == 'Anime coming soon':
        glob_text = 9
        response = await func_list(9)
        await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif text == 'Popular':
        glob_text = 10
        response = await func_list(10)
        await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif text == '🏠 Home':
        glob_text = -1
        page.format()
        is_searching = False
        await client.send_message(chat.id, '-', buttons=click_keyboard_button(False, State.main))
    elif text == 'More ...':
        page.increase_page_number()
        response = await func_list(glob_text)
        if glob_text == 11:
            await show_search_data_item(client, chat, response, click_keyboard_button(False, State.search))
        else:
            await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif text == '🔙':
        page.decrease_page_number()
        response = await func_list(glob_text)
        if glob_text == 11:
            await show_search_data_item(client, chat, response, click_keyboard_button(False, State.search))
        else:
            await show_low_data_item(client, chat, response, click_keyboard_button(False, State.news))
    elif re.findall("\|", text):
        split = text.split(' | ')
        response = await get_movie(split[0], split[1], split[2], split[3])
        await client.send_message(chat.id, response.to_string(), file=response.get_url(), link_preview=False,
                                  buttons=click_keyboard_button(False, State.main))

    elif text == '🔍 Search':
        await message.reply('type your movie or serial name')
        click_keyboard_button(True, State.main)
    elif is_searching:
        glob_text = 11
        page.set_search_name(message.text)
        response = await func_list(11)
        await show_search_data_item(client, chat, response, click_keyboard_button(False, State.search))



client.run_until_disconnected()



