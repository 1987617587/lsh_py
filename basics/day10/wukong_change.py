"""
# author Liu shi hao
# date: 2019/11/18 17:39
# file_name: wukong_change

"""
class Animal:



    def __init__(self,name) -> None:
        super().__init__()
        self.name = name

    def action(self):
        pass


class Brid(Animal):

    def __init__(self) -> None:
        super().__init__("鸟")

    def action(self):
        print("在天空翱翔")


class Fish(Animal):

    def __init__(self) -> None:
        super().__init__("鱼")

    def action(self):
        print("在水中游")

class Car:

    def __init__(self) -> None:
        super().__init__()
        self.name = "汽车"
    def action(self):
        print("小汽车滴滴的跑")



class WuKong:
    def change(self,animal):
        print(f"切换悟空模型到{animal.name}")
        animal.action()

wk = WuKong()
wk.change(Brid())
wk.change(Fish())
wk.change(Animal("蛇"))
wk.change(Car())