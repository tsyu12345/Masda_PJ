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

GS = 32
DOWN, LEFT, RIGHT, UP = 0,1,2,3


class Player:
    animcycle = 24  # アニメーション速度
    frame = 0

    def __init__(self, name, pos, dir):
        self.name = name  # プレイヤー名（ファイル名と同じ）
        self.images = split_image_load(load_image("%s.png" % name))
        self.image = self.images[0]  # 描画中のイメージ
        self.x, self.y = pos[0], pos[1]  # 座標（単位：マス）
        self.rect = self.image.get_rect(topleft=(self.x*GS, self.y*GS))
        self.direction = dir

    def update(self):
        # キャラクターアニメーション（frameに応じて描画イメージを切り替える）
        self.frame += 1
        self.image = self.images[self.direction *
                                 4+self.frame/self.animcycle % 4]

    def move(self, dir, map):
        """プレイヤーを移動"""
        if dir == DOWN:
            self.direction = DOWN
            if map.is_movable(self.x, self.y+1):
                self.y += 1
                self.rect.top += GS
        elif dir == LEFT:
            self.direction = LEFT
            if map.is_movable(self.x-1, self.y):
                self.x -= 1
                self.rect.left -= GS
        elif dir == RIGHT:
            self.direction = RIGHT
            if map.is_movable(self.x+1, self.y):
                self.x += 1
                self.rect.left += GS
        elif dir == UP:
            self.direction = UP
            if map.is_movable(self.x, self.y-1):
                self.y -= 1
                self.rect.top -= GS

    def draw(self, screen):
        screen.blit(self.image, self.rect)

