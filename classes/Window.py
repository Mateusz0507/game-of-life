import pygame as pg
from colors import BLACK
from constants import (
    CELL_SIZE,
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    STARTING_WINDOW_WIDTH,
    STARTING_WINDOW_HEIGHT,
    MINIMAL_WINDOW_WIDTH,
    MINIMAL_WINDOW_HEIGHT,
)


class Window:
    def __init__(
        self,
        name,
        width=STARTING_WINDOW_WIDTH,
        height=STARTING_WINDOW_HEIGHT,
        fullscreen=False,
    ):
        pg.display.set_caption(name)
        self.width = width
        self.height = height
        self.surface = pg.display.set_mode((width, height), pg.RESIZABLE)
        self.fullscreen = fullscreen

    def change_fullscreen_mode(self, board):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            self.surface = pg.display.set_mode(
                (SCREEN_WIDTH, SCREEN_HEIGHT), pg.FULLSCREEN
            )
        else:
            self.surface = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)
        board.change_size(self.width, self.height, self.fullscreen)

    def resize(self, event_width, event_height, board):
        if not self.fullscreen:
            new_width = CELL_SIZE * (event_width // CELL_SIZE)
            new_height = CELL_SIZE * (event_height // CELL_SIZE)
            self.width = max(new_width, MINIMAL_WINDOW_WIDTH)
            self.height = max(new_height, MINIMAL_WINDOW_HEIGHT)
            self.surface = pg.display.set_mode((self.width, self.height), pg.RESIZABLE)
            board.change_size(self.width, self.height, self.fullscreen)

    def draw(self, sidebar, board, mouse_x, mouse_y):
        self.surface.fill(BLACK)
        sidebar.draw(self.surface)
        board.draw(self.surface)
        if board.is_mouse_over(mouse_x):
            board.draw_selected_cell(self.surface, mouse_x, mouse_y)
        pg.display.update()
