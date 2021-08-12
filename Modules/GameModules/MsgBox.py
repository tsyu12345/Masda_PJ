import pygame
from pygame.locals import *
import sys
from .EventSE import EventSound
class MsgBox():

    def __init__(self, msg_list:list):
        self.msg_list = msg_list
        self.text_index = 0
        self.font = pygame.font.Font('font_data/PixelMplus-20130602/PixelMplus12-Regular.ttf', 25)
        self.font.set_bold(True)
        self.text_render = self.font.render("", True, (255, 255, 255))
        self.msg_index = 0
        self.posx = 70
        self.posy = 410
        self.end_flg = False
        
        self.label:list = []
        self.label.append(self.font.render(self.msg_list[self.msg_index], True, (255, 255, 255)))
        self.label.append(self.font.render(self.msg_list[self.msg_index+1], True, (255, 255, 255)))
        self.label.append(self.font.render(self.msg_list[self.msg_index+2], True, (255, 255, 255)))
        self.frame = 0
        self.frame_reset = False
        self.disped_list = [False, False, False]
        self.disabled = False
        self.eventSE = EventSound()
    
    def display(self, screen:pygame.Surface, point:tuple):
        #print(self.msg_index)
        self.frame += 1
        self.msg_box = pygame.Rect(point[0], point[1], point[2], point[3])
        pygame.draw.rect(screen, (255, 255, 255), self.msg_box, 6)  # 縁
        pygame.draw.rect(screen, (0, 0, 0), self.msg_box)  # メッセージボックス
        try:
            screen.blit(self.label[0], (self.posx, self.posy))
            screen.blit(self.label[1], (self.posx,self.posy+40))
            screen.blit(self.label[2], (self.posx,self.posy+80))
        except IndexError:
            self.end_flg = True
        pygame.display.update()
        

    """   
    def name_tag(self, screen:pygame.Surface,name:str):
        tag_rect_point = pygame.Rect(self.msg_box.left+70, self.msg_box.top-20, 120, 20)
        tag_font = pygame.font.Font('font_data\PixelMplus-20130602\PixelMplus12-Regular.ttf', 15)
        pygame.draw.rect(screen, (255, 255, 255), tag_rect_point, 3)  # 縁
        pygame.draw.rect(screen, (0, 0, 0), tag_rect_point)
        name_text = tag_font.render(name, True, (255, 255, 255))
        screen.blit(name_text, (self.msg_box.left+70, self.msg_box.top-20))
        pygame.display.update()  
    """   
        #text_render = self.font.render(self.msg_list[0:int(self.frame/10)], True, (255, 255, 255))
    
    def text_update(self, event:pygame.event):
        """call in main loop of pygame.event.get()"""
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                self.eventSE.key_Enter.play()
                try:
                    self.label = []
                    self.msg_index += 3 
                    self.frame = 0       
                    self.label.append(self.font.render(self.msg_list[self.msg_index], True, (255, 255, 255)))
                    self.label.append(self.font.render(self.msg_list[self.msg_index+1], True, (255, 255, 255)))
                    self.label.append(self.font.render(self.msg_list[self.msg_index+2], True, (255, 255, 255)))

                except IndexError:
                    self.end_flg = True
                
class OneLineMsgBox(MsgBox):
    def __init__(self, msg_list, points:tuple):
        super().__init__(msg_list)
        self.frame = 0
        self.index = 0
        self.text = self.font.render("", True, (255, 255, 255))
        self.points:tuple = points

    def display(self, screen:pygame.Surface):
        try: 
            msg_box = pygame.Rect(self.points[0], self.points[1], self.points[2], self.points[3])
            pygame.draw.rect(screen, (255, 255, 255), msg_box, 6)  # 縁
            pygame.draw.rect(screen, (0, 0, 0), msg_box)  # メッセージボックス
            screen.blit(self.text, (self.points[0]+15, self.points[1]+ 15))
            #print("blited")
            pygame.display.update()
            #pygame.time.wait(30)
            self.frame += 1
            self.text = self.font.render(self.msg_list[self.index][0:self.frame], True, (255, 255, 255))
            if self.frame <= len(self.msg_list[self.msg_index]):
                self.eventSE.text_update.play()
        except IndexError:
            self.end_flg = True    

    def text_update(self, event:pygame.event):
        try:
            if self.frame >= len(self.msg_list[self.index]):
                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        self.eventSE.key_Enter.play()
                        self.frame = 0
                        self.index += 1
        except IndexError:
            self.end_flg = True    

def example():
    # pygame window initialization
    pygame.init()
    font = pygame.font.Font(
        'font_data/misaki_mincho.ttf', 26)
    font.set_bold(True)
    width = 800  # screeen
    height = 640
    pygame.display.set_mode((width, height), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("マス打")
    msg_box_point = (50, 400, 700, 150)
    msg_list = [
        "時は20XX年。",
        "人類はパソコンを発明した。",
        "人々はそれを当たり前のように使いこなしていた。＿",
        "そんな世界にとつぜん「魔王、北原」が現れた。",
        "北原は魔物たちを世界にバラマキ、",
        "人々の生活を脅かし始めた。＿",
        "北原は「タイピングが上手い奴を連れてこい」、",
        "と人々に警告した。",
        "これまで何人もの勇敢な者が＿",
        "北原に立ち向かったが誰も倒すことが出来なかった。",
        "ある少年が立ち上がった。彼の名はマスダ。",
        "魔王に親を殺された復習を果たすべく旅に出る。＿",
        "あなたは、マスダとなり、",
        "魔王を倒さなければなりません。",
        "これからその方法を伝授します。＿"
    ]
    msg_box = MsgBox(msg_list=msg_list)
    while True:
        msg_box.display(screen, point=msg_box_point)
        pygame.display.update()
        for event in pygame.event.get():
            # 終了用のイベント処理
            msg_box.text_update(event)
            if msg_box.end_flg == True:
                pygame.quit()
                sys.exit()

            if event.type == QUIT:          # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            


        
if __name__ == "__main__":
    example()