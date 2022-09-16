import pygame as pg
import ctypes


ctypes.windll.user32.SetProcessDPIAware()
pg.init()

STARTING_FPS = 3
STARTING_WINDOW_WIDTH = 600
STARTING_WINDOW_HEIGHT = 600

CELL_SIZE = 10
FONT_SIZE = 25
BUTTON_HEIGHT = 30
SIDEBAR_WIDTH = 200
MINIMAL_WINDOW_WIDTH = 600
MINIMAL_WINDOW_HEIGHT = 600
SCREEN_WIDTH = pg.display.Info().current_w
SCREEN_HEIGHT = pg.display.Info().current_h
