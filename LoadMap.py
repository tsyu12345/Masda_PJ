import pygame 
from pygame.locals import *
import pytmx
from pytmx.util_pygame import load_pygame


def load_image(filename, colorkey=None):
    image = pygame.image.load(filename)
    image = image.convert_alpha()
    return image
    
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
    
    def is_movable(self, x, y): #マップの移動可否判定:現在調整中。。。
        """(x,y)は移動可能か？"""
        # マップ範囲内か？
        if x < 0 or x > self.col-1 or y < 0 or y > self.row-1:
            return False
        # マップチップは移動可能か？
        if self.map[y][x] == 1:  # 水は移動できない
            return False
        return True

class ActionMap():
    def __init__(self, map:Map, screen:pygame.Surface):
        self.map = map
        self.screen = screen
    
    def calc_offset(self, playerX, playerY):
        w, h = self.screen.get_size()
        offsetX = playerX - w/2
        offsetY = playerY - h/2
        return offsetX, offsetY

   

        
