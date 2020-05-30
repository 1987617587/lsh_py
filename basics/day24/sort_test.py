"""
# author Liu shi hao
# date: 2019/11/28 11:53
# file_name: test

"""

# # 冒泡排序
import random
import time


def bubble_sort1(arr: list):
    temp = True
    while temp:
        temp = False
        for i in range(len(arr) - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                temp = True
    return arr


arr1 = list(range(10000))
random.shuffle(arr1)
s = time.time()
print(bubble_sort1(arr1))

print(time.time() - s)


def bubble_sort(arr: list):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


arr1 = list(range(10000))
random.shuffle(arr1)
s = time.time()
print(bubble_sort(arr1))

print(time.time() - s)


# print(id(arr1))
# print(bubble_sort(arr1))
# print(id(bubble_sort(arr1)))
#

# # 选择排序
def selection_sort(arr: list):
    for i in range(len(arr) - 1):
        min_num = i
        for j in range(i + 1, len(arr)):
            if arr[min_num] > arr[j]:
                min_num = j
        if min_num != i:
            arr[min_num], arr[i] = arr[i], arr[min_num]
    return arr


arr1 = list(range(10000))
random.shuffle(arr1)
s = time.time()
print(selection_sort(arr1))

print(time.time() - s)


# 二分法查找
def dichotomy(arr: list, num: int):
    start = 0
    end = len(arr) - 1
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == num:
            return True
        if arr[mid] > num:
            end = mid
        else:
            start = mid + 1
    return False


# print(dichotomy([1, 2, 3, 4, 5],1))


def er(arr: list, num: int):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == num:
            return True
        if arr[mid] > num:
            end = mid - 1
        else:
            start = mid + 1
    return False


print(er([1, 2, 3, 4, 5], 3))


# 插入排序
def insertion_sort(arr: list):
    for i in range(1, len(arr)):
        pre = i - 1
        key = arr[i]
        while arr[pre] > key and pre >= 0:
            arr[pre + 1] = arr[pre]
            pre -= 1
        arr[pre + 1] = key
    return arr


# print(insertion_sort([1, 7, 6, 4, 5]))


def insertion_sort1(arr: list):
    for i in range(1, len(arr)):
        insert_index = i
        temp = arr[i]  # 监事稍
        while arr[insert_index - 1] > temp and insert_index > 0:
            arr[insert_index] = arr[insert_index - 1]
            insert_index -= 1
        arr[insert_index] = temp
    return arr


# s = time.time()
# print(insertion_sort1(list(range(10000))))
#
# print(time.time() - s)


def insertion_sort_2(arr):
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr.insert(j, arr.pop(i))  # 取出要比较的数，判断是否应该插入
    return arr


# print(insertion_sort_2([1, 7, 6, 4, 5]))


# 快速排序
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


# li = [3, 6, 7, 4, 8, 1]
# print(quick_sort1(li))


def quick_sort2(arr: list):
    s, e = 0, len(arr) - 1
    flag = True
    # T:临界值在左端，F:在右端
    while s < e:
        if arr[s] > arr[e]:
            arr[s], arr[e] = arr[e], arr[s]
            flag = not flag
        if flag:
            e -= 1
        else:
            s += 1


# li = [3, 6, 7, 4, 8, 1]
# quick_sort2(li)

from queue import LifoQueue


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


# li = [3, 6, 7, 4, 10, 99, 8, 1, 2]
li = list(range(1, 10000))
# random.shuffle(li)
print(li)
s = time.time()
quick_sort(li)
print(time.time() - s)
print(li)
