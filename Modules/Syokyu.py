import pygame
from pygame.locals import *
from pygame import mixer
#from pytmx.util_pygame import load_pygame
from .GameModules.LoadMap import Map
from .GameModules.MsgBox import MsgBox, OneLineMsgBox
from .GameModules.battleWindow import *
from .GameModules.LocalFunc import *
from .GameModules.Charactor import Player
from .GameModules.EventSE import EventSound as ES
from .GameModules.EventSE import PlayerSound as PS

GS = 32
DOWN, LEFT, RIGHT, UP = 0,1,2,3

def main():
    #init pygame
    pygame.init()
    font = pygame.font.Font('font_data/PixelMplus-20130602/PixelMplus10-Regular.ttf', 25)
    font.set_bold(True)
    width = 800  # screeen
    height = 640
    pygame.display.set_mode((width, height), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("マス打")
    # 必要なオブジェクト（部品）
    main_flg =True
    story_flg = True
    battle = False
    #Msg Box
    story1 = [
        "...",
        "",
        "",#
        "なにかが空で光っている...",
        "",
        "",#
        "マスダー、、マスダーよ。",
        "聞くがいい。",
        "ここからが魔物の住まう領域じゃ。",#
        "各地に散らばる魔物を倒し、",
        "果ての海の向こう岸にある、",
        "魔王北原の城を目指すのじゃ！。",#
        "...",
        "",
        "",#
        "え？",
        "どこに行けばいいかって？",
        "",#
        "そーですね、まずは",
        "...",
        "",#
        "冒険初級の街「ロンデル」に",
        "行ってもらおうかのぉ。",
        "",#
        "そこで、モンスターとの戦闘になれてもらうのが",
        "先決じゃな。",
        "",#
        "...",
        "",
        "",#
        "ん？",
        "なかまは増えないのかって？。",
        "",#
        "確かに、ドラ●ンクエストでは、",
        "仲間が増えていくが、、、",
        "",#
        "このRPGでは、そんなのはないぞ？",
        "",
        "",#
        "...",
        "",
        "",#
        "なぜって、そりゃあ...",
        "作る時間がなかったからじゃな！",
        "ガハハハッ！",#
        "ごほん！。",
        "",
        "",#
        "では勇者よ！",#
        "これが冒険のはじまりじゃ！",
        "幸運を。...",#
        ]
    frame = 0
    msg_box = MsgBox(story1)
    msg_box_point = (50, 400, 700, 150)
    hotoke = load_image('images/Characters/other/0205000021.png')
    #Map
    map = Map('Map_data/SyokyuMapData.tmx')
    #Player
    player = Player('images/Characters/hero/pipo-charachip027c.png', 10, 1, screen)
    player.posX, player.posY = 400, 320
    """
    heishi_pos = [[], [], [], []]
    murabito_A_pos = [[],[],[],[],[],[],[],[]]
    murabito_B_pos = [[],[],[],[],[],[],[],[]]
    heishi = Character('images/Characters/キャラチップ/pipo-charachip018.png',1,1, screen)
    murabitoA = Character('images/Characters/キャラチップ/pipo-charachip016a.png', 1,1, screen)
    murabitoB = Character('images/Characters/キャラチップ/pipo-charachip025c.png',1,1,screen)
    """
    #Draw Window

    while story_flg:
        if msg_box.msg_index >= 6:
            pygame.time.wait(30)
            frame += 1
            if frame > 255:
                frame = 255
            pygame.draw.rect(screen, (frame, frame, frame), Rect(0, 0, width, height))
            screen.blit(hotoke, (msg_box_point[0]+40, msg_box_point[1]-60))
        msg_box.display(screen, msg_box_point)
        
        pygame.display.update()
        if msg_box.end_flg:
            story_flg = False
            main_flg = True
            break
        for event in pygame.event.get():
            msg_box.text_update(event)
            exit_game(event)
    
    
    #pygame.init()
    murabito_msg1= [
        "ダンジョンの場所かい？",
        "さーおいらはしらないねぇ"
    ]
    murabito_msg2 = ["ここは皇女殿下の城だ。","招待されたものしか入場できんぞ。","分かったらさっさと帰れ。"]
    murabito_msg3 = ["ダンジョンの場所だって？","それなら前、川向うで見たよ。","おっかなくて逃げてきたんだ。","兄ちゃん、あいつらを倒してきてくれよ。"]
    announce_list = ["まずは、ダンジョンの場所を調べよう！。", "村人に話しかけると何か得られそうだ。"]
    announce_list2 = ["どうやら、川の向こう側にあるよだ。","ダンジョンは洞窟の形をしているみたいだぞ。"]
    mob_box_point = (50, 400, 700, 150)
    mob1 = OneLineMsgBox(murabito_msg1,mob_box_point)
    mob2 = OneLineMsgBox(murabito_msg2,mob_box_point)
    mob3 = OneLineMsgBox(murabito_msg3,mob_box_point)
    announce_box_point = (50, height/2, width - 100, 80)
    announce_box = OneLineMsgBox(announce_list,announce_box_point)
    announce_box2 = OneLineMsgBox(announce_list2, announce_box_point)
    #p = Pool(1)
    #p.apply_async(playsound, args=(['sounds/OpeningThema/8bit01.mp3']))
    pygame.init()
    mixer.init()
    mixer.music.load('sounds/OpeningThema/8bit01.mp3')
    mixer.music.play(-1)
    while main_flg:
        #pygame.draw.rect(screen, (0, 0, 0), Rect(0, 0, width, height))
        map.draw_map(screen, player.posX, player.posY)
        player.display(screen)

        if player.posX==464 and player.posY ==608:
            if mob2.end_flg == False:
                mob2.display(screen)
            #else:
                #mob2.end_flg = False
        if player.posX == 176 and player.posY ==608:
            if mob3.end_flg == False:
                mob3.display(screen)
            else:
                if announce_box2.end_flg == False:
                    announce_box2.display(screen)
            #else:
                #mob3.end_flg = False    
        if player.posX == 368 and player.posY ==448:
            if mob1.end_flg == False:
                mob1.display(screen)
            #else:
                #mob1.end_flg = False
        if announce_box.end_flg == False:
            announce_box.display(screen)
        
        if player.posX ==816 and player.posY ==192:
            battle = True
            main_flg = False
            #p.terminate()
            mixer.music.stop()
            break
           
        pygame.display.update()
        for event in pygame.event.get():
            announce_box.text_update(event)
            announce_box2.text_update(event)
            mob1.text_update(event)
            mob2.text_update(event)
            mob3.text_update(event)
            player.move(event)
            exit_game(event)

    pygame.init()
    event_sound = ES()
    monster = Monster('images/Characters/enemys/pipo-enemy46set/240x240/pipo-enemy001b.png', (width / 2, height/2-100),5,1)
    aitem_btn = Button("アイテム", (255, 255, 255), (0, 0, 0), (width / 4, height-100, 100, 30))
    status_bar = DisplayParameter(10, 1)
    dic = {
            'RPG':"rpg",
            '冒険':'bouken',
            'イス':"isu",
            '消しゴム':"kesigomu",
            '焼肉':"yakiniku",
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
            '筆箱':'fudebako',
            ' ':' '#End
        }
    typeGame = TypeingGame(dic, 7)
    typeGame.count_down.start_cnt()
    gameOver = False
    gameClear = False
    #p = Pool(1)
    #p.apply_async(playsound, args=(['sounds/OpeningThema/8bit28.mp3']))
    mixer.init()
    mixer.music.load('sounds/OpeningThema/8bit28.mp3')
    mixer.music.play(-1)
    while battle:
        pygame.draw.rect(screen, (0, 0, 0), Rect(0, 0, width, height))
        monster.display(screen)
        aitem_btn.display(screen)
        status_bar.display(screen)
        typeGame.display(screen)
        typeGame.count_down.display(screen)
        if typeGame.damege:
            print("in")
            status_bar.HP -= 1
            player.HP -= 1
            typeGame.damege = False
        
        if player.HP == 0:
            #p.terminate()
            gameOver = True
            battle = False
            break

        if typeGame.end_flg:
            print("in")
            #p.terminate()
            mixer.music.stop()
            gameClear = True
            battle = False
            break
            #pygame.quit()
            #sys.exit()
        pygame.display.update()
        
        #イベント処理
        for event in pygame.event.get():
            # 終了用のイベント処理
            exit_game(event)
            event_sound.event_catch_se(event)
            typeGame.input_word(event)


    pygame.init()
    story_over = [
        "...",
        "",
        "",#
        "ああ...",
        "",
        "",#
        "勇者よ、、",
        "死んでしまうとは情けない。",
        "",#
        "王道なら、",
        "教会へ行き",
        "復活できるけど、",#
        "ここにはそんなものありませーん！",
        "",
        "",#
        "負けた罰として、",
        "おぬしのレベルを２つ下げる！！",
        "",#
        "魔王は今回とは桁違いの強さ、、",
        "先行きが不安じゃのぉ、、、",
        "",#
        ]
    frame = 0
    msg_box_over = MsgBox(story_over)
    msg_box_point = (50, 400, 700, 150)
    hotoke = load_image('images/Characters/other/0205000021.png')
    #p = Pool(1)
    #p.apply_async(playsound, args=(['sounds/OpeningThema/gameover.mp3']))
    mixer.init()
    mixer.music.load('sounds/OpeningThema/gameover.mp3')
    mixer.music.play(-1)
    while gameOver:
        if msg_box_over.msg_index >= 6:
            pygame.time.wait(30)
            frame += 1
            if frame > 255:
                frame = 255
            pygame.draw.rect(screen, (frame, frame, frame), Rect(0, 0, width, height))
            screen.blit(hotoke, (msg_box_point[0]+40, msg_box_point[1]-60))
        msg_box_over.display(screen, msg_box_point)
        pygame.display.update()
        if msg_box_over.end_flg:
            #p.terminate()
            mixer.music.stop()
            break
        for event in pygame.event.get():
            msg_box_over.text_update(event)
            exit_game(event)
    
    story2 = [
        "...",
        "",
        "",#
        "なにかが空で光っている...",
        "",
        "",#
        "マスダー、、マスダーよ。",
        "よくぞ初級コースをクリアしたな！",
        "だが、ここからが本番じゃ。",#
        "まだ各地に散らばる魔物はたくさんおる",
        "",
        "",#
        "勇者よ、",
        "おぬしはもっと強くならねばならん。",
        "",#
        "今回はクリアした報酬として、",
        "おぬしのレベルを2つばかり上げてやろう。",
        "",#
        "だが、まだまだじゃ。",
        "魔王は今回とは桁違いの強さ、、",
        "あなどってはいかんぞ？",#
        "...",
        "",
        "",#
        "ん？つぎの場所はどこだって？",
        "",
        "",#
        "...",
        "",
        "",#
        "メタい話、忙しくてまだ開発途中なんじゃ...",
        "完成したら教えるから、",
        "すこし宿屋でまっててくれたまえ。",#
        "...",
        "いや、まじごめんて。",
        "",#
        "そんな、怒らないでよ！",
        "",
        "",#
        ]
    frame = 0
    msg_box2 = MsgBox(story2)
    msg_box_point = (50, 400, 700, 150)
    housyuu_se = PlayerSound()
    hotoke = load_image('images/Characters/other/0205000021.png')
    #p = Pool(1)
    #p.apply_async(playsound, args=(['sounds/OpeningThema/neoRock33.mp3']))
    mixer.init()
    mixer.music.load('sounds/OpeningThema/neoRock33.mp3')
    mixer.music.play(-1)
    while gameClear:
        if msg_box2.msg_index == 15:
            housyuu_se.levelUP.play()
        if msg_box2.msg_index >= 6:
            pygame.time.wait(30)
            frame += 1
            if frame > 255:
                frame = 255
            pygame.draw.rect(screen, (frame, frame, frame), Rect(0, 0, width, height))
            screen.blit(hotoke, (msg_box_point[0]+40, msg_box_point[1]-60))
        msg_box2.display(screen, msg_box_point)
        
        pygame.display.update()
        if msg_box2.end_flg:
            #p.terminate()
            mixer.music.stop()
            break
        for event in pygame.event.get():
            msg_box2.text_update(event)
            exit_game(event)

    
if __name__ == '__main__':
    main()