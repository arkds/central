import sqlite3

from models import Temperature


class Repository(object):
    def __init__(self, url):
        self.connection = sqlite3.connect(url)

        c = self.connection.cursor()
        c.execute(
            "CREATE TABLE IF NOT EXISTS temperatures ("
            "id INT PRIMARY KEY,"
            "temperature INT, "
            "timestamp INT"
            ")"
        )
        self.connection.commit()

    def add_temperature(self, model: Temperature):
        c = self.connection.cursor()
        c.execute(
            "INSERT INTO temperatures (temperature, timestamp) VALUES (?, ?)",
            (model.temperature, model.timestamp)
        )
        self.connection.commit()

    def last_temperature(self):
        c = self.connection.cursor()
        c.execute(
            "SELECT a.*"
            "FROM temperatures a"
            "LEFT OUTER JOIN temperatures b"
            "    ON a.id = b.id AND a.timestamp < b.timestamp"
            ""
        )
        self.connection.commit()
