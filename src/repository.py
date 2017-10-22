from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import DATABASE_URL


class Repository(object):
    def __init__(self, url):
        self.engine = create_engine(DATABASE_URL, echo=True)
        self.Session = sessionmaker(bind=self.engine)

    def add(self, entry):
        session = self.Session()
        session.add(entry)
        session.commit()
