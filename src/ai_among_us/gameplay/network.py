import logging
import socket

from src.ai_among_us.config import settings


class Network:
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = settings.GAMEPLAY_SERVER_ADDRESS
        self.port = settings.GAMEPLAY_SERVER_PORT
        self.address = (self.server, self.port)
        self.game = self.connect()

    def connect(self):
        try:
            self.client.connect(self.address)
            communication = self.client.recv(2048 * 2).decode()
            return communication
        except socket.error as e:
            logging.error(e)
            raise e

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048).decode()
        except socket.error as e:
            logging.error(e)
            raise e
