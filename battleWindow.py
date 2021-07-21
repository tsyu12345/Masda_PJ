from LoadMap import load_image
import pygame
from pygame.locals import *
import sys
from Button import Button

class Monster:
    def __init__(self, img_path:str, position:tuple, HP:int, level:int):
        self.path = img_path
        self.HP = HP
        self.level = level
        self.img = load_image(self.path)
        self.position = position
    
    def display(self, screen:pygame.Surface,):
        screen.blit(self.img, self.position)    

class DisplayParameter:
    def __init__(self, HP, Level):
        self.HP = HP
        self.level = Level
        self.text_col:tuple = (255, 255, 255)
        font = pygame.font.Font('font_data/misaki_gothic_2nd.ttf', 20)
        font.set_bold(True)
        col1 = "HP："
        col2 = "LV："
        self.hp_text = font.render(col1+str(self.HP), True, self.text_col)
        self.lv_text = font.render(col2+str(self.level), True, self.text_col)

    def display(self, screen:pygame.display):
        width, height = screen.get_size()
        screen.blit(self.hp_text, (width / 2, height-250))
        rect = pygame.Rect(width / 2 + 100, height-250, 20, 20)
        pygame.draw.rect(screen, (5, 150, 5), rect)
        screen.blit(self.lv_text, (200, height-250))

class TypeingGame:
    def __init__(self, question_dic:dict):
        self.q_dic = question_dic
    
    def return_question(self, index):
        q:list = list(self.q_dic.keys())
        return q[index]
    
    def return_ans(self, index):
        q = self.return_question(index)
        return self.q_dic[q]

    def game(self, screen, index):
        w, h = screen.get_size()
        font = pygame.font.Font('font_data/misaki_gothic_2nd.ttf', 100)
        font.set_bold(True)
        question = self.return_question(index)
        q_text = font.render(question, True, (255, 255, 255))
        screen.blit(q_text, (w/2 - 40, h / 2))
        answer = self.return_ans(index)
        ans_text = font.render(answer, True, (255, 255, 255))
        screen.blit(ans_text, (w/2-40, h/2 + 40))
        

def load_image(filename, colorkey=None):
    image = pygame.image.load(filename)
    image = image.convert_alpha()
    return image

def main():
    #init pygame window
    pygame.init()
    font = pygame.font.Font('font_data/misaki_gothic_2nd.ttf', 20)
    font.set_bold(True)
    width = 800 #screeen
    height = 640
    pygame.display.set_mode((width, height), 0, 32)
    screen = pygame.display.get_surface()
    
    pygame.display.set_caption("マス打")
    #必要な変数等
    battle_mode = True
    monster = Monster(
        'images/Characters/enemys/pipo-enemy46set/120x120/pipo-enemy002.png', (width / 2, height/2-100),5,1)
    aitem_btn = Button("アイテム", (255, 255, 255), (0, 0, 0), (width / 4, height-100, 100, 30))
    status_bar = DisplayParameter(10, 10)
    dic = {
            'RPG':"RPG",
            '冒険':'bouken',
            'イス':"isu",
            '消しゴム':"kesigomu",
            '焼肉':"yainiku",
            '鏡':"kagami",
            'お金':"okane",
            'ネクタイ':"nekutai",
            '傘':"kasa",
            'ゴミ':"gomi",
            'マクラ':"makura",
            '電気':"dennki",
            'マウス':"mausu",
            '教科書':"kyoukasyo",
            'うちわ':"uchiwa",
            '帽子':"boushi",
            '筆箱':'fudebako'            
    }
    typeGame = TypeingGame(dic)
    #Example
    while battle_mode:#main window loop
        pygame.draw.rect(screen, (50, 100, 50), pygame.Rect(100, 20, width-200, height-300), 1)
        monster.display(screen)
        aitem_btn.display(screen)
        status_bar.display(screen)
        typeGame.game(screen, 4)
        pygame.display.update()

        # イベント処理
        for event in pygame.event.get():
            # 終了用のイベント処理
            if event.type == QUIT:          # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:       # キーを押したとき   
                if event.key == K_ESCAPE:   # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()

if __name__ == '__main__':
    main()
                
