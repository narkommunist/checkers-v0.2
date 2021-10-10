import pygame
from consts import *

class Board:
    def __init__(self):
        #self.field = [[], [], [], [], [], [], [], []]
        self.items = []
        self.selected = None
        self.b_left = self.w_left = 12
        self.b_kings = self.w_kings = 0

    def generate(self, win):
        items_b, items_w = [], []
        for i in range(7, 4, -1):
            if i == 6: s = 1    # <------------
            else: s = 0         # TRY TO FIX IT
            for j in range(s, 8, 2):
                items_b.append(Item(i+j, win, BLUE, 50 + 100*j, 50 + 100*i))
                print('[ADDED b]' + str(i+j))
        
        for i in range(3):
            if i == 1: s = 0    # <------------
            else: s = 1         # TRY TO FIX IT
            for j in range(s, 8, 2):
                items_w.append(Item(i+j, win, WHITE, 50 + 100*j, 50 + 100*i))
                print('[ADDED w]' + str(i+j))
        self.items = [items_w, items_b]

    def draw_board(self, win):
        image = pygame.image.load('./sourses/field.png')
        image = pygame.transform.scale(image, (800, 800))
        #win.fill(BLACK)
        win.blit(image, (0, 0))
        for el in self.items:
            for i in el:
                i.draw()

    def get_items(self):
        return self.items


class Item:
    def __init__(self, id, win, col, x, y):
        self.win = win
        self.id = id
        self.color = col
        self.x = x
        self.y = y
        self.marked = False

    def draw(self):
        r = 45
        #pygame.draw.circle(self.win, self.color, (self.x, self.y), r)
        if self.color == BLUE: img = './sourses/black.png'
        else: img = './sourses/white.png'
        if self.marked: img = './sourses/selected.png'

        IMAGE = pygame.image.load(img).convert_alpha()
        IMAGE = pygame.transform.scale(IMAGE, (90, 90))
        rect = IMAGE.get_rect()
        rect.center = (self.x, self.y)
        self.win.blit(IMAGE, rect)

    def show_tip(self, x, y):
        print('[CALCULATING TIP]')
        img = './sourses/tip.png'
        IMAGE = pygame.image.load(img).convert_alpha()
        IMAGE = pygame.transform.scale(IMAGE, (30, 30))
        rect = IMAGE.get_rect()
        rect.center = (x, y)
        self.win.blit(IMAGE, rect)

    def select(self):
        self.marked = True
        x1, y1 = self.x + 100, self.y - 100
        x2, y2 = self.x - 100, self.y - 100
        self.show_tip(x1, y1)
        print('[TIP SHOWED]')
        #self.show_tip(x2, y2)
    
    def unselect(self):
        self.marked = False
    
    def get_size(self):
        return [self.x, self.y]

    def get_color(self):
        return self.color
