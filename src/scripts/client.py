import logging

from src.ai_among_us.gameplay import (
    Network,
    Player,
)
import pygame


pygame.font.init()

width = 700
height = 700
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Client")

def main():
    run = True
    clock = pygame.time.Clock()
    n = Network()
    game = n.game
    logging.info(f"Received game from server: {game}")

    while run:
        clock.tick(60)
        try:
            game = n.send("get")
        except:
            run = False
            logging.info("Couldn't get game")
            break
        break


def menu_screen():
    run = True
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        win.fill((128, 128, 128))
        font = pygame.font.SysFont("comicsans", 60)
        text = font.render("Click to Play!", 1, (255,0,0))
        win.blit(text, (100,200))
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                run = False

    main()


if __name__ == '__main__':
    logging.basicConfig(
        level=logging.INFO,
        handlers=[logging.StreamHandler()],
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    )
    logging.info("Starting client...")
    while True:
        menu_screen()