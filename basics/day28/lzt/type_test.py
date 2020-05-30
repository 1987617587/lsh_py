# author:lzt
# date: 2019/12/11 10:12
# file_name: type_test
# 类的生成方式:
# 1.自定义一个类 产生对象或使用其中的类的成员时 类自动产生
# 2.要使用元类产生类
# 3.可以干预类的出现过程


# class TypeTest:
#     pass
#
#
# tt = TypeTest
# tt()


#
#
# print(type(TypeTest))

# 哪个数据结构维护了类内部的成员__dict__
# print(TypeTest.__dict__)

# 类名
# 父类元组
# 内部属性
# class_a = type("A", (object,), {"name": "张三", "func1": lambda: print("这是类中的方法")})
# # print(type(class_a))
# obj1 = class_a()
# print(obj1)
# print(obj1.name)
# class_a.func1()
from typing import Any


class Animal:

    def __init__(self) -> None:
        super().__init__()

    def eat(self):
        print("吃")


def action(self):
    print("动态追加的方法！")


# 元函数
# 类名，父类元组，类的属性字典
def type_function(class_name, tuple_supers, clss_dict):
    print("元函数拦截到类的生成！")
    print(class_name, tuple_supers, clss_dict)
    # 通过拦截添加父类
    # 转换：list
    list_supers = list(tuple_supers)
    list_supers.append(Animal)
    # 通过拦截添加变量
    clss_dict["qiku"] = "奇酷课堂"
    clss_dict["action"] = action
    return type(class_name, tuple(list_supers), clss_dict)


# 自定义元类:必须从元类继承
class TypeClass(type):

    def __new__(cls, class_name, tuple_supers, clss_dict) -> Any:
        print("元类拦截到类的生成！")
        print(class_name, tuple_supers, clss_dict)
        # 通过拦截添加父类
        # 转换：list
        list_supers = list(tuple_supers)
        list_supers.append(Animal)
        # 通过拦截添加变量
        clss_dict["qiku"] = "奇酷课堂"
        clss_dict["action"] = action
        return super().__new__(cls, class_name, tuple(list_supers), clss_dict)


# class TypeTest(metaclass=type_function):
class TypeTest(metaclass=TypeClass):
    def __init__(self) -> None:
        super().__init__()
        print("类的对象的初始化")


t1 = TypeTest()
if hasattr(t1,"eat"):
    t1.eat()
if hasattr(t1,"qiku"):
    print(t1.qiku)
if hasattr(t1,"action"):
    t1.action()
