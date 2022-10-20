from telethon.sync import Button

from utilities.classes import State, Page

channel = ''
movie_db = None
is_searching = False
first_run = True
state = State.main
function_number = -1
wait_seconds = 10
page = Page()
start_buttons = [
    [Button.text('🔍 Search', resize=True), Button.text('🔥 News', resize=True),
     Button.text('💢 Updates', resize=True)],
    [Button.text('Top By Likes', resize=True), Button.text('Top Movies', resize=True),
     Button.text('Top Series', resize=True)],
    [Button.text('Coming Soon', resize=True), Button.text('In Theaters', resize=True),
     Button.text('Popular', resize=True)],
    [Button.text('Box Office', resize=True), Button.text('Anime Airing', resize=True),
     Button.text('Anime Coming Soon', resize=True)],
]
news_button = [Button.text('🏠 Home', resize=True), Button.text('More ...', resize=True)]
search_button = [Button.text('🔙', resize=True), Button.text('🏠 Home', resize=True),
                 Button.text('More ...', resize=True)]
channel_button = [Button.url('Movie Tracker', url='https://t.me/movie_tracker1')]
option = ['🔥 News', '💢 Updates', 'Top By Likes', 'Top Movies', 'Top Series', 'Coming Soon', 'In Theaters', 'Box Office', 'Anime Airing', 'Anime Coming Soon', 'Popular']
