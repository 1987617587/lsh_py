"""
# author Liu shi hao
# date: 2019/11/18 17:48
# file_name:

"""


# 某枪战游戏中：
# 角色类：Role
# 属性:
# 血量
# 枪支库：考虑用什么类型存储
# 当前选择的枪支
# 方法：
# 更换枪支
# 开火
# 枪支类：
# 属性：
# range
# 射程
# hurt伤害值
# 方法：
# 开火: fire
#
# 手枪类:PistolGun
# 来福枪类：RifleGun
# 激光枪：LaserGun

class Gun():

    def __init__(self, name, range, hurt) -> None:
        super().__init__()
        self.name = name
        self.range = range
        self.hurt = hurt

    def fire(self):
        print(f"{self.name}开火，射程：{self.range},伤害：{self.hurt}")


class PistolGun(Gun):

    def __init__(self) -> None:
        super().__init__("来福枪", 20, 25)

    def fire(self):
        print(f"{self.name}开火，射程：{self.range},伤害：{self.hurt} da da da")


class RifleGun(Gun):

    def __init__(self) -> None:
        super().__init__("激光枪", 100, 50)

    def fire(self):
        print(f"{self.name}开火，射程：{self.range},伤害：{self.hurt} ，zi zi zi")


class LaserGun(Gun):

    def __init__(self) -> None:
        super().__init__("手枪", 30, 10)

    def fire(self):
        print(f"{self.name}开火，射程：{self.range},伤害：{self.hurt} ，biu biu biu")


class Role:

    def __init__(self) -> None:
        super().__init__()
        self.hp = 1000
        self.guns = [PistolGun(), RifleGun(), LaserGun()]
        self.gun = self.guns[0]

    def change(self):
        an = input("是否切换枪支？y/n")
        if an == "y":
            for i in range(len(self.guns)):
                print(f"{i + 1}.{self.guns[i].name}", end=" ")

            choice = input("请输入1-3进行选择：")
            if choice in ["1", "2", "3"]:
                self.gun = self.guns[int(choice) - 1]  # 得到列表中的类

    def fire(self):
        self.gun.fire()  # RifleGun().fire() 调用对应类中的方法


while 1:
    role1 = Role()
    role1.change()
    role1.fire()






