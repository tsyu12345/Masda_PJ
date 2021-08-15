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

GS = 32
DOWN, LEFT, RIGHT, UP = 0,1,2,3


def Battle(monster_img, sound_path, battle_instance:TypeingGame, screen:pygame.Surface, player:Player):
    width, height = screen.get_size()
    monster = Monster(monster_img, (width / 2, height/2-100),5,1)
    aitem_btn = Button("アイテム", (255, 255, 255), (0, 0, 0), (width / 4, height-100, 100, 30))
    status_bar = DisplayParameter(10, 1)
    mixer.music.load(sound_path)
    mixer.music.play(-1)
    battle_instance.count_down.start_cnt()
    while True:
        pygame.draw.rect(screen, (0, 0, 0), Rect(0, 0, width, height))
        monster.display(screen)
        aitem_btn.display(screen)
        status_bar.display(screen)
        battle_instance.display(screen)
        battle_instance.count_down.display(screen)
        #battle_instance.count_down.display(screen)
        pygame.display.update()
        if battle_instance.damege:
            #print("in")
            status_bar.HP -= 1
            player.HP -= 1
            battle_instance.damege = False

        if player.HP == 0:
            #p.terminate()
            gameOver = True
            break

        if battle_instance.end_flg:
            mixer.music.stop()
            mixer.music.load('sounds/OpeningThema/NeoRock47.mp3')
            mixer.music.set_volume(0.3)
            mixer.music.play(-1)
            return True
            #break
        for event in pygame.event.get():
            exit_game(event)
            battle_instance.input_word(event)
    
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
    story1 = [
        "冒険を初めて数か月がたった。",
        "初級の街ロンデルにて修行の日々を送っていた。",
        "そろそろ次の街へ行かないとなぁ。",#
        "・・・",
        "",
        "",#
        "マスダー、、マスダーよ。",
        "久しぶりじゃのぉ。",
        "元気しとったか",#
        "そろそろ冒険者中級コースへ挑戦じゃな。",
        "",
        "",#
        "次に行ってもらう街は、",
        "アルヌスという街じゃ！。",
        "",#
        "この街は、海辺に面しておる。",
        "",
        "",#
        "その海の先には、",
        "あの魔王北原のいる城があるじゃろう。",
        "",#
        "ここで十分に力を積まなければ、",
        "あの魔王に勝つことは到底できまい...。",
        "",#
        "そこでじゃ！",
        "今この街は、魔王の放ったモンスター",
        "たちによって、すこし荒らされておる。",#
        "ここのモンスターたちはちょいとばかり強い",
        "モンスターが多い。",
        "",#
        "いい練習相手になるじゃろう。",
        "森の入口にある洞窟で特訓できるはずじゃ。",
        "",#
        "モンスターを倒した後は、",
        "海辺へ向かい、いよいよ魔王城へ突入じゃ！",
        "",#
        "では幸運をいのる...。",
        "",
        "",#
    ]
    story_box = MsgBox(story1)
    story_box_point = (50, 400, 700, 150)
    hotoke = load_image('images/Characters/other/0205000021.png')
    #状態フラグ変数
    first_story_flg = True
    bouken_flg = False
    quest_flg = False
    battle_list = [False,False,False,False,False]
    #以下メインループ

    while first_story_flg:
        story_box.display(screen, story_box_point)
        pygame.display.update()
        if story_box.msg_index >= 6:
            screen.blit(hotoke, (story_box_point[0]+40, story_box_point[1]-60))
        if story_box.end_flg:
            first_story_flg = False
            bouken_flg = True
            break
        for event in pygame.event.get():
            exit_game(event)#終了用イベント処理
            story_box.text_update(event)

    map_data = 'Map_data/TyukyuMapData.tmx'
    map = Map(map_data)
    player = Player('images/Characters/hero/pipo-charachip027c.png',screen, map)
    player.posX, player.posY = 35, 275

    mob_imgs_list = ["images/Characters/キャラチップ/pipo-charachip028c.png",]
    mobs = []
    for mob in mob_imgs_list:
        add = Character(mob,screen)
        mobs.append(add)
    mixer.init()
    mixer.music.load('sounds/OpeningThema/NeoRock47.mp3')
    mixer.music.set_volume(0.3)
    mixer.music.play(-1)
    
    #ランダム座標戦闘用の問題
    random_question1 = {
        "k-平均法":"kheikinnhou",
        "DeepLearning":"deeplearning",
        "Watson":"watson",
        "エキスパートシステム":"ekisupa-tosisutemu",
        "人工知能":"zinnkoutinou",
        "サポートベクターマシン":"sapo-tobekta-masinn",
        "汎用人工知能":"hannyouzinnkoutinou",
        "方策勾配法":"housakukoubaihou",
        "パーセプトロン":"pa-seputoronn",
    }
    random_question2 = {
        "そめおかりゅうご":"someokaryuugo",
        "とにかくかわいい":"tonikakukawaii",
        "くぼさんは僕を許さない":"kubosannhabokuwoyurusanai",
        "ジョンマッカ―シー":"zyonnmakka-si-",
        "バラクオバマ":"barakuobama",
        "北原鉄朗":"kitaharateturou",
        "尾上パンダ":"onouepannda",
        "思春期症候群":"sisyunnkisyoukougunn",
        "ビットコイン":"bittokoinn",
        "イーロンマスク":"i-ronnmasuku",
    }
    random_question3 = {
        "加藤純一":"katouzyunniti",
        "Processing":"processing",
        "Python":"python",
        "マスダハルキ":"masudaharuki",
        "ぐらんぶる":"gurannburu",
        "ニューラルネットワーク":"nyu-rarunettowa-ku",
        "ダートマス会議":"da-tomasukaigi",
        "アダムヴァイスハオプト":"adamuvaisuhaoputo",
        "マンハッタン計画":"mannhattannkeikaku",
        "ハリーSトルーマン":"hari-storu-mann",
    }
    random_question4 = {
        "Eye of Providence":"eyeofprovidence",
        "ジェイコブグリーンバーグ":"zyeikobuguri-nnba-gu",
        "フクロウ":"hukurou",
        "国会議事堂":"kokkaigizidou",
        "千葉駅前交番":"tibaekimaekoubann",
        "エヴァンゲリオン":"evanngerionn",
        "碇シンジ":"ikarisinnzi",
        "Iris":"iris",
        "スイス":"suisu",
        "Earthquake Projector":"earthquakeprojector",
    }
    quest_question = {
        "Search Engine Optimization":"searchengineoptimization",
        "LandingPage":"landingpage",
        "重要業績評価指標":"zyuuyougyousekihyoukasihyou",
        "CostPerAction":"costperaction",
        "Electronic Commerce":"electroniccommerce",
        "Business to Business":"businesstobusiness",
        "Business to Custome":"businesstocustome",
        "Dennis MacAlistair Ritchie":"dennismacalistairritchie",
        "千円札の裏":"sennennsatunoura",
        "富士山":"huzisann",
        "野口英世":"nogutihideyo",
        "JavaScript":"javascript",
        "Lethal Autonomous Wepons Systems":"lethalautonomousweponssystems",
    }

    ranndomBattle1 = TypeingGame(random_question1, 6)
    ranndomBattle2 = TypeingGame(random_question2, 6)
    ranndomBattle3 = TypeingGame(random_question3, 6)
    ranndomBattle4 = TypeingGame(random_question4, 6)
    quest = TypeingGame(quest_question, 5)
    battle_se = EventSound()
    #battle_points = 
    
    while bouken_flg:
        map.draw_map(screen, player.posX, player.posY)
        player.display(screen)
        pygame.display.update()
        player.move()

        if player.posX == 323.0 and player.posY == 275.0 and battle_list[0] == False:
            battle_se.battle_catch.play()
            pygame.draw.rect(screen, (255,255, 255), Rect(0, 0, width, height))
            pygame.display.update()
            pygame.time.wait(1000)
            battle = Battle(
                'images/Characters/enemys/pipo-enemy46set/120x120/pipo-enemy005.png', 
                'sounds/BattleSounds/RandomBattle.mp3', ranndomBattle1, screen, player)
            if battle == False:
                bouken_flg = False
                break
            battle_list[0] = battle
        
        if player.posX == 667.0 and player.posY == 563.0 and battle_list[1] == False:
            battle_se.battle_catch.play()
            pygame.draw.rect(screen, (255,255, 255), Rect(0, 0, width, height))
            pygame.display.update()
            pygame.time.wait(1000)
            battle = Battle(
                'images/Characters/enemys/pipo-enemy46set/120x120/pipo-enemy022.png', 
                'sounds/BattleSounds/RandomBattle2.mp3', ranndomBattle2, screen, player)
            if battle == False:
                bouken_flg = False
                break
            battle_list[1] = battle

        if player.posX == 323.0 and player.posY == 699.0 and battle_list[2] == False:
            battle_se.battle_catch.play()
            pygame.draw.rect(screen, (255,255, 255), Rect(0, 0, width, height))
            pygame.display.update()
            pygame.time.wait(1000)
            battle = Battle(
                'images/Characters/enemys/pipo-enemy46set/120x120/pipo-enemy038b.png', 
                'sounds/BattleSounds/RandomBattle3.mp3', ranndomBattle3, screen, player)
            if battle == False:
                bouken_flg = False
                break
            battle_list[2] = battle
        
        if int(player.posX/GS) == 3 and int(player.posY/GS) == 21 and battle_list[4]== False:
            battle_se.battle_catch.play()
            pygame.draw.rect(screen, (255,255, 255), Rect(0, 0, width, height))
            pygame.display.update()
            pygame.time.wait(1000)
            battle = Battle(
                'images/Characters/enemys/pipo-enemy46set/120x120/pipo-enemy034.png', 
                'sounds/BattleSounds/RandomBattle5.mp3', quest, screen, player)
            if battle == False:
                bouken_flg = False
                break
            battle_list[4] = battle
            map.draw_map(screen, player.posX, player.posY)
            player.display(screen)
            pygame.display.update()
            announce_msg = ["洞窟を攻略したぞ。次は海へ行ってみよう。"]
            announce_box_point = (50, height/2, width - 100, 80)
            anonnce = OneLineMsgBox(announce_msg, announce_box_point)
            while True:
                anonnce.display(screen)
                pygame.display.update()
                if anonnce.end_flg:
                    break
                for event in pygame.event.get():
                    anonnce.text_update(event)
                    exit_game(event)#終了用イベント処理

        
        if player.posX == 1107.0 and player.posY == 1051.0 and battle_list[3] == False:
            battle_se.battle_catch.play()
            pygame.draw.rect(screen, (255,255, 255), Rect(0, 0, width, height))
            pygame.display.update()
            pygame.time.wait(1000)
            battle = Battle(
                'images/Characters/enemys/pipo-enemy46set/120x120/pipo-enemy042a.png', 
                'sounds/BattleSounds/RandomBattle4.mp3', ranndomBattle4, screen, player)
            if battle == False:
                bouken_flg = False
                break
            battle_list[3] = battle
            map.draw_map(screen, player.posX, player.posY)
            player.display(screen)
            pygame.display.update()
            
    
        if False not in battle_list:
            msg_list1 = [
                "よくやった！。",
                "これでこの街のモンスターは全てたおしたな。",
                "ではいよいよ海をわたり、魔王のいる島へ行くとするかの。",
                "この先さらなる試練が待ち構えておるはずじゃ。",
                "だが、中級レベルをクリアしたおぬしなら、必ず...",
                "必ずや、魔王北原を倒すことができようぞ！。",
                "わしは信じておるぞ。",
                "では行くのじゃ勇者よ！",
            ]
            end_msg = OneLineMsgBox(msg_list1, story_box_point)
            mixer.music.load('sounds/OpeningThema/tyuukyuuending.mp3')
            mixer.music.play(-1)
            while True:
                screen.blit(hotoke, (story_box_point[0]+40, story_box_point[1]-60))
                end_msg.display(screen)
                pygame.display.update()
                if end_msg.end_flg:
                    bouken_flg = False
                    mixer.music.stop()
                    break
                for event in pygame.event.get():
                    end_msg.text_update(event)
                    exit_game(event)#終了用イベント処理
        
        for event in pygame.event.get():
            exit_game(event)#終了用イベント処理
