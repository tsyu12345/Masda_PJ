#from LoadMap import load_image
import pygame
from pygame.locals import *
import sys
from .Button import Button
from .LocalFunc import *
#import threading as th
from .EventSE import *


class Monster:
    def __init__(self, img_path: str, position: tuple, HP: int, level: int):
        self.path = img_path
        self.HP = HP
        self.level = level
        self.img = load_image(self.path)
        self.position = position

    def display(self, screen: pygame.Surface,):
        screen.blit(self.img, self.position)


class DisplayParameter:
    def __init__(self, HP, Level):
        self.HP = HP
        self.level = Level
        self.text_col: tuple = (255, 255, 255)
        self.font = pygame.font.Font(
            'font_data/PixelMplus-20130602/PixelMplus12-Regular.ttf', 20)
        self.font.set_bold(True)
        col1 = "HP："
        col2 = "LV："
        self.hp_text = self.font.render(col1+str(self.HP), True, self.text_col)
        self.lv_text = self.font.render(col2+str(self.level), True, self.text_col)

    def display(self, screen: pygame.display):
        width, height = screen.get_size()
        self.hp_text = self.font.render("HP："+str(self.HP), True, self.text_col)
        screen.blit(self.hp_text, (width / 2, height-250))
        rect = pygame.Rect(width / 2 + 100, height-250, 20, 20)
        pygame.draw.rect(screen, (5, 150, 5), rect)
        screen.blit(self.lv_text, (200, height-250))


class CountDown():
    start = 0
    now_seconds = 0

    def __init__(self, end_seconds):
        self.start = pygame.time.get_ticks()
        self.end_seconds = end_seconds
        self.rest_time = self.end_seconds - self.now_seconds
        self.font = pygame.font.Font(
            'font_data/PixelMplus-20130602/PixelMplus12-Regular.ttf', 20)

    def start_cnt(self):
        self.start = pygame.time.get_ticks()

    def display(self, screen):
        """Display time parameter"""
        #print("in bar")
        self.now_seconds = (pygame.time.get_ticks() - self.start)/1000
        width, height = screen.get_size()
        self.rest_time = self.end_seconds - self.now_seconds
        prog_param = self.rest_time*50
        if self.rest_time < 0:
            prog_param = 0
        self.text = self.font.render(
            "残り時間: " + str(int(self.rest_time)), True, (255, 255, 255))
        screen.blit(self.text, (100, height/2 + 120))
        """draw time bar"""
        pygame.draw.rect(screen, (255, 255, 255), Rect(
            250, height/2 + 120, 500, 20), 2)  # 縁
        pygame.draw.rect(screen, (255, 50, 50), Rect(
            252, height/2 + 122, prog_param, 17))


class TypeingGame:
    def __init__(self, question_dic: dict, end_seconds: int):
        self.q_dic = question_dic
        self.damege = False
        self.inputKey_list = []
        self.index = 0
        self.question = self.return_question(self.index)
        self.answer = self.return_ans(self.index)
        self.end_flg = False
        self.count_down = CountDown(end_seconds)
        self.push_key:str = None
        self.play_se = PlayerSound()
    def return_question(self, index):
        q: list = list(self.q_dic.keys())
        return q[index]

    def return_ans(self, index):
        q = self.return_question(index)
        return self.q_dic[q]

    def judge(self, in_chr, out_chr):
        if in_chr == out_chr:
            return True
        else:
            return False

    def __play(self, input):
        """Back end of TypingGame.Use in for loop of pygame event"""
        self.question = self.return_question(self.index)
        self.answer = self.return_ans(self.index)
        #print("inp:" + str(len(self.inputKey_list)))
        #print("ans:" + str(len(self.answer)))
        if self.count_down.rest_time >= 0:
            if len(self.inputKey_list) == len(self.answer):
                self.index += 1
                self.inputKey_list = []
                self.play_se.succsess.play()
                self.count_down.start = pygame.time.get_ticks()
            else:
                # print(len(self.inputKey_list))
                judge = self.judge(input, self.answer[len(self.inputKey_list)])
                if judge == True:
                    print("judge : " + input)
                    self.inputKey_list.append(input)
        else: #when time out
            self.index += 1
            self.damege = True
            self.play_se.damege.play()
            self.inputKey_list = []
            self.count_down.start = pygame.time.get_ticks()



    def display(self, screen:pygame.Surface):
        w, h = screen.get_size()
        pygame.draw.rect(screen, (50, 100, 50), pygame.Rect(100, 20, w-200, h-300), 1)
        pygame.draw.rect(screen, (255, 255, 255), pygame.Rect(150, 50, 500, 200), 4)
        font = pygame.font.Font(
        'font_data/PixelMplus-20130602/PixelMplus12-Regular.ttf', 100)
        font.set_bold(True)
        #question = self.return_question(self.index)
        q_text = font.render(self.question, True, (255, 255, 255))
        q_text_rect = q_text.get_rect(center=(w/2, h/2 - 190))
        screen.blit(q_text, q_text_rect)
        #self.answer = self.return_ans(self.index)
        font = pygame.font.Font(
        'font_data/PixelMplus-20130602/PixelMplus12-Regular.ttf', 50)
        ans_text = font.render(self.answer, True, (255, 255, 255))
        ans_text_rect = ans_text.get_rect(center=(w/2 , h/2-120))
        ansed_text = font.render(self.answer[0:len(self.inputKey_list)], True, (255, 5, 5))
        #print(self.answer)
        screen.blit(ans_text, ans_text_rect)
        screen.blit(ansed_text, ans_text_rect)  
        
        #pygame.display.update()
        if self.index+1 == len(self.q_dic):#Judge End
            self.end_flg = True
        else:
            self.__play(self.push_key)
                

    def input_word(self, event):
        if event.type == KEYDOWN:
            self.push_key = pygame.key.name(event.key)

# Example
def main():
    # init pygame window
    pygame.init()
    font = pygame.font.Font('font_data/PixelMplus-20130602/PixelMplus12-Regular.ttf', 20)
    font.set_bold(True)
    width = 800 #screeen
    height = 640
    pygame.display.set_mode((width, height), 0, 32)
    screen = pygame.display.get_surface()
    
    pygame.display.set_caption("マス打")
    # 必要な変数等
    battle_mode = True
    monster = Monster(
        'images/Characters/enemys/pipo-enemy46set/120x120/pipo-enemy002.png', (width / 2, height/2-100),5,1)
    aitem_btn = Button("アイテム", (255, 255, 255), (0, 0, 0), (width / 4, height-100, 100, 30))
    status_bar = DisplayParameter(10, 10)
    dic = {
            'RPG':"rpg",
            '冒険':'bouken',
            'イス':"isu",
        }
        
            
                        
    
    typeGame = TypeingGame(dic, 10)
    #input_key = ""
    # Example
    while battle_mode:#main window loop
        pygame.draw.rect(screen, (0, 0, 0), Rect(0, 0, width, height))
        monster.display(screen)
        aitem_btn.display(screen)
        status_bar.display(screen)
        # th1 = th.Thread(target=typeGame.display, args=(screen, 5))
        # th1.start()
        #print(input_key)
        typeGame.display(screen)
        typeGame.count_down.display(screen)
        print(typeGame.index)
        pygame.display.update()
        
        #イベント処理
        for event in pygame.event.get():
            # 終了用のイベント処理
            typeGame.input_word(event)
            #input_key = typeGame.input_word(event)
            if event.type == QUIT:          # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:# キーを押したとき
                if event.key == K_ESCAPE:   # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()

if __name__ == '__main__':
    main()
                
