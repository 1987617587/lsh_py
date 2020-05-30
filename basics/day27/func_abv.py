"""
# author Liu shi hao
# date: 2019/12/10 11:24
# file_name: func_abv

"""
from functools import reduce


# map 建立映射关系
# arr1 = ["星期一", "星期二", "星期三", "星期四", "星期五", "星期六", "星期日"]
# arr2 = [1, 2, 3, 4, 5, 6, 7]
# print(dict(map(lambda x, y: (x, y), arr2, arr1)))


# filter过滤
# str1 = "afgAWGFAGSDAasfdasd"
# a_str = "".join(list(filter(lambda x: x == "a", str1)))
# print(a_str)
#
# arr1 = [1, 2, 33, 44, 55, 66, 77, 32, 88, 99]
# a_arr = list(filter(lambda x: x >= 60, arr1))
# print(a_arr)


class Student:
    def __init__(self, name, score) -> None:
        super().__init__()
        self.name = name
        self.score = score

    def __lt__(self, other):
        return self.name < self.name


stus = [Student('001', 87), Student('002', 57), Student('003', 67)]

stus2 = filter(lambda stu: stu.score >= 60, stus)
# filter支持迭代
for i in stus2:
    print(i.name, i.score)

s_stu3 = reduce(lambda x, y: x + y, [s.score for s in stus])
print(f"学生总成绩:{s_stu3}")

# reduce 只用于合并计算(对元素进行累积)

n = 5
n_fac = reduce(lambda x, y: x * y, list(range(2, n + 1)))
print(f"5的阶乘：{n_fac}")

# 排序 sort(原地排序)\sorted（非原地排序）
print("sort.score**********")
stus.sort(key=lambda s: s.score)
for i in stus:
    print(i.name, i.score)
print("sort.name**********")
stus.sort(key=lambda s: s.name)
for i in stus:
    print(i.name, i.score)

print("sorted.score**********")
n_stus = sorted(stus, key=lambda s: s.score)
for i in n_stus:
    print(i.name, i.score)
print("sorted.name**********")
n_stus = sorted(stus, key=lambda s: s.name)
for i in n_stus:
    print(i.name, i.score)
