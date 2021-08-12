import pygame 
from pygame.locals import *

class EndLole():
    def __init__(self, screen:pygame.Surface):
        self.screen = screen
        w,h = self.screen.get_size()
        self.posX = w/2
        self.posY = h 

    def display(self):
        font = pygame.font.Font('font_data/PixelMplus-20130602/PixelMplus12-Regular.ttf', 100)
        font.set_bold(True)
        text = font.render(self., True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.posX, self.posY))
        self.screen.blit(text, text_rect)