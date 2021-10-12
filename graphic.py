import pygame
from classes import *

pictures = { 
    BLACK: './sourses/black.png',
    WHITE: './sourses/white.png'
}

class Drawer:
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
            self.draw_Checker(i)
                    
    def draw_Checker(self, checker:Checker):
        x = checker.ind_to_coord()[0]
        y = checker.ind_to_coord()[1]
        img = pictures[checker.color]
        if checker.marked: img = './sourses/selected.png'

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

    def check_press(self, m_pos, checker:Checker):
        x = checker.ind_to_coord()[0]
        y = checker.ind_to_coord()[1]
        if (x-50 <= m_pos[0] <= x+50) and (y-50 <= m_pos[1] <= y+50):
            print('[',checker.x, checker.y, ']')
        return True if (x-50 <= m_pos[0] <= x+50) and (y-50 <= m_pos[1] <= y+50) else False