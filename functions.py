import pygame as pg
from constants import *


def calculating(old_board, new_board, width, height):
	for x in range(width):
		for y in range(height):
			old_board[y][x] = new_board[y][x]

	for x in range(width):
		for y in range(height):
			sum = 0
			for coords in [(y-1,x-1),(y-1,x),(y-1,x+1),(y,x-1),(y,x+1),(y+1,x-1),(y+1,x),(y+1,x+1)]:
				if 0 <= coords[0] < width and 0 <= coords[1] < height:
					sum += old_board[coords[0]][coords[1]]

			if (old_board[y][x]==1 and (sum==2 or sum==3)) or (old_board[y][x]==0 and sum==3):
				new_board[y][x] = 1
			else:
				new_board[y][x] = 0
	return old_board, new_board


def draw_board(window, board, width, height):
	for x in range(width):
		for y in range(height):
			if board[y][x] == 1:
				pg.draw.rect(window, WHITE, [x*CELL_SIZE, y*CELL_SIZE, CELL_SIZE, CELL_SIZE], 0)


def draw_pause_mode(window, width, height, size):
	corners = [[0, 0], [width, 0], [width, height], [0, height]]
	pg.draw.polygon(window, RED, corners, size)
