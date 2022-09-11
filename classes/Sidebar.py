import pygame as pg
from classes.Button import Button
from classes.Display import Display
from constants import SIDEBAR_WIDTH, STARTING_WINDOW_HEIGHT, STARTING_FPS
from colors import DARK_GREY


class Sidebar:
    def __init__(self):
        self.width = SIDEBAR_WIDTH
        self.height = STARTING_WINDOW_HEIGHT
        self.buttons = [
            Button('Exit', 35, 25, 50, 30, 'Exit'),
            Button('Empty board', self.width/2, 65, 80, 30, 'Empty'),
            Button('Fill board', self.width/2, 105, 80, 30, 'Fill'),
            Button('Decrease FPS', 30, 175, 40, 30, '-'),
            Button('Increase FPS', 70, 175, 40, 30, '+')]
        self.fps_display = Display(self.width/2, 145, 80, 30,
                                   'FPS', STARTING_FPS)

    def is_mouse_over_sidebar(self, mouse_x):
        return mouse_x <= SIDEBAR_WIDTH

    def draw(self, window):
        pg.draw.rect(window, DARK_GREY, [0, 0, self.width, self.height], 0)
        self.fps_display.draw(window)
        for button in self.buttons:
            button.draw(window)
