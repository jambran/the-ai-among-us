import pygame

class Button:
    """
    Object to represent a button in pygame
    """
    def __init__(self, text: str, x: int, y: int, color: str):
        self.text = text
        self.x = x
        self.y = y
        self.color = color
        self.width = 150
        self.height = 100

    def draw(self, win):
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.height))
        font = pygame.font.SysFont("comicsans", 40)
        text = font.render(self.text, 1, (255,255,255))
        win.blit(
            text,
            (self.x + round(self.width/2) - round(text.get_width()/2), self.y + round(self.height/2) - round(text.get_height()/2)),
        )

    def click(self, pos):
        x1 = pos[0]
        y1 = pos[1]
        if all(self.x <= x1 <= self.x + self.width,
               self.y <= y1 <= self.y + self.height):
            return True

        return False
