from telethon.sync import TelegramClient, Button

from utilities.consts import page


async def show_low_data_item(client: TelegramClient, chat, response, buttons):
    for item in response:
        try:
            await client.send_message(chat.id, item.to_string(), file=item.get_url(), link_preview=False,
                                      buttons=buttons)
        except:
            print("An exception occurred")


async def show_low_data_news_with_date(client: TelegramClient, channel, response):
    for item in response:
        try:
            await client.send_message(channel, item.to_string(), file=item.get_url(), link_preview=False)
        except:
            print("An exception occurred")


async def show_search_data_item(client: TelegramClient, chat, response, buttons):
    search_items = []
    for item in response:
        try:
            search_items.append(
                [Button.text(f"{item.rawTitle} | {item.type2} | {item.rating.imdb} | {item.year}", resize=True)])
        except:
            print("An exception occurred")
    if page.page_number == 1:
        search_items.insert(0, [buttons[1]])
    else:
        search_items.insert(0, [buttons[0], buttons[1]])
    if len(response) == 12:
        search_items.append([buttons[2]])
    await client.send_message(chat.id, '-', buttons=search_items)
