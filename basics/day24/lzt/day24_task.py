# author:lzt
# date: 2019/12/6 9:15
# file_name: day24_task
# 3.对象列表的插入排序怎么做？
import random
import time


class Account:

    def __init__(self, acc_id, name, money) -> None:
        super().__init__()
        self.acc_id = acc_id
        self.name = name
        self.money = money

    def __str__(self) -> str:
        return f"{self.acc_id} {self.name} {self.money}"

    def __lt__(self, other):
        return self.money < other.money

    def __gt__(self, other):
        return self.money > other.money

    def __eq__(self, o) -> bool:
        return self.money == o.money


# moneys = random.sample(list(range(10000)), k=10000)
moneys = list(range(10000))
accs = [Account(random.randint(10000, 99999), str(random.randint(9000, 1000000)), moneys.pop(0)) for i in range(10000)]


def insert_sort(arr: list):
    for i in range(1, len(arr)):
        temp = arr[i]
        insert = i
        while insert > 0 and temp < arr[insert - 1]:
            arr[insert] = arr[insert - 1]
            insert -= 1
        arr[insert] = temp


# insert_sort(accs)
# for i in accs:
#     print(i)


#
# 4.为一个对象列表追加10000个随机对象，并按照快速排序方案为其排序。最好计算出所消耗的时间。
def quick_sort(arr: list):
    if len(arr) < 2:
        return arr
    less, pivots, rights = [], [arr[0]], []

    for i in arr:
        if i < pivots[0]:
            less.append(i)
        elif i == pivots[0]:
            pivots.append(i)
        else:
            rights.append(i)

    return quick_sort(less) + pivots + quick_sort(rights)


from queue import LifoQueue


def quick_sort2(arr: list):
    objs = LifoQueue()
    objs.put(arr)
    ret = []
    while not objs.empty():
        arr = objs.get()

        less, pivots, rights = [], [arr.pop(0)], []

        for i in arr:
            if i < pivots[0]:
                less.append(i)
            elif i == pivots[0]:
                pivots.append(i)
            else:
                rights.append(i)

        # 将左中右放到栈中
        if len(rights) > 0:
            objs.put(rights)

        if len(pivots) > 0:
            objs.put(pivots)

        # 左边如果只剩一个元素的话 直接出栈
        if len(less) < 2:
            ret += less + objs.get()
        else:
            objs.put(less)

    return ret


s = time.time()
# accs = quick_sort(accs)
accs = quick_sort2(accs)
# for i in accs:
#     print(i)
print(time.time() - s)


#
# 5.接上一题：排序完毕后，按照客户需要查询的关键字对对象集合进行折半查询，查不到返回None，查询到返回查到的对象。
def half_search(arr: list, search_key):
    start = 0
    end = len(arr) - 1

    while start <= end:
        # 1 2 3
        mid = (start + end) // 2
        if arr[mid] == search_key:
            return arr[mid]
        elif search_key > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return None


money = 1999

obj = half_search(accs, Account(None, None, money))
print(obj)
