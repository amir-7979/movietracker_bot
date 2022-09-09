import os
import re
import threading
import time
import utilities.variables
import utilities.classes
import view_model.view_model
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.sync import events
from telethon.tl.functions.contacts import ResolveUsernameRequest


load_dotenv('scratch.env')
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
client = TelegramClient('bot', api_id, api_hash).start(bot_token=bot_token)


def get_new_data():
    # channel = await client(ResolveUsernameRequest('movie_tracker1'))
    print(time.ctime())
    threading.Timer(utilities.variables.wait_seconds, get_new_data).start()


async def get_news_with_data(t_client, channel):
    i = 1
    while True:
        response = await utilities.helper_function.get_news_with_date(i)
        await view_model.view_model.show_low_data_item(t_client, channel, response, utilities.helper_function.click_keyboard_button(False, utilities.classes.State.main))
        if len(response) != 12:
            return
        i = i + 1


# @client.on(events.Raw())
# async def rec_commands(event):


@client.on(events.NewMessage(pattern="/"))
async def rec_commands(event):
    global first_run
    message = event.message
    text = message.text
    chat = await event.get_chat()
    if text == '/start':
        await client.send_message(chat.id, 'Welcome to MovieTracker bot',
                                  buttons= utilities.helper_function.click_keyboard_button(False, utilities.classes.State.main))
        if first_run:
            first_run = False
            get_new_data()


@client.on(events.NewMessage(pattern=""))
async def rec_commands(event):
    message = event.message
    text = message.text
    chat = await event.get_chat()
    if text == '🔥 News':
        utilities.variables.function_number = 0
        response = await utilitiesfunc_list(0)
        await view_model.view_model.show_low_data_item(client, chat, response, utilities.helper_function.click_keyboard_button(False, utilities.classes.State.news))
    elif text == '💢 Updates':
        utilities.variables.function_number = 1
        response = await utilities.helper_function.func_list(1)
        await view_model.view_model.show_low_data_item(client, chat, response, utilities.helper_function.click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'Top by likes':
        utilities.variables.function_number = 2
        response = await utilities.helper_function.func_list(2)
        await view_model.view_model.show_low_data_item(client, chat, response, utilities.helper_function.click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'Top movies':
        utilities.variables.function_number = 3
        response = await utilities.helper_function.func_list(3)
        await view_model.view_model.show_low_data_item(client, chat, response, utilities.helper_function.click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'Top series':
        utilities.variables.function_number = 4
        response = await utilities.helper_function.func_list(4)
        await view_model.view_model.show_low_data_item(client, chat, response, utilities.helper_function.click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'Coming soon':
        utilities.variables.function_number = 5
        response = await utilities.helper_function.func_list(5)
        await view_model.view_model.show_low_data_item(client, chat, response, utilities.helper_function.click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'In theaters':
        utilities.variables.function_number = 6
        response = await utilities.helper_function.func_list(6)
        await view_model.view_model.show_low_data_item(client, chat, response, utilities.helper_function.click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'Box office':
        utilities.variables.function_number = 7
        response = await utilities.helper_function.func_list(7)
        await view_model.view_model.show_low_data_item(client, chat, response, utilities.helper_function.click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'Anime airing':
        utilities.variables.function_number = 8
        response = await utilities.helper_function.func_list(8)
        await view_model.view_model.show_low_data_item(client, chat, response, utilities.helper_function.click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'Anime coming soon':
        utilities.variables.function_number = 9
        response = await utilities.helper_function.func_list(9)
        await view_model.view_model.show_low_data_item(client, chat, response, utilities.helper_function.click_keyboard_button(False, utilities.classes.State.news))
    elif text == 'Popular':
        utilities.variables.function_number = 10
        response = await utilities.helper_function.func_list(10)
        await view_model.view_model.show_low_data_item(client, chat, response, utilities.helper_function.click_keyboard_button(False, utilities.classes.State.news))
    elif text == '🏠 Home':
        utilities.variables.function_number = -1
        utilities.variables.page.format()
        utilities.variables.is_searching = False
        await client.send_message(chat.id, '-', buttons= utilities.helper_function.click_keyboard_button(False, utilities.classes.State.main))
    elif text == 'More ...':
        utilities.variables.page.increase_page_number()
        response = await utilities.helper_function.func_list(utilities.variables.function_number)
        if utilities.variables.function_number == 11:
            await view_model.view_model.show_search_data_item(client, chat, response, utilities.helper_function.click_keyboard_button(False, utilities.classes.State.search))
        else:
            await view_model.view_model.show_low_data_item(client, chat, response, utilities.helper_function.click_keyboard_button(False, utilities.classes.State.news))
    elif text == '🔙':
        utilities.variables.page.decrease_page_number()
        response = await utilities.helper_function.func_list(utilities.variables.function_number)
        if utilities.variables.function_number == 11:
            await view_model.view_model.show_search_data_item(client, chat, response, utilities.helper_function.click_keyboard_button(False, utilities.classes.State.search))
        else:
            await view_model.view_model.show_low_data_item(client, chat, response, utilities.helper_function.click_keyboard_button(False, utilities.classes.State.news))
    elif re.findall("\|", text):
        split = text.split(' | ')
        response = await utilities.helper_function.get_movie(split[0], split[1], split[2], split[3])
        await client.send_message(chat.id, response.to_string(), file=response.get_url(), link_preview=False,
                                  buttons= utilities.helper_function.click_keyboard_button(False, utilities.classes.State.main))

    elif text == '🔍 Search':
        await message.reply('type your movie or serial name')
        utilities.helper_function.click_keyboard_button(True, utilities.classes.State.main)
    elif utilities.variables.is_searching:
        utilities.variables.function_number = 11
        utilities.variables.page.set_search_name(message.text)
        response = await utilities.helper_function.func_list(11)
        await view_model.view_model.show_search_data_item(client, chat, response, utilities.helper_function.click_keyboard_button(False, utilities.classes.State.search))


client.run_until_disconnected()
