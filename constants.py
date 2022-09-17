﻿import pygame as pg
import ctypes


ctypes.windll.user32.SetProcessDPIAware()
pg.init()
SCREEN_WIDTH = pg.display.Info().current_w
SCREEN_HEIGHT = pg.display.Info().current_h

STARTING_FPS = 3
DTYPE = 'int8'
CELL_SIZE = 10
FONT_SIZE = 25
SIDEBAR_WIDTH = 120
BUTTON_WIDTH = 100
BUTTON_HEIGHT = 20
BUTTON_SEPARATOR = 15
STARTING_WINDOW_WIDTH = SCREEN_WIDTH//3
STARTING_WINDOW_HEIGHT = SCREEN_HEIGHT//2
MINIMAL_WINDOW_WIDTH = SIDEBAR_WIDTH + 10*CELL_SIZE
MINIMAL_WINDOW_HEIGHT = 13*BUTTON_HEIGHT + 7*BUTTON_SEPARATOR
