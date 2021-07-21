import pygame
from pygame.locals import *

def load_image(filename, colorkey=None):
    image = pygame.image.load(filename)
    image = image.convert_alpha()
    return image #return pygame imgae object

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