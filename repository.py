from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL
from models import Temperature


class Repository(object):
    def __init__(self, url):
        self.engine = create_engine(DATABASE_URL, echo=True)
        self.Session = sessionmaker(bind=self.engine)

    def add(self, entry):
        session = self.Session()
        session.add(entry)
        session.commit()

    def temperatures(self, device_id):
        session = self.Session()
        return session.query(Temperature).filter(
            Temperature.device_id == device_id
        )
