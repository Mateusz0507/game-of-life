import pygame as pg
from buttons import EscapeButton, EmptyButton, FillButton, FpsUpButton, FpsDownButton
from constants import MENU_WIDTH, STARTING_WINDOW_HEIGHT
from colors import DARK_GREY


class Menu:
    def __init__(self):
        self.width = MENU_WIDTH
        self.height = STARTING_WINDOW_HEIGHT
        self.buttons = [
            EscapeButton(30, 25, 40, 30, 'Esc'),
            EmptyButton(self.width/2, 65, 80, 30, 'Empty'),
            FillButton(self.width/2, 105, 80, 30, 'Fill'),
            FpsDownButton(30, 145, 40, 30, '-'),
            FpsUpButton(70, 145, 40, 30, '+')]


    def draw(self, window):
        pg.draw.rect(window, DARK_GREY, [0, 0, self.width, self.height], 0) # Background
        for button in self.buttons:
            button.draw(window)
