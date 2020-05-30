"""
# author Liu shi hao
# date: 2019/12/11 10:23
# file_name: type_class_test

"""

# class_a = type('A', (object,), {'name': '张三', 'func1': lambda: print("这是类的方法")})
# obj1 = class_a()
# print(obj1.name)
# print(class_a.name)
# class_a.func1()
#
# print(class_a.__name__)
from typing import Any


class Animal:

    def __init__(self) -> None:
        super().__init__()

    def eat(self):
        print('吃')


def func1(self):
    print("走去")


def type_function(class_name, tuple_supers, class_dict):
    print("元函数拦截到类的生成")
    print(class_name, tuple_supers, class_dict)
    list_supers = list(tuple_supers)
    list_supers.append(Animal)
    class_dict['qiku'] = "蛋糕"
    class_dict['func1'] = func1
    return type(class_name, tuple(list_supers), class_dict)


class TypeClass(type):

    def __new__(cls, class_name, tuple_supers, class_dict) -> Any:
        print("元类拦截到类的生成")
        print(class_name, tuple_supers, class_dict)
        list_supers = list(tuple_supers)
        list_supers.append(Animal)
        class_dict['qiku'] = "奇酷"
        class_dict['func1'] = func1
        return super().__new__(cls, class_name, tuple(list_supers), class_dict)


class TypeTest(metaclass=TypeClass):  # 元类的方式
    # class TypeTest(metaclass=type_function):  # 元函数的方式

    def __init__(self) -> None:
        super().__init__()
        print("类的对象的初始化")


t1 = TypeTest()
if hasattr(t1, "func1"):
    t1.func1()
if hasattr(t1, "eat"):
    t1.eat()
if hasattr(t1, "qiku"):
    print(t1.qiku)
getattr(t1, "eat")  # 判断属性是否存在（消除找不到的警告）
