# 11、
# 编写武器类，
# a)	字段:名称、攻击力、重量。字段皆为私有变量
# b)	为该类编写三个初始化方法参数，用于初始化
# c)	为该类每个字段添加属性，对字段进行封装
# d)	为该类添加方法weapon_info,显示武器的所有信息，格式如下：
# 1.	宝剑的攻击力为 100，重量为1000 g
# 2.	手枪的攻击力为 500，重量为600 g
# e)	实例化5个武器放入武器列表，并依次执行weapon_info方法


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
        print(f"{self.__name}的攻击力为{self.__atk}，重量为{self.__weight}g")


weapons = [
    Weapon("宝剑", 150, 1000),
    Weapon("弓箭", 120, 500),
    Weapon("手枪", 170, 800),
    Weapon("宝刀", 200, 1100),
    Weapon("血滴子", 300, 1400)
]

for i in range(len(weapons)):
    weapons[i].weapon_info()
