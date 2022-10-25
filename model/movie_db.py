import sqlite3
from dataclasses import dataclass


@dataclass
class MovieDb:
    def __init__(self):
        self.connection = sqlite3.connect('movie_tracker.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS User (id INTEGER NOT NULL PRIMARY KEY, page INTEGER, function_number INTEGER, search_name TEXT);")

    def insert_page_db(self, data):
        self.cursor.execute("INSERT INTO User (id, page) values(?, ?) ON CONFLICT(id) DO UPDATE SET page = ?",
                            (data[0], int(data[1]), int(data[1])))
        self.connection.commit()

    def get_page_db(self, data):
        self.cursor.execute("SELECT page FROM User WHERE id == ?", (data[0],))
        response = self.cursor.fetchall()
        if len(response) == 0:
            return 1
        else:
            return response[0][0]

    def inc_page_db(self, data):
        self.cursor.execute("UPDATE User SET page=page + 1 WHERE id = ?", (data[0],))
        self.connection.commit()

    def dec_page_db(self, data):
        self.cursor.execute("UPDATE User SET page=page - 1 WHERE id = ? and page > 1", (data[0],))
        self.connection.commit()

    def reset_page_db(self, data):
        self.cursor.execute("UPDATE User SET page = 1 WHERE id = ?", (data[0],))
        self.connection.commit()

    def insert_function_number_db(self, data):
        self.cursor.execute(
            "INSERT INTO User (id, function_number) values(?, ?) ON CONFLICT(id) DO UPDATE SET function_number = ?",
            (data[0], int(data[1]), int(data[1])))
        self.connection.commit()

    def get_function_number_db(self, data):
        self.cursor.execute("SELECT function_number FROM User WHERE id == ?", (data[0],))
        response = self.cursor.fetchall()
        if len(response) == 0:
            return 1
        else:
            return response[0][0]

    def reset_function_number_db(self, data):
        self.cursor.execute("UPDATE User SET function_number = -1 WHERE id = ?", (data[0],))
        self.connection.commit()

    def insert_search_name_db(self, data):
        self.cursor.execute(
            "INSERT INTO User (id, search_name) values(?, ?) ON CONFLICT(id) DO UPDATE SET search_name = ?",
            (data[0], data[1], data[1]))
        self.connection.commit()

    def get_search_name_db(self, data):
        self.cursor.execute("SELECT search_name FROM User WHERE id == ?", (data[0],))
        response = self.cursor.fetchall()
        if len(response) == 0:
            return ''
        else:
            return response[0][0]

    def reset_search_name_db(self, data):
        self.cursor.execute("UPDATE User SET search_name = '' WHERE id = ?", (data[0],))
        self.connection.commit()

    def reset_all(self, data):
        self.cursor.execute("UPDATE User SET page = 1 , search_name = '' , function_number = -1  WHERE id = ?", (data[0],))
        self.connection.commit()
