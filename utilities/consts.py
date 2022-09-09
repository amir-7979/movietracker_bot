from telethon.sync import Button

from utilities.classes import State, Page

is_searching = False
first_run = True
state = State.main
function_number = -1
wait_seconds = 10
page = Page()
start_buttons = [
    [Button.text('🔍 Search', resize=True), Button.text('🔥 News', resize=True),
     Button.text('💢 Updates', resize=True)],
    [Button.text('Top by likes', resize=True), Button.text('Top movies', resize=True),
     Button.text('Top series', resize=True)],
    [Button.text('Coming soon', resize=True), Button.text('In theaters', resize=True),
     Button.text('Popular', resize=True)],
    [Button.text('Box office', resize=True), Button.text('Anime airing', resize=True),
     Button.text('Anime coming soon', resize=True)],
]

news_button = [Button.text('🏠 Home', resize=True), Button.text('More ...', resize=True)]
search_button = [Button.text('🔙', resize=True), Button.text('🏠 Home', resize=True),
                 Button.text('More ...', resize=True)]
