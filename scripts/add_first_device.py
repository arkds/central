from models import Device
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from src.config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)

Session = sessionmaker(engine)

session = Session()
session.add(Device(id=0))
session.commit()
