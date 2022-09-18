import os
import time
from telethon.sync import TelegramClient, Button
from model.dlink_model import DLinkItem
from utilities.variables import page


async def show_low_data_item(client: TelegramClient, chat, response, buttons):
    # await client.send_message(chat.id, response[0].to_string(),
    #                           file=response[0].get_url(),
    #                           link_preview=False, buttons=buttons)
    # await client.send_message(chat.id, '-', buttons=buttons)
    for item in response:
        try:
            await client.send_message(chat.id, item.to_string(), file=item.get_url(), link_preview=False,
                                      buttons=buttons)
            time.sleep(0.25)
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
                [Button.text(f"{item.rawTitle} | {item.type} | {item.rating.imdb} | {item.year}", resize=True)])
        except:
            print("An exception occurred")
    if page.page_number == 1:
        search_items.insert(0, [buttons[1]])
    else:
        search_items.insert(0, [buttons[0], buttons[1]])
    if len(response) == 12:
        search_items.append([buttons[2]])
    await client.send_message(chat.id, '-', buttons=search_items)


async def show_download_link_item(client: TelegramClient, chat, response: DLinkItem):
    if len(response.qualities) != 0:
        await get_movie_link(chat, client, response)
    else:
        await get_serial_season(chat, client, response)


async def get_movie_link(chat, client, response):
    link_items = []
    for item in response.qualities:
        try:
            if len(item.links) != 0:
                link_items.append(Button.url(f"{item.quality}", url=item.links[0].link))
        except:
            print("An exception occurred")
    await client.send_message(chat.id, response.title.capitalize(), buttons=link_items)


async def get_serial_season(chat, client, response):
    link_items = []
    for item in response.seasons:
        try:
            if len(item.episodes) != 0:
                link_items.append(
                    Button.inline(text=f"season {item.seasonNumber}", data=f"{response.id}-{item.seasonNumber}"))
        except:
            print("An exception occurred")
    if len(link_items) == 0:
        return await client.send_message(chat.id, 'There is no link to show!')
    else:
        return await client.send_message(chat.id, response.title.capitalize(), buttons=link_items)


async def get_serial_episode(client, chat, msg_id, response: DLinkItem, season_number):
    link_items = []
    for item in response.seasons[int(season_number) - 1].episodes:
        try:
            if len(item.links) != 0:
                link_items.append(Button.inline(text=f"ep {item.episodeNumber}",
                                                data=f"{response.id}-{season_number}-{item.episodeNumber}"))
        except:
            print("An exception occurred")
    i = 0
    new_link_items = []
    if len(link_items) < 5:
        new_link_items = link_items
    else:
        while i < len(link_items):
            if i + 5 <= len(link_items) :
                new_link_items.append([link_items[i], link_items[i + 1], link_items[i + 2], link_items[i + 3], link_items[i + 4]])
                i += 5
            else:
                new_link_items.append([link_items[i]])
                i += 1
    if len(link_items) == 0:
        return await client.send_message(chat.id, 'There is no link to show!')
    else:
        return await client.edit_message(chat.id, msg_id, f"{response.title.capitalize()} - season {season_number}",
                                     buttons=new_link_items)


async def get_serial_link(client, chat, msg_id, response: DLinkItem, season_number, episode_number):
    link_items = []
    for item in response.seasons[int(season_number) - 1].episodes[int(episode_number) - 1].links:
        try:
            if len(item.link) != 0:
                link_items.append(Button.url(f"{item.info}", url=item.link))
        except:
            print("An exception occurred")
    i = 0
    new_link_items = []
    if len(link_items) < 3:
        new_link_items = link_items
    else:
        while i < len(link_items):
            if i + 2 <= len(link_items) - 1:
                new_link_items.append([link_items[i], link_items[i + 1]])
                i += 2
            else:
                new_link_items.append([link_items[i]])
                i += 1
    if len(new_link_items) == 0:
        return await client.edit_message(chat.id, msg_id, 'There is no link to show!')
    else:
        return await client.edit_message(chat.id, msg_id, f"{response.title.capitalize()} - season {season_number} - "
                                                          f"episode {episode_number}", buttons=new_link_items)
