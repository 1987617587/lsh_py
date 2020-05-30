"""
# author Liu shi hao
# date: 2019/11/21 16:31
# file_name: day13_task

"""
import random


def in_int():
    while True:
        num = input("请输入整数：")
        if num.isdigit():
            return int(num)
        print("重新输入！")


# 1、建立一个汽车Auto类，包括轮胎个数，汽车颜色，车身重量、速度等成员变量。至少要求：
# 汽车能够加速，减速，停车。 再定义一个小汽车类Car，继承Auto，并添加空调、CD等成员变量，覆盖加速，减速的方法
#
class Auto:

    def __init__(self, tires_num, color, weight, speed) -> None:
        super().__init__()
        self.tires_num = tires_num
        self.color = color
        self.weight = weight
        self.speed = speed

    def speed_up(self):
        self.speed += 10

    def speed_down(self):
        if self.speed >= 5:
            self.speed -= 5

    def stop(self):
        self.speed = 0


class Car(Auto):

    def __init__(self, tires_num, color, weight, speed, air_cond, cd) -> None:
        super().__init__(tires_num, color, weight, speed)
        self.air_cond = air_cond
        self.cd = cd

    def speed_down(self):
        pass

    def speed_up(self):
        pass


# 2、定义一个"Role"类，有姓名，年龄，性别等成员变量
# 1） 要求封装所有属性。具有一个work()方法，该方法不返回任何值
# 2）从Role类派生出一个Employee类，并扩展 salary成员变量，还要求覆盖work()方法。
# 3） Manager类继承Employee类，有一个成员变量vehicle，还要求覆盖work()方法。
# 4）在测试中制造一个Role列表，放入2个Manager和3个Employee对象,统一让他们按照自己的工作方式开始工作
#
class Role:

    def __init__(self, name, age, gender) -> None:
        super().__init__()
        self._name = name
        self._age = age
        self._gender = gender

    @property
    def name(self):
        return self._name

    @property
    def age(self):
        return self._age

    @property
    def gender(self):
        return self._gender

    def work(self):
        pass


class Employee(Role):

    def __init__(self, name, age, gender, salary) -> None:
        super().__init__(name, age, gender)
        self._salary = salary

        @property
        def salary(self):
            return self._salary

    def work(self):
        print(f"员工{self.name}干活")


class Manager(Employee):

    def __init__(self, name, age, gender, salary, vehicle) -> None:
        super().__init__(name, age, gender, salary)
        self._vehicle = vehicle

    @property
    def vehicle(self):
        return self._vehicle

    def work(self):
        print(f"经理{self.name}指导工作")


list_role = [Manager("王经理", 34, "男", 12300, "BWM"),
             Manager("刘经理", 34, "男", 12300, "BWM"),
             Employee("小张", 34, "男", 4530),
             Employee("小李", 34, "男", 3230),
             Employee("小赵", 34, "男", 3600), ]

for i in range(len(list_role)):
    if type(list_role[i]) is Manager or Employee:
        list_role[i].work()


# 5、如何利用^对用户的密码进行加密和解密
#
def encrypt_decode():
    key = 123456
    pwd = in_int()
    encrypt_pwd = int(pwd) ^ key
    print(f"加密后的密码是：{encrypt_pwd}")
    decode_pwd = encrypt_pwd ^ key
    print(f"解密后的密码是：{decode_pwd}")


# encrypt_decode()


# 6、制作一个四位数字猜猜看小游戏
#    规则：3.1四个位置的数字(每一位都不重复)供用户输入
#             3.2若用户输入的不是4位数字请提示重新输入
#             3.3若数字和位置全对上得一个A
#             3.4若数字对了但是位置不对得一个B
#             3.5每轮为用户提示 XAXB 例如 1A3B即 4个数字都猜对了 但是只有一个数字的位置对了
#             3.6用户可以有9次机会
#             3.7机会用尽和猜对均提示用户是否继续还是结束退出？供用户选择
#             3.8若机会用尽请告知正确答案
#             3.9根据用户猜对所有次数为用户评定等级
#

