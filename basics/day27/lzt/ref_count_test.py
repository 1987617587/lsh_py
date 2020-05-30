# author:lzt
# date: 2019/12/10 10:27
# file_name: ref_count_test
import sys

a = 1

# 查看引用的计数情况：sys
print(sys.getrefcount(a))

b = a
list1 = [a]

print(sys.getrefcount(a))

b = 2
list1.remove(a)
# del a
# print(sys.getrefcount(a))

import gc
print(gc.get_threshold())
gc.set_threshold(100,5,2)


