import pygame as pg
import numpy as np
import time
from classes.Button import Button
from classes.Display import Display
from colors import DARK_GREY, BLACK, RED, GREEN
from constants import STARTING_FPS, STARTING_WINDOW_HEIGHT, \
                      SIDEBAR_WIDTH as SW, BUTTON_WIDTH as BW, BUTTON_HEIGHT as BH, BUTTON_SEPARATOR as BS


class Sidebar:
    def __init__(self):
        self.width = SW
        self.height = STARTING_WINDOW_HEIGHT
        self.pause_mode = True
        self.fps = STARTING_FPS
        self.last_update = time.time()
        # Array of board's update timings from last second
        self.timings_array = np.array([self.last_update], dtype='float64')

        self.buttons = [
            Button('Start/Stop', 0.5*SW, BS + 0.5*BH, BW, BH, 'Start', GREEN),
            Button('Empty board', 0.5*SW, 2*BS + 1.5*BH, BW, BH, 'Empty'),
            Button('Fill board', 0.5*SW, 3*BS + 2.5*BH, BW, BH, 'Fill'),
            Button('Decrease FPS', 0.5*SW - 0.25*BW, 4*BS + 5.5*BH, 0.5*BW, BH, '-'),
            Button('Increase FPS', 0.5*SW + 0.25*BW, 4*BS + 5.5*BH, 0.5*BW, BH, '+'),
            Button('Reset frames', 0.5*SW, 5*BS + 11.5*BH, BW, BH, 'Reset'),
            Button('Exit', 0.5*SW, 6*BS + 12.5*BH, BW, BH, 'Exit')
            ]
        self.fps_display = Display(0.5*SW, 4*BS + 4*BH, BW, BH, ['FPS limit:'], self.fps)
        self.actual_frames_display = Display(0.5*SW, 4*BS + 7*BH, BW, BH, ['actual FPS'], 0, BLACK, DARK_GREY)
        self.frames_display = Display(0.5*SW, 5*BS + 9.5*BH, BW, BH, ['frames', 'counter:'], 0)

    def is_mouse_over(self, mouse_x):
        return mouse_x <= self.width

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
        pg.draw.rect(window, DARK_GREY,
                     [0, 0, self.width, window.get_height()], 0)
        self.fps_display.draw(window)
        self.frames_display.draw(window)
        self.actual_frames_display.draw(window)
        for button in self.buttons:
            button.draw(window)
