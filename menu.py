import pygame as pg
from constants import MENU_WIDTH, STARTING_WINDOW_HEIGHT
from constants import DARK_GREY


class Menu:
    def __init__(self):
        self.width = MENU_WIDTH
        self.height = STARTING_WINDOW_HEIGHT


    def draw(self, window):
        pg.draw.rect(window, DARK_GREY, [0, 0, self.width, self.height], 0) # Background
