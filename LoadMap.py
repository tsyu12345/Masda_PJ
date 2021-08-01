import pygame 
from pygame.locals import *
import pytmx
from pytmx.util_pygame import load_pygame


def load_image(filename, colorkey=None):
    image = pygame.image.load(filename)
    image = image.convert_alpha()
    return image
    
class Map: #Tiledからの読み込みと描画担当
    GS = 16
    row = 50 #map row
    col = 40 #map column

    def __init__(self, data_path):
        self.gameMap = pytmx.load_pygame(data_path)
        #self.surface = pygame.Surface()
        self.tile_list = [] 

    def draw_map(self, screen:pygame.Surface, offsetX, offsetY):
        # マップの描画範囲を計算し描画
        width, height = screen.get_size()
        startx = offsetX / self.GS
        endx = startx + width/self.GS + 1
        starty = offsetY / self.GS
        endy = starty + height/self.GS + 1
        self.tile_list = []
        #self.tile_gid = []
        for layer in self.gameMap.visible_layers:
            #print(layer)
            for x, y, gid, in layer:
                #print(x)
                tile = self.gameMap.get_tile_image_by_gid(gid)
                #print(tile)
                if(tile != None):
                    self.tile_list.append(tile)
                    #self.tile_gid.append(gid)
                    #print(self.gameMap.tilewidth)
                    #screen.blit(tile, (x * self.gameMap.tilewidth-offsetX, y * self.gameMap.tileheight-offsetY))
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


        
