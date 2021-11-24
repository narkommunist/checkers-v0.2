import pygame

class Endshpile:
    def finish(self):
        background_colour = (255,255,255)
        (width, height) = (300, 200)
        screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption('Well played')
        screen.fill(background_colour)
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
