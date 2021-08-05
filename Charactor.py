import pygame
from pygame.locals import *
import pytmx
from pytmx.util_pygame import load_pygame
import sys
import csv
import os
from LoadMap import Map
from MsgBox import MsgBox
from battleWindow import *
from LocalFunc import *
from EventSE import EventSound as ES
from EventSE import PlayerSound as PS

GS = 32
DOWN, LEFT, RIGHT, UP = 0, 1, 2, 3


class Character:

    def __init__(self, img_filename, HP, Level):
        self.HP = HP
        self.Level = Level
        self.imgs = split_image_load(load_image(img_filename))
        self.posX = 0
        self.posY = 0
        self.animcycle = 24
        self.frame = 0
        self.clock = pygame.time.Clock()

    def draw(self, screen):
        self.clock.tick(60)
        screen.blit(self.imgs, (self.posX, self.posY))
        pygame.display.update()


class Player(Character):
    def __init__(self, img_filename, HP, Level):
        super().__init__(img_filename, HP, Level)

    def move(self):
        if event.key == K_DOWN:
            player_sound.walk.play()
            direction = DOWN
            player_y += 1
        if event.key == K_LEFT:
            player_sound.walk.play()
            direction = LEFT
            player_x -= 1
        if event.key == K_RIGHT:
            player_sound.walk.play()
            direction = RIGHT
            player_x += 1
        if event.key == K_UP:
            player_sound.walk.play()
            direction = UP
            player_y -= 1            

    
