import pygame as pg
from constants import FONT_SIZE
from colors import LIGHT_GREY, BLACK


class Button:
    def __init__(self, name, x, y, width, height, sign, color = LIGHT_GREY):
        self.name = name
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sign = sign
        self.color = color
        self.rect = pg.Rect(x - width/2, y - height/2, width, height)

    def is_clicked(self, mouse_x, mouse_y):
        return self.rect.collidepoint(mouse_x, mouse_y)

    def draw(self, window):
        pg.draw.rect(window, self.color, self.rect, 0)
        pg.draw.rect(window, BLACK, self.rect, 1)
        text = pg.font.Font(None, FONT_SIZE).render(self.sign, True, BLACK)
        text_rect = text.get_rect(center=(self.x, self.y))
        window.blit(text, text_rect)
