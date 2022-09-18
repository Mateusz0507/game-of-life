import pygame as pg
import numpy as np
import time
from classes.Button import Button
from classes.Display import Display
from colors import DARK_GREY, BLACK, RED, YELLOW, GREEN
from constants import (
    STARTING_FPS,
    STARTING_WINDOW_HEIGHT,
    SIDEBAR_WIDTH as SW,
    BUTTON_SEPARATOR as BS,
    BUTTON_WIDTH as BW,
    BUTTON_HEIGHT as BH,
)


class Sidebar:
    def __init__(self, width=SW, height=STARTING_WINDOW_HEIGHT):
        self.width = width
        self.height = height
        self.pause_mode = True
        self.fps = STARTING_FPS
        self.last_update = time.time()
        # Array of board's update timings from last second
        self.timings_array = np.array([self.last_update], dtype="float64")

        self.buttons = [
            Button("Start/Stop", 0.5 * SW, BS, "Start", GREEN),
            Button("Empty board", 0.5 * SW, 2 * BS + 1 * BH, "Empty"),
            Button("Fill board", 0.5 * SW, 3 * BS + 2 * BH, "Fill"),
            Button(
                "Decrease FPS",
                0.5 * SW - 0.25 * BW,
                4 * BS + 5 * BH,
                "-",
                width=0.5 * BW,
            ),
            Button(
                "Increase FPS",
                0.5 * SW + 0.25 * BW,
                4 * BS + 5 * BH,
                "+",
                width=0.5 * BW,
            ),
            Button("Reset frames", 0.5 * SW, 5 * BS + 11 * BH, "Reset"),
            Button("Exit", 0.5 * SW, 6 * BS + 12 * BH, "Exit"),
        ]
        self.fps_limit_display = Display(
            0.5 * SW, 4 * BS + 3 * BH, ["FPS limit:"], self.fps
        )
        self.actual_fps_display = Display(
            0.5 * SW, 4 * BS + 6 * BH, ["actual FPS"], 0, BLACK, DARK_GREY
        )
        self.frames_counter_display = Display(
            0.5 * SW, 5 * BS + 8 * BH, ["frames", "counter:"], 0
        )

    def is_mouse_over(self, mouse_x):
        return mouse_x <= self.width

    def is_time_to_update(self):
        self.last_update = time.time()
        return self.last_update - self.timings_array[-1] > 1 / self.fps

    def update_timings(self):
        self.frames_counter_display.amount += 1
        self.timings_array = np.append(self.timings_array, self.last_update)
        # Remove outdated timings (older than a second ago)
        for timing in self.timings_array:
            if self.last_update - timing > 1:
                self.timings_array = np.delete(self.timings_array, 0)
            else:
                break
        self.update_actual_fps()

    def update_actual_fps(self):
        actual_fps = self.timings_array.size
        self.actual_fps_display.color = (
            GREEN
            if actual_fps / self.fps > 0.75
            else YELLOW
            if actual_fps / self.fps > 0.5
            else RED
        )
        self.actual_fps_display.amount = actual_fps

    def change_pause_mode(self):
        self.pause_mode = not self.pause_mode
        if self.pause_mode:
            self.actual_fps_display.color = BLACK
        for button in self.buttons:
            if button.name == "Start/Stop":
                button.color = GREEN if self.pause_mode else RED
                button.sign = "Start" if self.pause_mode else "Stop"

    def draw(self, surface):
        pg.draw.rect(surface, DARK_GREY, [0, 0, self.width, surface.get_height()], 0)
        self.fps_limit_display.draw(surface)
        self.frames_counter_display.draw(surface)
        self.actual_fps_display.draw(surface)
        for button in self.buttons:
            button.draw(surface)
