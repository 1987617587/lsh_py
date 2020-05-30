"""
# author Liu shi hao
# date: 2019/12/5 9:08
# file_name: queue_test

"""
from queue import Queue

qu = Queue()


# print(qu.empty())
#
#
# for i in "123456":
#     qu.put(i)
#
# print(qu.qsize())
#
# print("*"*10)
# for j in qu.queue:
#     print(j)
# print("*"*10)
# for j in range(qu.qsize()):
#     print(qu.get())
# 8.如何用队列实现约瑟夫环
# 约瑟夫环：假设有n个人坐成一圈，从某个人开始报数，
# 数到m的人出圈，接着从出圈的下一个人开始重新报数，数到m的人再次出圈，如此反复，直到所有人都出圈，请列出出圈顺序。

def func8(n, m):
    for i in range(1, n + 1):
        qu.put(f"第{i}个人")

    count = 0
    while qu.qsize() != 0:
        date = qu.get()
        count += 1
        if count % m == 0:
            print(f"{date}out")
        else:
            qu.put(date)


func8(5, 3)


def func8_2(n, m):
    for i in range(1, n + 1):
        qu.put(f"第{i}个人")

    count = 0
    while qu.qsize() != 0:
        date = qu.get()
        count += 1
        if count == m:
            count = 0
            print(f"{date}out")
        else:
            qu.put(date)


func8_2(5, 3)
