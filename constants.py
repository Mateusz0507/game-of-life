import pygame as pg
import ctypes


ctypes.windll.user32.SetProcessDPIAware()
pg.init()


FONT_SIZE = 25
CELL_SIZE = 10
SIDEBAR_WIDTH = 100
STARTING_FPS = 3

STARTING_WINDOW_WIDTH = 600
STARTING_WINDOW_HEIGHT = 600

SCREEN_WIDTH = pg.display.Info().current_w
SCREEN_HEIGHT = pg.display.Info().current_h