def main():
    pygame.init()
    font = pygame.font.Font('font_data/PixelMplus-20130602/PixelMplus10-Regular.ttf', 25)
    font.set_bold(True)
    width = 800  # screeen
    height = 640
    pygame.display.set_mode((width, height), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("マス打")
    # 必要なオブジェクト（部品）
    main_flg = True
    move_play = True
    type_play = False
    battle = False
    battle_ex = True
    end_tyutorial = False
    #player オブジェクト(仮)
    player_imgs = split_image_load(load_image('images/Characters/hero/pipo-charachip027c.png'))
    direction = DOWN
    player_x, player_y = 200/GS,150/GS #初期位置
    animcycle = 24
    frame = 0
    clock = pygame.time.Clock()
    
    #マップオブジェクト
    map = Map('Map_data/tyutorial_test.tmx')
    
    #メッセージボックス
    text_list = [
        "ほっほっほ。ワシは仏じゃ。",
        "ここではこのゲームの操作方法について説明するぞ。",
        "",#1
        "え？画面にキャラクターがいないって？",
        "",
        "",#2
        "決して、説明用のキャラを用意するのが面倒だったとか",
        "締め切りまでに間に合わなかったとか、",
        "そーゆーのではないから！！",#3
        "おほん。",
        "では、気を取り直して、まずキャラ操作の説明じゃ。",
        "",#4
        "基本操作は簡単。",
        "キーボードの➞キーで動かすことができるぞ。",
        "",#5
        "すこし歩きまわってみるがよい。",
        "※→キーを押すとその方向に進みます。",
        "※Enterを押すと次に進みます。",#6
        "", 
        "",
        "",#
        "次は、敵との戦い方について教えよう。",
        "" 
        "", #8
        "",
        "マップにダンジョンの入口があるじゃろ？", 
        "そこまでいってみるのじゃ。",
        "", #9
    ]
    text_list2 = [
        "モンスターと戦うには",
        "タイピング勝負しなければならんぞ。", 
        "", #
        "制限時間以内に", 
        "タイピングできなければ",
        "ダメージを食らってしまうぞ。", #
        "ではすこし練習といこうかの。", 
        "", 
        "", #
    ]
    text_list3 = [
        "ほほぉ。",
        "なかなかやるではないか。",
        "",#
        "これならば冒険に出ても問題なかろう。",
        "",
        "",#
        "それでは勇者マスダよ、",
        "魔王北原を討伐し、",
        "世界に再び平穏をもたらすのじゃ！！",#
        ]
    dic = {
            'RPG':"rpg",
            '冒険':'bouken',
            'イス':"isu",
            ' ':' '#End
        }
    monster = Monster(
        'images/Characters/enemys/pipo-enemy46set/120x120/pipo-enemy002.png', (width / 2, height/2-100),5,1)
    aitem_btn = Button("アイテム", (255, 255, 255), (0, 0, 0), (width / 4, height-100, 100, 30))
    status_bar = DisplayParameter(10, 10)
    typeGame = TypeingGame(dic, 10)
    #text_render = font.render("", True, (255, 255, 255))
    move_cnt = 0
    disp_elps = False

    msg_box_point = (50, 400, 700, 150)
    msg_box = MsgBox(text_list)
    msg_box2 = MsgBox(text_list2)
    msg_box3 = MsgBox(text_list3)
    
    while main_flg:
        
        while end_tyutorial:
            pygame.init()
            pygame.draw.rect(screen, (0, 0, 0), Rect(0, 0, width, height))
            msg_box3.display(screen, msg_box_point)
            pygame.display.update()
            if msg_box3.end_flg:
                main_flg = False
                end_tyutorial = False
            for event in pygame.event.get():
                msg_box3.text_update(event)
                #input_key = typeGame.input_word(event)
                if event.type == QUIT:          # 閉じるボタンが押されたとき
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:# キーを押したとき
                    if event.key == K_ESCAPE:   # Escキーが押されたとき
                        pygame.quit()
                        sys.exit()


        while type_play:
            #Typing_tyutorial
            pygame.init()
            pygame.draw.rect(screen, (0, 0, 0), Rect(0, 0, width, height))
            monster.display(screen)
            aitem_btn.display(screen)
            status_bar.display(screen)
            if battle_ex:
                msg_box2.display(screen, msg_box_point)
                if msg_box2.end_flg:
                    battle_ex = False
                    battle = True
                    typeGame.count_down.start_cnt()
            if battle:
                typeGame.display(screen)
                typeGame.count_down.display(screen)
                if typeGame.end_flg:
                    #pygame.quit()
                    #sys.exit()
                    type_play = False
                    end_tyutorial = True

            
            pygame.display.update()
            
            #イベント処理
            for event in pygame.event.get():
                # 終了用のイベント処理
                if battle_ex:
                    msg_box2.text_update(event)
                if battle:
                    typeGame.input_word(event)

                #input_key = typeGame.input_word(event)
                if event.type == QUIT:          # 閉じるボタンが押されたとき
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:# キーを押したとき
                    if event.key == K_ESCAPE:   # Escキーが押されたとき
                        pygame.quit()
                        sys.exit()

        while move_play:
            clock.tick(60)
            frame += 1
            player_img = player_imgs[int(direction*4 + frame/animcycle%3)]
            map.draw_map(screen)
            screen.blit(player_img, (player_x*GS, player_y*GS))
            if msg_box.disabled == False:
                msg_box.display(screen, msg_box_point)
            if msg_box.end_flg and disp_elps:
                pygame.draw.circle(screen, (255,0,0), (595,425), 30, 5)
            pygame.display.update()
            
            if msg_box.msg_index == 18:
                msg_box.disabled = True
            else:
                msg_box.disabled = False
            if msg_box.end_flg:
                if frame % 100 == 0:
                    disp_elps = False
                else: 
                    disp_elps = True   
                msg_box.disabled = True
                if player_x*GS == 584.0 and player_y*GS == 406.0:
                    type_play = True
                    move_play = False
                    break
            #pygame.time.wait(100)
            #pygame.time.wait(80)
            #text_render = font.render(text_list[0:int(frame/10)], True, (255, 255, 255))
            
            for event in pygame.event.get():
                msg_box.text_update(event)
                if event.type == QUIT:          # 閉じるボタンが押されたとき
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:       # キーを押したとき
                    if event.key == K_ESCAPE:   # Escキーが押されたとき
                        pygame.quit()
                        sys.exit()
                    if event.key == K_DOWN:
                        direction = DOWN
                    #if is_movable(x, y+1):
                        player_y += 1
                    if event.key == K_LEFT:
                        direction = LEFT
                #if is_movable(x-1, y):
                        player_x -= 1
                    if event.key == K_RIGHT:
                        direction = RIGHT
                #if is_movable(x+1, y):
                        player_x += 1
                    if event.key == K_UP:
                        direction = UP
                #if is_movable(x, y-1):
                        player_y -= 1            

if __name__ == "__main__":
    main()