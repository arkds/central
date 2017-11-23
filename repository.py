from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL
from models import Temperature


class Repository(object):
    def __init__(self, url):
        self.engine = create_engine(DATABASE_URL, echo=True)
        self.Session = sessionmaker(bind=self.engine)

    # def add(self, entry):
    #     session = self.Session()
    #     session.add(entry)
    #     session.commit()

    def add_all(self, entries):
        session = self.Session()
        session.add_all(entries)
        session.commit()

    def temperatures(self, device_id):
        session = self.Session()
        return session.query(Temperature).filter(
            Temperature.device_id == device_id
        ).order_by(
            Temperature.timestamp.desc()
        )

    def delete_temperatures(self, temperatures):
        session = self.Session()
        for temp in temperatures:
            device_id, timestamp = temp['device_id'], temp['timestamp']
            session.delete(
                Temperature(
                    device_id=device_id,
                    timestamp=timestamp
                )
            )
