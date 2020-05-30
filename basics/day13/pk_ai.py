"""
# author Liu shi hao
# date: 2019/11/21 21:23
# file_name: pk_ai

"""
import random


class Player:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self._hp = 600
        self._atk = 15
        self._state = True

    @property
    def hp(self):
        return self._hp


    @property
    def atk(self):
        return self._atk

    @property
    def state(self):
        return self._state

    def attack(self, player):
        pass

    # 受伤方法
    def be_hurt(self, hurt):
        if self._state:
            self._hp = 0 if self._hp - hurt < 0 else self._hp - hurt
            self._state = self._hp > 0
            print(f"{self.name}原有血量{self._hp + hurt}，收到伤害{int(hurt)}，剩余血量{int(self._hp )}")
        else:
            print("请尊重死者！")
            return

    def __str__(self) -> str:
        return self.name + " " + str(self._hp)


class User(Player):
    def __init__(self, name) -> None:
        super().__init__(name)

    def attack(self, player):
        if not self._state:
            print("请安息！")
            self._state = False
            return
        hurt = 15
        print(f"{self.name}打出伤害{hurt}")
        player.be_hurt(hurt)


class Ai(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self._hp = 100

    def attack(self, player):
        if not self._state:
            print("请安息！")
            self._state = False
            return
        # 获取当前玩家的基础伤害值
        hurt = 5
        print(f"{self.name}打出伤害{hurt}")
        player.be_hurt(hurt)


user = User("玩家")
ai_1 = Ai("机器人一")
ai_2 = Ai("机器人二")
ai_3 = Ai("机器人三")


def pk():
    while ai_1.state and ai_2.state and ai_3.state or user.state:
        count = random.randint(1, 6)
        count = 0 if count < 4 else 1
        player1_choice = random.randint(0, 1)
        ai_1_choice = random.randint(0, 1)
        ai_2_choice = random.randint(0, 1)
        ai_3_choice = random.randint(0, 1)
        if player1_choice == count:
            user.attack(ai_1)
            user.attack(ai_2)
            user.attack(ai_3)
        # print(h)
        if ai_1.state and ai_1_choice ==count:
            ai_1.attack(user)
        if ai_2.state and ai_2_choice ==count:
            ai_2.attack(user)
        if ai_3.state and ai_3_choice ==count:
            ai_3.attack(user)
    print("玩家 win" if user.state else "机器人 win")

pk()