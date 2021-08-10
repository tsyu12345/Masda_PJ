import pygame
from pygame.locals import *
from GameModules.LoadMap import Map
from GameModules.battleWindow import *
from GameModules.LocalFunc import *
from GameModules.EventSE import EventSound as ES
from GameModules.EventSE import PlayerSound as PS

GS = 32
M_ROW = 40
M_COL = 50
DOWN, LEFT, RIGHT, UP = 0, 1, 2, 3


class Character:

    def __init__(self, img_filename, HP, Level, screen:pygame.Surface):
        self.HP = HP
        self.Level = Level
        self.imgs = split_image_load(load_image(img_filename))
        self.posX = 0
        self.posY = 0
        self.animcycle = 24
        self.frame = 0
        self.clock = pygame.time.Clock()
        self.screen = screen

    def display(self, screen):
        self.clock.tick(60)
        self.frame += 1
        img = self.imgs[int(0*4 + self.frame/self.animcycle%3)]
        screen.blit(img, (self.posX, self.posY))
        pygame.display.update()

class MobCharactor():
    def __init__(self, img, screen, pos_loist):
        self.screen = screen
        self.imgs = split_image_load(load_image(img))
        self.poslist = pos_loist

    def displpay(self):
        for pos in self.poslist:
            imgs = self.imgs[int(0*4 + frame/animcycle%3)]
            screen.blit(img, ())

class Player(Character):
    def __init__(self, img_filename, HP, Level, screen:pygame.Surface):
        super().__init__(img_filename, HP, Level,screen)
        self.playsound = PS()
        self.direction = DOWN

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
        if self.frame > 100:
            self.frame = 0
        #print((self.posX-offX, self.posY-offY))

    def move(self, event):
        if event.type == KEYDOWN:
            if event.key == K_DOWN and self.posY < M_ROW * GS:
                self.playsound.walk.play()
                self.direction = DOWN
                self.posY += GS
            if event.key == K_LEFT and self.posX > GS:
                self.playsound.walk.play()
                self.direction = LEFT
                self.posX -= GS
            if event.key == K_RIGHT and self.posX < M_COL * GS:
                self.playsound.walk.play()
                self.direction = RIGHT
                self.posX += GS
            if event.key == K_UP and self.posY > GS:
                self.playsound.walk.play()
                self.direction = UP
                self.posY -= GS       

    
