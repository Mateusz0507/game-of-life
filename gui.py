import pygame as pg
from constants import CELL_SIZE


class Gui:
    def __init__(self):
        self.window_w = 600 # Window width
        self.window_h = 600 # Window height
        self.window = pg.display.set_mode((self.window_w, self.window_h))
        self.cells_w = self.window_w//CELL_SIZE # Number of cells in every row
        self.cells_h = self.window_h//CELL_SIZE # Number of cells in every column
        self.board = [[0 for i in range(self.cells_w)] for j in range(self.cells_h)] # Board of cells
        self.fps = 3
        self.running = True
        self.pause_mode = True
        self.clock = pg.time.Clock()
