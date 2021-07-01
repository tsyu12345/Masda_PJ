import pygame
from pygame.locals import *
from pygame import mixer
import sys
import csv

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

class WorldMap:
    def __init__(self, csv_file):
        self.csv_file = csv_file
    
    def map_data(self):
        file = open(self.csv_file, "r", encoding='ms932', errors="", newline="")
        data = csv.reader(file, doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        map = []
        for row in data:
            map.append(row)
        return map
    
    def draw(self):
        map = self.map_data()
        row,col = len(map), len(map[0])
        imgs = [None] * 256             # マップチップ
        msize = 16                      # 1マスの大きさ[px]
        




def load_img(path):
    bg_img = pygame.image.load(path)
    bg = bg_img.convert_alpha()
    return bg



def main():
    map = WorldMap('Map_data/world Map1/world_map_data..csv')
    map.map_data()

    pygame.init()
    font = pygame.font.Font('font_data/misaki_gothic_2nd.ttf', 20)
    font.set_bold(True)
    width = 800
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

    #タイトルウィンドウ表示
    while True:
    
        screen.blit(bg, bg_rect)
        title.display(screen)
        pygame.draw.rect(screen, (255, 255,255), start, 6) #縁
        pygame.draw.rect(screen, (255, 255,255), end, 6)
        pygame.draw.rect(screen, (0, 0, 0), start)
        pygame.draw.rect(screen, (0, 0, 0), end)
        #以下はボタンテキストの描画screen.blit(btnObject, (x, y))
        screen.blit(s_text, (s_btn_point[0] + 60 , s_btn_point[1] + 15))
        screen.blit(e_text, (e_btn_point[0] + 63, e_btn_point[1] + 15))
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

                elif end.collidepoint(event.pos):
                    print("end button presssed!!")
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()