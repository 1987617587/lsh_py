# author:lzt
# date: 2019/12/10 11:07
# file_name: lambda_test
# 匿名函数的写法
# lambda 参数,....: 唯一的一个表达式
x1 = lambda: print(10)


# x1()
# x1()
# x1()
# x1()

# 带返回的lambda
# x2 = lambda x: x + 1
# print(x2(2))
# print(x2(3))
# print(x2(4))

# 函数也是成员的一个：函数化编程的第一要求
def args_func(func):
    func()


def func1():
    print("被传递的函数")


# args_func(func1)
args_func(lambda: print("匿名函数的逻辑"))
