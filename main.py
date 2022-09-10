import pygame as pg
import sys
from classes.Sidebar import Sidebar
from classes.Board import Board
from classes.Button import EscapeButton, EmptyButton, FillButton, \
						   FpsUpButton, FpsDownButton
from colors import BLACK
from constants import STARTING_WINDOW_WIDTH, STARTING_WINDOW_HEIGHT


def main():
	pg.init()
	window_w = STARTING_WINDOW_WIDTH # Window width
	window_h = STARTING_WINDOW_HEIGHT # Window height
	window = pg.display.set_mode((window_w, window_h))
	pg.display.set_caption("Game of Life")

	# Left sidebar with buttons
	sidebar = Sidebar()
	# Main board where cells are displayed
	board = Board(window_w, window_h)

	while True:
		mouse_x, mouse_y = pg.mouse.get_pos()
		for event in pg.event.get():
			if (event.type == pg.QUIT):
				sys.exit()
			elif (event.type == pg.MOUSEBUTTONDOWN and
					sidebar.is_mouse_over_sidebar(mouse_x)):
				for button in sidebar.buttons:
					if button.if_clicked(mouse_x, mouse_y):
						if isinstance(button, EscapeButton):
							sys.exit()
						elif isinstance(button, EmptyButton):
							button.use(board.array,
									   board.cells_w, board.cells_h)
						elif isinstance(button, FillButton):
							button.use(board.array,
									   board.cells_w, board.cells_h)
						elif isinstance(button, FpsUpButton):
							board.fps += 1
						elif (isinstance(button, FpsDownButton) and
								board.fps > 1):
							board.fps -= 1
			elif (event.type == pg.KEYDOWN):
				if (event.key == pg.K_ESCAPE):
					sys.exit()
				elif (event.key == pg.K_SPACE):
					board.pause_mode = not board.pause_mode
		if not sidebar.is_mouse_over_sidebar(mouse_x):
			if pg.mouse.get_pressed()[0]:
				board.change_cell(mouse_x, mouse_y, 1)
			elif pg.mouse.get_pressed()[2]:
				board.change_cell(mouse_x, mouse_y, 0)

		if (board.is_time_to_update() and not board.pause_mode):
			board.update()
		sidebar.fps_display.amount = board.fps

		window.fill(BLACK)
		sidebar.draw(window)
		board.draw(window, window_w, window_h)
		pg.display.update()


if __name__ == '__main__':
	main()
