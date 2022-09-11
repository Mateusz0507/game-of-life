import pygame as pg
from colors import RED, GREEN


def change_mode(board, sidebar):
    board.pause_mode = not board.pause_mode
    for button in sidebar.buttons:
        if (button.name == 'Start/Stop'):
            button.color = GREEN if board.pause_mode else RED
            button.sign = 'Start' if board.pause_mode else 'Stop'
