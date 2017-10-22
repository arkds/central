import os

DATABASE_URL = os.getenv('DATABASE_URL')
ROOT = os.path.dirname(os.path.realpath(__file__))
PORT = os.getenv('PORT')
