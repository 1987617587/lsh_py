"""
# author Liu shi hao
# date: 2019/11/15 16:53
# file_name: hero

"""


# 4.设计一个游戏角色类
#    属性:角色名、血量、魔法、状态
#    方法:释放技能 被伤害
#    要求:设计要合理
#
class Gamerole:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.__health = 100
        self.__magic = 1

        self.__state = True

    @property
    def name(self):
        return self.name

    @name.setter
    def name(self, value):
        if len(value) > 9 or len(value) < 2:
            print("姓名必须在2-9位之间！")
            return
        self.__name = value
        pass

    @property
    def health(self):
        return self.__health

    @property
    def magic(self):
        return self.__magic
