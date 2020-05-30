"""
# author Liu shi hao
# date: 2019/11/22 20:43
# file_name: base2

"""
# 11、
# 编写武器类，
# a)	字段:名称、攻击力、重量。字段皆为私有变量
# b)	为该类编写三个构造函数，用于初始化
# c)	为该类每个字段添加属性，对字段进行封装
# d)	为该类添加方法weapon_info,显示武器的所有信息，格式如下：
# 1.	宝剑的攻击力为 100，重量为1000 g
# 2.	手枪的攻击力为 500，重量为600 g
# e)	实例化5个武器放入武器列表，并依次执行weapon_info方法
#


class Weapon:

    def __init__(self, name, atk, weight) -> None:
        super().__init__()
        self.__name = name
        self.__atk = atk
        self.__weight = weight

    @property
    def name(self):
        return self.__name

    @property
    def atk(self):
        return self.__atk

    @property
    def weight(self):
        return self.__weight

    def weapon_info(self):
        print(f"{self.name}的攻击力为\t{self.atk}，重量为{self.weight}\tg")


weapon_list = [
    Weapon("宝剑", "100", "1000"),
    Weapon("手枪", "100", "600"),
    Weapon("步枪", "100", "3500"),
    Weapon("大刀", "100", "1500"),
    Weapon("手雷", "1000", "100")
]

for i in range(len(weapon_list)):
    if type(weapon_list[i]) is Weapon:
        weapon_list[i].weapon_info()
