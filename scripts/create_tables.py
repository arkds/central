from models import Base
from sqlalchemy import create_engine

from src.config import DATABASE_URL

engine = create_engine(DATABASE_URL, echo=True)

Base.metadata.create_all(engine)
