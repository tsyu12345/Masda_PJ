import pygame
from pygame.locals import *
#from playsound import playsound
import threading as th 
import sys
import csv

"""import game module"""
from LoadMap import Map

"""import game file"""
import tutorial
import game_tyutorial

"""here"""

class TitleText:
    def __init__(self, text, col_tuple):
        font = pygame.font.SysFont("hg正楷書体pro", 150)
        self.text = font.render(text, True, col_tuple, None)
    
    def display(self, screen):
        screen.blit(self.text, (40, 30))

class Button:    
    def btn_init(self, point_tuple):
        button = pygame.Rect(point_tuple[0], point_tuple[1], point_tuple[2], point_tuple[3])
        return button 


def load_img(path):
    img = pygame.image.load(path)
    img = img.convert()
    return img

def split_load_img(path, x, y, width, height):
    surface = pygame.Surface((16 ,16))
    surface.blit()
    img = pygame.image.pygame.load(path)
    img = img.convert()



def main():
    pygame.init()
    font = pygame.font.Font('font_data/misaki_gothic_2nd.ttf', 20)
    font.set_bold(True)
    width = 800 #screeen
    height = 640
    pygame.display.set_mode((width, height), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("マス打")
    #必要なオブジェクト（部品）をここへ
    bg = load_img('images/top_page/おまけピクチャ/800×600/pipo-pic001.jpg')#背景画像
    bg_rect = bg.get_rect()
    title = TitleText("マス打", (0, 0, 0))
    button = Button()
    s_btn_point = (width / 2 - 80, height / 2, 200, 50)
    e_btn_point = (width / 2 - 80, height / 2 + 100, 200, 50)
    s_text = font.render("はじめる", True, (255, 255, 255))
    e_text = font.render("おわる", True, (255, 255, 255))
    start = button.btn_init(s_btn_point)
    end = button.btn_init(e_btn_point)
    auth_font = pygame.font.SysFont("hg正楷書体pro", 20)
    auth_caption = pygame.Rect(0, 600, width, height-600)
    caption = auth_font.render("Copyright 2021-06-23 チームたんじろう all rights reserved", True, (0,0,0))
    """
    pygame.mixer.init()
    pygame.mixer.music.load('sounds/OpeningThema/魔王魂  8bit25.ogg') #BGM
    pygame.mixer.music.play(-1)
    """
    #th1 = th.Thread(target=playsound, args=(['sounds/OpeningThema/8bit03.mp3']), daemon=True)
    #th1.start()
    #タイトルウィンドウ表示
    title_page = True
    corse_select = False
    top_page = True
    while top_page:#全体のループ

        while title_page:
            screen.blit(bg, bg_rect)
            title.display(screen)
            pygame.draw.rect(screen, (255, 255,255), start, 6) #縁
            pygame.draw.rect(screen, (255, 255,255), end, 6)
            pygame.draw.rect(screen, (0, 0, 0), start)
            pygame.draw.rect(screen, (0, 0, 0), end)
            #以下はボタンテキストの描画screen.blit(btnObject, (x, y))
            screen.blit(s_text, (s_btn_point[0] + 60 , s_btn_point[1] + 15))
            screen.blit(e_text, (e_btn_point[0] + 63, e_btn_point[1] + 15))
            #著作権表示
            pygame.draw.rect(screen, (20, 200, 20), auth_caption)
            screen.blit(caption, (100+20, 600+15))
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
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if start.collidepoint(event.pos):
                        #ここにその後の処理を追加
                        print("start button pressed!!")
                        
                        corse_select = True
                        title_page = False
        
                    elif end.collidepoint(event.pos):
                        print("end button presssed!!")
                        pygame.quit()
                        sys.exit()
        
        #ワールドマップ画面
        #必要なオブジェクトを定義
        map = Map('Map_data/world_map.tmx')

        button = Button()
        course1_btn_point = (40, 500, 200, 50)
        course2_btn_point = (80, 420, 200, 50)
        course3_btn_point = (200, 330, 200, 50)
        course4_btn_point = (width - 300, 100, 200, 50)
        c1_text = font.render("チュートリアル", True, (255, 255, 255))
        c2_text = font.render("初級コース", True, (255, 255, 255))
        c3_text = font.render("中級コース", True, (255, 255, 255))
        c4_text = font.render("上級コース", True, (255, 255, 255))
        c1_btn = button.btn_init(course1_btn_point)
        c2_btn = button.btn_init(course2_btn_point)
        c3_btn = button.btn_init(course3_btn_point)
        c4_btn = button.btn_init(course4_btn_point)
        rn_text = font.render("もどる", True, (255, 255, 255))
        return_btn_point = (600, 500, 100, 50)
        return_btn = button.btn_init(return_btn_point)
        while corse_select:
            pygame.init()
            screen.fill((0, 0, 0))
            map.draw_map(screen)
            pygame.draw.rect(screen, (255, 255,255), c1_btn, 6) #縁
            pygame.draw.rect(screen, (255, 255,255), c2_btn, 6)
            pygame.draw.rect(screen, (255, 255,255), c3_btn, 6)
            pygame.draw.rect(screen, (255, 255,255), c4_btn, 6)
            pygame.draw.rect(screen, (255, 255,255), return_btn, 6)
            #以下はボタンテキストの描画screen.blit(btnObject, (x, y))
            pygame.draw.rect(screen, (0, 0, 0), return_btn)
            pygame.draw.rect(screen, (0, 0, 0), c1_btn)#ボタン本体
            pygame.draw.rect(screen, (0, 0, 0), c2_btn)
            pygame.draw.rect(screen, (0, 0, 0), c3_btn)
            pygame.draw.rect(screen, (0, 0, 0), c4_btn)
            screen.blit(c1_text, (course1_btn_point[0] + 30 , course1_btn_point[1] + 15))#ボタンテキスト
            screen.blit(c2_text, (course2_btn_point[0] + 50 , course2_btn_point[1] + 15))
            screen.blit(c3_text, (course3_btn_point[0] + 50 , course3_btn_point[1] + 15))
            screen.blit(c4_text, (course4_btn_point[0] + 50 , course4_btn_point[1] + 15))
            screen.blit(rn_text, (return_btn_point[0] + 20, return_btn_point[1] + 15))
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == QUIT:          # 閉じるボタンが押されたとき
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:       # キーを押したとき
                    if event.key == K_ESCAPE:   # Escキーが押されたとき
                        pygame.quit()
                        sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if c1_btn.collidepoint(event.pos):
                        #ここにその後の処理を追加
                        print("チュートリアル button pressed!!")
                        tutorial.main()
                        pygame.init()
                        game_tyutorial.main()                         
                    if c2_btn.collidepoint(event.pos):
                        #ここにその後の処理を追加
                        print("初級コース button pressed!!")
                        
                    if c3_btn.collidepoint(event.pos):
                        #ここにその後の処理を追加
                        print("中級コース button pressed!!")
                        
                    if c4_btn.collidepoint(event.pos):
                        #ここにその後の処理を追加
                        print("上級コース button pressed!!")
                        
                    if return_btn.collidepoint(event.pos):
                        title_page = True
                        corse_select = False
                        
   
if __name__ == "__main__":
    main()