def user_an():
    while 1:

        user_an = input("请输入不重复的4位数：")
        r_str = ""
        if user_an.isdigit():
            for i in range(len(user_an)):
                if user_an[i] not in r_str:
                    r_str += user_an[i]
            if len(r_str) == 4:
                return r_str


# user_an()


def an():
    while 1:

        r_str = ""
        for i in range(4):
            a = random.randint(0, 9)
            if str(a) not in r_str:
                r_str += str(a)
        if len(r_str) == 4:
            return r_str


# print(an())


def repeat_play():  # 定义重复玩函数
    while True:
        guess_nums()
        an = input("是否退出游戏？(y/n)")
        if an == "y":
            return False


def guess_nums():  # 猜数游戏
    i = 0
    game_answer = an()
    while i < 9:
        user_answer = user_an()

        print(f"答案{game_answer}")
        i += 1
        a, b = 0, 0
        if user_answer == game_answer:
            print(f"第{i}你猜中了,答案是{game_answer}")
            break
        for j in range(4):
            if user_answer[j] == game_answer[j]:
                a += 1
            else:
               if user_answer[j] in game_answer:
                    b += 1

        print(f"第{i}次你猜{user_answer},提示：{a}A{b }B")
    print(f"本轮随机答案为：{game_answer}")
    print(f"{i}次猜对，欧皇附体！") if i == 0 else print(f"{i}次猜对，运气真好！") \
        if i <= 4 else print(f"{i}次猜对，猜的不错！") if 9 > i > 5 else print(f"{i}次猜对，太及时了！") \
        if i == 10 else print("本次游戏未猜中，继续努力！")


# repeat_play()
# 7、计算1+22+33+44+…+nn的值  1 + 22 + 333 + 4444+ 55555+...nnnnnnn;
#
def func_7_1():
    n = in_int()
    sum = 1
    for i in range(2, n + 1):
        sum += i * 11
    return sum


# print(func_7_1())


def func_7_2():
    n = in_int()
    sum = 0
    for i in range(1, n + 1):
        sum += i * int("1" * i)
    return sum


# print(func_7_2())


# 8、我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？（百钱百鸡）
#
def is_the():
    for i in range(20):
        for j in range(33):
            for k in range(100):
                if i + j + k == 100 and 5 * i + 3 * j + k / 3 == 100:
                    # return f"鸡翁{i}、鸡母{j}、鸡雏{k}。"
                    print(f"鸡翁{i}、鸡母{j}、鸡雏{k}。")


# is_the()
# print(is_the())
# 9、编写小游戏
# a)	游戏中有一个玩家和3个AI（机器人）
# b)	玩家和每个机器人都有自己的生命值和攻击力；
# c)	玩家默认生命值600，机器人默认生命值为100；
# d)	玩家攻击力15，敌人攻击力为5；
# e)	游戏采用轮询方式；
# f)	每轮会一枚骰子，点数（1~6）；
# g)	所有参与者（玩家和每个AI）依次猜大小，无论是玩家还是机器人只要猜对就可以发动攻击
# i.	如果猜大，4~6是赢，1~3是输
# ii.	如果猜小，1~3是赢，4~6是输
# h)	只要玩家才对，那么玩家永远先手；如果猜不对，则才对的机器人按顺序执行；
# i)	战斗结束有以下几种情况：
# i.	玩家死亡
# ii.	敌人全部死亡
# j)	显示每一轮猜数的结果和答案，并显示每一轮过后玩家和AI的信息，显示最后的胜利是机器人一方还是玩家一方。
#
class Player:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self._hp = 100
        self._atk = 15
        self._state = True

    @property
    def hp(self):
        return self._hp


    @property
    def atk(self):
        return self._atk

    @property
    def state(self):
        return self._state

    def attack(self, player):
        pass

    # 受伤方法
    def be_hurt(self, hurt):
        if self._state:
            self._hp = 0 if self._hp - hurt < 0 else self._hp - hurt
            self._state = self._hp > 0
            print(f"{self.name}原有血量{self._hp + hurt}，收到伤害{int(hurt)}，剩余血量{int(self._hp )}")
        else:
            print("请尊重死者！")
            return

    def __str__(self) -> str:
        return self.name + " " + str(self._hp)


