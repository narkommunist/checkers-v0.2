import pygame
  
class InputField:
    def __init__(self, disp):
        self.display = disp
        self.base_font = pygame.font.Font(None, 32)
        self.user_text = ''
        self.input_rect = pygame.Rect(200, 200, 140, 32)
        self.rect = pygame.Rect(198, 198, 104, 36)

        self.color_active = pygame.Color('#E5E8C9')
        self.color_passive = pygame.Color('#D8D4D1')
        self.color = self.color_passive
        self.active = False
    def show(self):
        pygame.draw.rect(self.display, (0, 0, 0), self.rect)
        pygame.draw.rect(self.display, self.color, self.input_rect)
        text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
        self.display.blit(text_surface, (self.input_rect.x+5, self.input_rect.y+5))
        self.input_rect.w = max(100, text_surface.get_width()+10)
        self.rect.w = max(100, text_surface.get_width()+13)

    def Update(self, event):

        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.input_rect.collidepoint(event.pos):
                self.active = True
            else:
                self.active = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_BACKSPACE:
                self.user_text = self.user_text[:-1]
            else:
                self.user_text += event.unicode
    
        if self.active:
            self.color = self.color_active
        else:
            self.color = self.color_passive
            
        pygame.draw.rect(self.display, (0, 0, 0), self.rect)
        pygame.draw.rect(self.display, self.color, self.input_rect)
        text_surface = self.base_font.render(self.user_text, True, (255, 255, 255))
        self.display.blit(text_surface, (self.input_rect.x+5, self.input_rect.y+5))
        self.input_rect.w = max(100, text_surface.get_width()+10)
        self.rect.w = max(100, text_surface.get_width()+13)
        #pygame.display.flip()
        

