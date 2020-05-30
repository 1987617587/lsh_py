# author:lzt
# date: 2019/12/10 14:23
# file_name: partial_test

# 偏函数 降低参数个数的调用方式
# 产生新的函数


def file_write_objs(file, obj1, obj2, obj3):
    print(file)
    print(obj1)
    print(obj2)
    print(obj3)


# 某次的模块中 固定了文件的路径和名字
from functools import partial

# 偏函数
part_file_write = partial(file_write_objs, "1.py")
part_file_write(1, 2, 3)
part_file_write("a", "b", "c")

# open(encoding="utf-8")
my_open = partial(open, encoding="utf-8")

with my_open("1.txt", "w") as w:
    w.write("我是偏函数写的")
