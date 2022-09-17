import pygame as pg
from colors import BLACK
from constants import SCREEN_WIDTH, SCREEN_HEIGHT, \
                      MINIMAL_WINDOW_WIDTH, MINIMAL_WINDOW_HEIGHT


class Window:
    def __init__(self, name, width, height, fullscreen=False):
        pg.display.set_caption(name)
        self.width = width
        self.height = height
        self.surface = pg.display.set_mode((width, height), pg.RESIZABLE)
        self.fullscreen = fullscreen

    def change_fullscreen_mode(self, board):
        self.fullscreen = not self.fullscreen
        if self.fullscreen:
            self.surface = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT),
                                         pg.FULLSCREEN)
        else:
            self.surface = pg.display.set_mode((self.width, self.height),
                                                 pg.RESIZABLE)
        board.change_size(self.width, self.height, self.fullscreen)

    def resize(self, new_width, new_height, board):
        if not self.fullscreen:
            self.width = max(new_width, MINIMAL_WINDOW_WIDTH)
            self.height = max(new_height, MINIMAL_WINDOW_HEIGHT)
            self.surface = pg.display.set_mode((self.width, self.height),
                                               pg.RESIZABLE)
            board.change_size(self.width, self.height, self.fullscreen)

    def draw(self, sidebar, board, mouse_x, mouse_y):
        self.surface.fill(BLACK)
        sidebar.draw(self.surface)
        board.draw(self.surface)
        if board.is_mouse_over(mouse_x):
            board.draw_selected_cell(self.surface, mouse_x, mouse_y)
        pg.display.update()
