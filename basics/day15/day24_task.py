"""
# author arru shi hao
# date: 2019/12/5 20:06
# file_name: day24_task

"""

# 1.为一个既有数字又有小写字母的字符串进行字符排序。
# 要求使用冒泡排序
#
import random
import time
from queue import LifoQueue


def func1(msg: str):
    if msg.isalnum():
        arr = list(msg)
        for i in range(1, len(arr) - 1):
            for j in range(len(arr) - 1 - i):
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
        return "".join(arr)


print(func1("1jh23f"))


# 2.为一个既有数字又有大小写字母的字符串进行字符排序。
# 大小写字母排序时需要注意只比较字母的先后次序
# 例：1CaD =>1aCD
# 要求使用选择排序
#
def func2(msg: str):
    if msg.isalnum():
        arr = list(msg)
        for i in range(len(arr) - 1):
            min_num = i
            for j in range(i + 1, len(arr)):
                if arr[min_num].lower() > arr[j].lower():
                    min_num = j
            if min_num != i:
                arr[min_num], arr[i] = arr[i], arr[min_num]
        return "".join(arr)


print(func2("1GKjhL23kf"))


# 3.对象列表的插入排序怎么做？
#
class Student:

    def __init__(self, name, gender, stu_num, pid) -> None:
        super().__init__()
        self.stu_num = stu_num
        self.gender = gender
        self.name = name
        self.pid = pid

    def __lt__(self, other):
        return self.pid < other.pid

    def __gt__(self, other):
        return self.pid > other.pid

    # def __eq__(self, other):
    #     return self.pid == other.pid

    def __str__(self) -> str:
        return f"姓名{self.name}\t性别{self.gender}\t学号{self.stu_num}\t身份证号{self.pid}"


stus = [
    Student("sfs", "男", "001", 123),
    Student("fsg", "男", "002", 322),
    Student("ret", "女", "003", 192),
    Student("sdf", "男", "004", 222),
    Student("sdf", "nv", "005", 333)

]

for j in stus:
    print(j)

print("*" * 9, "排序结果如下", "*" * 9)


def insertion_sort1(arr: list):
    for i in range(1, len(arr)):
        insert_index = i
        temp = arr[i]  # 监事稍
        while arr[insert_index - 1] > temp and insert_index > 0:
            arr[insert_index] = arr[insert_index - 1]
            insert_index -= 1
        arr[insert_index] = temp
    return arr


# insertion_sort1(stus)
# for j in stus:
#     print(j)

# 4.为一个对象列表追加10000个随机对象，并按照快速排序方案为其排序。最好计算出所消耗的时间。
#
def quick_sort(arr):
    """
    模拟栈操作实现非递归的快速排序
    :param arr:
    :return:
    """
    if len(arr) < 2:
        return arr
    qu = LifoQueue()

    qu.put(len(arr) - 1)
    qu.put(0)
    while not qu.empty():
        left = qu.get()
        right = qu.get()
        index = part(arr, left, right)
        if left < index - 1:
            qu.put(index - 1)
            qu.put(left)
        if right > index + 1:
            qu.put(right)
            qu.put(index + 1)


def part(arr, s, e):
    flag = True
    # 分区操作，返回基准线下标
    pivot = arr[s]
    while s < e:
        # 判断 s > e
        if arr[s] > arr[e]:
            arr[s], arr[e] = arr[e], arr[s]
            flag = not flag
        # 方向需要左移或右移
        if flag:
            e -= 1
        else:
            s += 1
    # 此时start = end
    arr[s] = pivot
    return s


def quick_sort1(arr: list):
    # 划分两部分
    if len(arr) < 2:
        return arr
    less, pivot, right = [], arr[0], []
    for i in arr:
        if i < pivot:
            less.append(i)
        if i > pivot:
            right.append(i)

    return quick_sort1(less) + [pivot] + quick_sort1(right)


stus2 = []
num = random.sample(range(10000), 10000)
print(num)
for i in range(10000):  # 花里胡哨生成对象
    stus2.append(Student("".join(random.sample("abcdefghijklmnopqrstuvwxyz", 3)), random.choice("男女"),
                         str(i).rjust(4, "0"), str(num[i]).rjust(4, "0")))

# # 偷看一下学生对象是否正常
# for j in stus2:
#     print(j)

print("*" * 9, "递归方法快速排序结果如下", "*" * 9)
start_time = time.time()

stus2 = quick_sort1(stus2)
for j in stus2:
    print(j)
print(f"递归方法快速排序时间：{time.time() - start_time}")


# print("*" * 9, "使用栈快速排序结果如下", "*" * 9)
# start_time = time.time()
#
# quick_sort(stus2)
# for j in stus2:
#     print(j)
# print(f"使用栈方法快速排序时间：{time.time() - start_time}")
# print()
# 5.接上一题：排序完毕后，按照客户需要查询的关键字对对象集合进行折半查询，查不到返回None，查询到返回查到的对象。

def er(arr: list, num):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid].pid == num:
            return arr[mid]
        if arr[mid].pid > num:
            end = mid - 1
        else:
            start = mid + 1
    return None


print(er(stus2, "1233"))

#
# 2.汉诺塔问题的解决？
# 汉诺（Hanoi）塔问题：古代有一个梵塔，塔内有三个座A、B、C，A座上有n个盘子，盘子大小不等，大的在下，小的在上。
# 有一个和尚想把这n个盘子从A座移到C座，但每次只能允许移动一个盘子，并且在移动过程中，3个座上的盘子始终保持大盘在下，小盘在上。
# 在移动过程中可以利用B座，要求打印移动的步骤。如果只有一个盘子，则不需要利用B座，直接将盘子从A移动到C。
#
# 结束条件 n==1 A->C
# 1.将n-1个盘子 从A借助C 移到B
# 2.将n这个盘子移到C
# 3.将n-1个盘子 从B借助A 移到C