class User(Player):
    def __init__(self, name) -> None:
        super().__init__(name)

    def attack(self, player):
        if not self._state:
            print("请安息！")
            self._state = False
            return
        hurt = 15
        print(f"{self.name}打出伤害{hurt}")
        player.be_hurt(hurt)


class Ai(Player):
    def __init__(self, name) -> None:
        super().__init__(name)
        self._hp = 100

    def attack(self, player):
        if not self._state:
            print("请安息！")
            self._state = False
            return
        # 获取当前玩家的基础伤害值
        hurt = 15
        print(f"{self.name}打出伤害{hurt}")
        player.be_hurt(hurt)


user = User("玩家")
ai_1 = Ai("机器人一")
ai_2 = Ai("机器人二")
ai_3 = Ai("机器人三")


def pk_ai():
    while (ai_1.state and ai_2.state and ai_3.state )or user.state:
        count = random.randint(1, 6)
        count = 0 if count < 4 else 1
        player1_choice = random.randint(0, 1)
        ai_1_choice = random.randint(0, 1)
        ai_2_choice = random.randint(0, 1)
        ai_3_choice = random.randint(0, 1)
        if player1_choice == count and  user.state:
            if ai_1.state:
                user.attack(ai_1)
            if ai_2.state:
                user.attack(ai_2)
            if ai_3.state:
                user.attack(ai_3)
        if  not ai_1.state and not ai_2.state and  not ai_3.state or not user.state:
            break
        if ai_1.state and ai_1_choice ==count and  user.state:
            ai_1.attack(user)
        if ai_2.state and ai_2_choice ==count and user.state:
            ai_2.attack(user)
        if ai_3.state and ai_3_choice ==count and user.state:
            ai_3.attack(user)


    print("玩家 win" if user.state else "机器人 win")

pk_ai()
# 10、编写一个学生类：
# 学生类包括：
# 字段：名字、年龄、所属省份、所属市
# 属性：请封装上述字段
# 题目要求：
# 10.1编写一个学生列表，长度为3，放入不同省市的3个学生对象。名字和年龄自定义即可。
# 10.2写一个函数根据省份输出列表中该省份的所有学生信息。
# 10.3写一个函数根据所属市输出列表中该市的所有学生信息。
#
class Student:

    def __init__(self, name, age, province, city) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.province = province
        self.city = city

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value
        pass

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value <= 0:
            return
        else:
            self.__age = value
        pass

    @property
    def province(self):
        return self.__province

    @province.setter
    def province(self, value):
        self.__province = value
        pass

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value
        pass

    def __str__(self):
        return f"名字:{self.name} 年龄:{self.age} 所属省份:{self.province} 所属市:{self.city}。"


list_students = [Student("张三", 19, "河南", "郑州"),
                 Student("李四", 23, "浙江", "温州"),
                 Student("王五", 20, "新疆", "乌鲁木齐"),
                 ]


#
def province(arr: list):
    an = input("请输入要查询的省份：")
    for i in range(len(arr)):
        if type(arr[i]) is Student and an == arr[i].province:
            print(f"查询结果：{arr[i]}")


def city(arr: list):
    an = input("请输入要查询的市区：")
    for i in range(len(arr)):
        if type(arr[i]) is Student and an == arr[i].city:
            print(f"查询结果：{arr[i]}")


# province(list_students)
# city(list_students)


