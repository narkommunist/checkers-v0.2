import pygame
from consts import *
from classes import *
from graphic import Drawer

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ultra-Checkers')


def main():
	run = True
	board = Board()
	board.generate()
	drawer = Drawer(board, WIN)
	while run:
		cur_pos = pygame.mouse.get_pos()
		#print(cur_pos)
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				print('[BUTTON_PRESSED]')
				for j in board.get_elems():
					if drawer.check_press(cur_pos, j):
						j.select()
						drawer.show_tip(j.ind_to_coord())
					else:
						j.unselect()
		drawer.draw_board()
		pygame.display.update()
	pygame.quit()

main()