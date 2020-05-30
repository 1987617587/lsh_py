# author:lzt
# date: 2019/12/10 14:37
# file_name: de_func
# 闭包：保持函数状态:保持函数持有的数据
# 装饰器的基础


def class_func(name, age, gender):
    def student():
        print(name)
        print(age)
        print(gender)

    return student


# 函数像类一样保持了数据的状态
c1 = class_func("aaa", 18, "男")
# c1()
# c1()

c2 = class_func("bbb", 23, "女")
c1()
print("***********")
c2()


# 某3D画图工具中 用闭包保存已画过的图形位置(x,y,z) 以便再次画出该图形
def shape_3d(x, y, z):
    def draw():
        print(f"在{x},{y},{z}位置来画图！")

    return draw


shape1 = shape_3d(0, 0, 0)
shape2 = shape_3d(1, 1, 1)

shape1()
shape2()

