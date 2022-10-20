from enum import Enum


class State(Enum):
    main = 0
    news = 1
    search = 2
    searching = 3


class Page:
    search_name = ''
    func = ''

    def set_search_name(self, text):
        self.search_name = text

    def set_func(self, func):
        self.func = func

    def format(self):
        self.search_name = ''
        self.func = ''
