import pygame
import time
from pygame.locals import *
from pygame import mixer
import sys
import csv


def main():
    # pygame window initialization
    pygame.init()
    font = pygame.font.Font(
        'font_data/misaki_gothic_2nd.ttf', 26)
    font.set_bold(True)
    width = 800  # screeen
    height = 640
    pygame.display.set_mode((width, height), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("マス打")
    # 必要なオブジェクト（部品）を以下へ
    start_text = "ぼうけんをはじめますか？"
    y_n_text = "Y/N ??:選択するにはどれかキーを押してください。_"
    text_render = font.render("", True, (255, 255, 255))
    select_render = font.render(y_n_text, True, (255, 255, 255))
    msg_box_point = (50, 400, 700, 150)
    msg_box = pygame.Rect(
        msg_box_point[0], msg_box_point[1], msg_box_point[2], msg_box_point[3])
    sub_msg_box_point = (50, height / 2 + 80, 700, 100)
    sub_msg_box = pygame.Rect(
        sub_msg_box_point[0], sub_msg_box_point[1], sub_msg_box_point[2], sub_msg_box_point[3])
    sub_msg = "え？　もう一度聞きます。_"
    sub_render = font.render("", True, (255, 255, 255))
    counter = 0
    bd_t_cnt = 0
    bad_cnt = 0
    #状態遷移感知変数
    tutorial = True
    first_select = True
    bad = False
    op_end = False
    end = False
    first_story = False
    play_tutorial = False
    #以下本編用
    story_text = [
        "時は20XX年。",
        "人類はパソコンを発明した。",
        "人々はそれを当たり前のように使いこなしていた。＿",
        "そんな世界にとつぜん「魔王、北原」が現れた。",
        "北原は魔物たちを世界にバラマキ、",
        "人々の生活を脅かし始めた。＿",
        "北原は「タイピングが上手い奴を連れてこい」、",
        "と人々に警告した。",
        "これまで何人もの勇敢な者が＿",
        "北原に立ち向かったが誰も倒すことが出来なかった。",
        "ある少年が立ち上がった。彼の名はマスダ。",
        "魔王に親を殺された復習を果たすべく旅に出る。＿",
        "あなたは、マスダとなり、",
        "魔王を倒さなければなりません。",
        "これからその方法を伝授します。＿"
    ]
    posx = 70
    posy = 410
    s_i = 0
    label = []

    while tutorial:
        if bad_cnt == 3:
            start_text = "ぼうけんをはじめなくてもいいですか？"
        pygame.draw.rect(screen, (0, 0, 0), Rect(0, 0, width, height))
        while first_select:
            pygame.draw.rect(screen, (255, 255, 255), msg_box, 6)  # 縁
            pygame.draw.rect(screen, (0, 0, 0), msg_box)  # メッセージボックス
            pygame.time.wait(80)
            screen.blit(text_render, (70, 410))  # メッセージの表示
            if counter >= len(start_text) + 5:
                screen.blit(select_render, (70, 450))
            pygame.display.update()

            pygame.time.wait(100)
            counter += 1
            text_render = font.render(
                start_text[0:counter], True, (255, 255, 255))

            # イベント処理
            for event in pygame.event.get():
                # 終了用のイベント処理
                if event.type == QUIT:          # 閉じるボタンが押されたとき
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:  # キーEvent
                    if pygame.key.name(event.key) == "y":
                        first_story = True
                        first_select = False
                        print("yes pressed")

                    elif pygame.key.name(event.key) == "n":
                        bad = True
                        first_select = False
                        if bad_cnt == 3:
                            bad = False
                            op_end = True
                            first_select = False

                    if event.key == K_ESCAPE:   # Escキーが押されたとき
                        pygame.quit()
                        sys.exit()

        bd_t_cnt = 0
        if bad_cnt == 1:
            sub_msg = "いや、なんでよ。マジでもう一回聞くよ？＿"
        if bad_cnt == 2:
            sub_msg = "お前何してんの。'y'押さないと何も始まんないよ！"
        while bad:
            pygame.draw.rect(screen, (255, 255, 255), sub_msg_box, 6)  # 縁
            pygame.draw.rect(screen, (0, 0, 0), sub_msg_box)
            screen.blit(
                sub_render, (sub_msg_box_point[0] + 50, sub_msg_box_point[1] + 15))
            pygame.display.update()

            pygame.time.wait(100)
            bd_t_cnt += 1
            sub_render = font.render(
                sub_msg[0:bd_t_cnt], True, (255, 255, 255))

            for event in pygame.event.get():
                # 終了用のイベント処理
                if event.type == QUIT:          # 閉じるボタンが押されたとき
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        bad_cnt += 1
                        bad = False
                        first_select = True

        while op_end:
            pygame.draw.rect(screen, (0, 0, 0), Rect(0, 0, width, height))
            pygame.draw.rect(screen, (255, 255, 255), sub_msg_box, 6)  # 縁
            pygame.draw.rect(screen, (0, 0, 0), sub_msg_box)
            end_render = font.render(
                "はい！ひっかかった～～～乙～～。＿", True, (255, 255, 255))
            screen.blit(
                end_render, (sub_msg_box_point[0]+5, sub_msg_box_point[1]+15))

            pygame.display.update()
            for event in pygame.event.get():
                # 終了用のイベント処理
                if event.type == QUIT:          # 閉じるボタンが押されたとき
                    pygame.quit()
                    sys.exit()

                if event.type == KEYDOWN:
                    if event.key == K_RETURN:
                        op_end = False
                        end = True

        text = "それではぼうけんをはじめます。"
        counter = 0
        while end:
            pygame.draw.rect(screen, (255, 255, 255), msg_box, 6)  # 縁
            pygame.draw.rect(screen, (0, 0, 0), msg_box)  # メッセージボックス
            pygame.time.wait(80)
            screen.blit(text_render, (70, 410))  # メッセージの表示
            pygame.display.update()
            pygame.time.wait(100)
            counter += 1
            text_render = font.render(text[0:counter], True, (255, 255, 255))
            if counter == len(text) + 5:
                #その後のチュートリアルの処理
                first_story = True
                end = False
            for event in pygame.event.get():
                if event.type == QUIT:          # 閉じるボタンが押されたとき
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:  # キーEvent
                    if event.key == K_ESCAPE:   # Escキーが押されたとき
                        pygame.quit()
                        sys.exit()
            
        while first_story:
            pygame.draw.rect(screen, (0, 0, 0), Rect(0, 0, width, height))
            pygame.draw.rect(screen, (255, 255, 255), msg_box, 6)  # 縁
            pygame.draw.rect(screen, (0, 0, 0), msg_box)  # メッセージボックス
            pygame.time.wait(80)
            label.append(font.render(story_text[s_i], True, (255, 255, 255)))
            label.append(font.render(story_text[s_i+1], True, (255, 255, 255)))
            label.append(font.render(story_text[s_i+2], True, (255, 255, 255)))
            screen.blit(label[0], (posx, posy))
            screen.blit(label[1], (posx,posy+40))
            screen.blit(label[2], (posx,posy+80))
            pygame.display.update()


            for event in pygame.event.get():
                if event.type == QUIT:          # 閉じるボタンが押されたとき
                    pygame.quit()
                    sys.exit()
                if event.type == KEYDOWN:  # キーEvent
                    if event.key == K_ESCAPE:   # Escキーが押されたとき
                        pygame.quit()
                        sys.exit()
                    if event.key == K_RETURN:
                        try:
                            s_i += 3
                            label[0] = font.render(story_text[s_i], True, (255, 255, 255))
                            label[1] = font.render(story_text[s_i+1], True, (255, 255, 255))
                            label[2] = font.render(story_text[s_i+2], True, (255, 255, 255))
                        except IndexError:
                            first_story = False
                            tutorial = False
                            #play_tutorial = True
                            #pygame.quit()
    

if __name__ == "__main__":
    main()
