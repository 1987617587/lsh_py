# author:lzt
# date: 2019/11/21 9:14
# file_name: day12_task
# 1.
# 定义一个人的类（属性有名字，年龄，编号（类属性）。写一个能输出各个属性值的方法show_info（）），
# 定义一个学生类（属性有性别），学生继承人类
# 要求：
# （1）父类的属性由父类的初始化方法完成
# （2）子类的属性一部分由父类初始化，一部分自己初始化
# （3）在子类中重写父类的show_info（）方法
# （4）声明学生类的对象，调用学生的显示信息的方法。
# （5）编号需要自动生成，从1开始，随对象数目增加而自动增长。
from typing import Any


class Person:
    num = 0

    def __init__(self, name, age) -> None:
        super().__init__()
        self.name = name
        self.age = age
        Person.num += 1

    def show_info(self):
        print(f"{self.name} {self.age} {Person.num}")


class Student(Person):

    def __init__(self, name, age, gender) -> None:
        super().__init__(name, age)
        self.gender = gender
        self.stu_num = Person.num

    def show_info(self):
        super().show_info()
        print(f"{self.gender} {self.stu_num}")


# s1 = Student("stu1", 19, "女")
# s2 = Student("stu2", 19, "女")
# s3 = Student("stu3", 19, "女")
# s4 = Student("stu4", 19, "女")
# s5 = Student("stu5", 19, "女")
# s1.show_info()
# s2.show_info()
# s3.show_info()
# s4.show_info()
# s5.show_info()
#
# 2.
# 定义Animal抽象类，含有属性name，gender，age，对象方法sleep，run，
# 编写一个子类Person，继承Animal类，然后调用父类的属性和方法
# 要求人类对象的数目在运行期间不能超过5个。
class Animal:

    def __init__(self, name, gender, age) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender

    def sleep(self):
        pass

    def run(self):
        pass


class Task2Person(Animal):
    _instance = []
    _count = -1
    _flag = False

    def __new__(cls, name, gender, age) -> Any:
        cls._count += 1
        if len(cls._instance) < 5:
            cls._instance.append(super().__new__(cls))
        return cls._instance[cls._count % 5]

    def __init__(self, name, gender, age) -> None:
        if not Task2Person._flag:
            super().__init__(name, gender, age)
            Task2Person._flag = True


print(id(Task2Person("", "", "")))
print(id(Task2Person("", "", "")))
print(id(Task2Person("", "", "")))
print(id(Task2Person("", "", "")))
print(id(Task2Person("", "", "")))
print("**********************")
print(id(Task2Person("", "", "")))
print(id(Task2Person("", "", "")))
print(id(Task2Person("", "", "")))
print(id(Task2Person("", "", "")))
print(id(Task2Person("", "", "")))
#
# 3.
# （1）父类Employee属性：name、sex ，company，boss
# （2）子类 Worker继承自Employee
# 属性：
# category;//类别
# dress_allowance; //是否提供服装津贴 ，
# 自定义方法 is_dress_all() 这个方法 负责通过判断dress_allowance的值输出是否提供服装津贴。
# 新建一个Worker对象，输出这个对象的所有属性
# 并调用is_dress_all()方法得到津贴信息
# 要求：所有员工共用两个属性：公司和老板
class Emp:
    company = "BAT"
    boss = "Ma"

    def __init__(self, name, sex) -> None:
        super().__init__()
        self.name = name
        self.sex = sex


class Worker(Emp):

    def __init__(self, name, sex, category, dress_allowance) -> None:
        super().__init__(name, sex)
        self.category = category
        self.dress_allowance = dress_allowance

    def is_dress_all(self):
        if self.dress_allowance:
            return 300
        return 0


# worker1 = Worker("xx1", "男", "技术员", False)
# print(worker1.is_dress_all())
#
#
# 4.
# 为“无名的粉”写一个类：
# class NamelessNoodles
# 要求：
# 1.有三个属性：
# 类别:category
# 粉的分量(两)：quantity
# 是否带汤：like_soup
# 所属店名（共享）
# 粉的名字（共用）
# 2. 重写初始化方法，以便于初始化过程可以多样化生成对象
# 如：
# f1 = NamelessNoodles("牛肉", 3, True);
# f2 = NamelessNoodles("牛肉", 2);
# 如何使得下列语句构造出来的粉对象是酸辣、2两、带汤的？
# f3 = NamelessNoodles();
class NamelessNoodles:
    name = "无名店"
    noodles = "无名粉"

    def __init__(self, category="酸辣", quantity=2, like_soup=True) -> None:
        super().__init__()
        self.category = category
        self.quantity = quantity
        self.like_soup = like_soup

    def __str__(self) -> str:
        return f"{NamelessNoodles.name}--{NamelessNoodles.noodles} {self.category},{self.quantity},{self.like_soup}"


# print(NamelessNoodles())
# print(NamelessNoodles(quantity=3))
#
#
# 5.
# 算法题：
# 进制转换
# n进制的转换
# 例如：
# 13换算为3进制=>111
# 13换算为5进制=>23
def parse(num, base_num):
    """
    进行进制转换
    :param num:数字
    :param base_num:进制数
    :return:转换后的字符串
    """
    ret = ""
    # 取商求余
    while num != 0:
        ret = "(" + str(num % base_num) + ")" + ret
        num = num // base_num
    return ret


print(parse(21, 11))
