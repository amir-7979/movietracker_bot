# await bot.send_file(chat.id, 'C:\\Users\\amirn\Desktop\\amir.jpg')
#
#     await bot.download_profile_photo('me')
#     messages = bot.get_messages(chat.id)
#     messages[0].download_media()


# if text[0] == '/start':
#     await event.respond('welcome to MoviTracker Bot')
#     return
#
# if text[0] == '/news':
#     response = await get_news()
#     # for item in response:
#     await bot.send_message(chat.id, f'[ ]({response[0].posters[0].url})', parse_mode='markdown')

# await event.respond("{0} \n"
#     "name : {1} \n"
#     "type : {2} \n"
#     "rate : {3} \n"
#     "year : {4} \n"
#     "s_id : {5} \n"
#     "".format(item.posters[0].url, item.title, item.type, item.rating.imdb, item.year, item.s_id))




# elif text[0] == '/news':
#     response = await get_news()
#     for item in response:
#         await event.respond(str(item))
#     return
#
# elif text[0] == '/news':
#     response = await get_news()
#     for item in response:
#         await event.respond(str(item))
#     return
#
# elif text[0] == '/news':
#     response = await get_news()
#     for item in response:
#         await event.respond(str(item))
#     return
#
# elif text[0] == '/news':
#     response = await get_news()
#     for item in response:
#         await event.respond(str(item))
#     return
#
# elif text[0] == '/news':
#     response = await get_news()
#     for item in response:
#         await event.respond(str(item))
#     return
#
# elif text[0] == '/news':
#     response = await get_news()
#     for item in response:
#         await event.respond(str(item))
#     return
#
# elif text[0] == '/news':
#     response = await get_news()
#     for item in response:
#         await event.respond(str(item))
#     return
# else:
#     return

# @bot.on(events.NewMessage(pattern="/"))
# async def add_member(event):
#     text = event.message.text.split(" ")
#     chat = await event.get_chat()
#     if text[0] == '/news':
#         response = await get_news()
#         #for item in response:
#         item = response[0]
#         await bot.send_message(chat.id, item.to_string(), file=item.get_url())




# @bot.on(events.NewMessage(pattern=""))
# async def add_member(event):
#     text = event.message.text.split(" ")
#     chat = await event.get_chat()
#     message = event.message
#     print(text)
#     print(chat)
#     print(message)
#     if text[0] == '/news':
#         response = await get_news()
#         #for item in response:
#         item = response[0]
#         await bot.send_message(chat.id, item.to_string(), file=item.get_url(), link_preview=False)
#
#
# bot.run_until_disconnected()

# message = await client.send_message(
#         chat.id,
#         'This message has **bold**, `code`, __italics__ and '
#         'a [nice website](https://example.com)!',
#         link_preview=False
#     )