# 11、有n盏灯,放在一排,从1到n依次顺序编号，灯有开关两种状态.有m个人也从1到m依次顺序编号，灯默认全部关闭，第1个人（1号）将灯全部打开；
# 第2个人（2号）将凡是2的倍数的灯关闭；第3个人（3号）将凡是3的倍数的灯作相反处理（该灯如是打开的,则将它关闭；
# 如是关闭的,则将它打开）.以后的人都和3号一样,将凡是自己编号倍数的灯作相反处理.编写方法，传入第m个人操作后，返回亮着灯的序号的列表
#
def func_11():
    n = in_int()
    m = in_int()
    x = [1] * n
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if j % i == 0:
                x[j - 1] = x[j - 1] * -1
    for k in range(0, n):
        if x[k] == 1:
            print(f"第{ k + 1}号灯灭着")
        else:
            print(f"第{ k + 1}号灯亮着")


func_11()


# 12、（1）定义一个人类作为基类，有姓名、性别、年龄，再由基类派生出教师类和学生类，教师类增加工号、职称和工资，学生类增加学号、班级、专业和入学成绩;
# （2）创建一个列表存放3个学生和2名教师;
# （3）编写方法，传入参数是（2）创建的列表，返回工资最高的教师和成绩最好的学员。
# （4）打印出（3）返回的学员和教师信息。
#
class Person:

    def __init__(self, name, gender, age) -> None:
        super().__init__()
        self.name = name
        self.gender = gender
        self.age = age

    def highest(self, arr: list):
        pass


class Teacher(Person):

    def __init__(self, name, gender, age, t_num, title, salary) -> None:
        super().__init__(name, gender, age)
        self.t_num = t_num
        self.title = title
        self.salary = salary

    def __str__(self) -> str:
        return f"姓名{self.name}、性别{self.name}、年龄{self.age}、工号{self.t_num}、职称{self.title}、工资{self.salary}"


class Student(Person):

    def __init__(self, name, gender, age, s_num, class_num, major, ad_score) -> None:
        super().__init__(name, gender, age)
        self.s_num = s_num
        self.class_num = class_num
        self.major = major
        self.ad_score = ad_score

    def __str__(self) -> str:
        return f"姓名{self.name}、性别{self.name}、年龄{self.age}、学号{self.s_num}、班级{self.class_num}、专业{self.major}、入学成绩{self.ad_score}"


list_12 = [
    Student("xas", "男", 22, "001", "一班", "计算机", 78),
    Student("sdf", "男", 19, "003", "二班", "电子工程", 68),
    Student("khj", "男", 24, "007", "三班", "工商管理", 58),
    Teacher("lzt", "男", 30, "001", "讲师", 20000),
    Teacher("pxk", "女", 30, "002", "讲师", 18000)
]

r_list1 = []
r_list2 = []


def highest(arr: list):
    for i in range(len(arr)):
        if type(arr[i]) is Student:
            r_list1.append(arr[i].ad_score)
        if type(arr[i]) is Teacher:
            r_list2.append(arr[i].salary)
    s = max(r_list1)
    t = max(r_list2)
    for j in range(len(arr)):
        if type(arr[j]) is Student and s == arr[j].ad_score:
            print(f"最高成绩的学生信息：{arr[j]}")
        if type(arr[j]) is Teacher and t == arr[j].salary:
            print(f"最高工资的教师信息：{arr[j]}")


# highest(list_12)
# 13、程序中定义一个机器人类（Robot），该类中定一个静态数据成员__robot_count表示机器人人数，以及一个类方法get_count来访问该字段。
# 问题：如何做到机器人人数这个字段的值和产生的机器人对象数目保持一致。
#
from typing import Any


class Pobot:
    __robot_count = 0

    def __new__(cls) -> Any:
        cls.__robot_count += 1
        return super().__new__(cls)

    @classmethod
    def get_count(cls):
        print(cls.__robot_count)


# p1 = Pobot()
# p2 = Pobot()
# p3 = Pobot()
# Pobot.get_count()


# 14、求以下表达式的值，写出您想到的一种或几种实现方法： 1-2+3-4+……+m(至少2种)


def func_14_2():
    m = in_int()
    if m % 2 == 0:
        return -m / 2
    return m - m // 2


# print(func_14_2())

def func_14_1():
    m = in_int()
    sum = 0
    for i in range(m + 1):
        if i % 2 == 0:
            sum -= i
        else:
            sum += i
    return sum

# print(func_14_1())
