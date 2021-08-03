import pygame
from pygame.locals import *
import pytmx
from pytmx.util_pygame import load_pygame
import sys
import csv
import os
from LoadMap import Map
from MsgBox import MsgBox

GS = 32
DOWN, LEFT, RIGHT, UP = 0,1,2,3


def load_image(filename):
    image = pygame.image.load(filename)
    return image #return pygame imgae object

def split_image(image):
    """分割したイメージを格納したリストを返す"""
    imageList = []
    for i in range(0, 128, GS):
        for j in range(0, 128, GS):
            surface = pygame.Surface((GS, GS))
            surface.blit(image, (0, 0), (j, i, GS, GS))
            surface.convert()
            imageList.append(surface)
            #print(imageList)
    return imageList
class Player:
    animcycle = 24  # アニメーション速度
    frame = 0

    def __init__(self, name, pos, dir):
        self.name = name  # プレイヤー名（ファイル名と同じ）
        self.images = split_image(load_image("%s.png" % name))
        self.image = self.images[0]  # 描画中のイメージ
        self.x, self.y = pos[0], pos[1]  # 座標（単位：マス）
        self.rect = self.image.get_rect(topleft=(self.x*GS, self.y*GS))
        self.direction = dir

    def update(self):
        # キャラクターアニメーション（frameに応じて描画イメージを切り替える）
        self.frame += 1
        self.image = self.images[self.direction *
                                 4+self.frame/self.animcycle % 4]

    def move(self, dir, map):
        """プレイヤーを移動"""
        if dir == DOWN:
            self.direction = DOWN
            if map.is_movable(self.x, self.y+1):
                self.y += 1
                self.rect.top += GS
        elif dir == LEFT:
            self.direction = LEFT
            if map.is_movable(self.x-1, self.y):
                self.x -= 1
                self.rect.left -= GS
        elif dir == RIGHT:
            self.direction = RIGHT
            if map.is_movable(self.x+1, self.y):
                self.x += 1
                self.rect.left += GS
        elif dir == UP:
            self.direction = UP
            if map.is_movable(self.x, self.y-1):
                self.y -= 1
                self.rect.top -= GS

    def draw(self, screen):
        screen.blit(self.image, self.rect)


def main():
    pygame.init()
    font = pygame.font.Font('font_data/misaki_gothic_2nd.ttf', 25)
    font.set_bold(True)
    width = 800  # screeen
    height = 640
    pygame.display.set_mode((width, height), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("マス打")
    # 必要なオブジェクト（部品）
    main_flg = True
    move_play = True
    type_play = False
    #player オブジェクト(仮)
    player_imgs = split_image(load_image('images/Characters/hero/pipo-charachip027c.png'))
    direction = DOWN
    player_x, player_y = 200/GS,150/GS #初期位置
    animcycle = 24
    frame = 0
    clock = pygame.time.Clock()
    
    #マップオブジェクト
    map = Map('Map_data/tyutorial_test.tmx')
    
    #メッセージボックス
    text_list = [
        "ほっほっほ。ワシは仏じゃ。",
        "ここではこのゲームの操作方法について説明するぞ。",
        "",#1
        "え？画面にキャラクターがいないって？",
        "",
        "",#2
        "決して、説明用のキャラを用意するのが面倒だったとか",
        "締め切りまでに間に合わなかったとか、",
        "そーゆーのではないから！！",#3
        "おほん。",
        "では、気を取り直して、まずキャラ操作の説明じゃ。",
        "",#4
        "基本操作は簡単。",
        "キーボードの➞キーで動かすことができるぞ。",
        "",#5
        "すこし歩きまわってみるがよい。",
        "",
        "",#6
    ]

    #text_render = font.render("", True, (255, 255, 255))
    msg_box_point = (50, 400, 700, 150)
    msg_box = MsgBox(text_list)
    while main_flg:
        while move_play:
            clock.tick(60)
            frame += 1
            player_img = player_imgs[int(direction*4 + frame/animcycle%3)]
            map.draw_map(screen)
            screen.blit(player_img, (player_x*GS, player_y*GS))
            msg_box.display(screen, msg_box_point)
            pygame.display.update()
            #pygame.time.wait(100)
            #pygame.time.wait(80)
            #text_render = font.render(text_list[0:int(frame/10)], True, (255, 255, 255))
            
            for event in pygame.event.get():
                msg_box.text_update(event)
                if msg_box.end_flg == True:
                    pygame.quit()
                    sys.exit()
                if event.type == QUIT:          # 閉じるボタンが押されたとき
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:       # キーを押したとき
                    if event.key == K_ESCAPE:   # Escキーが押されたとき
                        pygame.quit()
                        sys.exit()
                    if event.key == K_DOWN:
                        direction = DOWN
                    #if is_movable(x, y+1):
                        player_y += 1
                    if event.key == K_LEFT:
                        direction = LEFT
                #if is_movable(x-1, y):
                        player_x -= 1
                    if event.key == K_RIGHT:
                        direction = RIGHT
                #if is_movable(x+1, y):
                        player_x += 1
                    if event.key == K_UP:
                        direction = UP
                #if is_movable(x, y-1):
                        player_y -= 1            

if __name__ == "__main__":
    main()