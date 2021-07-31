import pygame
from pygame.locals import *
import sys

class MsgBox():

    def __init__(self, msg_list:list):
        self.msg_list = msg_list
        self.text_index = 0
        self.font = pygame.font.Font('font_data/misaki_gothic_2nd.ttf', 25)
        self.font.set_bold(True)
        self.text_render = self.font.render("", True, (255, 255, 255))
    
    def display(self, screen:pygame.Surface, point:tuple):
        msg_box = pygame.Rect(point[0], point[1], point[2], point[3])
        pygame.draw.rect(screen, (255, 255, 255), msg_box, 6)  # 縁
        pygame.draw.rect(screen, (0, 0, 0), msg_box)  # メッセージボックス
        screen.blit(self.text_render, (70, 410))  # メッセージの表示
        
        pygame.display.update()
    
    def text_update(self, index):
        
