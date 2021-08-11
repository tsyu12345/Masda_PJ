import pygame
from pygame.locals import * 
from .EventSE import EventSound
class MainMenu():
    def __init__(self, menu_list:list, color:tuple, size:tuple, font_size:int):
        self.menu_list = menu_list
        self.color = color
        self.size = size 
        self.font_size = font_size
        self.font = pygame.font.Font('font_data/PixelMplus-20130602/PixelMplus10-Regular.ttf', font_size)
        self.renders = []
        #self.text_rect = pygame.Rect()
        self.menu_box = pygame.Rect(self.size[0], self.size[1], self.size[2], self.size[3])
        self.carsol = [[self.size[0] + 10, self.size[1] + 20],[self.size[0] + 30, self.size[1] + 30], [self.size[0] + 10, self.size[1] + 40]]
        self.carsol_cnt = 0
        self.sound = EventSound()
        for text in menu_list:
            self.renders.append(self.font.render(text, True, (255, 255, 255)))
    
    def display(self, screen:pygame.Surface):
        pygame.draw.rect(screen, self.color, self.menu_box)#本体
        pygame.draw.rect(screen, (255, 255, 255), self.menu_box, 3)#縁
        pygame.draw.polygon(screen, (255, 255, 255), self.carsol)
        for i, render in enumerate(self.renders):
            screen.blit(render, (self.size[0] + 40, self.size[1]+ 15 + i * (self.font_size + 20)))
    
    def carsol_controle(self, event:pygame.event):
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                pass
                #self.sound.key_Enter.play()

            if self.carsol_cnt < len(self.menu_list)-1:
                if event.key == K_DOWN:
                    self.carsol_cnt += 1
                    self.sound.menu_carsol_move.play()
                    for pos in self.carsol:
                        pos[1] += (self.font_size + 20)
                        
            if self.carsol_cnt != 0:
                if event.key == K_UP:
                    self.carsol_cnt -= 1
                    self.sound.menu_carsol_move.play()
                    for pos in self.carsol:
                        pos[1] -= (self.font_size + 20)
            
            


#Example
if __name__ == "__main__":
    from LocalFunc import exit_game
    # init pygame window
    pygame.init()
    #font = pygame.font.Font('font_data/PixelMplus-20130602/PixelMplus12-Regular.ttf', 20)
    #font.set_bold(True)
    width = 800 #screeen
    height = 640
    pygame.display.set_mode((width, height), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("マス打")

    list = [
        "はじめる",
        "終わる",
        "しこる"
    ]
    menu_point = (20, 20, 200, 200)
    menu = MainMenu(list, (0, 0, 0), menu_point, 30)
    sound = EventSound()
    while True:
        menu.display(screen)
        pygame.display.update()
        for event in pygame.event.get():
            sound.event_catch_se(event)
            menu.carsol_controle(event)
            exit_game(event)
       

    
    
        

