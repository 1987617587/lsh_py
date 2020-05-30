import random
from typing import Any

poker_colors = ["♠", "♥", "♣", "◆"]
# ☠:大王 ☃:小王
jokers_colors = ["☠", "☃"]
# A J-K
poker_show = ["A", "J", "Q", "K", "", ""]


class Poker:

    def __new__(cls, color, num) -> Any:
        if color not in poker_colors and color not in jokers_colors:
            return
        if color in poker_colors and (num < 1 or num > 13):
            return
        if color in jokers_colors and num != 14 and num != 15:
            return
        return super().__new__(cls)

    def __init__(self, color, num) -> None:
        super().__init__()
        self.__color = color
        self.__num = num

    @property
    def color(self):
        return self.__color

    @property
    def num(self):
        return self.__num

    def __str__(self) -> str:

        return f"{self.__color}" \
            f"{poker_show[0] if self.__num == 1 else poker_show[self.__num - 10] if self.__num > 10 else self.__num}"


class Player:

    def __init__(self, name: str) -> None:
        super().__init__()
        self.__name = name
        self.__pokers = []

    def get_poker(self, poker: Poker):
        self.__pokers.append(poker)

    def out_poker(self, poker: Poker):
        self.__pokers.remove(poker)

    def show_pokers(self):
        for i in range(len(self.__pokers)):
            print(self.__pokers[i], end="  ")
        print()


class FightLandlords:

    def __init__(self) -> None:
        super().__init__()
        self.__players = []
        self.__init_pokers()

    def __init_pokers(self):
        self.__pokers = []
        # 产生54张扑克牌
        # 产生52张普通牌
        for i in range(len(poker_colors)):
            for j in range(1, 14):
                self.__pokers.append(Poker(poker_colors[i], j))
        # 加入大小王
        self.__pokers.append(Poker(jokers_colors[0], 15))
        self.__pokers.append(Poker(jokers_colors[1], 14))
        pass

    def game(self):
        # 三位玩家进场
        for i in range(3):
            self.__players.append(Player(input(f"玩家{i + 1}名字")))
            # 测试随机
            # self.__players.append(Player("玩家"))

        # 洗牌
        random.shuffle(self.__pokers)

        # 发牌
        for i in range(17):
            for j in range(3):
                self.__players[j].get_poker(self.__pokers[0])
                del self.__pokers[0]

        # 为每个玩家展示牌面
        for i in range(3):
            self.__players[i].show_pokers()

        # 显示底牌
        for i in range(len(self.__pokers)):
            print(self.__pokers[i], end=" ")
        print()


FightLandlords().game()
