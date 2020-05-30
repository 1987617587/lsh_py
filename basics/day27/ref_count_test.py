"""
# author Liu shi hao
# date: 2019/12/10 10:32
# file_name: ref_count_test

"""
import sys

a = 1
print(sys.getrefcount(a))
b = a
print(sys.getrefcount(a))
b = 1

print(sys.getrefcount(a))

import gc

print(gc.get_threshold())
# print(gc.set_threshold(100,10,10))  # 修改
