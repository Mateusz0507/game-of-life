import pygame as pg
from colors import WHITE, BLACK
from constants import FONT_SIZE


class Display:
    def __init__(self, x, y, width, height, words, amount,
                 color = WHITE, background = BLACK):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.words = words
        self.amount = amount
        self.color = color
        self.background = background

    def draw(self, window):
        rectangle = pg.Rect(0, 0, self.width, (len(self.words)+1)*self.height)
        rectangle.center = (self.x, self.y)
        pg.draw.rect(window, self.background, rectangle, 0)
        messages = self.words.copy()
        messages.append(str(self.amount))
        for i, message in enumerate(messages):
            text = pg.font.Font(None, FONT_SIZE).render(message, True,
                                                        self.color)
            text_rect = text.get_rect(center=(self.x, self.y +
                                              (i - (len(messages)-1)/2)*self.height))
            window.blit(text, text_rect)
