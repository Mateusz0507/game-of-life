import pygame as pg
from functions import *
from constants import *
from gui import Gui


def main():
	gui = Gui()

	pg.init()
	gui.window = pg.display.set_mode((gui.window_w, gui.window_h))
	pg.display.set_caption("Game of Life")

	refresh_cooldown = 60/gui.fps

	while gui.running:
		gui.clock.tick(60)
		for event in pg.event.get():
			if event.type == pg.QUIT:
				pg.quit()
			if event.type == pg.KEYDOWN:
				if event.key == pg.K_ESCAPE:
					gui.running = False
				elif event.key == pg.K_SPACE:
					gui.pause_mode = not gui.pause_mode
				elif event.key == pg.K_a and gui.fps > 1:
					gui.fps -= 1
				elif event.key == pg.K_d:
					gui.fps += 1
			if pg.mouse.get_pressed()[0]:
				x, y = pg.mouse.get_pos()
				gui.new_tick[y//CELL_SIZE][x//CELL_SIZE] = 1
			elif pg.mouse.get_pressed()[2]:
				x, y = pg.mouse.get_pos()
				gui.new_tick[y//CELL_SIZE][x//CELL_SIZE] = 0

		gui.window.fill(BLACK)

		if not gui.pause_mode and refresh_cooldown < 1:
			gui.last_tick, gui.new_tick = calculating(gui.last_tick, gui.new_tick, gui.cells_w, gui.cells_h)
			refresh_cooldown = 60/gui.fps
		refresh_cooldown -= 1

		draw_board(gui.window, gui.new_tick, gui.cells_w, gui.cells_h)
		if gui.pause_mode:
			draw_pause_mode(gui.window, gui.window_w, gui.window_h, 5)
		pg.display.update()


if __name__ == '__main__':
	main()
