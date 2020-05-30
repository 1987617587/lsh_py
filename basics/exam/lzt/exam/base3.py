# 12、
# 对于微波炉来说，就应该拥有所有微波炉的共性，拥有方法：
# 打开设备open和关闭设备close
# 微波炉类进行功能设计：
# 定时功能——timer(self,second:int)
# 响铃功能——sound(self,volume:str)
# 显示功能——show(self)
# 强度设定——config(self,power:float)
# 针对以上设计，自行编写2个微波炉的子类，每个类至少拥有两项附加功能，并测试这些类。


class MicrowaveOven:
    def open(self):
        print("打开微波炉")

    def close(self):
        print("关闭微波炉")

    def timer(self, second: int):
        pass

    def sound(self, volume: str):
        pass

    def show(self):
        pass

    def config(self, power: float):
        pass


class GreeMicrowaveOven(MicrowaveOven):

    def timer(self, second: int):
        print("设定定时")

    def sound(self, volume: str):
        print(f"到点就闹 {volume}")


class MediaMicrowaveOven(MicrowaveOven):

    def show(self):
        print("当前信息：xxxx")

    def config(self, power: float):
        print(f"已设定强度为{power}")


def use_microwave_oven(mo):
    mo.open()
    mo.show()
    mo.config(1.3)
    mo.timer(100)
    mo.sound("加热完成")
    mo.close()


use_microwave_oven(GreeMicrowaveOven())
use_microwave_oven(MediaMicrowaveOven())


