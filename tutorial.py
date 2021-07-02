import pygame
from pygame.locals import *
from pygame import mixer
import sys
import csv

class typeing:

    def question_dict(self):
        dic = {
            'RPG':"RPG",
            '冒険':'bouken',
            'イス':"isu",
            '消しゴム':"kesigomu",
            '焼肉':"yainiku",
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
            '筆箱':'fudebako'            
        }
        return dic

    def game(self):
        word_list = []
        romaji_list = []
        question = self.question_dict
        for i in question.keys():
            word_list.append(i)
        
        for i in question.values():
            romaji_list.append(i)
            
             