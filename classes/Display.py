import pygame as pg
from colors import WHITE, BLACK
from constants import FONT_SIZE


class Display:
    def __init__(self, x, y, width, height, prefix, amount,
                 color = WHITE, background = BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.prefix = prefix
        self.amount = amount
        self.color = color
        self.background = background
        self.rect = pg.Rect(0, 0, width, height)
        self.rect.center = (x, y)

    def draw(self, window):
        pg.draw.rect(window, self.background, self.rect, 0)
        message = f'{self.prefix}: {self.amount}'
        text = pg.font.Font(None, FONT_SIZE).render(message, True, self.color)
        text_rect = text.get_rect(center=(self.x, self.y))
        window.blit(text, text_rect)
