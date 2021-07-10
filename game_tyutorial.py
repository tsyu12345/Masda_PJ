import pygame
import sys
import csv
import os

GS = 16
DOWN, LEFT, RIGHT, UP = "s", "a", "d", "w"


def load_image(filename, colorkey=None):
    filename = os.path.join("data", filename)
    image = pygame.image.load(filename)
    image = image.convert()
    return image


def split_image(image):
    """分割したイメージを格納したリストを返す"""
    imageList = []
    for i in range(0, 80, GS):
        for j in range(0, 80, GS):
            surface = pygame.Surface((GS, GS))
            surface.blit(image, (0, 0), (j, i, GS, GS))
            surface.convert()
            imageList.append(surface)
    return imageList


class Map:
    imgs = [None] * 10

    def __init__(self, csv_file):
        self.csv_file = csv_file
        self.map = self.map_data()
        self.row, self.col = len(self.map), len(self.map[0])
        self.msize = 16

    def map_data(self):  # TiledからのCSV読み込み
        file = open(self.csv_file, "r", encoding='ms932',
                    errors="", newline="")
        data = csv.reader(file, doublequote=True, lineterminator="\r\n",
                          quotechar='"', skipinitialspace=True)
        map = []
        for row in data:
            map.append(row)
        return map

    def draw(self, screen):
        for i in range(self.row):
            for j in range(self.col):
                screen.blit(self.imgs[int(self.map[i][j])],
                            (j*self.msize, i*self.msize))


class Player:
    animcycle = 24  # アニメーション速度
    frame = 0

    def __init__(self, name, pos, dir):
        self.name = name  # プレイヤー名（ファイル名と同じ）
        self.images = split_image(load_image("%s.png" % name))
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
    font = pygame.font.Font('font_data/misaki_gothic_2nd.ttf', 20)
    font.set_bold(True)
    width = 800  # screeen
    height = 640
    pygame.display.set_mode((width, height), 0, 32)
    screen = pygame.display.get_surface()
    pygame.display.set_caption("マス打")
    # 必要なオブジェクト（部品）
    play = True
    #マップチップの選択
    Map.imgs[1] = load_image('images/Map/mapchip2_0724/mapchip2/MapChip/kusa1-tuti1.png')#クラス変数imgsの指定
    Map.imgs[4] = load_image('images/Map/mapchip2_0724/mapchip2/MapChip/kusa1-kusa2.png')
    map = Map('Map_data/tyutorial_map_data/tyutorial_test..csv')

    while play:

        map.draw(screen)

        for event in pygame.event.get():
            if event.type == QUIT:          # 閉じるボタンが押されたとき
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:       # キーを押したとき
                if event.key == K_ESCAPE:   # Escキーが押されたとき
                    pygame.quit()
                    sys.exit()

if __name__ == "__main__":
    main()