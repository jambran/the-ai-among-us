import json
import logging

from src.ai_among_us.gameplay import (
    Network,
    Button,
)
import pygame

from src.ai_among_us.gameplay.game import GameInfo

pygame.font.init()

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("The AI Among Us")

lobby_buttons = [
    Button("Join", 500, 500, (0, 0, 0)),
]


def get_center_x_coordinate(text):
    return width / 2 - text.get_width() / 2


def get_center_y_coordinate(text):
    return height / 2 - text.get_height() / 2


def draw_lobby(win, game: GameInfo):
    win.fill((128, 128, 128))

    # show title
    font = pygame.font.SysFont("comicsans", 80)
    text = font.render("Lobby", 1, (255, 0, 0), True)
    win.blit(
        text,
        (get_center_x_coordinate(text), 100),
    )

    # show join code
    font = pygame.font.SysFont("comicsans", 50)
    text = font.render(f"Invite friends: {game.id}", 1, (255, 0, 0), True)
    win.blit(
        text,
        (get_center_x_coordinate(text), get_center_y_coordinate(text)),
    )

    # create text box for user to input name
    input_box = font.render("", True, (0, 0, 0))
    win.blit(input_box, (100, 10))

    # enter button
    for button in lobby_buttons:
        button.draw(win)

    pygame.display.update()

    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False


def play():

    # todo - create game or join game path. Right now, only create new game.
    n = Network()
    game = n.game
    logging.info(f"Received game from server: {game}")
    game_info = GameInfo.parse_obj(json.loads(game))

    draw_lobby(win, game_info)


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        handlers=[logging.StreamHandler()],
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.info("Starting client...")
    play()
