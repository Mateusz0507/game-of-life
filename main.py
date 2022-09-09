import pygame as pg
from menu import Menu
from board import Board
from buttons import EmptyButton, FillButton
from colors import BLACK
from constants import STARTING_WINDOW_WIDTH, STARTING_WINDOW_HEIGHT, MENU_WIDTH



def main():
	pg.init()
	window_w = STARTING_WINDOW_WIDTH # Window width
	window_h = STARTING_WINDOW_HEIGHT # Window height
	window = pg.display.set_mode((window_w, window_h))
	pg.display.set_caption("Game of Life")

	menu = Menu() # Left sidebar with buttons
	board = Board(window_w, window_h) # Main board where cells are displayed

	fps = 3
	clock = pg.time.Clock()
	refresh_cooldown = 60/fps

	running = True
	while running:
		clock.tick(60)
		mouse_x, mouse_y = pg.mouse.get_pos()

		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()

			if event.type == pg.MOUSEBUTTONDOWN and mouse_x <= MENU_WIDTH:
				for button in menu.buttons:
					if button.if_clicked(mouse_x, mouse_y):
						if type(button) == EmptyButton:
							button.use(board.array, board.cells_w, board.cells_h)
						if type(button) == FillButton:
							button.use(board.array, board.cells_w, board.cells_h)

			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					running = False
				elif event.key == pg.K_SPACE:
					board.pause_mode = not board.pause_mode
				elif event.key == pg.K_a and fps > 1:
					fps -= 1
				elif event.key == pg.K_d:
					fps += 1

			if pg.mouse.get_pressed()[0] and mouse_x >= MENU_WIDTH:
				board.change_cell(mouse_x, mouse_y, 1)
			elif pg.mouse.get_pressed()[2] and mouse_x >= MENU_WIDTH:
				board.change_cell(mouse_x, mouse_y, 0)

		if not board.pause_mode and refresh_cooldown < 1:
			board.calculating_new_array()
			refresh_cooldown = 60/fps
		refresh_cooldown -= 1

		window.fill(BLACK)
		menu.draw(window)
		board.draw(window, window_w, window_h)
		pg.display.update()


if __name__ == '__main__':
	main()
