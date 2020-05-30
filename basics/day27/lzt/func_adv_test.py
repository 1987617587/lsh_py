# author:lzt
# date: 2019/12/10 11:21
# file_name: func_adv_test
# 高阶函数
# map
# list1 = ["星期一", "星期二", "星期三", "星期四"]
# list2 = [1, 2, 3]
# print(dict(map(lambda x, y: (x, y), list2, list1)))


# 请找出字符串中所有的a
# str1 = "asdasdasdasd"
# a_list = "".join(list(filter(lambda x: x == "a", str1)))
# print(a_list)

# 筛选出列表中所有及格的学生
from functools import reduce


class Student:

    def __init__(self, name, s) -> None:
        super().__init__()
        self.name = name
        self.s = s

    # def __lt__(self, other):
    #     return self.name < other.name


stus = [Student("001", 59), Student("000", 56), Student("003", 88)]
#
# stus2 = filter(lambda stu: stu.s >= 60, stus)
#
# # filter支持直接迭代！！！
# for i in stus2:
#     print(i.name, i.s)


# reduce:只用于合并计算（并发式）不支持对象
# 某数阶乘
# n = 5
# n_fac = reduce(lambda x, y: x * y, list(range(1, n + 1)))
# print(n_fac)
#
# # 计算所有学生的总成绩
# s_total = reduce(lambda x, y: x + y, [s.s for s in stus])
# print(s_total)

# sort/sorted
# stus.sort(key=lambda s: s.s)
# for i in stus:
#     print(i.name, i.s)
#
# stus.sort(key=lambda s:s.name)
# for i in stus:
#     print(i.name, i.s)

# 产生新列表 非原地排序！
sort_stus = sorted(stus, key=lambda x: x.name)
for i in sort_stus:
    print(i.name, i.s)

