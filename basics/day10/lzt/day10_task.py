# author:lzt
# date: 2019/11/19 10:13
# file_name: day10_task

# 1、定义一个Person类，它包含数据成员age, name和gender。
# 从Person中派生一个类Employee,在新类中添加一个数据成员，存储个人的number.
# 再从Employee中派生一个类Executive,每个派生类都应该定义一个方法，
# 来显示相关的信息（名称和类型，如”Fred Smith is an Employee”）。
# 编写一个列表，包含3个Executive对象，2个一般的Employee对象，然后显示它们的信息。
import math


class Person:
    def __init__(self, age, name, gender) -> None:
        # age, name和gender
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender

    def show(self):
        print(f"{self.name} is a Person")


class Employee(Person):

    def __init__(self, age, name, gender, number) -> None:
        super().__init__(age, name, gender)
        self.number = number

    def show(self):
        print(f"{self.name} is an Employee")


class Executive(Employee):

    def show(self):
        print(f"{self.name} is an Executive")


# 测试写的员工类
# emps = \
#     [
#         Executive(19, "exe1", "男", 1001),
#         Executive(21, "exe2", "男", 1002),
#         Executive(20, "exe3", "男", 1003),
#         Employee(22, "emp1", "男", 1000),
#         Employee(23, "emp2", "女", 1001)
#     ]
#
# for i in range(len(emps)):
#     emps[i].show()
#
# 2、设计一个图书管理系统,基类为类Book,要求有书名和作者属性，
# 由Book类派生子类AudioBook(有声书，需要具有演说者属性)，
# 对于Book和AudioBook进行合理的属性及行为的抽象，同时实现该类的控制台打印方法
class Book:

    def __init__(self, book_name, author) -> None:
        super().__init__()
        self.__book_name = book_name
        self.__author = author

    @property
    def book_name(self):
        return self.__book_name

    @property
    def author(self):
        return self.__author


class AudioBook(Book):

    def __init__(self, book_name, author, speaker) -> None:
        super().__init__(book_name, author)
        self.speaker = speaker

    @property
    def speaker(self):
        return self.__speaker

    @speaker.setter
    def speaker(self, value):
        self.__speaker = value
        pass


#
# 3、以点（Point）类为基类，重新定义矩形类和圆类。
# 点为直角坐标点，矩形水平放置，由左下方的顶点和长宽定义。
# 圆由圆心和半径定义。派生类操作判断任一坐标点是在图形内，
# 还是在图形的边缘上，还是在图形外。缺省初始化图形退化为点。
# 要求包括拷贝初始化方法。编程测试类设计是否正确。
class Point:

    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def distance(self, other_point):
        """
        判断某一点的位置是否在图形上、外、中
        :param other_point:平面图形上任意一点
        :return:0:图形上 1：图形外 -1：图形中
        """
        pass


class Rec(Point):

    def __init__(self, x, y, w, h) -> None:
        super().__init__(x, y)
        self.w = w
        self.h = h

    def distance(self, other_point: Point):
        if other_point.x < self.x or other_point.x > self.x + self.w \
                or other_point.y < self.y or other_point.y > self.y + self.h:
            return 1
        elif self.x < other_point.x < self.x + self.w and self.y < other_point.y < self.y + self.h:
            return -1
        else:
            return 0


