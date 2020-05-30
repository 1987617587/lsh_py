"""
# author Liu shi hao
# date: 2019/12/10 15:34
# file_name: generator_test

"""
# 什么是生成器
# 通过列表生成式，我们可以直接创建一个列表。但是，受到内存限制，列表容量肯定是有限的。
# 而且，创建一个包含100万个元素的列表，不仅占用很大的存储空间，如果我们仅仅需要访问前面几个元素，
# 那后面绝大多数元素占用的空间都白白浪费了。所以，如果列表元素可以按照某种算法推算出来，
# 那我们是否可以在循环的过程中不断推算出后续的元素呢？这样就不必创建完整的list，从而节省大量的空间。
# 在Python中，这种一边循环一边计算的(延迟/惰性)机制，称为生成器：generator
#
# 生成器的创建：
# 方法1
# 把一个列表生成式的 [ ] 改成 ( )
"""
生成器
"""
L = [x * x for x in range(5)]
# 列表类型为class 'list
print(L, type(L))
G = (x * x for x in range(5))
# 生成器类型为 class 'generator
print(G, type(G))
# 可以使用next获取元素
print(next(G))
print("----")
# 可以使用for对生成器遍历
for r in G:
    print(r)
print("----")


# 方法2
# 用函数来创建
# 打印裴波拉契算法（从第三项开始均为前两项的和）
def fib(times):
    n = 0
    a, b = 1, 1
    while n < times:
        if n < 2:  # 函数中若出现yield 本函数即为生成器 支持next(本生成器)惰性求值
            yield 1
        else:
            # 0 1 1 2 3 5 8
            a, b = b, b + a
            yield b
        n += 1
    return "finish"


r = fib(8)
while True:
    # 若要获取"finish"这个返回值 必须捕捉StopIteration这个异常
    try:
        x = next(r)
        print(x)
    except StopIteration as e:
        print(e.value)
        break


# 生成器的特点：节约内存
# 迭代到下一次的调用时，所使用的参数都是第一次所保留下的，
# 即是说，在整个所有函数调用的参数都是第一次所调用时保留的，而不是新创建的。

# i = 0
#
#
# def my_generator():
#     global i
#     while True:
#         i += 1
#         yield i
#
#
# m1 = my_generator()
# print('#' * 10)
# print(next(m1))
# print(next(m1))
# print(next(m1))
# print(next(m1))

def fibona(n: int):
    if n < 1:
        return
    before = 0
    cur = 1
    while n > 0:
        yield cur
        before, cur = cur, before + cur
        n -= 1
    return "ok"


f10 = fibona(10)
print("*" * 19)
try:
    while 1:
        print(next(f10))
except StopIteration as e:
    print(e)

i = 0


def my_generator1():
    global i
    while True:
        i += 1
        yield i


j = 10000


def my_generator2():
    global j
    while True:
        j -= 1
        yield j


m1 = my_generator1()
m2 = my_generator2()
while 1:
    a, b = next(m1), next(m2)
    if a == b:
        print(a, b)
        break


def next_func(n: int):
    i = 0
    while i < n:
        i += 1
        print(next(m1))
        # print(next(m2))


next_func(5)
next_func(5)
next_func(5)
