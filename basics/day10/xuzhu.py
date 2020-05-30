"""
# author Liu shi hao
# date: 2019/11/18 15:15
# file_name: xuzhu

"""


class Daji:

    def __init__(self, dj_level, wu_level, c_level) -> None:
        super().__init__(wu_level, c_level)
        self.dj_level = dj_level

    def dj_skill(self):
        print("变身妲己，和妲己一起玩耍吧！")


class Wukong:

    def __init__(self, wu_level, c_level) -> None:
        super().__init__(c_level)
        self.wu_level = wu_level

    def wu_skill(self):
        print("变身悟空，手起捧落，哇！世界安静了！")


class Chengyaojin:
    def __init__(self, c_level) -> None:
        super().__init__()
        self.c_level = c_level

    def c_skill(self):
        print("变身程咬金，进攻就是最好的防守！")


class Yuange(Daji, Wukong, Chengyaojin):
    pass


y1 = Yuange(1, 2, 4)
y1.dj_skill()
y1.c_skill()
y1.wu_skill()
print(y1.wu_level)
