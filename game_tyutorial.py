import pygame
from pygame.locals import *
import pytmx
from pytmx.util_pygame import load_pygame
import sys
import csv
import os

GS = 32
DOWN, LEFT, RIGHT, UP = 0,1,2,3


def load_image(filename, colorkey=None):
    image = pygame.image.load(filename)
    image = image.convert_alpha()
    return image

def split_image(image):
    """分割したイメージを格納したリストを返す"""
    imageList = []
    for i in range(0, 128, GS):
        for j in range(0, 128, GS):
            surface = pygame.Surface((GS, GS))
            surface.blit(image, (0, 0), (j, i, GS, GS))
            surface.convert_alpha()
            imageList.append(surface)
            print(imageList)
    return imageList


class Map: #Tiledからの読み込みと描画担当

    row = 800 #map row
    col = 640 #map column

    def __init__(self, data_path):
        self.gameMap = pytmx.load_pygame(data_path)

    def draw_map(self, screen):
        for layer in self.gameMap.visible_layers:
            for x, y, gid, in layer:
                tile = self.gameMap.get_tile_image_by_gid(gid)
                if(tile != None):
                    screen.blit(tile, (x * self.gameMap.tilewidth, y * self.gameMap.tileheight))
    
    def is_movable(self, x, y): #マップの移動可否判定
        """(x,y)は移動可能か？"""
        # マップ範囲内か？
        if x < 0 or x > self.col-1 or y < 0 or y > self.row-1:
            return False
        # マップチップは移動可能か？
        if self.map[y][x] == 1:  # 水は移動できない
            return False
        return True
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
    play = True
    #player オブジェクト(仮)
    player_imgs = split_image(load_image('images/Characters/hero/pipo-charachip027c.png'))
    direction = DOWN
    player_x, player_y = 1,1
    animcycle = 24
    frame = 0
    clock = pygame.time.Clock()
    
    #マップオブジェクト
    map = Map('Map_data/tyutorial_test.tmx')
    
    #メッセージボックス
    start_text = "→、←、↑、↓で動くぞ！！"
    text_render = font.render("", True, (255, 255, 255))
    msg_box_point = (50, 400, 700, 150)
    msg_box = pygame.Rect(msg_box_point[0], msg_box_point[1], msg_box_point[2], msg_box_point[3])
    
    while play:
        clock.tick(60)
        frame += 1
        player_img = player_imgs[int(direction*4 + frame/animcycle%3)]
        map.draw_map(screen)
        screen.blit(player_img, (player_x*GS, player_y*GS))
        pygame.draw.rect(screen, (255, 255, 255), msg_box, 6)  # 縁
        pygame.draw.rect(screen, (0, 0, 0), msg_box)  # メッセージボックス
        screen.blit(text_render, (70, 410))  # メッセージの表示
       
        pygame.display.update()
        
        #pygame.time.wait(100)
        #pygame.time.wait(80)
        text_render = font.render(start_text[0:int(frame/10)], True, (255, 255, 255))
        
        for event in pygame.event.get():
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