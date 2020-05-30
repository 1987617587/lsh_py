# author:lzt
# date: 2019/12/10 15:37
# file_name: generator_test
# big_list = [x for x in range(99999999999999999999999)]
big_list = (x for x in range(99999999999999999999999))

# print(type(big_list))

# 惰性求值
# nums = 10000
# while nums > 0:
#     print(next(big_list))
#     nums -= 1
#
# nums = 10000
# while nums > 0:
#     print(next(big_list))
#     nums -= 1


# 自定义生成器:yield的标记


i = 0


def my_generator():
    global i
    while 1:
        i += 1
        yield i


# m1 = my_generator()
# print(type(m1))
# print(next(m1))
# print(next(m1))
# print(next(m1))
# print(next(m1))

# i = 0
# m2 = my_generator()
# print(type(m2))
# print(next(m2))

# print(next(m1))
# print(next(m1))


def fibona(n: int):
    if n < 1:
        return
    before = 0
    cur = 1
    while n > 0:
        yield cur  # 暂停函数执行 让函数状态继续保持 让程序看起来像多道程序一样并发执行
        before, cur = cur, before + cur
        n -= 1
    return "ok"


# f10 = fibona(10)
# # for i in f10:
# #     print(i)
# try:
#     while 1:
#         print(next(f10))
# except StopIteration as e:
#     print(e)

i2 = 10000


def my_generotor2():
    global i2
    while 1:
        i2 -= 1
        yield i2


m1 = my_generator()
m2 = my_generotor2()

while 1:
    data1 = next(m1)
    data2 = next(m2)
    print(f"m1:{data1}")
    print(f"m2:{data2}")
    if data1 == data2:
        break

