import pygame as pg
from components import EscapeButton, EmptyButton, FillButton, \
                        FpsUpButton, FpsDownButton, Display
from constants import MENU_WIDTH, STARTING_WINDOW_HEIGHT, STARTING_FPS
from colors import DARK_GREY


class Menu:
    def __init__(self):
        self.width = MENU_WIDTH
        self.height = STARTING_WINDOW_HEIGHT
        self.buttons = [
            EscapeButton(30, 25, 40, 30, 'Esc'),
            EmptyButton(self.width/2, 65, 80, 30, 'Empty'),
            FillButton(self.width/2, 105, 80, 30, 'Fill'),
            FpsDownButton(30, 175, 40, 30, '-'),
            FpsUpButton(70, 175, 40, 30, '+')]
        self.fps_display = Display(self.width/2, 145, 80, 30, 'FPS', STARTING_FPS)


    def draw(self, window):
        pg.draw.rect(window, DARK_GREY, [0, 0, self.width, self.height], 0) # Background
        self.fps_display.draw(window)
        for button in self.buttons:
            button.draw(window)
