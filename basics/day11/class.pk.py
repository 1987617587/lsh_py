"""
# author Liu shi hao
# date: 2019/11/19 18:47
# file_name: class.pk

"""
# 12、创建一个玩家类，玩家有名称、生命值、魔法值、攻击力、生存状态5个属性；生命值、魔法值、攻击力、生存状态属性都是只读的；
# 生命值、魔法值、攻击力的初值分别为800、100、50；玩家类有一个攻击方法：public void attack(Player player)。
# 玩家类有两个子类：野蛮人和魔法师。野蛮人每次攻击造成的伤害在[攻击力-10] 到[攻击力+10]之间（这个伤害值是一个随机值），
# 另外野蛮人有一个被动技能（不消耗魔法），有25%的几率产生1次暴击，每次暴击产生的伤害是原来的3倍；
# 魔法师每次攻击造成的伤害在攻击力的80%~100%之间（也是一个随机数），魔法师每次攻击消耗18点魔法，它会额外减少对方12%的生命值。
# 现在分别创建一个野蛮人、魔法师对象，让他们进行PK，就是你打我一下，我打你一下，直到有一方死亡为止；野蛮人先攻击。
#
import random


class Player:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self._hp = 800
        self._mp = 100
        self._atk = 50
        self._state = True

    @property
    def hp(self):
        return self._hp

    @property
    def mp(self):
        return self._mp

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
        else:
            print("请尊重死者！")

    def __str__(self) -> str:
        return f"{self.name}，剩余血量{self._hp}"


class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name)

    def attack(self, player):
        if not self._state:
            print("请安息！")
            return
        # 获取当前玩家的基础伤害值
        hurt = self._atk + random.randint(-10, 10)
        # 附加职业伤害值
        if 1 == random.randint(1, 4):
            hurt *= 3
        # 减掉对方的血量值
        print(f"{self.name}打出伤害{hurt}")
        player.be_hurt(hurt)


class Magic(Player):
    def __init__(self, name) -> None:
        super().__init__(name)

    def attack(self, player):
        if not self._state:
            print("请安息！")
            return
        # 获取当前玩家的基础伤害值
        hurt = (self._atk / 10) * random.randint(8, 10)
        # 附加职业伤害值
        if self._mp >= 18:
            self._mp -= 18
            hurt += player._hp * 0.12
        # 减掉对方的血量值
        print(f"{self.name}打出伤害{hurt}，剩余魔法值{self.mp}")
        player.be_hurt(hurt)


h = Human("野蛮人")
m = Magic("法师")
while h.state and m.state:
    m.attack(h)
    print(h)
    if h.state:
        h.attack(m)
    print(m)
print("野蛮人 win" if h.state else "法师 win")


class Player:

    def __init__(self, name, ) -> None:
        super().__init__()
        self._name = name
        self._health = 800
        self._mp = 100
        self._atk = 50
        self._living_state = True

    @property
    def name(self):
        return self._name

    @property
    def health(self):
        return self._health

    @property
    def mp(self):
        return self._mp

    @property
    def atk(self):
        return self._atk

    @property
    def living_state(self):
        return self._living_state

    def public_void_attack(self):
        pass

    def attack(self,player):
        pass
    def be_hurt(self,hurt):
        if self.living_state:
            self._health = 0 if self.health - hurt< 0else self.health
            self._living_state = self.health>0
            print(f"{self.name}原有血量{self.health}，收到伤害{hurt}，剩余血量{self.health - hurt}")
        else:
            print("敌方已死！")

class Barbarian(Player):

    def __init__(self) -> None:
        super().__init__("野蛮人")


    def attack(self,player):
        if not self.living_state:
            print("安息！")
            return
        hurt = self.atk + random.randint(-10,10)
        if 1 == random.randint(1,4):
            hurt*=3
        print(f"{self.name}打出伤害{hurt}")
        player.be_hurt(hurt)

class Sorcerer(Player):

    def __init__(self) -> None:
        super().__init__("魔法师")

    def attack(self, player):
        if not self.living_state:
            print("安息！")
            return
        hurt = (self.atk / 10)* random.randint(8,10)
        if self._mp >= 18:
            self._mp -= 18
            hurt += player._health * 0.12
        # 减掉对方的血量值
        print(f"{self.name}打出伤害{hurt}")
        player.be_hurt(hurt)

player1 = Barbarian()
player2 = Sorcerer()



def pk():
    while player1.living_state and player2.living_state:
        player1.attack(player2)

        if  player1.living_state and player2.living_state:
            player2.attack(player1)


    print(f"{player1.name}死亡，游戏结束") if player2.living_state else print(f"{player2.name}死亡，游戏结束")

#
pk()