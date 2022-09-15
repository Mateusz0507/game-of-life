import pygame as pg
import numpy as np
from constants import SIDEBAR_WIDTH, CELL_SIZE, SCREEN_WIDTH, SCREEN_HEIGHT
from colors import WHITE, RED, GREEN


class Board:
    def __init__(self, window_w, window_h):
        # self.c_width and self.c_height are size
        # of the board expressed in number of cells
        self.c_width, self.c_height = \
            self.calculate_cell_coords(window_w, window_h)
        self.array = np.zeros((self.c_width, self.c_height), dtype='int8')

    # Gets coordinates on screen expressed in pixels,
    # returns coordinates of cell on the board
    def calculate_cell_coords(self, input_x, input_y):
        x = (input_x - SIDEBAR_WIDTH)//CELL_SIZE
        y = input_y//CELL_SIZE
        return x, y

    # Resize the board to the given size
    def change_size(self, window_w, window_h, fullscreen):
        if fullscreen:
            new_c_width, new_c_height = \
                self.calculate_cell_coords(SCREEN_WIDTH, SCREEN_HEIGHT)
        else:
            new_c_width, new_c_height = \
                self.calculate_cell_coords(window_w, window_h)
        new_array = np.zeros((new_c_width, new_c_height), dtype='int8')
        min_w = min(self.c_width, new_c_width)
        min_h = min(self.c_height, new_c_height)
        part_to_keep = self.array[:min_w, :min_h]
        new_array[:min_w, :min_h] = part_to_keep
        self.array = new_array
        self.c_width = new_c_width
        self.c_height = new_c_height

    def change_cell(self, mouse_x, mouse_y, value):
        x, y = self.calculate_cell_coords(mouse_x, mouse_y)
        if (0 <= x < self.c_width and 0 <= y < self.c_height):
            self.array[x, y] = value

    def update(self):
        new_array = np.zeros((self.c_width, self.c_height), dtype='int8')
        for x in range(self.c_width):
            for y in range(self.c_height):
                sum = 0
                for coords in [
                        (x-1, y-1), (x, y-1), (x+1, y-1),
                        (x-1, y),             (x+1, y),
                        (x-1, y+1), (x, y+1), (x+1, y+1)
                        ]:
                    if (0 <= coords[0] < self.c_width and
                            0 <= coords[1] < self.c_height):
                        sum += self.array[coords[0], coords[1]]
                if ((self.array[x, y] == 1 and (sum == 2 or sum == 3)) or
                        (self.array[x, y] == 0 and sum == 3)):
                    new_array[x, y] = 1
                else:
                    new_array[x, y] = 0
        self.array = new_array

    def draw(self, window, window_w, window_h):
        for x in range(self.c_width):
            for y in range(self.c_height):
                if (self.array[x, y] == 1):
                    pg.draw.rect(window, WHITE, [
                                                x*CELL_SIZE + SIDEBAR_WIDTH,
                                                y*CELL_SIZE,
                                                CELL_SIZE,
                                                CELL_SIZE
                                                 ], 0)

    def draw_selected_cell(self, window, mouse_x, mouse_y):
        x, y = self.calculate_cell_coords(mouse_x, mouse_y)
        pg.draw.rect(window, RED, [
                                    x*CELL_SIZE + SIDEBAR_WIDTH,
                                    y*CELL_SIZE,
                                    CELL_SIZE,
                                    CELL_SIZE
                                        ], 2)
