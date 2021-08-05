import pygame
from pygame.locals import *
import sys

GS = 32
def load_image(filename):
    image = pygame.image.load(filename).convert_alpha()
    #image = image.convert_alpha()
    return image #return pygame imgae object

def split_image_load(image):
    """分割したイメージを格納したリストを返す"""
    imageList = []
    for i in range(0, 128, GS):
        for j in range(0, 128, GS):
            surface = pygame.Surface((GS, GS))
            surface.blit(image, (0, 0), (j, i, GS, GS))
            #surface.convert()
            surface.set_colorkey(surface.get_at((0,0)), RLEACCEL)
            surface.convert()
            imageList.append(surface)
    return imageList 

def exit_game(event:pygame.event):
    # 終了用のイベント処理
    if event.type == QUIT:          # 閉じるボタンが押されたとき
        pygame.quit()
        sys.exit()
    if event.type == KEYDOWN:       # キーを押したとき
        if event.key == K_ESCAPE:   # Escキーが押されたとき
            pygame.quit()
            sys.exit()