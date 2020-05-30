"""
# author Liu shi hao
# date: 2019/11/14 15:44
# file_name: day8_class_test

"""

# 示例：
# 自行车：
# 数据（属性或者状态）： 车架尺寸、 车轮尺寸、 牌子、 材料名称…
# 操作（方法或者功能）： 变速、移动、 修理…
#
import math


class Bike:

    def __init__(self, carriage_geometry, vehicle_geometry, plate, materials) -> None:
        super().__init__()
        self.carriage_geometry = carriage_geometry
        self.vehicle_geometry = vehicle_geometry
        self.plate = plate
        self.materials = materials

    def shifting(self):
        print("变速")

    def move(self):
        print("移动")

    def repair(self):
        print("修理")


# Windows窗口：
# 数据（属性或者状态）： 颜色、 样式、 标题、 位置…
# 操作（方法或者功能）： 打开窗口、 改变大小、 移动位置…

class Windows:

    def __init__(self, color, style, title, location) -> None:
        super().__init__()
        self.color = color
        self.style = style
        self.title = title
        self.location = location

    def open_windows(self):
        print("打开窗口")

    def change_size(self):
        print("改变尺寸大小")

    def move_location(self):
        print("移动位置")


# 鱼：
# 数据：年龄、大小、颜色、名字
# 操作：游泳、捕食、睡觉...
#
class Fish:

    def __init__(self, age, size, color, name) -> None:
        super().__init__()
        self.age = age
        self.size = size
        self.color = color
        self.name = name

    def swim(self):
        print("游泳")

    def eat(self):
        print("捕食")

    def sleep(self):
        print("睡觉")


# 编写圆类：
# 数据：半径、坐标
# 操作：求面积、求周长

class Circle:

    def __init__(self, r, pos_x,pos_y) -> None:
        super().__init__()
        self.r = r
        self.pos_x = pos_x
        self.pos_y = pos_y

    def find_area(self):
        s = math.pi * self.r ** 2
        print(s)
        return s

    def find_girth(self):
        girth = math.pi * self.r * 2
        print(girth)
        return girth


# find_girth(1)

c1 = Circle(2, 3,3)
c3 = Circle(3, 5,5)
c2 = Circle(8, 0,0)
Circle.find_girth(c1)
print(f"在({c1.pos_x},{c1.pos_y})点画半径为{c1.r}的圆,他的周长是{c1.find_girth()}，面积是{c1.find_area()}")
print(f"在({c2.pos_x},{c2.pos_y})点画半径为{c2.r}的圆,他的周长是{c2.find_girth()}，面积是{c2.find_area()}")
print(f"在({c3.pos_x},{c3.pos_y})点画半径为{c3.r}的圆,他的周长是{c3.find_girth()}，面积是{c3.find_area()}")