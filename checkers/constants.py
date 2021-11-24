import pygame
import os.path

WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# rgb
#BROWN = 
WHITE = (234, 182, 126, 92)
BLACK = (79, 52, 16, 31)
BRAWN = (102, 62, 20)
GREY = (0,0,0)
GREEN = (0, 255, 0, 30)

PICS = {BLACK: 'sourses/black.png', WHITE: 'sourses/white.png', GREEN: 'sourses/tip.png'}
CROWN = pygame.transform.scale(pygame.image.load(os.path.abspath('checkers/sourses/crown.png')), (44, 25))
