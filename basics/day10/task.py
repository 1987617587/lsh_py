"""
# author Liu shi hao
# date: 2019/11/18 18:55
# file_name: task

"""


# 1、定义一个Person类，它包含数据成员age, name和gender。
# 从Person中派生一个类Employee,在新类中添加一个数据成员，存储个人的number.
# 再从Employee中派生一个类Executive,每个派生类都应该定义一个方法，来显示相关的信息（名称和类型，如”Fred Smith is an Employee”）。
# 编写一个列表，包含3个Executive对象，2个一般的Employee对象，然后显示它们的信息。
#
class Person:

    def __init__(self, age, name, gender) -> None:
        super().__init__()
        self.age = age
        self.name = name
        self.gender = gender


class Employee(Person):

    def __init__(self, age, name, gender, number) -> None:
        super().__init__(age, name, gender)
        self.number = number

    def show(self):
        print(f"{self.name} is an Employee")


class Executive(Employee):

    def show(self):
        print(f"{self.name} is an Executive")


list1 = [Executive(53, "李四", "男", "001"),
         Executive(43, "王五", "男", "011"),
         Executive(23, "赵月", "女", "006"),
         Employee(25, "张三", "男", "001"),
         Employee(29, "陈东", "男", "211")]


def show_all():
    for i in range(len(list1)):
        list1[i].show()


# show_all()
# 2、设计一个图书管理系统,基类为类Book,要求有书名和作者属性，
# 由Book类派生子类AudioBook(有声书，需要具有演说者属性)，
# 对于Book和AudioBook进行合理的属性及行为的抽象，
# 同时实现该类的控制台打印方法
#
class Book:

    def __init__(self, title, author) -> None:
        super().__init__()
        self.title = title
        self.author = author

        @property
        def title(self):
            return title

        @property
        def author(self):
            return author


class AudioBook(Book):

    def __init__(self, title, author, speaker, gender) -> None:
        super().__init__(title, author)
        self.speaker = speaker
        self.gender = gender

    def speak(self):
        print(f"下面请收听演说者{self.speaker}，{self.gender}，演说:{self.author}的作品<<{self.title}>>。")


a1 = AudioBook("老人与海", "欧内斯特·米勒尔·海明威", "张三", "男")


# a1.speak()
# 3、以点（Point）类为基类，重新定义矩形类和圆类Rectangle class and circle class。点为直角坐标点，矩形水平放置，由左下方的顶点和长宽定义。
# 圆由圆心和半径定义。派生类操作判断任一坐标点是在图形内，还是在图形的边缘上，还是在图形外。缺省初始化图形退化为点。
# 要求包括拷贝初始化方法。编程测试类设计是否正确。
#
class Point:

    def __init__(self, x, y) -> None:
        super().__init__()
        self.x = x
        self.y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(eval(str(value))) == int:
            self.__x = int(value)
        elif type(eval(str(value))) == float:
            self.__x = float(value)
        else:
            print("格式错误,无法画图！")
        pass

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(eval(str(value))) == int:
            self.__y = int(value)
        elif type(eval(str(value))) == float:
            self.__y = float(value)
        else:
            print("格式错误,无法画图！")
        pass


class Rectangle(Point):

    def __init__(self, x, y, length, width) -> None:
        super().__init__(x, y)
        self.length = length
        self.width = width

    @property
    def length(self):
        return self.__length

    @length.setter
    def length(self, value):
        if type(eval(str(value))) == int:
            self.__length = int(value)
        elif type(eval(str(value))) == float:
            self.__length = float(value)
        else:
            print("格式错误,无法画出矩形！")
        pass

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(eval(str(value))) == int:
            self.__width = int(value)
        elif type(eval(str(value))) == float:
            self.__width = float(value)
        else:
            print("格式错误,无法画出矩形！")
        pass

    def judge(self, r_x, r_y):
        j1 = r_x - self.x
        j2 = r_y - self.y
        j3 = self.width+self.y - r_y
        j4 = self.length+self.x - r_x
        if min(j1,j2,j3,j4)==0:
            print("在矩形上")
        elif max(j1,j2,j3,j4) < self.length and max(j1,j2,j3,j4) < self.width:
            print("在矩形内")
        else:
            print("在矩形外")

class Circle(Point):

    def __init__(self, x, y,r) -> None:
        super().__init__(x, y)
        self.r = r
    @property
    def r(self):
        return self.__r

    @r.setter
    def r(self, value):
        if type(eval(str(value))) == int:
            self.__r = int(value)
        elif type(eval(str(value))) == float:
            self.__r = float(value)
        else:
            print("格式错误,无法画出圆！")
        pass
    def judge(self, r_x, r_y):

        if (r_x - self.x) ** 2 + (r_y - self.y) ** 2  == self.r**2:
            print("在圆上")
        elif (r_x - self.x) ** 2 + (r_y - self.y) ** 2 < self.r**2:
            print("在圆内")
        else:
            print("在圆外")

# c1 = Circle(0,0,2)
# c1.judge(2,1)
# r1 = Rectangle(0,0,3,4)
# r1.judge(3,1)
# 4、对平面形体有长和面积，周长、面积应怎样计算（用什么方法）?要求实现运行时的多态性。请编程，并测试。
# Shape
# 正方形(Square) 长方形(Rectangle) 圆形(Circle) 圆环(Annulus)
#
import math


class Shape:
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def perimeter(self):
        pass


class Square(Shape):

    def __init__(self, name, length, area) -> None:
        super().__init__(name)
        self.length = length
        self.area = area

    def perimeter(self):
        w = self.area / self.length
        perimeter = 2 * (w + self.length)
        print(f"{self.name}的周长是{perimeter}")


class Rectangle(Square):
    pass


class Circle(Shape):

    def __init__(self, name, length, area) -> None:
        super().__init__(name)
        self.length = length
        self.area = area

    def perimeter(self):
        perimeter = 2 * self.length * math.pi
        print(f"{self.name}的周长是{perimeter}")

class Annulus(Circle):

    def perimeter(self):
        perimeter = 2 * (self.area /self.length )
        print(f"{self.name}的周长是{perimeter}")


class Count:
    def change(self, shape: Shape):
        print(f"切换图形到{shape.name}")
        shape.perimeter()

s1 = Count()
s1.change(Rectangle("正方形",2,4))


# 5、某公司雇员（Employee）包括经理（Manager），技术人员（Technician）和销售员（Salesman）。以Employee类为基类派生出Manager，Technician和Salesman类；Employee类的属性包括姓名、职工号、工资级别，月薪（实发基本工资加业绩工资）。操作包括月薪计算方法（pay()），该方法要求输入请假天数，扣去应扣工资后，得出实发基本工资。
# Technician类派生的属性有每小时附加酬金和当月工作时数，及研究完成进度系数。业绩工资为三者之积。也包括同名的pay()方法，工资总额为基本工资加业绩工资。
# Salesman类派生的属性有当月销售额和酬金提取百分比，业绩工资为两者之积。也包括同名的pay()方法，工资总额为基本工资加业绩工资。
# Manager类派生属性有固定奖金额和业绩系数，业绩工资为两者之积。工资总额也为基本工资加业绩工资。编程实现工资管理。