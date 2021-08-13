"""dependency library import"""
import pygame
from pygame.locals import *
from pygame import mixer
import sys
#import csv

"""import game module"""
#from GameModules.LoadMap import Map
from Modules.GameModules.LocalFunc import *
from Modules.GameModules.Menu import MainMenu
from Modules.GameModules.EventSE import EventSound
from LoadingAnimation import TextAnimation
"""import game file"""
from Modules import game_tyutorial
from Modules import tutorial
from Modules import Syokyu
from Modules import Tyukyu

class TitleText:
    def __init__(self, text, col_tuple):
        font = pygame.font.Font(
        'font_data/PixelMplus-20130602/PixelMplus12-Regular.ttf', 150)
        self.text = font.render(text, True, col_tuple, None)
    
    def display(self, screen):
        screen.blit(self.text, (40, 30))

class Button:    
    def btn_init(self, point_tuple):
        button = pygame.Rect(point_tuple[0], point_tuple[1], point_tuple[2], point_tuple[3])
        return button 

class SelectCorseCarsol:
    def __init__(self, menu_cnt):
        self.carsol_cnt = 0
        self.max_menu_cnt = menu_cnt
        self.sound = EventSound()
        self.pos_list = [
            [[10, 500],[30, 520],[10, 540]],#チュートリアル
            [[50, 430],[70, 450],[50, 470]],#初級
            [[175, 330],[195, 350],[175, 370]],#中級
            [[460, 110],[490, 130],[460, 150]],#上級
            [[570, 500],[590, 520],[570, 540]],#もどる
            ]
        self.carsol = self.pos_list[0]

    def display(self, screen):
        pygame.draw.polygon(screen, (5, 255, 5), self.carsol)
        pygame.display.flip()

    def carsol_controle(self, event):
        print(self.carsol_cnt)
        if event.type == KEYDOWN:
            if event.key == K_RETURN:
                return self.carsol_cnt
                #self.sound.key_Enter.play()

            if self.carsol_cnt < self.max_menu_cnt:
                if event.key == K_RIGHT:
                    self.carsol_cnt += 1
                    self.sound.menu_carsol_move.play()
                    for i,pos in enumerate(self.pos_list):
                        if self.carsol_cnt == i:
                            self.carsol = pos
                            break 

            if self.carsol_cnt != 0:
                if event.key == K_LEFT:
                    self.carsol_cnt -= 1
                    self.sound.menu_carsol_move.play()
                    for i,pos in enumerate(self.pos_list):
                        if self.carsol_cnt == i:
                            self.carsol = pos
                            break
