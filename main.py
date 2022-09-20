import os
import re
import threading
import time


from telethon.events import NewMessage, CallbackQuery
import utilities.variables
import utilities.classes
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.sync import events
from api_requests.movie_request import *
from utilities.helper_function import *
from view_model.view_model import show_low_data_item, show_search_data_item, show_download_link_item, \
    get_serial_episode, get_serial_link

load_dotenv('scratch.env')
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


# def get_new_data():
#     channel = await client(ResolveUsernameRequest('movie_tracker1'))
#     #print(time.ctime())
#     #threading.Timer(utilities.variables.wait_seconds, get_new_data).start()
#

async def get_news_with_data(t_client, channel):
    i = 1
    while True:
        response = await get_news_with_date(i)
        await show_low_data_item(t_client, channel, response,
                                 click_keyboard_button(False, utilities.classes.State.main))
        if len(response) != 12:
            return
        i = i + 1


@client.on(events.NewMessage(pattern="/"))
async def rec_commands(event: NewMessage.Event):
    global first_run
    message = event.message
    text: str = message.text
    chat = await event.get_chat()
    split = text.split(' ')
    if len(split) == 1:
        if text == '/start':
            await check_user_sub(client, chat, event, True)
            # res = await client.get_messages(limit=10)
            # print(res)
        # if first_run:
        #     first_run = False
        #     get_new_data()
    else:
        sub = await check_user_sub(client, chat, event, False)
        if not sub:
            return
        response = await get_links(split[1])
        await show_download_link_item(client, chat, response)


@client.on(events.CallbackQuery())
async def handler(event: CallbackQuery.Event):
    chat = await event.get_chat()
    data = str(event.data)
    data: str = re.findall(r"'([^']*)'", data)[0]
    list = data.split('-')
    if len(list) == 2:
        response = await get_links(list[0])
        await get_serial_episode(client, chat, event.original_update.msg_id, response, list[1])
    elif len(list) == 3:
        response = await get_links(list[0])
        await get_serial_link(client, chat, event.original_update.msg_id, response, list[1], list[2])
    return


@client.on(events.NewMessage(pattern=""))
async def rec_commands(event):
    message = event.message
    text = message.text
    chat = await event.get_chat()
    sub = await check_user_sub(client, chat, event, False)
    if not sub:
        return
    if text == '🔥 News':
        utilities.variables.function_number = 0
        response = await func_list(0)
        await show_low_data_item(client, chat, response,
                                 click_keyboard_button(False, utilities.classes.State.news))
    elif text == '💢 Updates':
        utilities.variables.function_number = 1
        response = await func_list(1)
        await show_low_data_item(client, chat, response,
                                 click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'Top By Likes':
        utilities.variables.function_number = 2
        response = await func_list(2)
        await show_low_data_item(client, chat, response,
                                 click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'Top Movies':
        utilities.variables.function_number = 3
        response = await func_list(3)
        await show_low_data_item(client, chat, response,
                                 click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'Top Series':
        utilities.variables.function_number = 4
        response = await func_list(4)
        await show_low_data_item(client, chat, response,
                                 click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'Coming Soon':
        utilities.variables.function_number = 5
        response = await func_list(5)
        await show_low_data_item(client, chat, response,
                                 click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'In Theaters':
        utilities.variables.function_number = 6
        response = await func_list(6)
        await show_low_data_item(client, chat, response,
                                 click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'Box Office':
        utilities.variables.function_number = 7
        response = await func_list(7)
        await show_low_data_item(client, chat, response,
                                 click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'Anime Airing':
        utilities.variables.function_number = 8
        response = await func_list(8)
        await show_low_data_item(client, chat, response,
                                 click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'Anime Coming Soon':
        utilities.variables.function_number = 9
        response = await func_list(9)
        await show_low_data_item(client, chat, response,
                                 click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'Popular':
        utilities.variables.function_number = 10
        response = await func_list(10)
        await show_low_data_item(client, chat, response,
                                 click_keyboard_button(False, utilities.classes.State.news))
    elif text == '🏠 Home':
        utilities.variables.function_number = -1
        utilities.variables.page.format()
        utilities.variables.is_searching = False
        await client.send_message(chat.id, 'Choose one of the options below', buttons=click_keyboard_button(False, utilities.classes.State.main))
    elif text == 'More ...':
        utilities.variables.page.increase_page_number()
        response = await func_list(utilities.variables.function_number)
        if utilities.variables.function_number == 11:
            await show_search_data_item(client, chat, response, click_keyboard_button(False,
                                                                                      utilities.classes.State.search))
        else:
            await show_low_data_item(client, chat, response, click_keyboard_button(False, utilities.classes.State.news))
    elif text == '🔙':
        utilities.variables.page.decrease_page_number()
        response = await func_list(utilities.variables.function_number)
        if utilities.variables.function_number == 11:
            await show_search_data_item(client, chat, response, click_keyboard_button(False,
                                                                                      utilities.classes.State.search))
        else:
            await show_low_data_item(client, chat, response,
                                     click_keyboard_button(False, utilities.classes.State.news))
    elif re.findall("\|", text):
        split = text.split(' | ')
        response = await get_movie(split[0], split[1], split[2], split[3])
        await client.send_message(chat.id, response.to_string(), file=response.get_url(), link_preview=False,
                                  buttons=click_keyboard_button(False, utilities.classes.State.main))

    elif text == '🔍 Search':
        await client.send_message(chat.id, 'type your movie or serial name', buttons=click_keyboard_button(True, utilities.classes.State.searching))
        click_keyboard_button(True, utilities.classes.State.main)
    elif utilities.variables.is_searching:
        await client.send_message(chat.id, 'searching...')
        utilities.variables.function_number = 11
        utilities.variables.page.set_search_name(message.text)
        response = await func_list(11)
        await show_search_data_item(client, chat, response,
                                    click_keyboard_button(False, utilities.classes.State.search))


client.run_until_disconnected()
