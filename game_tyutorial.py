import pygame
from pygame.locals import *
import pytmx
from pytmx.util_pygame import load_pygame
import sys
import csv
import os

GS = 16
DOWN, LEFT, RIGHT, UP = "s", "a", "d", "w"


def load_image(filename, colorkey=None):
    image = pygame.image.load(filename)
    image = image.convert()
    return image

def mapchip_split(pixcel, path):
    chip_img = pygame.image.load(path)


def split_image(image):
    """分割したイメージを格納したリストを返す"""
    imageList = []
    for i in range(0, 80, GS):
        for j in range(0, 80, GS):
            surface = pygame.Surface((GS, GS))
            surface.blit(image, (0, 0), (j, i, GS, GS))
            surface.convert()
            imageList.append(surface)
    return imageList


class Map: #Tiledからの読み込みと描画担当
    def __init__(self, data_path):
        self.gameMap = pytmx.load_pygame(data_path)
    
    def draw_map(self, screen):
        for layer in self.gameMap.visible_layers:
            for x, y, gid, in layer:
                tile = self.gameMap.get_tile_image_by_gid(gid)
                if(tile != None):
                    screen.blit(tile, (x * self.gameMap.tilewidth, y * self.gameMap.tileheight))

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
    font = pygame.font.Font('font_data/misaki_gothic_2nd.ttf', 20)
    font.set_bold(True)
    width = 800  # screeen
    height = 640
    pygame.display.set_mode((width, height), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("マス打")
    # 必要なオブジェクト（部品）
    play = True
    #マップチップの選択
    map = Map('Map_data/tyutorial_test.tmx')
    while play:
        map.draw_map(screen)        
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == QUIT:          # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:       # キーを押したとき
                if event.key == K_ESCAPE:   # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()