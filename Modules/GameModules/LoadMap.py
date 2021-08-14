import pygame 
from pygame.locals import *
import pytmx

GS = 32
class Map: #Tiledからの読み込みと描画担当
    row = 40
    col = 50
    def __init__(self, data_path):
        self.gameMap = pytmx.load_pygame(data_path)
        self.gid = 0

    def calc_offset(self, screen:pygame.Surface ,px, py):
       # print("px")
        #print(px)
        w, h = screen.get_size()    
        offsetX = px - w/2
        offsetY = py - h/2
        return offsetX, offsetY

    def draw_map(self, screen, px, py):
        w, h = screen.get_size()
        offX, offY = self.calc_offset(screen, px, py)
        if offX < 0:
            offX = 0
        if offX > w:
            offX = w
        if offY < 0:
            offY = 0
        if offY > h:
            offY = h
        #print("off:" + str(offX) + "," + str(offY))
        #print("pxy:" + str(px) + "," + str(py))
        map_startX = int(offX / GS) 
        map_startY = int(offY / GS) 
        #print("map_st:" + str(map_startX) + "," + str(map_startY))
        #print(map_startX, map_startY)
        map_endX = int(map_startX + w / GS) + 1
        map_endY = int(map_startY + h / GS) + 1
        #print("map_ed:" + str(map_startX)+","+ str(map_startY))

        for y in range(map_startY, map_endY):
            if y < 0:
                y = 1
            if y > self.row-1:
                y = self.row-1
            for x in range(map_startX, map_endX):
                if x < 0:
                    x = 1
                if x > self.col-1:
                    x = self.col-1

                #print("x, y:" +  str(x) + "," + str(y))
                tile = self.gameMap.get_tile_image(x, y, 0)   
                if tile != None :
                    screen.blit(tile, (x * self.gameMap.tilewidth -offX, y * self.gameMap.tileheight-offY))
                    try:
                        tile2 = self.gameMap.get_tile_image(x, y, 1)
                        if tile2 != None:
                            screen.blit(tile2, (x * GS-offX, y * GS-offY))
                    except ValueError:
                        pass

        """
        if (offX < 0 or offY < 0) or (offX > w-GS or offY > h-GS):
            for layer in self.gameMap.visible_layers:
                for row, col, gid, in layer:
                    print("gid:" + str(gid))
                    print("x, y:" + str(row) + "," + str(col))
                    tile = self.gameMap.get_tile_image_by_gid(gid)
                    if tile != None:
                            #print(row)
                            #screen.blit(tile, (row* self.gameMap.tilewidth, col * self.gameMap.tileheight))
                        screen.blit(tile, (row* self.gameMap.tilewidth, col * self.gameMap.tileheight))
        else:
            for y in range(map_startY, map_endY):
                for x in range(map_startX, map_endX):
                    #print("x, y:" + str(x) + "," + str(y))
                    #self.gameMap.reload_images()
                    tile = self.gameMap.get_tile_image(x, y, 1)
                    #print(tile)
                    if tile != None :
                        screen.blit(tile, (x * self.gameMap.tilewidth -offX, y * self.gameMap.tileheight-offY))
                    try:
                        tile2 = self.gameMap.get_tile_image(x, y, 2)
                        if tile2 != None:
                            screen.blit(tile2, (x * GS-offX, y * GS-offY))
                    except ValueError:
                        pass
        """
    def isMove(self, px, py):
        try:
            tile = self.gameMap.get_tile_image(int(px/GS), int(py/GS), 1)
        except ValueError:
            tile = 0 #オブジェクトがない場合、プレイヤーは動ける。0。
        #print(gid)
        print(tile)
        if tile != None:#オブジェクトがある場合は0以外のgidを持っているので、False動けない
            return False
        else:
            return True
        



   

        
