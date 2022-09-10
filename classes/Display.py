import pygame as pg
from constants import FONT_SIZE
from colors import WHITE, BLACK


class Display:
    def __init__(self, x, y, width, height, prefix, amount):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.prefix = prefix
        self.amount = amount
        self.rect = pg.Rect(x - width/2, y - height/2, width, height)

    def draw(self, window):
        pg.draw.rect(window, BLACK, self.rect, 0)
        message = f'{self.prefix}: {self.amount}'
        text = pg.font.Font(None, FONT_SIZE).render(message, True, WHITE)
        text_rect = text.get_rect(center=(self.x, self.y))
        window.blit(text, text_rect)
