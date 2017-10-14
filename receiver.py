"""Deploying this module requires prior UART setup. Read the official docs."""

from time import *

from serial import Serial

from config import DB_URL, TEMPERATURE_UPDATE_INTERVAL
from models import Temperature
from repository import Repository


class Receiver(object):
    def __init__(self, baud_rate):
        self.port = Serial('/dev/serial0', baudrate=baud_rate)

    def read(self):
        temperature = self.port.read()[0]
        timestamp = time()
        return Temperature(temperature, timestamp)


def main():
    receiver = Receiver(9600)
    repository = Repository(DB_URL)
    while True:
        repository.add_temperature(receiver.read())
        sleep(TEMPERATURE_UPDATE_INTERVAL)


def _test():
    while True:
        receiver = Receiver(9600)
        print(receiver.read()[0])


if __name__ == '__main__':
    _test()
