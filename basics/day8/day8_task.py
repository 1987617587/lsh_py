"""
# author Liu shi hao
# date: 2019/11/14 17:11
# file_name: day8_task

"""

# 1.尝试写一个学员类，想一想都应该有些什么变量和方法，并产生5个对象来表示你自己及身边的四位同学吧，
# 你觉得程序中的对象和你们是什么关系？学员类和你们又是什么关系？


import math


class Students:
    # 成员变量：姓名，性别，年龄，电话
    def __init__(self, name, age, sex, tel) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.sex = sex
        self.tel = tel

    # 成员方法 ：交流，学习，吃饭，睡觉
    def exchange(self):
        print(f"{self.name}交流")

    def study(self):
        print(f"{self.name}学习")

    def eat(self):
        print(f"{self.name}吃饭")

    def sleep(self):
        print(f"{self.name}睡觉")


stu1 = Students("诸葛", 23, "男", 1991)
stu2 = Students("张良", 24, "男", 1992)
stu3 = Students("孙膑", 23, "男", 1993)
stu4 = Students("鬼谷子", 21, "男", 1994)
stu5 = Students("吴用", 20, "男", 1995)


# stu5.study()
# 2.员工类：属性：名字、工号、部门、工资 方法：涨工资
#
class Employee:

    def __init__(self, name, job_number, department, salary) -> None:
        super().__init__()
        self.name = name
        self.job_number = job_number
        self.department = department
        self.salary = salary

    def pay_rise(self):
        self.salary *= 1.5


# 3.电脑类：属性：牌子，主板，cpu，内存，显示器，显卡等，方法：运行
#
class Computer:

    def __init__(self, brand, motherboard, cpu, memory, monitor, video_card) -> None:
        super().__init__()
        self.brand = brand
        self.motherboard = motherboard
        self.cpu = cpu
        self.memory = memory
        self.monitor = monitor
        self.video_card = video_card

    def operation(self):
        print(f"{self.cpu}CPU运行")


# 4.设计一个游戏角色类
#    属性:角色名、血量、魔法、状态
#    方法:释放技能 被伤害
#    要求:设计要合理
#
class Gamerole:

    def __init__(self, name, health, magic, state) -> None:
        super().__init__()
        self.name = name
        self.health = health
        self.magic = magic
        self.state = state

    def release_skills(self):
        while self.state == 0:
            self.health -= 50
            print("正在被伤害")
        else:
            return

    def be_hurt(self):
        while self.state == 1:
            print("正在释放技能")
        else:
            return


# 5.Lader类具有类型为浮点数的上底、下底、高、面积属性，具有返回面积的功能，
# 包括一个初始化方法对上底、下底、高进行初始化。
# Circle类具有类型为浮点型的半径、周长和面积属性，具有返回周长、面积的两个方法，
# 包括一个初始化方法对半径进行初始化。测试类Lader和类Circle的功能。
#
class Lader:

    def __init__(self, upper_base, lower_base, height) -> None:
        super().__init__()
        self.upper_base = upper_base
        self.lower_base = lower_base
        self.height = height

    def area(self):
        area = (self.upper_base + self.lower_base) * self.height / 2
        return area


lader1 = Lader(1, 2, 2)


# print(f"该梯形面积为：{lader1.area()}")


class Circle:

    def __init__(self, r) -> None:
        super().__init__()
        self.r = r

    def area(self):
        area = self.r ** 2 * math.pi
        return area

    def circumference(self):
        circumference = self.r * 2 * math.pi
        return circumference


circle1 = Circle(1)


# print(f"该圆的周长为：{circle1.circumference()}，面积为：{circle1.area()}。")

# 6.定义一个人类Person：
# 1)定义一个方法say_hello()，可以向对方发出问候语“hello,my name is XXX”
# 2)有三个属性：名字、身高、体重
# 3)通过初始化方法，分别给三个属性赋值
# 4)测试:
# 1、创建两个对象，分别是zhangsan，1.73，55；lishi，1.80，65
# 2、分别调用对象的say_hello()方法。
#
class Person:

    def __init__(self, name, height, weight) -> None:
        super().__init__()
        self.name = name
        self.height = height
        self.weight = weight

    def say_hello(self):
        print(f"hello,my name is {self.name}")


