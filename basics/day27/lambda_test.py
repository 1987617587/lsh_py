"""
# author Liu shi hao
# date: 2019/12/10 11:15
# file_name: lambda_test

"""


def args_func(func):
    func()


def func1():
    print("被传递的函数")


# args_func(func1)

args_func(lambda: print("匿名函数的逻辑"))
