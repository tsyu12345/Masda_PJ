import pygame
from pygame.locals import *
import pytmx
from pytmx.util_pygame import load_pygame
from LoadMap import Map
from MsgBox import MsgBox
from battleWindow import *
from LocalFunc import *
from Charactor import Player
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
    story_flg = True
    #Msg Box
    story1 = [
        "...",
        "",
        "",#
        "なにかが空で光っている...",
        "",
        "",#
        "マスダー、、マスダーよ。",
        "聞くがいい。",
        "ここからが魔物の住まう領域じゃ。",#
        "各地に散らばる魔物を倒し、",
        "果ての海の向こう岸にある、",
        "魔王北原の城を目指すのじゃ！。",#
        "...",
        "",
        "",#
        "え？",
        "どこに行けばいいかって？",
        "",#
        "そーですね、まずは",
        "",
        "",#
        "",
        "",
        "",#
        "",
        "",
        "",#

        ]
    msg_box = MsgBox(story1)
    msg_box_point = (50, 400, 700, 150)
    #Map
    map = Map('Map_data/SyokyuMapData.tmx')
    #Player
    player = Player('images/Characters/hero/pipo-charachip027c.png', 10, 1, screen)
    player.posX, player.posY = 400, 320
    #Draw Window

    while story_flg:
        pygame.draw.rect(screen, (0, 0, 0), Rect(0, 0, width, height))
        msg_box.display(screen, msg_box_point)
        pygame.display.update()
        for event in pygame.event.get():
            msg_box.text_update(event)
            exit_game(event)
    
    
    while main_flg:
        pygame.draw.rect(screen, (0, 0, 0), Rect(0, 0, width, height))
        map.draw_map(screen, player.posX, player.posY)
        player.display(screen)
        pygame.display.update()
        for event in pygame.event.get():
            player.move(event)
            exit_game(event)
if __name__ == '__main__':
    main()