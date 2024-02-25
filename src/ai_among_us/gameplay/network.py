import socket

from src.ai_among_us.config import settings
from src.utils.exception_logging import log_exception


class Network:
    MAX_GAME_SIZE = 2048 * 2


    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = settings.GAMEPLAY_SERVER_ADDRESS
        self.port = settings.GAMEPLAY_SERVER_PORT
        self.address = (self.server, self.port)
        self.game = self.connect()


    @log_exception
    def connect(self):
        self.client.connect(self.address)
        communication = self.client.recv(self.MAX_GAME_SIZE).decode()
        return communication

    @log_exception
    def send(self, data):
        self.client.send(str.encode(data))
        communication = self.client.recv(self.MAX_GAME_SIZE).decode()
        return communication