class Circle(Point):

    def __init__(self, x, y, r) -> None:
        super().__init__(x, y)
        self.r = r

    def distance(self, other_point):
        c_o = (other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2
        if c_o > self.r ** 2:
            return 1
        elif c_o < self.r ** 2:
            return -1
        else:
            return 0


# sk_rec = Rec(0, 0, 5, 5)
# role_pos = Point(0, 3)
# print("未命中" if sk_rec.distance(role_pos) == 1
#       else ("命中" if sk_rec.distance(role_pos) == -1 else "边缘特效命中"))
# sk_circle = Circle(0, 0, 3)
# role_pos = Point(0, 4)
# print("未命中" if sk_circle.distance(role_pos) == 1
#       else ("命中" if sk_circle.distance(role_pos) == -1 else "边缘特效命中"))


#
# 4、对平面形体有长和面积，周长、面积应怎样计算（用什么方法）?要求实现运行时的多态性。请编程，并测试。
# Shape
# 正方形(Square) 长方形(Rectangle) 圆形(Circle) 圆环(Annulus)
class Shape:
    def area(self):
        pass

    def per(self):
        pass


class Square(Shape):

    def __init__(self, side) -> None:
        super().__init__()
        self.side = side

    def area(self):
        return self.side ** 2

    def per(self):
        return 4 * self.side


class Annulus(Shape):

    def __init__(self, inner_r, outer_r) -> None:
        super().__init__()
        self.inner_r = inner_r
        self.outer_r = outer_r

    def area(self):
        return math.pi * (self.outer_r ** 2 - self.inner_r ** 2)

    def per(self):
        return 2 * math.pi * (self.outer_r + self.inner_r)


# shapes = [Square(5), Square(6), Annulus(1, 3), Square(10)]
#
# for i in range(len(shapes)):
#     print(shapes[i].area())
#     print(shapes[i].per())
#
# 5、某公司雇员（Employee）包括经理（Manager），技术人员（Technician）和销售员（Salesman）。
# 以Employee类为基类派生出Manager，Technician和Salesman类；
# Employee类的属性包括姓名、职工号、工资级别，月薪（实发基本工资加业绩工资）。
# 操作包括月薪计算方法（pay()），该方法要求输入请假天数，扣去应扣工资后，得出实发基本工资。
# Technician类派生的属性有每小时附加酬金和当月工作时数，及研究完成进度系数。业绩工资为三者之积。也包括同名的pay()方法，
# 工资总额为基本工资加业绩工资。
# Salesman类派生的属性有当月销售额和酬金提取百分比，业绩工资为两者之积。也包括同名的pay()方法，
# 工资总额为基本工资加业绩工资。
# Manager类派生属性有固定奖金额和业绩系数，业绩工资为两者之积。工资总额也为基本工资加业绩工资。编程实现工资管理。
class Employee:

    def __init__(self, name, empno, salary_level, salary) -> None:
        super().__init__()
        # 姓名、职工号、工资级别，月薪
        self.name = name
        self.empno = empno
        self.salary_level = salary_level
        self.salary = salary

    def pay(self, days):
        return self.salary - self.salary / 30 * days


class Manager(Employee):

    def __init__(self, name, empno, salary_level, salary, bonus, percent) -> None:
        super().__init__(name, empno, salary_level, salary)
        self.bonus = bonus
        self.percent = percent

    def pay(self, days):
        return super().pay(days) + self.bonus * self.percent


class Technician(Employee):

    def __init__(self, name, empno, salary_level, salary, reward_by_hour, hours, percent) -> None:
        super().__init__(name, empno, salary_level, salary)
        self.reward_by_hour = reward_by_hour
        self.hours = hours
        self.percent = percent

    def pay(self, days):
        return super().pay(days) + self.reward_by_hour * self.hours * self.percent


class Salesman(Employee):

    def __init__(self, name, empno, salary_level, salary, sales, percent) -> None:
        super().__init__(name, empno, salary_level, salary)
        self.sales = sales
        self.percent = percent

    def pay(self, days):
        return super().pay(days) + self.sales * self.percent


emps = [
    Manager("m1", "001", 3, 35000, 50000, 0.9),
    Manager("m2", "002", 3, 25000, 20000, 0.9),
    Technician("t1", "0001", 2, 15000, 20, 160, 0.95),
    Technician("t2", "0002", 2, 12000, 20, 140, 0.8),
    Salesman("s1", "01", 1, 5000, 150000, 0.01)
]

for i in range(len(emps)):
    print(emps[i].pay(0))
