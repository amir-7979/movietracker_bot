import os
from dotenv import load_dotenv
from telethon import TelegramClient
from telethon.events import NewMessage, CallbackQuery
from telethon.sync import events
from model.movie_db import MovieDb
from utilities.functions import user_start, check_user_sub, set_download_button, download_handler_type, find_method, \
    reset_db
import utilities

load_dotenv('scratch.env')
api_id = int(os.getenv('API_ID'))
api_hash = os.getenv("API_HASH")
bot_token = os.getenv("BOT_TOKEN")
bot_id = os.getenv("BOT_ID")
utilities.variables.server_address = os.getenv("SERVER_ADDRESS")
bot = TelegramClient('bot2', api_id, api_hash).start(bot_token=bot_token)
global movie_db
movie_db = MovieDb()

@bot.on(events.NewMessage(pattern="/start"))
async def start_command(event: NewMessage.Event):
    text_message: str = event.message.text
    chat = await event.get_chat()
    split = text_message.split(' ')
    if len(split) == 1:
        if text_message == '/start':
            await user_start(bot, chat, event, bot_id)
    else:
        subscription = await check_user_sub(bot, chat, event, False)
        if not subscription:
            # todo show message
            return
        await set_download_button(bot, chat, split)


@bot.on(events.CallbackQuery())
async def download_handler(event: CallbackQuery.Event):
    chat = await event.get_chat()
    data: str = str(event.data)
    await download_handler_type(bot, chat, data, event)
    return


@bot.on(events.NewMessage(pattern=""))
async def other_commands(event):
    text: str = event.message.text
    if not text.startswith('/start'):
        message_text = event.message.text
        chat = await event.get_chat()
        subscription = await check_user_sub(bot, chat, event, False)
        user_id = event.original_update.message.peer_id.user_id
        if not subscription:
            return
        await find_method(bot, chat, message_text, user_id)
    else:
        reset_db(event.original_update.message.peer_id.user_id)


bot.run_until_disconnected()
