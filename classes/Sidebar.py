import pygame as pg
import time
from classes.Button import Button
from classes.Display import Display
from constants import SIDEBAR_WIDTH, STARTING_WINDOW_HEIGHT, STARTING_FPS
from colors import DARK_GREY, GREEN


class Sidebar:
    def __init__(self):
        self.width = SIDEBAR_WIDTH
        self.height = STARTING_WINDOW_HEIGHT

        self.pause_mode = True
        self.fps = STARTING_FPS
        self.last_update = time.time()

        self.buttons = [
            Button('Exit', self.width/2, 25, 80, 30, 'Exit'),
            Button('Empty board', self.width/2, 65, 80, 30, 'Empty'),
            Button('Fill board', self.width/2, 105, 80, 30, 'Fill'),
            Button('Decrease FPS', 30, 175, 40, 30, '-'),
            Button('Increase FPS', 70, 175, 40, 30, '+'),
            Button('Reset frames', self.width/2, 245, 80, 30, 'Reset'),
            Button('Start/Stop', self.width/2, 285, 80, 30, 'Start', GREEN)
            ]
        self.fps_display = Display(self.width/2, 145, 80, 30, 'FPS',
                                   STARTING_FPS)
        self.frames_display = Display(self.width/2, 215, 80, 30, 'frames', 0)

    def is_time_to_update(self):
        return time.time()-self.last_update > 1/self.fps

    def is_mouse_over(self, mouse_x):
        return mouse_x <= SIDEBAR_WIDTH

    def draw(self, window):
        pg.draw.rect(window, DARK_GREY, [0, 0, self.width, self.height], 0)
        self.fps_display.draw(window)
        self.frames_display.draw(window)
        for button in self.buttons:
            button.draw(window)
