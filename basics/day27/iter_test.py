"""
# author Liu shi hao
# date: 2019/12/10 15:05
# file_name: iter_test

"""
# 判断是否可迭代或是否为迭代器：
from collections.abc import Iterator, Iterable


# 迭代和迭代器：
# 可迭代的对象对应的类中只有：__iter__()方法
# 需要内置函数iter()的支持才可迭代
# class MyList:
#
#     def __init__(self, my_list) -> None:
#         super().__init__()
#         self.my_list = my_list
#
#     def __iter__(self):
#         return iter(self.my_list)
#
#
# my_list = MyList([1, 2, 3, 4])
# print(isinstance(my_list, Iterable))  # 可迭代
# print(isinstance(my_list, Iterator))  # 不是迭代器
# for i in my_list:
#     print(i)


# 迭代器：包含__iter__()方法和__next__()方法：
# 直接可迭代也可以next(本迭代对象)
class MyList:
    cur_inx = -1

    def __init__(self, my_list) -> None:
        super().__init__()
        self.my_list = my_list

    def __iter__(self):
        return self

    def __next__(self):
        MyList.cur_inx += 1
        if MyList.cur_inx >= len(self.my_list):
            raise StopIteration
        return self.my_list[MyList.cur_inx]


my_list = MyList([1, 2, 3, 4])
print(next(my_list))  # 迭代器支持next
print(next(my_list))
print(next(my_list))
print(next(my_list))
# print(next(my_list))

# for i in my_list:
#     print(i)


# 判断是否为迭代器
print(isinstance("123", Iterator))

# 判断是否为可迭代
# print(isinstance([1, 2, 3], Iterable))
# for i in [1,2,3]:
#     print(i)

# 生成器既可以迭代也可以next
