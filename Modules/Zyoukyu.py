import pygame
from pygame.locals import *
from pygame import mixer
from random import randint
#from pytmx.util_pygame import load_pygame
from .GameModules.LoadMap import Map
from .GameModules.MsgBox import MsgBox, OneLineMsgBox
from .GameModules.battleWindow import *
from .GameModules.LocalFunc import *
from .GameModules.Charactor import Player
from .GameModules.Charactor import Character 
from .GameModules.EventSE import EventSound as ES
from .GameModules.EventSE import PlayerSound as PS


GAMEOVER = False

def Battle(monster_img, sound_path, dic, screen:pygame.Surface, player:Player):
    width, height = screen.get_size()
    if monster_img != None:
        monster = Monster(monster_img, (width / 2, height/2-100),5,1)
    aitem_btn = Button("アイテム", (255, 255, 255), (0, 0, 0), (width / 4, height-100, 100, 30))
    status_bar = DisplayParameter(player.HP, 1)
    typing = TypeingGame(dic,4)
    gameOver = False
    mixer.music.load(sound_path)
    mixer.music.play(-1)
    typing.count_down.start_cnt()
    while True:
        pygame.draw.rect(screen, (0, 0, 0), Rect(0, 0, width, height))
        if monster_img != None:
            monster.display(screen)
        aitem_btn.display(screen)
        status_bar.display(screen)
        typing.display(screen)
        typing.count_down.display(screen)
        #typing.count_down.display(screen)
        pygame.display.update()

        if player.HP == 0:
            #p.terminate()
            gameOver = True
            break

        if typing.damege:
            #print("in")
            status_bar.HP -= 1
            player.HP -= 1
            typing.damege = False

        if typing.end_flg:
            mixer.music.stop()
            mixer.music.load('sounds/OpeningThema/NeoRock62.mp3')
            mixer.music.set_volume(0.3)
            mixer.music.play(-1)
            return True
            #break
        for event in pygame.event.get():
            exit_game(event)
            typing.input_word(event)
        
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
            player.HP = 10
            mixer.music.stop()
            gameOver = False
            return False
        for event in pygame.event.get():
            msg_box_over.text_update(event)
            exit_game(event)

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
    #導入ストーリ
    story_text = [
        "俺はついに、魔王北原の住む島に到着した。",
        "",
        "",#
        "ここからいったい",
        "どんな戦いが待っているのだろう。",
        "皆目見当もつかない。",#
        "だが俺はこれまでの冒険で",
        "パワーアップしてるはずだ！。",
        "",#
        "いくぞ！",
        "うぉぉぉぉぉぉ！！！",
    ]
    story_box = MsgBox(story_text)
    story_box_point = (50, 400, 700, 150)
    hotoke = load_image('images/Characters/other/0205000021.png')
    #状態フラグ変数
    first_story_flg = True
    bouken_flg = False
    lasbos = False
    battle_list = [False,False,False,False]
    #Sounds
    event_SE = EventSound()
    #play_SE = PlayerSound()
    #Map
    map = Map('Map_data/ZyoukyuuMapData.tmx')
    #Player
    player = Player('images/Characters/hero/pipo-charachip027c.png', screen, map)
    player.posX, player.posY =304, 1224

    while first_story_flg:
        story_box.display(screen, story_box_point)
        pygame.display.update()
        if story_box.end_flg:
            first_story_flg = False
            bouken_flg = True
            break
        for event in pygame.event.get():
            exit_game(event)#終了用イベント処理
            story_box.text_update(event)
    mixer.init()
    mixer.music.load('sounds/OpeningThema/NeoRock62.mp3')
    mixer.music.set_volume(0.3)
    mixer.music.play(-1)
    
    q1 = {
        "魔王魂":"maoudamasii",
        "GitHub":"github",
        "レイカーツワイル":"reika-tuwairu",
        "オーケストラ":"o-kesutora",
        "breakfast":"breakfast",
        "民俗音楽":"minnzokuonngaku",
        "モンスター":"monnsuta-",
        "ロンギヌスの槍":"ronnginusunoyari",
        "死海文書":"sikaimonnzyo",
        "ヤマト作戦":"yamatosakusenn",
        "日本国憲法":"nihonnkokukennpou",
        "東ロボ君":"tourobokunn",
        "正義の鉄拳":"seiginotekkenn",
    }
    q2 = {
        "深層学習":"sinnsougakusyuu",
        "Windows":"windows",
        "Mac":"mac",
        "Intel":"intel",
        "酸化防止剤":"sannkabousizai",
        "自動運転":"zidouunntenn",
        "スピリタス":"supiritasu",
        "サッポロビール":"sapporobi-ru",
        "目覚まし時計":"mesamasidokei",
        "スペルミス":"superumisu",
        "オレンジオイル":"orennzioiru",
        "ブルートゥース":"buru-tlu-su",
    }
    q3 = {
        "朝ごはん":"asagohann",
        "食べてますか":"tabetemasuka",
        "お盆":"obonn",
        "犬":"inu",
        "猫":"neko",
        "もう少しでクリアだよ":"mousukosidekuriadayo",
        "次はいよいよ魔王だ":"tugihaiyoiyomaouda",
    }

    q4 = {
        "グレートブリテン":"gure-toburitenn",
        "北アイルランド連合王国":"kitaairuranndorenngououkoku",
        "スリランカ民主社会主義共和国":"surirannkaminnsyusyakaisyugikyouwakoku",
        "グレナディーン諸島":"gurenadeli-nnsyotou",
        "朝鮮民主主義人民共和国":"tyousennminnsyusyugizinnmimmkyouwakoku",
        "東ティーモール民主共和国":"higasiteli-mo-ruminnsyukyouwakoku",
        "ネパール連邦民主共和国":"nepa-rurennpouminnsyukyouwakoku",
        "アルジェリア民主人民共和国":"aruzyeriaminnsyuzinnminnkyouwakoku",
        "サントメプリンシペ":"sanntomepurinnsipe",
        "情報科学":"zyouhoukagaku",
        "フーリエ変換":"hu-riehennkann",
        "スペクトログラム":"supekutoroguramu",
        "コンピュータサイエンス":"konnpyu-ta-saiennsu",
    }
    
    while bouken_flg:
        map.draw_map(screen, player.posX, player.posY)
        player.display(screen)
        pygame.display.update()
        player.move()
        posX = int(player.posX/GS) 
        posY = int(player.posY/GS)
        if posX == 18 and posY == 24 and battle_list[0] == False:
            event_SE.battle_catch.play()
            pygame.draw.rect(screen, (255,255, 255), Rect(0, 0, width, height))
            pygame.display.update()
            pygame.time.wait(1000)
            battle = Battle('images/Characters/enemys/pipo-enemy46set/120x120/pipo-boss002.png', 'sounds/BattleSounds/RandomBattle5.mp3', q1, screen, player)
            if battle == False:
                bouken_flg = False
                break
            battle_list[0] = battle
        if posX == 29 and posY == 20 and battle_list[1] == False:
            event_SE.battle_catch.play()
            pygame.draw.rect(screen, (255,255, 255), Rect(0, 0, width, height))
            pygame.display.update()
            pygame.time.wait(1000)
            battle = Battle('images/Characters/enemys/pipo-enemy46set/120x120/pipo-boss003.png', 'sounds/BattleSounds/RandomBattle.mp3', q2, screen, player)
            if battle == False:
                bouken_flg = False
                break
            battle_list[1] = battle
        if posX == 42 and posY == 14 and battle_list[2] == False:
            event_SE.battle_catch.play()
            pygame.draw.rect(screen, (255,255, 255), Rect(0, 0, width, height))
            pygame.display.update()
            pygame.time.wait(1000)
            battle = Battle('images/Characters/enemys/pipo-enemy46set/120x120/pipo-boss004.png', 'sounds/BattleSounds/RandomBattle3.mp3', q3, screen, player)
            if battle == False:
                bouken_flg = False
                break
            battle_list[2] = battle
        
        if posX == 44 and posY == 8:
            lasbos = True
            mixer.music.stop()
            bouken_flg = False
            
        for event in pygame.event.get():
            exit_game(event)#終了用イベント処理


    story_text2 = [
        "俺はついに、魔王北原の城へついた。", 
        "魔王ついに俺はここまで辿り着いたぞ！",
        "「勇者よ我は魔王北原、」",
        "「貴様の到着を今や遅しと待ちわびておったぞ！」",
        "「世界の平和取り戻したくば、」",
        "「この私を倒してみよ！！！」",
        "いままでよくもやってくれたなぁぁ！！", 
        "くらえ鍛え上げたタイピングスキルを！"
    ]
    story_box = OneLineMsgBox(story_text2, story_box_point)
    kitahara = pygame.image.load('images/Characters/enemys/lasbos.png').convert()
    color_key = kitahara.get_at((0, 0))
    kitahara.set_colorkey(color_key, RLEACCEL)
    kitahara_hello = pygame.mixer.Sound('sounds/voice/kitahara1.wav')
    voiced=False
    while lasbos:
        pygame.draw.rect(screen, (0,0, 0), Rect(0, 0, width, height))
        if story_box.index >= 2:
            #print(kitahara)
            screen.blit(kitahara, (150, 0))
        story_box.display(screen)
        pygame.display.update()
        #print(story_box.index)
        if story_box.index ==2 and voiced == False:
            kitahara_hello.play()
            voiced = True
        if story_box.end_flg:
            event_SE.battle_catch.play()
            pygame.draw.rect(screen, (255,255, 255), Rect(0, 0, width, height))
            pygame.display.update()
            pygame.time.wait(1000)
            battle = Battle(None, 'sounds/BattleSounds/lasbos.mp3', q4, screen, player)
            if battle == False:
                lasbos = False
                break
            battle_list[3] = battle
        for event in pygame.event.get():
            exit_game(event)#終了用イベント処理
            story_box.text_update(event)
        






