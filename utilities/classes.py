from enum import Enum


class State(Enum):
    main = 0
    news = 1
    search = 2
    quality = 3
    season = 4
    episode = 5


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
