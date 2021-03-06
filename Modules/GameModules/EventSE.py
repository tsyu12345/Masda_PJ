import pygame
from pygame.locals import *

class EventSound:
    def __init__(self):
        self.key_yes = pygame.mixer.Sound('sounds/OtherSounds/key_yes.wav')
        self.key_no = pygame.mixer.Sound('sounds/OtherSounds/key_no.wav')
        self.key_Enter = pygame.mixer.Sound('sounds/OtherSounds/key_Enter.wav')
        self.yes_btn = pygame.mixer.Sound('sounds/clickSound/systen40.wav')
        self.no_btn = pygame.mixer.Sound('sounds/clickSound/systen41.wav')
        self.btn_select = pygame.mixer.Sound('sounds/OtherSounds/button_select.wav')
        self.text_update = pygame.mixer.Sound('sounds/OtherSounds/serif.wav')
        self.menu_carsol_move = pygame.mixer.Sound('sounds/OtherSounds/NES-RPG02-06(Select).wav')
        self.select_course = pygame.mixer.Sound('sounds/OtherSounds/start.wav')
        self.battle_catch = pygame.mixer.Sound('sounds/OtherSounds/battleCatch.wav')
    
    def event_catch_se(self, event:pygame.event, btn=None):
        """Use in event for loop of pygame.event.get(). """
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                self.key_Enter.play()
        if event.type == MOUSEBUTTONDOWN and btn != None:
            for button in btn:
                if button.collidepoint(event.pos):
                    self.btn_select.play()

class PlayerSound:
    """Definiction of PlayerSound effect"""
    def __init__(self):
        self.walk = pygame.mixer.Sound('sounds/PlaySounds/walk.wav')
        self.succsess = pygame.mixer.Sound('sounds/PlaySounds/succsess.wav')
        self.damege = pygame.mixer.Sound('sounds/PlaySounds/powerdown02.wav')
        self.levelUP = pygame.mixer.Sound('sounds/PlaySounds/levelup.wav')
