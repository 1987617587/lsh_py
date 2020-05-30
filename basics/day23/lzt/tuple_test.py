# author:lzt
# date: 2019/12/4 10:27
# file_name: tuple_test
# 元组的创建
# 单元素时必须带,
# ()
t1 = (1,)
print(type(t1))

t2 = tuple((1, 2, 3))
# # print(t2[0])

# 元组的不可修改
t3 = (1, 2, 3, 4)


# 增加元素? err
# t3.__add__(10)

# 删除 err
# del t3[0]

# 插入？ err

# 修正数据
# 不可变类型 err
# t3[0] = 10

# 可变类型
class Student:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name


t_stus = (Student("小明"), Student("小红"))

# 不可改变对象的指向 err
# t_stus[0] = Student("小花")


# 可改变对象内部的数据
t_stus[0].name = "小花"

print(t_stus[0].name)

t_stus2 = t_stus
print(id(t_stus))
print(id(t_stus2))
