import pygame as pg
import numpy as np
import sys
from classes.Board import Board
from classes.Button import Button
from classes.Sidebar import Sidebar
from colors import BLACK
from constants import STARTING_WINDOW_WIDTH, STARTING_WINDOW_HEIGHT, \
                      SCREEN_WIDTH, SCREEN_HEIGHT, MINIMAL_WINDOW_HEIGHT, MINIMAL_WINDOW_WIDTH, DTYPE


def main():
    window_w = STARTING_WINDOW_WIDTH # Window width
    window_h = STARTING_WINDOW_HEIGHT # Window height
    pg.display.set_caption("Game of Life")
    window = pg.display.set_mode((window_w, window_h), pg.RESIZABLE)
    fullscreen = False

    # Left sidebar with buttons
    sidebar = Sidebar()
    # Main board where cells are displayed
    board = Board(window_w, window_h)

    while True:
        mouse_x, mouse_y = pg.mouse.get_pos()
        for event in pg.event.get():
            if (event.type == pg.QUIT):
                sys.exit()
            elif (event.type == pg.KEYDOWN):
                if (event.key == pg.K_ESCAPE):
                    sys.exit()
                elif (event.key == pg.K_SPACE):
                    sidebar.change_mode()
                elif (event.key == pg.K_f):
                    fullscreen = not fullscreen
                    if fullscreen:
                        window = pg.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pg.FULLSCREEN)
                    else:
                        window = pg.display.set_mode((window_w, window_h), pg.RESIZABLE)
                    board.change_size(window_w, window_h, fullscreen)
            elif (event.type == pg.VIDEORESIZE):
                if not fullscreen:
                    window_w = max(event.w, MINIMAL_WINDOW_WIDTH)
                    window_h = max(event.h, MINIMAL_WINDOW_HEIGHT)
                    window = pg.display.set_mode((window_w, window_h), pg.RESIZABLE)
                    board.change_size(window_w, window_h, fullscreen)
            elif (event.type == pg.MOUSEBUTTONDOWN):
                if(sidebar.is_mouse_over(mouse_x) and event.button == 1):
                    for button in sidebar.buttons:
                        if button.is_clicked(mouse_x, mouse_y):
                            if (button.name == 'Exit'):
                                sys.exit()
                            elif (button.name == 'Empty board'):
                                board.array = np.zeros(board.array.shape, dtype=DTYPE)
                            elif (button.name == 'Fill board'):
                                board.array = np.ones(board.array.shape, dtype=DTYPE)
                            elif (button.name == 'Increase FPS'):
                                sidebar.fps += 1
                            elif (button.name == 'Decrease FPS' and
                                    sidebar.fps > 1):
                                sidebar.fps -= 1
                            elif (button.name == 'Reset frames'):
                                sidebar.frames_counter_display.amount = 0
                            elif (button.name == 'Start/Stop'):
                                sidebar.change_mode()
        if not sidebar.is_mouse_over(mouse_x):
            if pg.mouse.get_pressed()[0]:
                board.change_cell(mouse_x, mouse_y, 1)
            elif pg.mouse.get_pressed()[2]:
                board.change_cell(mouse_x, mouse_y, 0)

        if (sidebar.is_time_to_update() and not sidebar.pause_mode):
            board.update()
            sidebar.update_timings()
        sidebar.fps_limit_display.amount = sidebar.fps

        window.fill(BLACK)
        sidebar.draw(window)
        board.draw(window, window_w, window_h)
        if not sidebar.is_mouse_over(mouse_x):
            board.draw_selected_cell(window, mouse_x, mouse_y)
        pg.display.update()


if __name__ == '__main__':
    main()
