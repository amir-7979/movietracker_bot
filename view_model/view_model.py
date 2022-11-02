import time

from telethon.sync import TelegramClient

from model.dlink_model import DLinkItem
from model.telbot_model import TelBotItem
from utilities.variables import *


async def show_low_data_item(client: TelegramClient, chat, response):
    global news_button
    if len(response) == 0:
        return await client.send_message(chat.id, 'Nothing to show!')
    else:

        for item in response:
            try:
                await client.send_message(chat.id, item.to_string(), file=item.get_url(), link_preview=False,
                                          buttons=news_button)
                time.sleep(0.1)
            except:
                print("An exception occurred")


async def show_item_channel(client: TelegramClient, channel, response):
    for item in response:
        try:
            await client.send_message(channel, item.to_string_channel(), file=item.get_url(), link_preview=False)
        except:
            print("An exception occurred")


async def show_search_data_item(client: TelegramClient, chat, user_id, response, buttons, page_number):
    if len(response) == 0:
        return await client.send_message(chat.id, 'Nothing to show!')
    else:
        search_items = []
        for item in response:
            try:
                search_items.append(
                    [Button.text(f"{item.rawTitle} | {item.type} | {item.rating.imdb} | {item.year}", resize=True)])
            except:
                print("An exception occurred")
        if page_number == 1:
            search_items.insert(0, [buttons[1]])
        else:
            search_items.insert(0, [buttons[0], buttons[1]])
        if len(response) == 12:
            search_items.append([buttons[2]])
        await client.send_message(chat.id, 'Choose one of the options below', buttons=search_items)
        return search_items


async def get_movie_link(chat, client, response: DLinkItem):
    link_items = []
    for item in response.qualities:
        try:
            if len(item.links) != 0:
                link_items.append(Button.url(f"{item.quality}", url=item.links[0].link))
        except:
            print("An exception occurred")
    await client.send_message(chat.id, response.rawTitle, buttons=link_items)


async def get_serial_seasons(chat, client: TelegramClient, response: TelBotItem):
    if len(response.seasonEpisode) == 0:
        return await client.send_message(chat.id, 'No season found!')
    link_items = []
    for item in response.seasonEpisode:
        if item.seasonNumber <= response.latestData.season:
            try:
                link_items.append(
                    Button.inline(text=f"season {item.seasonNumber}",
                                  data=f"{response.id}-{response.type}-{item.seasonNumber}"))
            except:
                print("An exception occurred")

    i = 0
    new_link_items: list = []
    if len(link_items) < 5:
        new_link_items = link_items
    else:
        while i < len(link_items) and i + 5 <= len(link_items):
            new_link_items.append(
                [link_items[i], link_items[i + 1], link_items[i + 2], link_items[i + 3], link_items[i + 4]])
            i += 5
        new_link_items.extend([link_items[i:]])
    if len(link_items) == 0:
        return await client.send_message(chat.id, 'There is no link to show!')
    else:
        return await client.send_message(chat.id, response.rawTitle, buttons=new_link_items)


async def get_serial_episode(client, chat_id, msg_id, response: TelBotItem, season_number: str):
    elems = (elem for elem in response.seasonEpisode if elem.seasonNumber == int(season_number))
    elems2 = list(elems)
    if elems2[0].episodes == 0:
        return await client.send_message(chat_id, 'No episode found!')
    link_items = []
    for item in range(elems2[0].episodes):
        if int(season_number) < response.latestData.season or (
                int(season_number) == response.latestData.season and (item + 1) <= response.latestData.episode):
            try:
                link_items.append(Button.inline(text=f"ep {int(item) + 1}",
                                                data=f"{response.id}-{response.type}-{season_number}-{item}"))
            except:
                print("An exception occurred")
    i = 0
    new_link_items = []
    if len(link_items) < 5:
        new_link_items = link_items
    else:
        while i < len(link_items) and i + 5 <= len(link_items):
            new_link_items.append(
                [link_items[i], link_items[i + 1], link_items[i + 2], link_items[i + 3], link_items[i + 4]])
            i += 5
        new_link_items.extend([link_items[i:]])
    if len(link_items) == 0:
        return await client.send_message(chat_id, 'There is no link to show!')
    else:
        return await client.edit_message(chat_id, msg_id, f"{response.rawTitle} - season {season_number}",
                                         buttons=new_link_items)


async def get_serial_link(client, chat_id, msg_id, response: DLinkItem, season_number, episode_number):
    # todo go back to season
    if len(response.seasons) == 0:
        return await client.edit_message(chat_id, msg_id, 'There is no link to show!')
    if len(response.seasons[0].episodes) == 0:
        return await client.edit_message(chat_id, msg_id, 'There is no link to show!')
    link_items = []
    for item in response.seasons[0].episodes[0].links:
        try:
            if len(item.link) != 0:
                link_items.append(Button.url(f"{item.info}", url=item.link.replace(' ', '%20')))
        except:
            print("An exception occurred")

    i = 0
    new_link_items = []
    if len(link_items) < 3:
        new_link_items = link_items
    else:
        while i < len(link_items) and i + 2 <= len(link_items) - 1:
            new_link_items.append([link_items[i], link_items[i + 1]])
            i += 2
        new_link_items.extend([link_items[i:]])
    if len(new_link_items) == 0:
        return await client.edit_message(chat_id, msg_id, 'There is no link to show!')
    else:
        return await client.edit_message(chat_id, msg_id, f"{response.rawTitle} - season {season_number} - "
                                                          f"episode {int(episode_number) + 1}", buttons=new_link_items)
