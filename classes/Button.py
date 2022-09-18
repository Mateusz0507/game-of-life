import pygame as pg
from colors import LIGHT_GREY, BLACK
from constants import FONT_SIZE, BUTTON_WIDTH, BUTTON_HEIGHT


class Button:
    # (x, y) are the coordinates to the center of the top side of the button
    def __init__(
        self,
        name,
        x,
        y,
        sign,
        color=LIGHT_GREY,
        width=BUTTON_WIDTH,
        height=BUTTON_HEIGHT,
    ):
        self.name = name
        self.x = x
        self.y = y
        self.sign = sign
        self.color = color
        self.width = width
        self.height = height
        self.rect = pg.Rect(0, 0, width, height)
        self.rect.midtop = (x, y)

    def is_clicked(self, mouse_x, mouse_y):
        return self.rect.collidepoint(mouse_x, mouse_y)

    def draw(self, surface):
        pg.draw.rect(surface, self.color, self.rect, 0)
        pg.draw.rect(surface, BLACK, self.rect, 1)
        text = pg.font.Font(None, FONT_SIZE).render(self.sign, True, BLACK)
        text_rect = text.get_rect(center=(self.x, self.y + self.height / 2))
        surface.blit(text, text_rect)
