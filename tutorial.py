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
        'font_data/PixelMplus-20130602/PixelMplus10-Regular.ttf', 26)
    font.set_bold(True)
    width = 800  # screeen
    height = 640
    pygame.display.set_mode((width, height), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("マス打")
    # 必要なオブジェクト（部品）を以下へ
    tutorial = True
    first_select = True
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
    bad = False
    op_end = False
    end = False

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
                pygame.quit()
                #その後のチュートリアルの処理
                
            if event.type == QUIT:          # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:  # キーEvent
                if event.key == K_ESCAPE:   # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()
    

if __name__ == "__main__":
    main()
