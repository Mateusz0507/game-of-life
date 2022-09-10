import pygame as pg
from constants import FONT_SIZE
from colors import LIGHT_GREY, BLACK


class Button:
    def __init__(self, x, y, width, height, sign):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.sign = sign
        self.rect = pg.Rect(x - width/2, y - height/2, width, height)

    def if_clicked(self, mouse_x, mouse_y):
        if self.rect.collidepoint(mouse_x, mouse_y):
            return True
        return False

    def draw(self, window):
        pg.draw.rect(window, LIGHT_GREY, self.rect, 0)
        pg.draw.rect(window, BLACK, self.rect, 1)
        text = pg.font.Font(None, FONT_SIZE).render(self.sign, True, BLACK)
        text_rect = text.get_rect(center=(self.x, self.y))
        window.blit(text, text_rect)


class EmptyButton(Button):
    def use(self, board, width, height):
        for x in range(width):
            for y in range(height):
                board[y][x] = 0


class FillButton(Button):
    def use(self, board, width, height):
        for x in range(width):
            for y in range(height):
                board[y][x] = 1


class EscapeButton(Button):
    pass


class FpsUpButton(Button):
    pass


class FpsDownButton(Button):
    pass
