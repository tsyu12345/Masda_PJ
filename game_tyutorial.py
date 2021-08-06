import pygame
from pygame.locals import *
import pytmx
from pytmx.util_pygame import load_pygame
import sys
import csv
import os
from LoadMap import Map
from Charactor import Player
from MsgBox import MsgBox
from battleWindow import *
from LocalFunc import *
from EventSE import EventSound as ES
from EventSE import PlayerSound as PS
from playsound import playsound
from  multiprocessing import Pool
GS = 32
DOWN, LEFT, RIGHT, UP = 0,1,2,3

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
    #player オブジェクト
    player = Player('images/Characters/hero/pipo-charachip027c.png', 10, 1, screen)
    player.posX, player.posY = 250, 300
    #player_imgs = split_image_load(load_image('images/Characters/hero/pipo-charachip027c.png'))
    direction = DOWN
    #player_x, player_y = 250/GS,300/GS #初期位置
    animcycle = 24
    frame = 0
    clock = pygame.time.Clock()
    
    hotoke = load_image('images/Characters/other/0205000021.png')
    #マップオブジェクト
    map = Map('Map_data/tyutorialMapData.tmx')
    
    #メッセージボックス
    text_list = [
        "ほっほっほ。ワシは仏じゃ。",
        "ここではこのゲームの操作方法について説明するぞ。",
        "",#1
        "え？なんかしょぼいいって？",
        "",
        "ぶっ殺すぞ？",#2
        "決して、マップ作るのが面倒だったとか",
        "締め切りまでに間に合わなかったとか、",
        "そーゆーのではないからな。",#3
        "それにいまEsc押そうとしただろう。",
        "もう少し、がんばろうか？",
        "",#
        "おほん。",
        "では、気を取り直して、まずキャラ操作の説明じゃ。",
        "",#4
        "基本操作は簡単。",
        "キーボードの→キーで動かすことができるぞ。",
        "",#5
        "すこし歩きまわってみるがよい。",
        "※→キーを押すとその方向に進みます。",
        "※Enterを押すと次に進みます。",#6
        "",
        "",
        "",#
        "どーかな。", 
        "感覚はつかめたじゃろう。",
        "",
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

    event_sound = ES()
    player_sound = PS()

    msg_box_point = (50, 400, 700, 150)
    msg_box = MsgBox(text_list)
    msg_box2 = MsgBox(text_list2)
    msg_box3 = MsgBox(text_list3)
    p = Pool(1)
    p.apply_async(playsound, args=(['sounds/OpeningThema/8bit22.mp3']))
    while main_flg:
        
        while end_tyutorial:
            pygame.init()
            pygame.draw.rect(screen, (0, 0, 0), Rect(0, 0, width, height))
            msg_box3.display(screen, msg_box_point)
            pygame.display.update()
            if msg_box3.end_flg:
                main_flg = False
                end_tyutorial = False
                p.terminate()
            for event in pygame.event.get():
                event_sound.event_catch_se(event)
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
                event_sound.event_catch_se(event)
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
            #player_img = player_imgs[int(direction*4 + frame/animcycle%3)]
            #map.draw_map(screen, player_x*GS, player_y*GS)
            map.draw_map(screen, player.posX, player.posY)
            player.display(screen)
            #screen.blit(player_img, (player_x*GS, player_y*GS))
            if msg_box.disabled == False:
                screen.blit(hotoke, (msg_box_point[0]+40, msg_box_point[1]-60))
                msg_box.display(screen, msg_box_point)
                #msg_box.name_tag(screen, 'ほとけ')
            #if msg_box.end_flg and disp_elps:
               # pygame.draw.circle(screen, (255,0,0), (595+player.offX,425+player.offY), 30, 5)
            pygame.display.update()
            
            if msg_box.msg_index == 21:
                msg_box.disabled = True
            else:
                msg_box.disabled = False
            if msg_box.end_flg:
                if frame % 100 == 0:
                    disp_elps = False
                else: 
                    disp_elps = True   
                msg_box.disabled = True
                if player.posX == 1114 and player.posY == 844:
                    type_play = True
                    move_play = False
                    break
            #pygame.time.wait(100)
            #pygame.time.wait(80)
            #text_render = font.render(text_list[0:int(frame/10)], True, (255, 255, 255))
            
            for event in pygame.event.get():
                exit_game(event)
                player.move(event)
                event_sound.event_catch_se(event)
                msg_box.text_update(event)
                

if __name__ == "__main__":
    main()