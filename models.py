from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class PeripheralDevice(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
    secret = Column(String)
    hub = Column(Integer, ForeignKey('hubs.id'))


class Hub(Base):
    __tablename__ = 'hubs'

    id = Column(Integer, primary_key=True)
    user = Column(Integer, ForeignKey('users.id'))


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String)
