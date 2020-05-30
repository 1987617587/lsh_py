"""
# author Liu shi hao
# date: 2019/11/20 17:14
# file_name: day12_task

"""

# 1.
# 定义一个人的类（属性有名字，年龄，编号（类属性）。写一个能输出各个属性值的方法show_info（）），
# 定义一个学生类（属性有性别），学生继承人类
# 要求：
# （1）父类的属性由父类的初始化方法完成
# （2）子类的属性一部分由父类初始化，一部分自己初始化
# （3）在子类中重写父类的show_info（）方法
# （4）声明学生类的对象，调用学生的显示信息的方法。
# （5）编号需要自动生成，从1开始，随对象数目增加而自动增长。
#

from typing import Any


class Person:
    num = 0

    def __init__(self, name, age) -> None:
        super().__init__()
        self.name = name
        self.age = age
        Person.num += 1

    def show_info(self):
        print(f"名字:{self.name}，年龄:{self.age}，编号:{Person.num}。")


class Student(Person):

    def __init__(self, name, age, gender) -> None:
        super().__init__(name, age)
        self.gender = gender
        self.num = Person.num

    def show_info(self):
        print(f"名字:{self.name}，性别:{self.gender}，年龄:{self.age}，编号:{self.num}。")


s1 = Student("张三", "男", 18)
s2 = Student("李四", "男", 18)


s1.show_info()
s2.show_info()


# 2.
# 定义Animal抽象类，含有属性name，gender，age，对象方法sleep，run，
# 编写一个子类Person，继承Animal类，然后调用父类的属性和方法
# 要求人类对象的数目在运行期间不能超过5个。
#
class Animal:
    def __init__(self, name, gender, age) -> None:
        super().__init__()
        self.name = name
        self.gender = gender
        self.age = age

    def sleep(self):
        pass

    def run(self):
        pass


class Preson(Animal):
    _instance = []
    _flag = -1

    def __new__(cls, name, gender, age) -> Any:
        cls._flag += 1
        if len(cls._instance)< 5:
            cls._instance.append(super().__new__(cls))
        return cls._instance[cls._flag% 5]

    def __init__(self, name, gender, age) -> None:
        if Preson._flag<5:
            super().__init__(name, gender, age)

    def __str__(self) -> str:
        return f"{self.name} {self.gender} {self.age}"


p1 = Preson("1", "男", 18)
p2 = Preson("2", "男", 18)
p3 = Preson("3", "男", 18)
p4 = Preson("4", "男", 18)
p5 = Preson("5", "男", 18)
p6 = Preson("6", "男", 18)
p7 = Preson("7", "男", 18)
print(id(p1))
print(id(p6))
print(id(p7))
print(p6)
print(p1)


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
#
class Employee:
    company = "京东"
    boss = "刘强东"

    def __init__(self, name, sex) -> None:
        super().__init__()
        self.name = name
        self.sex = sex


class Worker(Employee):

    def __init__(self, name, sex, category, dress_allowance) -> None:
        super().__init__(name, sex)
        self.category = category
        self.dress_allowance = dress_allowance

    def is_dress_all(self):
        if self.dress_allowance == "是" or "1":
            return " 提供服装津贴"
        return "不提供服装津贴"
        pass

    def __str__(self) -> str:
        return f"{self.company} {self.boss} {self.name} {self.sex} {self.category} {self.dress_allowance}"


w1 = Worker("小王", "男", "黄种人", "1")
# print(w1)
print(w1.is_dress_all())


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
#
class NamelessNoodles:
    name = "无名街霸粉"
    shop_name = "天下无名"
    _instance = 0

    def __init__(self, category="酸辣", quantity=2, like_soup=True) -> None:
        super().__init__()

        self.category = category
        self.quantity = quantity
        self.like_soup = like_soup

    def __str__(self) -> str:
        return f"{self.category}, {self.quantity}两，带汤" if self.like_soup else f"{self.category},{self.quantity}两，不带汤"


f1 = NamelessNoodles("牛肉", 3, True)
f2 = NamelessNoodles("牛肉", 2)
f3 = NamelessNoodles()
print(f1)
print(f2)
print(f3)


# print(f3.make())
#
# 5.
# 算法题：
# 进制转换
# n进制的转换
# 例如：
# 13换算为3进制=>111
# 13换算为5进制=>23
def in_int_n():
    while True:
        num = input("请输入要转换的n进制n(暂支持36进制):")
        if num.isdigit():
            return int(num)
        print("重新输入！")


def in_int_m():
    while True:
        num = input("请输入要转换整数m:")
        if num.isdigit():
            return int(num)
        print("重新输入！")


def conversion_base():
    m = in_int_m()
    n = in_int_n()
    str1 = ""
    while m != 0:
        if m % n >n:
            str1 =  str(chr(m % n+55))  + str1
        # str1 = "|"+str(m % n) +"|"+ str1  # 取余数，按位数累加到字符串
        else:
            if m % n > 9:
                str1 = str(chr(m % n + 55)) + str1
            else:
                str1 = str(m % n)  + str1
        m = m // n  # 取商做下一次的除数
    return str1


# def conversion_base():
#     m = in_int_m()
#     n = in_int_n()
#     str1 = ""
#     while m != 0:
#         str1 = "|"+str(m % n) +"|"+ str1  # 取余数，按位数累加到字符串
#         m =m// n  # 取商做下一次的除数
#     return str1

print(conversion_base())
