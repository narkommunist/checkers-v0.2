import pygame
from consts import *
from classes import *

pictures = { 
    BLACK: './sourses/black.png',
    WHITE: './sourses/white.png'
}

class Drawing:
    def __init__(self, board, win):
        self.board = board
        self.win = win
        pass

    def draw_board(self):
        image = pygame.image.load('./sourses/field.png')
        image = pygame.transform.scale(image, (800, 800))
        #win.fill(BLACK)
        self.win.blit(image, (0, 0))
        for i in self.board.get_elems():
            self.draw_item(i)
                    
    def draw_item(self, checker:Item):
        y = checker.y * 100 + 50
        x = (8 - checker.x)*100 - 50
        img = pictures[checker.color]
        #if self.marked: img = './sourses/selected.png'

        IMAGE = pygame.image.load(img).convert_alpha()
        IMAGE = pygame.transform.scale(IMAGE, (90, 90))
        rect = IMAGE.get_rect()
        rect.center = (y, x)
        self.win.blit(IMAGE, rect)

    def show_tip(self, x, y):
        print('[CALCULATING TIP]')
        img = './sourses/tip.png'
        IMAGE = pygame.image.load(img).convert_alpha()
        IMAGE = pygame.transform.scale(IMAGE, (30, 30))
        rect = IMAGE.get_rect()
        rect.center = (x, y)
        self.win.blit(IMAGE, rect)