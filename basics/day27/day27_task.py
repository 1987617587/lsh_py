"""
# author Liu shi hao
# date: 2019/12/10 17:53
# file_name: day27_task

"""
# 1，exec1.py文件
# 使用yield得到生成器
# i = 0
#
#
# def my_generator():
#     global i
#     while 1:
#         i += 1
#         yield 1
#
#
# m1 = my_generator()
# print(next(m1))
# print(next(m1))
# print(next(m1))
# 创建列表，元组，字典，字符串，整形
arr1 = [1, 2, 3, 4]
tup1 = (11, 22, 33, 44)
dic1 = {1: 1, 2: 2, 3: 3}
str1 = "abcd"
num1 = 9999
# 判断以上类型是否可以迭代，是否是迭代器
from collections.abc import Iterator, Iterable

print("#" * 20, "列表")
print(f"{arr1}可以迭代") if isinstance(arr1, Iterable) else print(f"{arr1}不可以迭代")
print(f"{arr1}是迭代器") if isinstance(arr1, Iterator) else print(f"{arr1}不是迭代器")
print("#" * 20, "元组")
print(f"{tup1}可以迭代") if isinstance(tup1, Iterable) else print(f"{tup1}不可以迭代")
print(f"{tup1}是迭代器") if isinstance(tup1, Iterator) else print(f"{tup1}不是迭代器")
print("#" * 20, "字典")
print(f"{dic1}可以迭代") if isinstance(dic1, Iterable) else print(f"{dic1}不可以迭代")
print(f"{dic1}是迭代器") if isinstance(dic1, Iterator) else print(f"{dic1}不是迭代器")
print("#" * 20, "字符串")
print(f"{str1}可以迭代") if isinstance(str1, Iterable) else print(f"{str1}不可以迭代")
print(f"{str1}是迭代器") if isinstance(str1, Iterator) else print(f"{str1}不是迭代器")
print("#" * 20, "整形")
print(f"{num1}可以迭代") if isinstance(num1, Iterable) else print(f"{num1}不可以迭代")
print(f"{num1}是迭代器") if isinstance(num1, Iterator) else print(f"{num1}不是迭代器")
# 如果是迭代器则使用next得到所有内容
