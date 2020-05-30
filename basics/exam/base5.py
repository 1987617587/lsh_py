"""
# author Liu shi hao
# date: 2019/11/22 20:44
# file_name: base5

"""

#
# 14、
# 斗地主游戏是扑克游戏的一种，请按下面的要求编写类：
# 1.扑克类 字段方法自定义 合理即可
# 2.玩家类 字段方法自定义 合理即可
# 3.游戏类 字段方法自定义 合理即可
# 实现功能：
# 1.按斗地主的规则自动洗牌，自动发牌
# 2.玩家可查看自己手中的牌
# 注意：只写一副牌的情况，只完成要求即可，可自由发挥。
# 附图：黑红梅方的符号见下面的ASCII码表图

import random


# 自己写的判断用户输入整数的函数
def in_int():
    while 1:
        num = input("请输入整数：")
        if not num.isdigit():
            continue
        return int(num)


class Cards:
    def __init__(self):  # 生成一副54张的牌
        self.allcards = ['joker', 'Joker']  # 表示小王，大王
        for i in range(1, 14):
            for k in range(4):
                if k == 0:
                    self.allcards.append(chr(9824) + str(i))
                elif k == 1:
                    self.allcards.append(chr(9827) + str(i))
                elif k == 2:
                    self.allcards.append(chr(9829) + str(i))
                else:
                    self.allcards.append(chr(9830) + str(i))

    def shuffle_card(self):  # 洗牌，打乱顺序
        random.shuffle(self.allcards)

    def landowner_card(self):  # 底牌三张先抽出
        landowner_cards = []
        for i in range(3):
            landowner_cards.append(self.allcards[i])
            self.allcards.remove(self.allcards[i])  # 最后的牌剩余51
        return landowner_cards

    def take_card(self, your_card):  # 发牌，默认为17张
        # your_card = []
        for i in range(17):
            your_card.append(self.allcards.pop())
        return your_card

    def recovery(self, Ifshuffle=True):  # 收牌，重新开始，默认洗牌
        if Ifshuffle:
            self.__init__()
            self.shuffle_card()
        else:
            self.__init__()


class Player:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.cards = []  # 列表存牌

    def call_landowner(self):
        call_num = in_int()  # 比分抢地主
        return call_num

    def look_cards(self):  # 玩家看牌
        print(self.cards)


class Gamecards:

    @classmethod
    def welcome(cls):
        print("欢迎来到激情斗地主！")

    @classmethod
    def exit(cls):
        print("欢迎下次再来！")


def play_game():
    # 游戏开始
    Gamecards.welcome()
    player1 = Player("玩家1")
    player2 = Player("玩家2")
    player3 = Player("玩家3")
    c1 = Cards()  # 产生一副牌
    c1.shuffle_card()  # 洗牌
    landowner_card = c1.landowner_card()
    player1.cards = c1.take_card(player1.cards)  # 玩家拿牌 即发牌
    player2.cards = c1.take_card(player2.cards)  # 玩家拿牌
    player3.cards = c1.take_card(player3.cards)  # 玩家拿牌
    player1.look_cards()  # 玩家看牌
    player2.look_cards()
    player3.look_cards()
    # 开始抢地主
    num1 = player1.call_landowner()  # 依次报价抢地主
    num2 = player1.call_landowner()
    num3 = player1.call_landowner()
    if max(num1, num2, num3) == num1:
        player1.cards.append(landowner_card)
    elif max(num1, num2, num3) == num2:
        player2.cards.append(landowner_card)
    else:
        player3.cards.extend(landowner_card)
    # 得出地主 地主获得底牌
    player1.look_cards()  # 玩家看牌
    player2.look_cards()
    player3.look_cards()
    # 此时可以开始打牌了，用牌数判断地主，让地主先出牌，有待后续。。

    Gamecards.exit()  # 退出游戏界面显示


play_game()
