# author:lzt
# date: 2019/12/10 15:06
# file_name: iterable_iterator_test
# iterable:可迭代
# iterator:迭代器
from collections.abc import Iterable, Iterator


# 某些数据结构是否可迭代:
print(isinstance([1, 2, 3], Iterable))
print(isinstance("asdasd", Iterable))

# 支持迭代：for i in 可迭代的对象
# for i in [1, 2, 3]:
#     print(i)

# 迭代器:next()
# list1 = [1, 2, 3]
# print(next(list1))

# 声明一个支持迭代的自定义的类


class MyList:
    # 声明一个类变量 用于保存当前迭代的位置
    __cur = -1

    def __init__(self, my_list) -> None:
        super().__init__()
        self.my_list = my_list

    # 为了支持迭代 需要__iter__
    # def __iter__(self):
    #     return iter(self.my_list)

    # 迭代器:
    # 将当前类的对象变成迭代器对象
    def __iter__(self):
        return self

    # 迭代的方式
    def __next__(self):
        # 让迭代器指向后一个位置
        MyList.__cur += 1
        # 若无元素可迭代:
        if MyList.__cur >= len(self.my_list):
            raise StopIteration
        return self.my_list[MyList.__cur]


m_list = MyList([1, 2, 3, 4])
# print(isinstance(m_list,Iterable))
print(isinstance(m_list, Iterator))
# for i in m_list:
#     print(i)
# print(next(m_list))
# print(next(m_list))
# print(next(m_list))
# print(next(m_list))
# print(next(m_list))
# for i in m_list:
#     print(i)




