import pygame as pg
import numpy as np
import time
from classes.Button import Button
from classes.Display import Display
from constants import SIDEBAR_WIDTH, STARTING_WINDOW_HEIGHT, STARTING_FPS
from colors import BLACK, DARK_GREY, RED, GREEN


class Sidebar:
    def __init__(self):
        self.width = SIDEBAR_WIDTH
        self.height = STARTING_WINDOW_HEIGHT

        self.pause_mode = True
        self.fps = STARTING_FPS
        self.last_update = time.time()
        # Array of board's update timings from last second
        self.timings_array = np.array([self.last_update], dtype='float64')

        self.buttons = [
            Button('Exit', self.width/2, 25, 80, 30, 'Exit'),
            Button('Empty board', self.width/2, 65, 80, 30, 'Empty'),
            Button('Fill board', self.width/2, 105, 80, 30, 'Fill'),
            Button('Decrease FPS', 30, 175, 40, 30, '-'),
            Button('Increase FPS', 70, 175, 40, 30, '+'),
            Button('Reset frames', self.width/2, 245, 80, 30, 'Reset'),
            Button('Start/Stop', self.width/2, 285, 80, 30, 'Start', GREEN)
            ]
        self.fps_display = Display(self.width/2, 145, 80, 30, 'FPS', self.fps)
        self.frames_display = Display(self.width/2, 215, 80, 30, 'frames', 0)
        self.actual_frames_display = Display(self.width/2, 325, 80, 30,
                                             'actual', 0, BLACK, DARK_GREY)

    def is_mouse_over(self, mouse_x):
        return mouse_x <= SIDEBAR_WIDTH

    def is_time_to_update(self):
        self.last_update = time.time()
        return self.last_update-self.timings_array[-1] > 1/self.fps

    def update_timings(self):
        self.frames_display.amount += 1
        self.actual_frames_display.amount = self.timings_array.size
        self.timings_array = np.append(self.timings_array, self.last_update)
        for timing in self.timings_array:
            if self.last_update-timing > 1:
                self.timings_array = np.delete(self.timings_array, 0)
            else:
                break

    def change_mode(self):
        self.pause_mode = not self.pause_mode
        for button in self.buttons:
            if (button.name == 'Start/Stop'):
                button.color = GREEN if self.pause_mode else RED
                button.sign = 'Start' if self.pause_mode else 'Stop'

    def draw(self, window):
        pg.draw.rect(window, DARK_GREY, [0, 0, self.width, window.get_height()], 0)
        self.fps_display.draw(window)
        self.frames_display.draw(window)
        self.actual_frames_display.draw(window)
        for button in self.buttons:
            button.draw(window)
