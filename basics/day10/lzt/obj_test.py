# author:lzt
# date: 2019/11/19 14:23
# file_name: obj_test
# == vs is
# ==：对于不可变的类型 直接比较其数据内容
# a = "abc"
# b = "abc"
# print(a == b)

# is:id(数据量):尽量在None值的判断上使用
# def show_id():
#     print(id("1"))
#     print(id(400))
#
# print(id("1"))
# print(id(400))
# show_id()

# 可变类型的比较：
# ==:若重写了__eq__ 那么比较的结果取决于方法的返回值
# 若未重写 那么将比较两个对象的地址
class Student(object):
    """
    学生类
    """

    def __init__(self, name, age) -> None:
        """
        这个是学生的初始化方法
        :param name:学员名字
        :param age:学员年龄
        """
        super().__init__()
        self.name = name
        self.age = age

    # 若__eq__这个魔法方法未重写：默认用object里的方法：和is效果相同
    # 对==做运算符重载
    def __eq__(self, o) -> bool:
        # self vs o
        return self.name == o.name and self.age == o.age

    def __gt__(self, other):
        return self.age > other.age

    def __str__(self) -> str:
        return f"学员名:{self.name} 年龄:{self.age}"


# s1 = Student("001", 21)
# s2 = Student("001", 19)
# print(s1 == s2)
# print(s1 > s2)
# print(s1.__class__)
# print(s1.__dir__())
# print(s1.__init__.__doc__)
# print(s1)
# print(s2)
# s2 = s1
# print(id(s1),id(s2))
# print(s1 == s2)
# print(s1 is s2)

class Animal:
    def __init__(self, type_name) -> None:
        super().__init__()
        self.type_name = type_name

    def eat(self):
        print("动物吃")


class Dog(Animal):
    def play(self):
        print("狗狗玩耍")


class Cat(Animal):
    def catch_mouse(self):
        print("猫捉老鼠")


# 保证代码的健壮性：功能调用前的类型辨识
def do_action(an):
    # if isinstance(an,Animal):
    if type(an) is Animal:
        an.eat()
    elif an.__class__ is Dog:
        an.play()
    else:
        an.catch_mouse()


# do_action(Dog("狗"))
# do_action(Cat("猫"))
# do_action(Animal("动物"))

# 规定传参的参数的类型必须为某种类别
def feed(an):
    if issubclass(type(an), Animal):
        an.eat()
    else:
        print("养不起")


# feed(Dog("狗"))
# feed(Animal("动物"))
# feed(Student("111", 19))

# 有啥用啥?
def show_obj(obj):
    # 显示所有obj中可用的内容:dir(obj)
    # print(dir(obj))
    if "type_name" in dir(obj):
        print(obj.type_name)
    if hasattr(obj, "play"):
        obj.play()
    if hasattr(obj, "catch_mouse"):
        obj.catch_mouse()


show_obj(Animal("animal"))
show_obj(Dog("狗"))
show_obj(Cat("猫"))