man1 = Person("zhangsan", 1.73, 55)
man2 = Person("lisi", 1.80, 65)


# man1.say_hello()
# man2.say_hello()
# 7.
# 定义一个矩形类Rectangle：
# 1)定义三个方法：get_area()求面积、get_per()求周长，show_all()输出长、宽、面积、周长。
# 2)有2个属性：长length、宽width
# 3)通过初始化方法分别给两个属性赋值
#
class Rectangle:

    def __init__(self, length, width) -> None:
        super().__init__()
        self.length = length
        self.width = width

    def get_area(self):
        return self.length * self.width

    def get_per(self):
        return sum(self.length, self.width) * 2

    def show_all(self):
        print(f"长:{self.length}、宽:{self.width}、面积:{self.length * self.width}、周长;{(self.length + self.width) * 2}")


rectangle1 = Rectangle(2, 8)


# print(rectangle1.get_area())
# print(rectangle1.get_per())
# rectangle1.show_all()

#
# 8.
# 定义一个普通用户类
# 普通用户类具备的属性：用户名、密码、权限
# 普通用户类具备的方法：登录、注册
#
# 注意：请详细测试该类
#
class User:

    def __init__(self, user_name=None, password=None, permission=None) -> None:
        super().__init__()
        self.user_name = user_name
        self.password = password
        self.permission = permission

    def register(self):
        i = 0
        self.user_name = input("请输入要注册用户名：")
        self.password = input("请输入密码：")
        an = input("请选择权限(1,管理员  2,用户)：")
        if an == "1":
            while i < 3:
                in_admin_psw = input("请输入管理员密码：")
                if in_admin_psw == "666666":
                    self.permission = "管理员"
                    print("注册管理员成功，正在返回登录！")
                    break
                else:
                    i += 1
                    if i == 3:
                        print("注册管理员失败！")
                        self.permission = "普通用户"
                        break
                    print(f"管理员密码输入错误！您还有{3 - i}次机会！")
        else:
            self.permission = "普通用户"
            print("注册成功，正在返回登录！")

    def login(self):
        for i in range(3):
            user_name = input("请输入用户名：")
            password = input("请输入密码：")
            if user_name != self.user_name or self.password != password:
                print(f"用户名或密码输入有误，请重新输入，您还有{2 - i}次机会。") if i != 2 else print("您三次输入都有误，请与管理员联系")
            else:
                print("登录成功!")
                return self.user_name, self.password, self.permission

    # def exit(self):
    #     an = input("是否确人退出登录(y/n)：")
    #     if an == "y":
    #


# user1 = User()
# user1.register()
# print(user1.login())


# user1 = User()
# user1.register()
# user1.login()   # 登录成功之后，退出类，再次登录无法登录。
# print(user1.login())  # 登录成功之后，不退出类，直接再次登录登录成功。


class Users:

    def __init__(self, user_name, password, pri) -> None:
        super().__init__()
        self.user_name = user_name
        self.password = password
        self.pri = pri

    def login(self, user_name, password):
        return self.user_name == user_name and self.password == password

    def register(self, user_name, password, pri):
        self.user_name = user_name
        self.password = password
        self.pri = pri


# 准备数据库中的对象列表
users = \
    [
        Users("asd", "121", "admin"),
        Users("user1", "121", "admin"),
        Users("user1", "121", "user"),
        Users("user1", "121", "user"),
        Users("user1", "121", "user"),
    ]

# 模拟前端验证
# 模拟登录
for j in range(3):
    user_name = input("用户名：")
    password = input("密 码：")
    # 匹配数据库中对象信息
    user_login = None
    for i in range(len(users)):
        if users[i].login(user_name, password):
            print("登录成功！")
            user_login = users[i]
            break
    else:
        print(f"用户名或密码输入有误，请重新输入，您还有{2 - j}次机会。") if j != 2 else print("您三次输入都有误，请与管理员联系")

    if user_login is not None:
        break
