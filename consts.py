from enum import Enum
from telethon.sync import Button


class State(Enum):
    main = 0
    news = 1
    search = 2
    quality = 3
    season = 4
    episode = 5


def get_keyboard_button(enum):
    if enum == State.main:
        return start_buttons
    elif enum == State.news:
        return news_button
    elif enum == State.search:
        return search_button


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


class Page:
    search_name = ''
    page_number = 1
    func = ''

    def set_search_name(self, text):
        self.search_name = text

    def set_func(self, func):
        self.func = func

    def increase_page_number(self):
        self.page_number = self.page_number + 1

    def decrease_page_number(self):
        if self.page_number > 1:
            self.page_number = self.page_number - 1

    def format(self):
        self.page_number = 1
        self.search_name = ''
        self.func = ''


page = Page()
