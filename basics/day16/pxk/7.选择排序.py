li = [8, 5, 1, 6, 4]


# def choose_sort(li):
#     #外层循环控制比较的轮数
#     for i in range(len(li)-1):
#         #先假定一个最小值的下标
#         min = i
#         #内层循环控制比较的次数
#         for j in range(i+1,len(li)):
#             #比较
#             if li[min]>li[j]:
#                 min = j
#         #每轮比较结束后进行值交换
#         li[min],li[i] = li[i],li[min]
#
# choose_sort(li)
# print(li)
#
#


def dichotomy(arr: list, num: int):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == num:
            return True
        if arr[mid] > num:
            end = mid
        else:
            start = mid + 1
    return False


print(dichotomy([1, 2, 3, 4, 5], 0))
da