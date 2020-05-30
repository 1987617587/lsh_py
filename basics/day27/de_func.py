"""
# author Liu shi hao
# date: 2019/12/10 14:47
# file_name: de_func
闭包 保存函数状态（保持数据）

"""


def class_func(name, age, gender):
    def student():
        print(name, age, gender)

    return student


c1 = class_func("张三", 19, "男")
c2 = class_func("李四", 29, "男")
c3 = class_func("赵月", 22, "女")


# c1()
# c2()
# c3()


def func_3d(x, y, z):
    def draw():
        print(x, y, z)

    return draw


d1 = func_3d(1, 2, 3)
d1()
