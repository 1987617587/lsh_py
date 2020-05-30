"""
# author Liu shi hao
# date: 2019/11/28 11:53
# file_name: test

"""


# li = [0, 1, 2, 3, 4, 5, 6]
# li_1 = [i + 1 for i in li]
# li_2 = [li[i] + 1 for i in li]
# li_3 = [int(chr(i)) for i in range(49, 56)]
# print(li_1)
# print(li_2)
# print(li_3)
# print([(x, y) for x in "123" for y in "314" if x != y])
# ma = [[1, 2, 3, 4],
#       [5, 6, 7, 8],
#       [9, 10, 11, 12]]
# print(list(zip(*ma)))
#
# print([[row[i] for row in ma] for i in range(4)])
#
# arr1 = [3, 2, 1, 5, 7, 9, 8]
#
# # 冒泡排序
def bubble_sort(arr: list):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


# print(bubble_sort(arr1))
# # 选择排序
def selection_sort(arr: list):
    for i in range(len(arr) - 1):
        min_num = i
        for j in range(i + 1, len(arr)):
            if arr[min_num] > arr[j]:
                min_num = j
        arr[min_num], arr[i] = arr[i], arr[min_num]
    return arr


# print(selection_sort([3, 2, 4, 1]))

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


# print(dichotomy([1, 2, 3, 4, 5],3))


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


# print(er([1, 2, 3, 4, 5], 8))

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


print(insertion_sort([1, 7, 6, 4, 5]))


def insertion_sort_2(arr):
    for i in range(1, len(arr)):
        for j in range(i):
            if arr[i] < arr[j]:
                arr.insert(j, arr.pop(i))  # 取出要比较的数，判断是否应该插入
    return arr


print(insertion_sort_2([1, 7, 6, 4, 5]))
