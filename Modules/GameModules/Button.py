import pygame
from pygame.locals import *

class Button:
    def __init__(self, btn_text:str, text_col:tuple, btn_col:tuple, postion:tuple):
        font = pygame.font.Font('font_data/misaki_gothic_2nd.ttf', 20)
        font.set_bold(True)
        self.pos = postion
        self.btn_col = btn_col
        self.text = font.render(btn_text, True, text_col)
        self.body = pygame.Rect(postion[0], postion[1], postion[2], postion[3])

    def display(self, screen):
        pygame.draw.rect(screen, (255, 255,255), self.body, 6) #縁
        pygame.draw.rect(screen, self.btn_col, self.body)
        screen.blit(self.text, (self.pos[0] + 10 , self.pos[1] + 5))

    def select_detect(self, event:pygame.event, key_code):
        if event.type == KEYDOWN:
            if event.key == key_code:
                return True