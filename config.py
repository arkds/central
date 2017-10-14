import os

TEMPERATURE_UPDATE_INTERVAL = 60  # seconds

ROOT = os.path.dirname(os.path.realpath(__file__))
DB_URL = os.path.join(ROOT, 'db.sqlite3')

TGB_TOKEN = os.getenv('TGB_TOKEN')
