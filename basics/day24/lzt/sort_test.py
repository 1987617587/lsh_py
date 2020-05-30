# author:lzt
# date: 2019/12/5 14:47
# file_name: sort_test
import random

# 冒泡
import sys
import time


def bubble_Sort(arr: list):
    # 冒泡次数
    # n个数冒泡n-1
    for i in range(len(arr) - 1):
        # j-1 j j+1
        # j:[0,len-1]
        # 5 3 2 6 8
        for j in range(len(arr) - 1 - i):
            # 比较完就交换
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# arr = random.sample(list(range(10000)), k=10000)


arr = list(range(10000))


# print(arr)
# s = time.time()
# bubble_Sort(arr)
# print(time.time() - s)


# print(arr)


# 选择
def select_sort(arr: list):
    for i in range(len(arr) - 1):
        min_pos = i
        for j in range(i + 1, len(arr)):
            # 只比较 不交换
            # 记忆最新的最小的位置
            if arr[min_pos] > arr[j]:
                min_pos = j
        # 判断min_pos和i位置若不相同 再交换
        if min_pos != i:
            arr[min_pos], arr[i] = arr[i], arr[min_pos]


# select_sort(arr)
# print(arr)
# s = time.time()
# select_sort(arr)
# print(time.time() - s)

# 插入
def insert_sort(arr: list):
    # 控制插入的次数
    for i in range(1, len(arr)):
        # 监视哨
        temp = arr[i]
        # 寻找插入位置 还是当前位置为最佳
        insert_index = i

        # temp vs insert_index-1
        # insert_index>0
        while insert_index > 0 and temp < arr[insert_index - 1]:
            # 移动元素位置
            arr[insert_index] = arr[insert_index - 1]
            insert_index -= 1
        # 插入数据
        if insert_index != i:
            arr[insert_index] = temp


# insert_sort(arr)
# print(arr)
# s = time.time()
# insert_sort(arr)
# print(time.time() - s)

# 快速排序的划分：
# 借助数据结构的算法
def quick_sort1(arr: list):
    """
    为某个序列进行划分：按首元素为界 化为左小右大的两个列表
    :param arr:某列表
    :return:左 中间临界值 右
    """
    if len(arr) < 2:
        return arr
    less, pivot, right = [], arr[0], []

    for i in arr:
        if i < pivot:
            less.append(i)
        if i > pivot:
            right.append(i)
    return quick_sort1(less) + [pivot] + quick_sort1(right)


# print(quick_sort1([5, 3, 2, 4, 7, 9]))
# s = time.time()
# quick_sort1(arr)
# print(time.time() - s)


# 原地划分
def quick_sort2(arr: list, start, end):
    """
    为序列的某部分进行划分
    :param arr:序列
    :param start:开始位置
    :param end:结束位置
    :return:None
    """
    if start < end:
        s = start
        e = end
        # True:临界值在左边 F:临界值在右边
        flag = True

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
        # [start,e-1]:左边
        quick_sort2(arr, start, e - 1)
        # [s+1,end]
        quick_sort2(arr, s + 1, end)


# arr = [5, 3, 2, 4, 7, 9]
# quick_sort2(arr, 0, len(arr) - 1)
# print(arr)
sys.setrecursionlimit(1000000)
s = time.time()
quick_sort2(arr, 0, len(arr) - 1)
print(time.time() - s)
