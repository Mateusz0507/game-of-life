import pygame as pg
import time
from constants import MENU_WIDTH, CELL_SIZE, STARTING_FPS
from colors import WHITE, RED, GREEN


class Board:
	def __init__(self, window_w, window_h):
		# self.cells_w/self.cells_h inform about number
		# of cells in every row/column of self.array
		self.cells_w = (window_w - MENU_WIDTH)//CELL_SIZE
		self.cells_h = window_h//CELL_SIZE
		self.array = [[0 for i in range(self.cells_w)]
						 for j in range(self.cells_h)]
		self.pause_mode = True
		self.fps = STARTING_FPS
		self.last_update = time.time()

	def change_cell(self, mouse_x, mouse_y, new_value):
		y = mouse_y // CELL_SIZE
		x = (mouse_x - MENU_WIDTH) // CELL_SIZE
		if (0 <= x < self.cells_w and 0 <= y < self.cells_h):
			self.array[y][x] = new_value

	def is_time_to_update(self):
		if (time.time()-self.last_update > 1/self.fps):
			return True
		return False

	def update(self):
		new_array = [[0 for i in range(self.cells_w)]
						for j in range(self.cells_h)]
		for x in range(self.cells_w):
			for y in range(self.cells_h):
				sum = 0
				for coords in [
						(x-1, y-1), (x, y-1), (x+1, y-1),
						(x-1, y),			  (x+1, y),
						(x-1, y+1),	(x, y+1), (x+1, y+1)
						]:
					if (0 <= coords[0] < self.cells_w and
							0 <= coords[1] < self.cells_h):
						sum += self.array[coords[1]][coords[0]]
				if ((self.array[y][x] == 1 and (sum == 2 or sum == 3)) or
						(self.array[y][x] == 0 and sum == 3)):
					new_array[y][x] = 1
				else:
					new_array[y][x] = 0
		self.array = new_array
		self.last_update = time.time()

	def draw(self, window, window_w, window_h):
		for x in range(self.cells_w):
			for y in range(self.cells_h):
				if (self.array[y][x] == 1):
					pg.draw.rect(window, WHITE, [
												x*CELL_SIZE + MENU_WIDTH,
												y*CELL_SIZE,
												CELL_SIZE,
												CELL_SIZE
												 ], 0)
		color = RED if self.pause_mode else GREEN
		corners = [
			[MENU_WIDTH, 0],
			[window_w, 0],
			[window_w, window_h],
			[MENU_WIDTH, window_h]
			]
		pg.draw.polygon(window, color, corners, 5)
