import sqlite3
from dataclasses import dataclass


@dataclass
class MovieDb:
    def __init__(self):
        self.connection = sqlite3.connect('movie_tracker.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute("CREATE TABLE IF NOT EXISTS User (id INTEGER NOT NULL PRIMARY KEY, page INTEGER);")

    def insert_db(self, data):
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
