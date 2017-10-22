from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import DATABASE_URL
from models import Device

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(engine)

session = Session()
session.add(Device(id=666))
session.commit()
