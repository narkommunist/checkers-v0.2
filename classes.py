import pygame
from consts import *

pictures = { 
    BLACK: './sourses/black.png',
    WHITE: './sourses/white.png'
}

class Board:
    def __init__(self):
        self.field = []
        self.b_left = self.w_left = 12
        self.b_kings = self.w_kings = 0

    def generate(self):
        for i in range(7, 4, -1):
            if i == 6: s = 1    # <------------
            else: s = 0         # TRY TO FIX IT
            for j in range(s, 8, 2):
                print (i, j)
                self.field.append(Checker(WHITE, j, i))
                
        for i in range(3):
            if i == 1: s = 0    # <------------
            else: s = 1         # TRY TO FIX IT
            for j in range(s, 8, 2):
                self.field.append(Checker(BLACK, j, i))

    def get_elems(self):
        return self.field


class Checker(pygame.sprite.Sprite):
    def __init__(self, col, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.color = col
        img = pictures[col]
        self.image = pygame.image.load(img).convert_alpha()
        self.rect = self.image.get_rect(center = ((8 - x)*100 - 50, y * 100 + 50))
        self.marked = False
        self.x = x
        self.y = y

    def select(self):   #   <---FIX
        self.marked = True
        #x2, y2 = self.x - 100, self.y - 100
    
    def unselect(self):
        self.marked = False
    
    def get_size(self):
        return [self.x, self.y]

    def get_color(self):
        return self.color

    def ind_to_coord(self):
        y = self.y * 100 + 50
        x = (8 - self.x)*100 - 50
        return [x, y]

    def move(self, place):
        x = place[0]
        y = place[1]
        self.rect.x = x
        self.rect.y = y
    
