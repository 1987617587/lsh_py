# author:lzt
# date: 2019/11/18 16:38
# file_name: py_test
# def action(act):
#     print(type(act))
#
# action(1231)
# 多态：方便协作
# class Animal:
#     def eat(self):
#         pass
#
#
# class Dog(Animal):
#
#     def eat(self):
#         print("狗吃骨头")
#
#
# class Cat(Animal):
#
#     def eat(self):
#         print("猫吃鱼")
#
#
# def feed(an):
#     an.eat()


# feed(Dog())
# feed(Cat())

# 多态:代码扩展
# 角色类
# PK
class Role:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def attack(self):
        print(f"{self.name}角色攻击")


class Soldier(Role):

    def attack(self):
        print(f"{self.name}物理攻击")


class Master(Role):

    def attack(self):
        print(f"{self.name}魔法攻击")


def PK(role1, role2):
    role1.attack()
    role2.attack()

class NPC:
    def attack(self):
        print("NPC攻击")

PK(role1("程咬金"),NPC)
# PK(Role("程咬金"), Role("荆轲"))
# PK(Soldier("程咬金"), Master("妲己"))


# 多态：统一管理家族对象
# 模拟悟空变化动物
# class Animal:
#
#     def __init__(self, name) -> None:
#         super().__init__()
#         self.name = name
#
#     def action(self):
#         pass
#
#      def car(self):
#          print("")
#
# class Fish(Animal):
#
#     def __init__(self) -> None:
#         super().__init__("鱼")
#
#     def action(self):
#         print("在水中游来游去")
#
#
# class Bird(Animal):
#
#     def __init__(self) -> None:
#         super().__init__("鸟")
#
#     def action(self):
#         print("在天空自由翱翔")






# class WuKong:
    # animal这个标识符接收所有的动物 而后做出相同的处理 会根据多态性做出不同得响应
    # 要求:1.必须传入动物对象 2.对象必须具备action和name
    # 如何约束类型为Animal :Animal
    # def change_animal(self, animal: Animal):
    #     print(f"切换悟空模型到{animal.name}")
    #     animal.action()


# wk = WuKong()
# wk.change_animal(Bird())
# wk.change_animal(Fish())
# wk.change_animal("123")

