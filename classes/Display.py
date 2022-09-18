import pygame as pg
from colors import WHITE, BLACK
from constants import FONT_SIZE, BUTTON_WIDTH, BUTTON_HEIGHT


class Display:
    # (x, y) are the coordinates to the center of the top side of the display
    def __init__(self, x, y, message, amount, color=WHITE, background=BLACK,
                 width=BUTTON_WIDTH, height=BUTTON_HEIGHT):
        self.x = x
        self.y = y
        self.message = message
        self.amount = amount
        self.color = color
        self.background = background
        self.width = width
        self.height = height
        self.total_height = (len(self.message) + 1) * self.height
        self.rect = pg.Rect(0, 0, self.width, self.total_height)
        self.rect.midtop = (x, y)

    def draw(self, surface):
        pg.draw.rect(surface, self.background, self.rect, 0)
        words = self.message.copy()
        words.append(str(self.amount))
        word_count = len(words)
        for i, word in enumerate(words):
            text = pg.font.Font(None, FONT_SIZE).render(word, True, self.color)
            text_rect = text.get_rect(center=(self.x,
                                              self.y + (0.5 + i)*self.height))
            surface.blit(text, text_rect)
