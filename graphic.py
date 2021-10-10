import pygame
from consts import *
from classes import *

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
        for i in range(7, 4, -1):
            if i == 6: s = 1    # <------------
            else: s = 0         # TRY TO FIX IT
            for j in range(s, 8, 2):
                if self.board.get_elems()[i][j].get_color() == WHITE:
                    self.draw_item(j*100 + 50, (8-i)*100 - 50, self.board.get_elems()[i][j].get_color())
        for i in range(3):
            if i == 1: s = 0    # <------------
            else: s = 1         # TRY TO FIX IT
            for j in range(s, 8, 2):
                if self.board.get_elems()[i][j].get_color() == BLACK:
                    self.draw_item(j*100 + 50, (8-i)*100-50, self.board.get_elems()[i][j].get_color())
                    
    def draw_item(self, x, y, color):
        r = 45
        if color == BLACK: img = './sourses/black.png'
        else: img = './sourses/white.png'
        #if self.marked: img = './sourses/selected.png'

        IMAGE = pygame.image.load(img).convert_alpha()
        IMAGE = pygame.transform.scale(IMAGE, (90, 90))
        rect = IMAGE.get_rect()
        rect.center = (x, y)
        self.win.blit(IMAGE, rect)

    def show_tip(self, x, y):
        print('[CALCULATING TIP]')
        img = './sourses/tip.png'
        IMAGE = pygame.image.load(img).convert_alpha()
        IMAGE = pygame.transform.scale(IMAGE, (30, 30))
        rect = IMAGE.get_rect()
        rect.center = (x, y)
        self.win.blit(IMAGE, rect)