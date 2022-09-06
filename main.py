# LPM/PPM - komórki, ESC - exit, A/S/D - zarządzanie czasem
import pygame as pg
pg.init()

#screenObject = pg.display.Info()
# win_width = screenObject.current_w
#win_height = screenObject.current_h
win_width = win_height = 600 #<-----

WIN = pg.display.set_mode((win_width, win_height))
pg.display.set_caption("Game of Life")

block_size = 15 #<-----
FPS = 3 #<-----

blocks = win_height//block_size
last_round = [[0 for i in range(blocks)] for i in range(blocks)]
new_round = [[0 for i in range(blocks)] for i in range(blocks)]

BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
################################################################################
def calculating():
	for x in range(blocks):
		for y in range(blocks):
			last_round[x][y] = new_round[x][y]

	for x in range(blocks):
		for y in range(blocks):
			sum = 0
			for coords in [(x-1,y-1),(x-1,y),(x-1,y+1),(x,y-1),(x,y+1),(x+1,y-1),(x+1,y),(x+1,y+1)]:
				if 0 <= coords[0] < blocks and 0 <= coords[1] < blocks:
					sum += last_round[coords[0]][coords[1]]

			if (last_round[x][y]==1 and (sum==2 or sum==3)) or (last_round[x][y]==0 and sum==3):
				new_round[x][y] = 1
			else:
				new_round[x][y] = 0

def draw_board():
	for column in range(blocks):
		for row in range(blocks):
			if new_round[column][row] == 1:
				pg.draw.rect(WIN, WHITE, [column*block_size, row*block_size, block_size, block_size], 0)

def draw_pause():
	pg.draw.line(WIN, RED, [0, win_height], [win_width, win_height], 5)
	pg.draw.line(WIN, RED, [win_width, 0], [win_width, win_height], 5)
	pg.draw.line(WIN, RED, [0, 0], [0, win_height], 5)
	pg.draw.line(WIN, RED, [0, 0], [win_width, 0], 5)
################################################################################
running = True
pause = True
refresh_cooldown = 60/FPS
while running:
	pg.time.Clock().tick(60)
	for event in pg.event.get():
		if event.type == pg.QUIT:
			pg.quit()
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_s:
				pause = not pause
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_a and FPS > 1:
				FPS -= 1
		if event.type == pg.KEYDOWN:
			if event.key == pg.K_d:
				FPS += 1
			if event.key == pg.K_ESCAPE:
				running = False
		if pg.mouse.get_pressed()[0]:
			x, y = pg.mouse.get_pos()
			new_round[x//block_size][y//block_size] = 1
		elif pg.mouse.get_pressed()[2]:
			x, y = pg.mouse.get_pos()
			new_round[x//block_size][y//block_size] = 0

	WIN.fill(BLACK)

	if not pause and refresh_cooldown < 1:
		calculating()
		refresh_cooldown = 60/FPS
	refresh_cooldown -= 1

	draw_board()
	if pause:
		draw_pause()
	pg.display.update()
################################################################################
#WIN.blit(pg.image.load('tło.png'),(0,0))
#SCREEN.blit(pg.font.SysFont('Sans',30).render('MODE',True,BLACK,WHITE),(40,110))
#pg.draw.circle(SCREEN,BLACK,(x,y),SIZE,0)
#pg.draw.rect(SCREEN,WHITE,[25, 175, 100, 370],0)
#pg.draw.line(SCREEN,BLACK,[75,220],[75,520],3)
