import pygame as pg
import numpy as np
import sys
from classes.Window import Window
from classes.Button import Button
from classes.Sidebar import Sidebar
from classes.Board import Board
from colors import BLACK
from constants import DTYPE, SCREEN_WIDTH, SCREEN_HEIGHT, \
                      MINIMAL_WINDOW_HEIGHT, MINIMAL_WINDOW_WIDTH


def main():
    # Window of the program
    window = Window('Game of Life')
    # Left sidebar with buttons
    sidebar = Sidebar()
    # Board where cells are displayed
    board = Board(window.width, window.height)

    while True:
        mouse_x, mouse_y = pg.mouse.get_pos()
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                sys.exit()
            elif (event.type == pg.KEYDOWN):
                if (event.key == pg.K_ESCAPE):
                    sys.exit()
                elif (event.key == pg.K_SPACE):
                    sidebar.change_pause_mode()
                elif (event.key == pg.K_f):
                    window.change_fullscreen_mode(board)
            elif (event.type == pg.VIDEORESIZE):
                window.resize(event.w, event.h, board)
            elif (event.type == pg.MOUSEBUTTONDOWN):
                if(sidebar.is_mouse_over(mouse_x) and event.button == 1):
                    for button in sidebar.buttons:
                        if button.is_clicked(mouse_x, mouse_y):
                            if (button.name == 'Exit'):
                                sys.exit()
                            elif (button.name == 'Empty board'):
                                board.array = np.zeros(board.array.shape,
                                                       dtype=DTYPE)
                            elif (button.name == 'Fill board'):
                                board.array = np.ones(board.array.shape,
                                                      dtype=DTYPE)
                            elif (button.name == 'Increase FPS'):
                                sidebar.fps += 1
                            elif (button.name == 'Decrease FPS' and
                                    sidebar.fps > 1):
                                sidebar.fps -= 1
                            elif (button.name == 'Reset frames'):
                                sidebar.frames_counter_display.amount = 0
                            elif (button.name == 'Start/Stop'):
                                sidebar.change_pause_mode()
        if board.is_mouse_over(mouse_x):
            if pg.mouse.get_pressed()[0]:
                board.change_cell(mouse_x, mouse_y, 1)
            elif pg.mouse.get_pressed()[2]:
                board.change_cell(mouse_x, mouse_y, 0)

        if (sidebar.is_time_to_update() and not sidebar.pause_mode):
            board.update()
            sidebar.update_timings()
        sidebar.fps_limit_display.amount = sidebar.fps
        window.draw(sidebar, board, mouse_x, mouse_y)


if __name__ == '__main__':
    main()
