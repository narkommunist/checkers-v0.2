import pygame
import subprocess
import os.path
#from IF import InputField

class Option:

    hovered = False
    
    def __init__(self, text, pos):
        self.text = text
        self.pos = pos
        self.set_rect()
        self.draw()
            
    def draw(self):
        self.set_rend()
        #display.blit(menu_font.render(self.text, True, (0, 0, 0)), self.rect)
        image = pygame.image.load(os.path.abspath('checkers/sourses/button.png'))
        image = pygame.transform.scale(image, (170, 35))
        display.blit(self.rend, self.rect)
        butt_rect = self.rect
        #butt_rect.topleft = (self.pos[0]-50, self.pos[1]-50)
        #display.blit(image, butt_rect)
        
        
    def set_rend(self):
        self.rend = menu_font.render(self.text, True, self.get_color())
        
    def get_color(self):
        if self.hovered:
            return (244, 230, 213)
        else:
            return (150, 150, 150)
        
    def set_rect(self):
        self.set_rend()
        self.rect = self.rend.get_rect()
        self.rect.topleft = self.pos


def signin(display, login, passw):
    display.fill((0, 0, 0))
    pass

pygame.init()
display = pygame.display.set_mode((480, 320))
print(os.path.abspath('checkers/sourses/icon.png'))
icon = pygame.image.load(os.path.abspath('checkers/sourses/icon.png'))
pygame.display.set_icon(icon)
pygame.display.set_caption('PoluPoker 2D')
bg = pygame.image.load(os.path.abspath('checkers/sourses/bg.png'))
bg = pygame.transform.scale(bg, (480, 320))
menu_font = pygame.font.Font(None, 40)
options = [Option("NEW GAME", (155, 105)), Option("SIGN IN", (150, 155)),
           Option("OPTIONS", (160, 205))]
#login_input = InputField(display)
while True:
    pygame.event.pump()
    display.fill((0, 0, 0))
    display.blit(bg, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN and options != []:
            if options[0].rect.collidepoint(pygame.mouse.get_pos()):
                subprocess.call('main.py', shell=True)
            if options[1].rect.collidepoint(pygame.mouse.get_pos()):
                #options = []
                pass
        if options == []:
            #login_input.show()
            #login_input.Update(event)
            pass
        else:
            for option in options:
                if option.rect.collidepoint(pygame.mouse.get_pos()):
                    option.hovered = True
                else:
                    option.hovered = False
                option.draw()
    pygame.display.update()
