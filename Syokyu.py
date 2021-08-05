import pygame
from pygame.locals import *
import pytmx
from pytmx.util_pygame import load_pygame
import sys
import csv
import os
from LoadMap import Map
from MsgBox import MsgBox
from battleWindow import *
from LocalFunc import *
from EventSE import EventSound as ES
from EventSE import PlayerSound as PS
GS = 32
DOWN, LEFT, RIGHT, UP = 0,1,2,3

def main():
    #init pygame
    pygame.init()
    font = pygame.font.Font('font_data/PixelMplus-20130602/PixelMplus10-Regular.ttf', 25)
    font.set_bold(True)
    width = 800  # screeen
    height = 640
    pygame.display.set_mode((width, height), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("マス打")
    # 必要なオブジェクト（部品）
    main_flg =True

    #Map
    map = Map('Map_data/SyokyuMapData.tmx')
    #Player
    player = split_image_load(load_image('images/Characters/hero/pipo-charachip027c.png'))
    #Draw Window
    while main_flg:

        map.draw_map(screen)
        pygame.display.update()
        for event in pygame.event.get():
            

if __name__ == '__main__':
    main()