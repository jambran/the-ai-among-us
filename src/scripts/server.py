import logging
import socket
from _thread import start_new_thread
import random

from src.ai_among_us.config import settings
from src.ai_among_us.gameplay.game import Game

CAPTIAL_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def threaded_client(conn, game):
    # conn.send(str.encode(str("hello")))
    conn.send(str.encode(game.game_info.json()))
    # conn.send(str.encode(str(game)))

    # reply = ""
    # while True:
    #     try:
    #         data = conn.recv(4096).decode()
    #
    #         if gameId in games:
    #             game = games[gameId]
    #
    #             if not data:
    #                 break
    #             else:
    #                 if data == "reset":
    #                     game.resetWent()
    #                 elif data != "get":
    #                     game.play(p, data)
    #
    #                 conn.sendall(pickle.dumps(game))
    #         else:
    #             break
    #     except:
    #         break

    # print("Lost connection")
    # try:
    #     del games[gameId]
    #     print("Closing Game", gameId)
    # except:
    #     pass
    # idCount -= 1
    conn.close()


def create_game_id():
    character_choices = random.choices(CAPTIAL_LETTERS, k=4)
    # todo - we'll need to make sure the id is unique when we get to a server hosting multiple games
    id_ = r"".join(character_choices)
    return id_


def main():
    server = settings.gameplay_server_address
    port = settings.gameplay_server_port

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.bind((server, port))
    except socket.error as e:
        str(e)

    s.listen(2)
    logging.info("Waiting for a connection, Server Started")

    while True:
        conn, addr = s.accept()
        logging.info(f"Connected to: {addr}")

        id_ = create_game_id()

        new_game = Game(id_)
        logging.info(f"New game created: {new_game.game_info.dict()}")

        start_new_thread(threaded_client, (conn, new_game))

if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        handlers=[logging.StreamHandler()],
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    main()
