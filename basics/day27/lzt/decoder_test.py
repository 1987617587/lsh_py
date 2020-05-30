# author:lzt
# date: 2019/12/10 16:31
# file_name: decoder_test
# 装饰器

# 装饰器可以装饰 函数 类方法 成员方法 类函数 类
import sys
import time


def buy():
    """
    购买道具的方法
    :return:
    """
    print("购买道具！")


cur_user = None

# 必须为登录用户
# 在不许改动原函数的情况下 限定函数的执行环境！！！ 开闭原则
# 用闭包完成函数的装饰 为原型函数追加了限定！！！
# 还原函数的原型
from functools import wraps


def check_login(func):
    # 还原原型函数
    @wraps(func)
    def do_func():
        """
        装饰后的方法
        :return:
        """
        if cur_user is None:
            print("请先登录!")
        else:
            func()

    return do_func


# func1 = check_login(buy)
# print(func1)
# print(func1.__doc__)
# func1()


# python特有的装饰方式
@check_login
def pk():
    print("和别人决斗！")


# pk()


# 追加两行#
# ######################
# 欢迎来到奇酷课堂
# ######################
def add_chars(func):
    @wraps(func)
    def wrapper():
        print("#" * 40)
        func()
        print("#" * 40)

    return wrapper


@add_chars
def welcome():
    print("欢迎来到奇酷课堂")


# welcome()

# 装饰器装饰函数有参数和返回值
def check_index(func):
    @wraps(func)
    def wrapper(arr: list, index: int, new_value: int):
        if index < 0 or index >= len(arr):
            return
        return func(arr, index, new_value)

    return wrapper


@check_index
def change_list(arr: list, index: int, new_value: int):
    arr[index] = new_value
    return arr[index]


# print(change_list([1, 2, 3], 1, 111))


# 装饰器装饰成员方法 类方法 类函数
# 成员方法的装饰器
def obj_wrapper(func):
    @wraps(func)
    def wrapper(self):
        print("对成员方法的前处理")
        print(self)
        func(self)
        print("成员方法的后处理")

    return wrapper


def wrapper_class_method(func):
    @wraps(func)
    def wrapper(cls):
        s = time.time()
        func(cls)
        print(time.time() - s)

    return wrapper


class UI:

    @obj_wrapper
    def foreach(self):
        for i in range(100):
            print(i)


    @classmethod
    @wrapper_class_method
    def operator(cls):
        print("操作界面")

    @staticmethod
    def exit():
        print("询问是否确认退出！")


# UI().foreach()
UI.operator()
