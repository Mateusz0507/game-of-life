import pygame as pg
from colors import RED, GREEN


def change_mode(sidebar):
    sidebar.pause_mode = not sidebar.pause_mode
    for button in sidebar.buttons:
        if (button.name == 'Start/Stop'):
            button.color = GREEN if sidebar.pause_mode else RED
            button.sign = 'Start' if sidebar.pause_mode else 'Stop'
