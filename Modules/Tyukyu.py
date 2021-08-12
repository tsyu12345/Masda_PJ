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
        "",
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
    #マップ
    map = Map('Map_data/TyukyuMapData.tmx')
    #プレイヤー
    player = Player('images/Characters/hero/pipo-charachip027c.png', 10, 1, screen)
    player.posX, player.posY = 400, 320 #初期位置
    #状態フラグ変数
    first_story_flg = True
    bouken_flg = False
    battle_flg = False
    
    #以下メインループ

    while first_story_flg:
        story_box.display(screen, story_box_point)
        pygame.display.update()
        if story_box.msg_index >= 6:
            screen.blit(hotoke, (story_box_point[0]+40, story_box_point[1]-60))
        if story_box.end_flg:
            break
        for event in pygame.event.get():
            exit_game(event)#終了用イベント処理
            story_box.text_update(event)