# 模拟前端注册
# 模拟注册
register_user = Users(None,None,None)
user_name = input("注册用户名：")
while 1:
    password = input("注册密码：")
    re_password = input("请重复密码：")
    if password != re_password:
        print("两次输入不一致，请重新设定密码！")
        continue
    break
# 管理员注册验证
pri = input("请选择权限(1,管理员  2,用户)：")
i = 0

if pri == "1":
    while i < 3:
        in_admin_psw = input("请输入管理员密码：")
        if in_admin_psw == "666666":
            pri = "管理员"
            print("注册管理员成功，正在返回登录！")
            break
        else:
            i += 1
            if i == 3:
                print("注册管理员失败！")
                pri = "普通用户"
                break
            print(f"管理员密码输入错误！您还有{3 - i}次机会！")
else:
    pri = "普通用户"
    print("注册成功，正在返回登录！")

# 产生用户对象
register_user.register(user_name,password,pri)
# 注册成功的对象存入数据库
users.append(register_user)
# 遍历数据库，验证注册是否成功
for i in range(len(users)):
    print(f"用户名:{users[i].user_name} 密码:{users[i].password} 权限:{users[i].pri}")
# 9.
# 编写一个时间类My_Time，包含一个三个参数的初始化方法，3个属性hour,minute,second,
# 再加上一个转换成字符串的方法to_string。
#
# 注意：请注意时分秒的取值范围
#
class MyTime:

    def __init__(self, hour, minute, second) -> None:
        super().__init__()
        self.hour = hour
        self.minute = minute
        self.second = second

    def to_string(self):
        if 0 <= self.hour <= 23 and 0 <= self.minute <= 59 and 0 <= self.second <= 59:
            return str(self.hour) + "时" + str(self.minute) + "分" + str(self.second) + "秒"
        else:
            print(f"时间格式错误，无法转换！")
            return False


my_time1 = MyTime(1, 6, 43)


# print(my_time1.to_string())
#
# 10.
# 编写一个日期类My_Date，包含一个初始化方法，3个属性year,month,day，
# 再加上一个转换成字符串的方法to_string。
# 请注意月和日的取值范围
#
class MyDate:

    def __init__(self, year, month, day) -> None:
        super().__init__()
        self.year = year
        self.month = month
        self.day = day

    def to_string(self):  # 创建闰年，平年月份对应天数列表
        list_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        list_common_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.year > 0 and 0 < self.month <= 12 and self.day > 0:
            if (self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0) and \
                    self.day > list_leap_year[self.month - 1] or self.year % 4 != 0 and \
                    self.day > list_common_year[self.month - 1]:
                print(f"时间格式错误，无法转换！")
                return False
            else:
                return str(self.year) + "年" + str(self.month) + "月" + str(self.day) + "日"
        else:
            print(f"时间格式错误，无法转换！")
            return False


my_date1 = MyDate(2000, 2, 29)
print(my_date1.to_string())


#
# 11.
# 模拟简单的计算器。
# 定义名为Number的类，其中有两个整型数据对象n1和n2，声明为公有。
# 编写初始化方法，赋予n1和n2初始值，
# 再为该类定义加（addition）、减（subtration）、乘（multiplication）、除（division）等公有对象方法，
# 分别对两个属性执行加、减、乘、除的运算。
# 创建Number类的对象，调用各个方法，并显示计算结果。

class Number:

    def __init__(self, n1, n2) -> None:
        super().__init__()
        self.n1 = n1
        self.n2 = n2

    def addition(self):
        num_add = self.n1 + self.n2
        return num_add

    def minus(self):
        num_minus = self.n1 - self.n2
        return num_minus

    def multiplication(self):
        num_mul = self.n1 * self.n2
        return num_mul

    def division(self):
        if self.n1 == 0 or self.n2 == 0:
            print("无法执行除运算！")
            return False
        else:
            division = self.n1 / self.n2
            return division


num1 = Number(1, 2)
# print(num1.addition())
# print(num1.division())
# print(num1.multiplication())
# print(num1.minus())
