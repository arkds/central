import psycopg2

from config import DATABASE_URL


class Repository(object):
    def __init__(self, url):
        self.connection = psycopg2.connect(DATABASE_URL)

    def __
