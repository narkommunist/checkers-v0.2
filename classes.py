import pygame
from consts import *

class Board:
    def __init__(self):
        self.field = [[None]*8,
                      [None]*8,
                      [None]*8,
                      [None]*8,
                      [None]*8,
                      [None]*8,
                      [None]*8,
                      [None]*8,]
        self.b_left = self.w_left = 12
        self.b_kings = self.w_kings = 0

    def generate(self):
        for i in range(7, 4, -1):
            if i == 6: s = 1    # <------------
            else: s = 0         # TRY TO FIX IT
            for j in range(s, 8, 2):
                print (i, j)
                self.field[i][j] = Item(WHITE)
                
        for i in range(3):
            if i == 1: s = 0    # <------------
            else: s = 1         # TRY TO FIX IT
            for j in range(s, 8, 2):
                self.field[i][j] = Item(BLACK)

    '''def debug(self):
        for i in self.field:
            print(i)'''
    def get_elems(self):
        return self.field


class Item:
    def __init__(self, col):
        self.color = col
        self.marked = False

    def select(self):
        self.marked = True
        x1, y1 = self.x + 100, self.y - 100
        x2, y2 = self.x - 100, self.y - 100
        self.show_tip(x1, y1)
        print('[TIP SHOWED]')
    
    def unselect(self):
        self.marked = False
    
    def get_size(self):
        return [self.x, self.y]

    def get_color(self):
        return self.color

'''b = Board()
b.generate()
b.debug()'''