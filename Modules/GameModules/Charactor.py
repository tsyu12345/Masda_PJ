import pygame
from pygame.locals import *
import random
from .LoadMap import Map
#from battleWindow import *
from .LocalFunc import *
#from EventSE import EventSound as ES
from .EventSE import PlayerSound as PS

GS = 32
M_ROW = 40
M_COL = 50
DOWN, LEFT, RIGHT, UP = 0, 1, 2, 3


class Character:

    def __init__(self, img_filename, screen:pygame.Surface):
        w, h = screen.get_size()
        self.imgs = split_image_load(load_image(img_filename))
        self.posX = random.randint(0, 600)
        self.posY = random.randint(0, 600)
        self.startposX = self.posX
        self.startposY = self.posY
        self.animcycle = 24
        self.frame = 0
        self.clock = pygame.time.Clock()
        self.screen = screen
        self.direction = DOWN

    def calc_offset(self, p_mx, p_my):
        #w, h = self.screen.get_size()
        self.offX = self.posX -  pmx
        self.offY = self.posY - self.startposY
        return self.offX, self.offY

    def display(self):
        self.clock.tick(60)
        #offX, offY = self.calc_offset()
        self.frame += 1
        img = self.imgs[int(self.direction*4 + self.frame/self.animcycle%3)]
        #self.screen.blit(img, (self.posX-offX, self.posY-offY))
        pygame.display.update()
        if self.frame > 1000:
            self.frame = 0

    def move(self, move_range:tuple):
        """
        現在調整中、、。
        """
        self.posX += move_range[0][0]
        self.posY += move_range[0][1]

class Player(Character):
    HP = 10
    Level = 0
    def __init__(self, img_filename, screen:pygame.Surface, map_obj:Map):
        super().__init__(img_filename,screen)
        self.playsound = PS()
        self.direction = DOWN
        self.map = map_obj
    def calc_offset(self,screen):
        w, h = screen.get_size()
        self.offX = self.posX - w/2 
        self.offY = self.posY - h/2
        return self.offX, self.offY

    def display(self, screen:pygame.Surface):
        w, h = screen.get_size()
        offX,offY = self.calc_offset(screen)
        self.clock.tick(60)
        self.frame += 1
        img = self.imgs[int(self.direction*4 + self.frame/self.animcycle%3)]
        if offX < 0:
            offX = 0
        if offX > w:
            offX = w
        if offY < 0:
            offY = 0
        if offY > h:
            offY = h
            
        screen.blit(img, (self.posX-offX, self.posY-offY))
        pygame.display.update()
        print("x, y:" + str(self.posX) +", " +str(self.posY))
        #print("offXY:" + str(offX) + "," +str(offY))
        if self.frame > 1000:
            self.frame = 0
        #print((self.posX-offX, self.posY-offY))

    def move(self):
        pressed_key = pygame.key.get_pressed()
        movable = True#self.map.isMove(self.posX, self.posY)
        print(str(int(self.posX/GS)),","+ str(int(self.posY/GS)))
        if movable:
            if pressed_key[K_DOWN] and self.posY < M_ROW * GS:
                self.playsound.walk.play()
                self.direction = DOWN
                self.posY += GS /4
            if pressed_key[K_LEFT] and self.posX > GS:
                self.playsound.walk.play()
                self.direction = LEFT
                self.posX -= GS/4
            if pressed_key[K_RIGHT] and self.posX < M_COL * GS:
                self.playsound.walk.play()
                self.direction = RIGHT
                self.posX += GS/4
            if pressed_key[K_UP] and self.posY > GS:
                self.playsound.walk.play()
                self.direction = UP
                self.posY -= GS/4      

    
