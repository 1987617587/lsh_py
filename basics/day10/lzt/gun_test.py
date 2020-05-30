# author:lzt
# date: 2019/11/19 9:34
# file_name: gun_test
class Role:

    def __init__(self) -> None:
        # 血量
        # 枪支库：考虑用什么类型存储
        # 当前选择的枪支
        super().__init__()
        self.hp = 1000
        self.guns = [PistolGun(), RifleGun(), LaserGun()]
        self.gun = self.guns[0]

    # 更换枪支
    def change(self):
        # 打开枪支庫 展示所有的枪
        for i in range(len(self.guns)):
            print(f"{i + 1}.{self.guns[i].name}")
            # 1.手枪
            # 2.来福
            # 3.激光
        # 询问选择哪把枪
        choice = input("请输入1-3进行选择：")
        if choice in ["1", "2", "3"]:
            # 将当前的枪支变换为列表中某一把枪
            self.gun = self.guns[int(choice) - 1]

    # 开火
    def fire(self):
        self.gun.fire()


class Gun:

    def __init__(self, name, range, hurt) -> None:
        super().__init__()
        self.name = name
        self.range = range
        self.hurt = hurt

    def fire(self):
        pass


class PistolGun(Gun):

    def __init__(self) -> None:
        super().__init__("手枪", 30, 25)

    def fire(self):
        print("biubiubiu~~~~~~")


class RifleGun(Gun):

    def __init__(self) -> None:
        super().__init__("来复枪", 20, 50)

    def fire(self):
        print("pengpengpeng~~~~~~")


class LaserGun(Gun):

    def __init__(self) -> None:
        super().__init__("激光枪", 100, 70)

    def fire(self):
        print("zizizi~~~~~~~~~~~~")

role1 = Role()
while 1:
    role1.change()
    role1.fire()

