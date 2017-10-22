from sqlalchemy import Column, Float, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Temperature(Base):
    __tablename__ = 'temperatures'

    id = Column(Integer, primary_key=True)
    device_id = Column(Integer, ForeignKey('devices.id'), nullable=False)
    timestamp = Column(Float, unique=True)
    temperature = Column(Float)


class Device(Base):
    __tablename__ = 'devices'

    id = Column(Integer, primary_key=True)