def main():
    pygame.init()
    font = pygame.font.Font('font_data/PixelMplus-20130602/PixelMplus12-Regular.ttf', 20)
    font.set_bold(True)
    width = 800 #screeen
    height = 640
    pygame.display.set_mode((width, height), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("マス打")
    #必要なオブジェクト（部品）をここへ
    bg = load_image('images/top_page/おまけピクチャ/800×600/pipo-pic001.jpg')#背景画像
    bg_rect = bg.get_rect()
    title = TitleText("マス打", (0, 0, 0))
    menu_list = ["はじめる", "おわる", "エンドロール"]
    start_menu = MainMenu(menu_list, (0, 0, 0), (width / 2 - 100, height / 2, 250, 160), 25)
    eventSE = EventSound()
    #button = Button()
    #s_btn_point = (width / 2 - 80, height / 2, 200, 50)
    #e_btn_point = (width / 2 - 80, height / 2 + 100, 200, 50)
    #s_text = font.render("はじめる", True, (255, 255, 255))
    #e_text = font.render("おわる", True, (255, 255, 255))
    #start = button.btn_init(s_btn_point)
    #end = button.btn_init(e_btn_point)
    auth_font = pygame.font.Font('font_data/PixelMplus-20130602/PixelMplus12-Regular.ttf', 20)
    auth_caption = pygame.Rect(0, 600, width, height-600)
    caption = auth_font.render("Copyright 2021-06-23 チームたんじろう all rights reserved", True, (0,0,0))
    #BGM
    mixer.init()
    #pygame.mixer.init(22050,-16,2,2048)
    mixer.music.load('sounds/OpeningThema/8bit29.mp3')
    mixer.music.set_volume(0.2)
    mixer.music.play(-1)
    #p = Pool(1)
    #p.apply_async(playsound, args=(['sounds/OpeningThema/8bit29.mp3']))
    yes_se = pygame.mixer.Sound('sounds/clickSound/systen40.wav')
    no_se = pygame.mixer.Sound('sounds/clickSound/systen41.wav')
    #タイトルウィンドウ表示
    title_page = True
    corse_select = False
    top_page = True
    #OP_BGM.start()
    loading = TextAnimation("よみこみちゅう..." ,screen)
    while top_page:#全体のループ

        while title_page:
            print(start_menu.carsol_cnt)
            screen.blit(bg, bg_rect)
            title.display(screen)
            start_menu.display(screen)
            #著作権表示
            pygame.draw.rect(screen, (20, 200, 20), auth_caption)
            screen.blit(caption, (100+20, 600+15))
            pygame.display.update()
            # イベント処理
            for event in pygame.event.get():
                start_menu.carsol_controle(event)
                if event.type == QUIT:          # 閉じるボタンが押されたとき
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:       # キーを押したとき
                    if event.key == K_RETURN:
                        if start_menu.carsol_cnt == 0:
                            eventSE.yes_btn.play()
                            corse_select = True
                            title_page = False
                        if start_menu.carsol_cnt == 1:
                            eventSE.no_btn.play()
                            pygame.quit()
                            sys.exit()    
                    if event.key == K_ESCAPE:   # Escキーが押されたとき
                        pygame.quit()
                        sys.exit()
        """
        while loading.end_flg == False:
            loading.display(screen)
            pygame.display.update()
            for event in pygame.event.get():
                exit_game(event)        
        """
        #ワールドマップ画面
        #必要なオブジェクトを定義
        map = load_image('Map_data/worldMapData.png')
        button = Button()
        select_carsol = SelectCorseCarsol(5)
        course1_btn_point = (40, 500, 200, 50)
        course2_btn_point = (80, 420, 200, 50)
        course3_btn_point = (200, 330, 200, 50)
        course4_btn_point = (width - 300, 100, 200, 50)
        c1_text = font.render("チュートリアル", True, (255, 255, 255))
        c2_text = font.render("初級コース", True, (255, 255, 255))
        c3_text = font.render("制作中！！", True, (100, 100, 100))
        c4_text = font.render("近日公開！！", True, (100, 100, 100))
        c1_btn = button.btn_init(course1_btn_point)
        c2_btn = button.btn_init(course2_btn_point)
        c3_btn = button.btn_init(course3_btn_point)
        c4_btn = button.btn_init(course4_btn_point)
        rn_text = font.render("もどる", True, (255, 255, 255))
        return_btn_point = (600, 500, 100, 50)
        return_btn = button.btn_init(return_btn_point)
        pygame.init()
        while corse_select:
            screen.fill((0, 0, 0))
            screen.blit(map, (0,0))
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
            select_carsol.display(screen)
            pygame.display.update()

            for event in pygame.event.get():
                exit_game(event)
                cours = select_carsol.carsol_controle(event) #EnterKeyでいまセレクトしているボタンのindexを返す。

                
                if cours ==0:#チュートリアル
                    yes_se.play()
                    #p.terminate()
                    mixer.music.stop()
                    eventSE.select_course.play()
                    print("チュートリアル button pressed!!")
                    while loading.end_flg == False:
                        loading.display(screen)
                        pygame.display.update()
                        for event in pygame.event.get():
                            exit_game(event)     
                    tutorial.main()
                    pygame.init()
                    game_tyutorial.main()
                    print("END")
                    pygame.init()
                if cours == 1:#初級
                    yes_se.play()
                    #p.terminate()
                    mixer.music.stop()
                    eventSE.select_course.play()
                    print("初級コース button pressed!!")
                    while loading.end_flg == False:
                        loading.display(screen)
                        pygame.display.update()
                        for event in pygame.event.get():
                            exit_game(event)
                    Syokyu.main()
                    #pygame.init()
                    mixer.music.load('sounds/OpeningThema/8bit29.mp3')
                    mixer.music.play(-1)
                if cours == 2:#中級
                    print("中級コース button pressed!!")
                    yes_se.play()
                    mixer.music.stop()
                    eventSE.select_course.play()
                    Tyukyu.main()
                    mixer.music.load('sounds/OpeningThema/8bit29.mp3')
                    mixer.music.play(-1)
                if cours == 3:#上級
                    yes_se.play()
                    print("上級コース button pressed!!")
                if cours == 4:#もどる
                    no_se.play()
                    title_page = True
                    corse_select = False

                
"""
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if c1_btn.collidepoint(event.pos):
                        #ここにその後の処理を追加
                        yes_se.play()
                        #p.terminate()
                        mixer.music.stop()
                        print("チュートリアル button pressed!!")
                        tutorial.main()
                        pygame.init()
                        game_tyutorial.main()
                        print("END")
                        pygame.init()

                    if c2_btn.collidepoint(event.pos):
                        #ここにその後の処理を追加
                        yes_se.play()
                        #p.terminate()
                        mixer.music.stop()
                        print("初級コース button pressed!!")
                        Syokyu.main()
                        #pygame.init()
                        mixer.music.load('sounds/OpeningThema/8bit29.mp3')
                        mixer.music.play(-1)
                    
                    if c3_btn.collidepoint(event.pos):
                        #ここにその後の処理を追加
                        yes_se.play()
                        print("中級コース button pressed!!")
                        
                    if c4_btn.collidepoint(event.pos):
                        #ここにその後の処理を追加
                        yes_se.play()
                        print("上級コース button pressed!!")
                        
                    if return_btn.collidepoint(event.pos):
                        no_se.play()
                        title_page = True
                        corse_select = False
"""              
   
if __name__ == "__main__":
    main()