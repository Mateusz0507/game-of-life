import pygame as pg
from functions import *
from constants import *


def main():
	pg.init()
	window_w = 600 # Window width
	window_h = 600 # Window height
	window = pg.display.set_mode((window_w, window_h))
	pg.display.set_caption("Game of Life")

	cells_w = window_w//CELL_SIZE # Number of cells in every row
	cells_h = window_h//CELL_SIZE # Number of cells in every column

	last_tick = [[0 for i in range(cells_w)] for j in range(cells_h)]
	new_tick = [[0 for i in range(cells_w)] for j in range(cells_h)]

	fps = 3
	refresh_cooldown = 60/fps

	running = True
	pause_mode = True

	clock = pg.time.Clock()
	while running:
		clock.tick(60)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					running = False
				elif event.key == pg.K_SPACE:
					pause_mode = not pause_mode
				elif event.key == pg.K_a and fps > 1:
					fps -= 1
				elif event.key == pg.K_d:
					fps += 1
			if pg.mouse.get_pressed()[0]:
				x, y = pg.mouse.get_pos()
				new_tick[y//CELL_SIZE][x//CELL_SIZE] = 1
			elif pg.mouse.get_pressed()[2]:
				x, y = pg.mouse.get_pos()
				new_tick[y//CELL_SIZE][x//CELL_SIZE] = 0

		window.fill(BLACK)

		if not pause_mode and refresh_cooldown < 1:
			last_tick, new_tick = calculating(last_tick, new_tick, cells_w, cells_h)
			refresh_cooldown = 60/fps
		refresh_cooldown -= 1

		draw_board(window, new_tick, cells_w, cells_h)
		if pause_mode:
			draw_pause_mode(window, window_w, window_h, 5)
		pg.display.update()


if __name__ == '__main__':
	main()
