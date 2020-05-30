"""
# author Liu shi hao
# date: 2019/12/10 16:29
# file_name: check_test

"""

# 装饰器的作用：在不改变原函数的情况下给函数增加功能（切面编程）！
# 装饰器由闭包和语法糖组成
# 案例分析
# 用户查询商品列表业务逻辑
# def select_goods():
#     print("开始查询商品列表")
# select_goods()
# 调用select_goods方法即可查询商品列表
# 业务更改
# 在查询商品列表之前需要添加权限验证
# def select_goods():
#     name = input("请输入用户名")
#     if name == "lzt":
#         print("开始查询商品")
#     else:
#         print("无权查看")
# select_goods()
# 功能实现呃，但是改变了原有函数的
# 在增加新功能的情况下不改变原有业务逻辑实现，违背了开闭原则
#
# 使用装饰器
# @函数名 是python的一种语法糖。
# def checkaccess(sg):
#     def check():
#         name = input("输入用户名")
#         if name == "zzy":
#             sg()
#         else:
#             print("无权查看")
#     return check
# @checkaccess
# def selectgoods():
#     print("开始查询商品")
# selectgoods()
# 使用装饰器之后则selectgoods函数没有发生变化
#
# @函数名 执行逻辑:
# 检测到需要执行的函数selectgoods 拥有装饰器@checkaccess
# 不执行selectgoods 而是将selectgoods 作为参数传入checkaccess方法，
# 并且执行checkaccess 方法 此时sg =selectgoods将checkaccess的执行结果返回，
# 即将check方法的引用返回，即实际执行的是check方法。
import time
from functools import wraps


def buy():
    """
    购买道具的方法
    :return:
    """
    print("购买道具")


cur_user = None


def check_login(func):
    """
    装饰函数的方法
    :param func:
    :return:
    """

    @wraps(func)
    def do_func():
        if cur_user is None:
            print("请先登录！")
        else:
            func()

    return do_func


# func1 = check_login(buy)
# func1()
# print(func1.__doc__)

# 用python独有的方法优化上面的代码
@check_login
def pk():
    print("找人绝斗！")


pk()


def pr(func):
    @wraps(func)
    def do_func():
        print("#" * 20)
        func()
        print("#" * 20)

    return do_func


@pr
def welcome():
    print("欢迎来到奇酷课堂！")


@pr
def over():
    print("Game over！".rjust(15))


welcome()
over()


# 装饰带参和有返回值的函数
def check_index(func):
    @wraps(func)
    def wrapper(arr: list, index: int, new_value: int):
        if index < 0 or index >= len(arr):
            return
        return func(arr, index, new_value)  # 有返回值的函数装饰也必须有返回

    return wrapper


@check_index
def chang_list(arr: list, index: int, new_value: int):
    arr[index] = new_value
    return arr[index]


print(chang_list([1, 2], 2, 2))
print(chang_list([1, 2], 0, 2))


# 对成员方法，类方法，类函数装饰
def war_obj(func):
    @wraps(func)
    def wrapper(self):
        print("成员方法的前处理")
        print(self)
        func(self)
        print("成员方法的后处理")

    return wrapper


def wra_class(func):
    @wraps(func)
    def wrapper(cls):
        s = time.time()
        func(cls)
        print(time.time() - s)

    return wrapper


class UI:
    @war_obj
    def self_func(self):
        print("成员方法运行")

    @classmethod
    @wra_class
    def cls_func(cls):
        print("页面操作")


UI().self_func()
UI.cls_func()
