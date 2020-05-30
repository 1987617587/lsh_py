"""
# author Liu shi hao
# date: 2019/11/22 20:43
# file_name: base3

"""


# 12、
# 对于微波炉来说，就应该拥有所有微波炉的共性，拥有方法：
# 打开设备open和关闭设备close
# 微波炉类进行功能设计：
# 定时功能——timer(self,second:int)
# 响铃功能——sound(self,volume:str)
# 显示功能——show(self)
# 强度设定——config(self,power:float)
# 针对以上设计，自行编写2个微波炉的子类，每个类至少拥有两项附加功能，并测试这些类。
#

class MicrowaveOven:

    def __init__(self, brand, size, tce, weight) -> None:
        # 属性：品牌，尺寸，能耗等级，重量，工作时间默认为0
        super().__init__()
        self.__brand = brand
        self.__size = size
        self.__tce = tce
        self.__weight = weight
        self.times = 0

    @property
    def brand(self):
        return self.__brand

    @property
    def size(self):
        return self.__size

    @property
    def tce(self):
        return self.__tce

    @property
    def weight(self):
        return self.__weight

    def open(self):
        self.times += 1
        # print("开始工作")
        pass

    def close(self):
        self.times = 0
        pass


class MeiDi(MicrowaveOven):

    def timer(self, second: int):
        while self.times < second:
            self.open()

    def show(self):
        print(f"本微波炉工作时间为:{self.times}")


class Gree(MicrowaveOven):

    def __init__(self, brand, size, tce, weight, volume=10, pow=100.0) -> None:
        super().__init__(brand, size, tce, weight)
        self.volume = volume
        # 增加属性：音量，默认值10
        self.pow = pow
        # 增加属性：强度，默认值100.0

    def sound(self, volume: str):
        if volume.isdigit():
            self.volume = int(volume)

    def config(self, power: float):
        if type(power) == float:
            self.pow = power
        else:
            print("设定失败，已设定默认值")

    def __str__(self) -> str:
        return f"{self.brand}微波炉， 响铃声音{self.volume}，强度{self.pow}"


m1 = MeiDi("美的", "15寸", "A", "5kg")
g1 = Gree("格力", "20寸", "A", "8kg")

m1.timer(25)  # 定时工作
m1.show()  # 查看定时工作后的时间
m1.close()  # 关闭
m1.show()  # 再次查看工作时间为0

g1.sound("12")  # 设定声音大小
g1.config(120.5)  # 设定工作强度
print(g1)  # 查看
