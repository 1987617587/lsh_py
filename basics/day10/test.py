"""
# author Liu shi hao
# date: 2019/11/18 16:44
# file_name: test
多态
"""


class Animal:
    def eat(self):
        pass

    def play(self):
        pass


class Dog(Animal):

    def eat(self):
        print("狗吃骨头")

    def play(self):
        print("狗看门")


class Cat(Animal):
    def eat(self):
        print("猫吃鱼")

    def play(self):
        print("猫抓老鼠")


def feed(an):
    an.eat()


def skill(an):
    an.play()


feed(Cat())
feed(Dog())
skill(Dog())
skill(Cat())


class Role:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def attack(self):
        print(f"{self.name}角色攻击")


class Soldier(Role):
    def attack(self):
        print(f"{self.name}物理攻击")


class Master(Role):
    def attack(self):
        print(f"{self.name}魔法攻击")

class Students:   # 鸭子模型测试

    def __init__(self) -> None:
        super().__init__()
        self.name = "小李"

    def attack(self):
        print(f"{self.name}人身攻击")


def PK(role1, role2):
    role1.attack()
    role2.attack()


PK(Soldier("花木兰"), Master("安琪拉"))
PK(Soldier("花木兰"), Students())  # 鸭子模型测试


class Wukong:
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def change(self):
        print(f"{self.name}变化")


class Men(Wukong):

    def change(self):
        print(f"{self.name}变化成人")


class Tree(Wukong):

    def change(self):
        print(f"{self.name}变化成树")

class King(Wukong):

    def change(self):
        print(f"{self.name}变化成玉皇大帝")
class Bee(Wukong):

    def change(self):
        print(f"{self.name}变化成蜜蜂")

class woodman(Wukong):

    def change(self):
        print(f"{self.name}变化成樵夫")

# class Animal():
class Plany:

    def __init__(self) -> None:
        super().__init__()
        self.name = "悟空"

    def change(self):
        print(f"{self.name}变化成飞机")

def change(role1):
    role1.change()


change(King("孙悟空"))
change(Bee("孙悟空"))
change(Tree("孙悟空"))
change(Men("孙悟空"))
change(woodman("二郎神"))
change(Plany())
print(id(None))