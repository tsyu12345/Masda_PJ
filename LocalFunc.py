import pygame
from pygame.locals import *

GS = 16

def load_image(filename):
    image = pygame.image.load(filename).convert_alpha()
    #image = image.convert_alpha()
    return image #return pygame imgae object

def split_image_load(image):
    """分割したイメージを格納したリストを返す"""
    imageList = []
    for i in range(0, 64, GS):
        for j in range(0, 64, GS):
            surface = pygame.Surface((GS, GS))
            surface.blit(image, (0, 0), (j, i, GS, GS))
            #surface.convert()
            surface.set_colorkey(surface.get_at((0,0)), RLEACCEL)
            surface.convert()
            imageList.append(surface)
    return imageList 

def calc_offset(screen , playerX, playerY):
        w, h = screen.get_size()
        offsetX = playerX - w/2
        offsetY = playerY - h/2
        return offsetX, offsetY