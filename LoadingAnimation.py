import pygame
from pygame.locals import *
from pygame import mixer

class TextAnimation():
    def __init__(self, text, screen):
        self.w, self.h = screen.get_size()
        self.text = text
        self.posX = self.w
        self.posY = self.h / 2
        self.end_flg = False
    
    def display(self,screen:pygame.Surface):
        pygame.draw.rect(screen, (0, 0, 0), Rect(0, 0, self.w, self.h))
        font = pygame.font.Font('font_data/PixelMplus-20130602/PixelMplus12-Regular.ttf', 50)
        font.set_bold(True)
        render = font.render(self.text, True, (255,255,255))
        screen.blit(render, (self.posX, self.posY))
        pygame.display.update()
        #pygame.time.Clock().tick(60)
        pygame.time.wait(1)
        self.posX -= 1
        if self.posX == -1000:
            self.end_flg = True

if __name__ == '__main__':
    pygame.init()
    #font = pygame.font.Font('font_data/PixelMplus-20130602/PixelMplus12-Regular.ttf', 20)
    #font.set_bold(True)
    width = 800 #screeen
    height = 640
    pygame.display.set_mode((width, height), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("マス打")
    test = TextAnimation("よみこみちゅう", screen)
    while test.end_flg == False:
        test.display(screen)


