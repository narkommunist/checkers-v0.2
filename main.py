import pygame
from consts import *
from classes import *

WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ultra-Checkers')


def main():
	run = True
	board = Board()
	board.generate(WIN)
	while run:
		cur_pos = pygame.mouse.get_pos()
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				run = False
			if event.type == pygame.MOUSEBUTTONDOWN:
				print('[BUTTON_PRESSED]')
				for i in board.get_items():
					for j in i:
						if (j.get_size()[0]-50 < cur_pos[0] < j.get_size()[0]+50) and (j.get_size()[1]-50 < cur_pos[1] < j.get_size()[1]+50) and (j.get_color() != SELECTED): 
							print('[TRACKED_BP]')
							j.select()
						else: j.unselect()
		board.draw_board(WIN)
		pygame.display.update()
	pygame.quit()

main()