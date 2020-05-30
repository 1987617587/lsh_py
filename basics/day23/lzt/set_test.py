# author:lzt
# date: 2019/12/4 14:39
# file_name: set_test

# 创建一个集合
set1 = {1, 1, 1, 1, 1, 1, 1, 2, 3, 4, 5}
print(set1)

# 通过类创建集合
set2 = set("12312312")
# print(set2)

# 添加数据
set2.add("12")
set2.add(12)
# set2.add([1, 2, 3])
# update可以追加可迭代的元素序列
set2.update([2, 3, 4])
print(set2)

try:
    # 删除
    # set2.remove("12")
    # set2.remove("12")
    set2.discard("12")
    set2.discard("12")
    set2.discard("12")
    print(set2)
except KeyError:
    print("删除错误！")

# 迭代
for i in set2:
    print(i)

# 某占座系统内 出现重复的占座现象 现在需要将两个班的同学合为一班 请问怎么去掉重复的同学:
stus1 = {"001", "003", "002", "004"}
stus2 = {"001", "002", "003"}
print(stus1 | stus2)

# 请问哪些同学重复了?
print(stus1 & stus2)

# 若stus去掉重复的学生后剩余哪些学生?
print(stus1 - stus2)
print(stus2 - stus1)

# stus1中是否包含stus2
print(stus2.issubset(stus1))

# 询问某集合中是否含有某集合中的所有元素
print(stus1.issuperset(stus2))


# 集合如何完成去重！
# 不可变类型去重：数据相同即为重复！！！
# 1 1 1
# "123" "123"

# 可变类型的去重:对象去重:__eq__ __hash__
class Student:

    def __init__(self, name, age, pid) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.pid = pid

    def __str__(self) -> str:
        return f"{self.name} {self.age} {self.pid}"

    # obj1.__eq__(obj2)
    def __eq__(self, o) -> bool:
        return self.pid == o.pid

    def __hash__(self):
        return self.pid.__hash__()


stus = {
    Student("002", 19, "121xxxxx"),
    Student("003", 23, "121xxxxx"),
    Student("002", 21, "121xxxxx")
}

for i in stus:
    print(i)
