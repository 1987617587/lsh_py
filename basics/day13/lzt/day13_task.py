# author:lzt
# date: 2019/11/22 10:09
# file_name: day13_task
# 1、建立一个汽车Auto类，包括轮胎个数，汽车颜色，车身重量、速度等成员变量。至少要求：
# 汽车能够加速，减速，停车。 再定义一个小汽车类Car，继承Auto，并添加空调、CD等成员变量，覆盖加速，减速的方法
import random


class Auto:

    def __init__(self, w_count, color, weight, speed) -> None:
        super().__init__()
        self.w_count = w_count
        self.color = color
        self.weight = weight
        self.speed = speed

    def up_speed(self, up):
        pass

    def down_speed(self, down):
        pass

    def stop(self):
        print("刹车！")
        self.speed = 0


class Car(Auto):

    def __init__(self, w_count, color, weight, speed, air_con, CD) -> None:
        super().__init__(w_count, color, weight, speed)
        self.air_con = air_con
        self.CD = CD

    def up_speed(self, up):
        if self.speed + up < 120:
            self.speed += up
            print(f"汽车已加速到{self.speed}")
        else:
            print("小心超速，已修正速度！")

    def down_speed(self, down):
        if self.speed - down < 60:
            print("小心追尾！速度已修正！")
        else:
            self.speed -= down


# car = Car(4, "红色", 1.49, 100, "车载空调", "四小天鹅")
# car.up_speed(15)
# print(car.speed)
# car.down_speed(10)
# print(car.speed)

#
# 2、定义一个"Role"类，有姓名，年龄，性别等成员变量
# 1） 要求封装所有属性。具有一个work()方法，该方法不返回任何值
# 2）从Role类派生出一个Employee类，并扩展 salary成员变量，还要求覆盖work()方法。
# 3） Manager类继承Employee类，有一个成员变量vehicle，还要求覆盖work()方法。
# 4）在测试中制造一个Role列表，放入2个Manager和3个Employee对象,统一让他们按照自己的工作方式开始工作
class Role:

    def __init__(self, name, age, gender) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender

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
        if value < 0 or value > 149:
            print("年龄无效")
            self.__age = 18
            return
        self.__age = value
        pass

    @property
    def gender(self):
        return self.__gender

    @gender.setter
    def gender(self, value):
        if value not in ["男", "女"]:
            print("默认设定为男")
            self.__gender = "男"
            return
        self.__gender = value
        pass

    def work(self):
        pass


class Emp(Role):

    def __init__(self, name, age, gender, salary) -> None:
        super().__init__(name, age, gender)
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    def work(self):
        print("编写代码，单元测试！")


class Manager(Emp):

    def __init__(self, name, age, gender, salary, vehicle) -> None:
        super().__init__(name, age, gender, salary)
        self.vehicle = vehicle

    def work(self):
        print("接触客户 开会 查看进度！")


# roles = [
#     Manager("123", 19, "?", 19000, "杂牌车"),
#     Manager("122", 22, "?", 29000, "大众车"),
#     Emp("emp1", 18, "女", 9000),
#     Emp("emp2", 17, "女", 11000),
#     Emp("emp3", 19, "女", 12000)
# ]
#
# for i in range(len(roles)):
#     roles[i].work()

#
# 5、如何利用^对用户的密码进行加密和解密
# pwd = int(input("密码:"))
# key = 122
# print(f"加密后的密码:{pwd^key}")
# print(f"原始的密码:{pwd^key^key}")

#
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
# 游戏开始:设定待猜测数字(四位各位各不相同):
# 1234
# 用户猜测:
# 0123
# 游戏进行提示:
# 0A3B
# 1234
# 4A0B
# 游戏结束
def game():
    while 1:
        # 产生一个随机的四位各位各不相同的数字
        guess = ""
        while len(guess) != 4:
            num = random.randint(0, 9)
            if str(num) not in guess:
                guess += str(num)

        # print(guess)

        for j in range(9):
            # 用户输入四位各位各不相同的数字 1123
            while 1:
                user_num = input("请输入一个四位各位各不相同的数字：")
                if len(user_num)!= 4 or not user_num.isdigit():
                    print("必须全为数字！")
                    continue
                check = ""  # 123
                for i in range(len(user_num)):
                    if user_num[i] not in check:
                        check += user_num[i]
                # 判断check的长度
                if len(check) == 4:
                    break
                print("必须四位各位各不相同！")

            # 进行判断提示
            a_count = 0
            b_count = 0
            for i in range(4):
                # 按位判断:
                # 先判断A 先判断B？
                # A的判断
                if guess[i] == user_num[i]:
                    a_count += 1
                else:
                    # B判断
                    if user_num[i] in guess:
                        b_count += 1

            # 提示
            print(f"{a_count}A{b_count}B")

            # 进行一个正确的判断
            if a_count == 4:
                print("恭喜答对了！")
                if j < 5:
                    print("你太厉害了")
                else:
                    print("也很厉害！")
                break

            # 9次机会

        # 机会用尽 告知答案
        print(f"答案是{guess}！")

        # 询问是否继续
        if "y" == input("y-退出 其他-继续"):
            break


# game()


#
# 7、计算1+22+33+44+…+nn的值  1 + 22 + 333 + 4444+ 55555+...nnnnnnn;
def task7_1(n):
    if n > 9:
        return

    sum = 1
    for i in range(2, n + 1):
        sum += 11 * i
    return sum


def task7_2(n):
    if n > 9:
        return
    sum = 1
    for i in range(2, n + 1):
        sum += int(str(i) * i)
    return sum


# print(task7_1(3))
# print(task7_2(3))
#
# 8、我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，
# 鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？（百钱百鸡）
# for i in range(0, 21):
#     for j in range(0, 34):
#         for k in range(0, 101, 3):
#             if i + j + k == 100 and 5 * i + 3 * j + k // 3 == 100:
#                 print(i, j, k)

#
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
class Player:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.hp = 600
        self.atk = 15

    def be_hurt(self, hurt):
        if self.hp <= 0:
            print("该玩家已阵亡！")
            return
        self.hp -= hurt
        if self.hp < 0:
            self.hp = 0

    def attack(self, player):
        if self.hp <= 0:
            print("玩家已战败！")
            return
        # 猜大小
        guess = "大" if random.randint(1, 6) > 3 else "小"
        user_guess = "大" if input("1.大 其他.小") == "1" else "小"
        if guess == user_guess:
            player.be_hurt(self.atk)
        else:
            print("猜错！攻击失败！")
        pass

    def __str__(self) -> str:
        return f"{self.name} {self.hp}"


class AI(Player):

    def __init__(self, name) -> None:
        super().__init__(name)
        self.hp = 100
        self.atk = 15

    def attack(self, player):
        if self.hp <= 0:
            print("AI已战败！")
            return
        # 猜大小
        guess = "大" if random.randint(1, 6) > 3 else "小"
        user_guess = random.choice("大小")
        if guess == user_guess:
            player.be_hurt(self.atk)
        else:
            print("猜错！攻击失败！")
        pass


player = Player("战神1号")
ais = [
    AI("001"),
    AI("002"),
    AI("003")
]

while 1:
    # 玩家发起攻击：
    # AI谁活着按次序攻击
    for i in range(len(ais)):
        if ais[i].hp > 0:
            player.attack(ais[i])
            break

    # 显示双方的状态
    print("玩家状态：")
    print(player)

    print("AI的状态:")
    for i in range(len(ais)):
        print(ais[i])

    # AI死光
    if ais[2].hp <= 0:
        print("玩家获胜 游戏结束!")
        break

    # AI攻击
    for i in range(len(ais)):
        ais[i].attack(player)

    # 显示双方的状态
    print("玩家状态：")
    print(player)

    print("AI的状态:")
    for i in range(len(ais)):
        print(ais[i])

    # 判断玩家是否阵亡
    if player.hp <= 0:
        print("AI获胜 游戏结束")
        break


#
# 10、编写一个学生类：
# 学生类包括：
# 字段：名字、年龄、所属省份、所属市
# 属性：请封装上述字段
# 题目要求：
# 10.1编写一个学生列表，长度为3，放入不同省市的3个学生对象。名字和年龄自定义即可。
# 10.2写一个函数根据省份输出列表中该省份的所有学生信息。
# 10.3写一个函数根据所属市输出列表中该市的所有学生信息。
#
#
# 11、有n盏灯,放在一排,从1到n依次顺序编号，灯有开关两种状态.有m个人也从1到m依次顺序编号，
# 灯默认全部关闭，第1个人（1号）将灯全部打开；第2个人（2号）将凡是2的倍数的灯关闭；
# 第3个人（3号）将凡是3的倍数的灯作相反处理（该灯如是打开的,则将它关闭；如是关闭的,则将它打开）.
# 以后的人都和3号一样,将凡是自己编号倍数的灯作相反处理.编写方法，传入第m个人操作后，返回亮着灯的序号的列表
def task11(n, m):
    if n < 1 or m < 1:
        return
    # 设定一个和现实灯对应的列表(表示灯的开关状态)
    lights = [False] * n

    # 开始让人进入房间开始开关灯 灯编号%人编号 == 0:改变灯当前的状态:反转
    for i in range(1, m + 1):
        # i是人的编号:依次开关灯
        for j in range(len(lights)):
            # 灯的编号:j+1
            if (j + 1) % i == 0:
                lights[j] = not lights[j]

    ret = []
    # 哪些编号的灯还开着
    for i in range(len(lights)):
        if lights[i]:
            ret.append(i + 1)
    return ret


# 0 0 0 0 0
# 1 1 1 1 1
# 1 0 1 0 1
# 1 0 0 0 1
# print(task11(5, 3))
#
# 12、（1）定义一个人类作为基类，有姓名、性别、年龄，再由基类派生出教师类和学生类，
# 教师类增加工号、职称和工资，学生类增加学号、班级、专业和入学成绩;
# （2）创建一个列表存放3个学生和2名教师;
# （3）编写方法，传入参数是（2）创建的列表，返回工资最高的教师和成绩最好的学员。
# （4）打印出（3）返回的学员和教师信息。
class Person:

    def __init__(self, name, age, gender) -> None:
        super().__init__()
        self.name = name
        self.age = age
        self.gender = gender


class Teacher(Person):

    def __init__(self, name, age, gender, num, dp, salary) -> None:
        super().__init__(name, age, gender)
        self.num = num
        self.dp = dp
        self.salary = salary

    def __str__(self) -> str:
        return f"{self.name} {self.salary}"


class Student(Person):

    def __init__(self, name, age, gender, num, classes, lesson, score) -> None:
        super().__init__(name, age, gender)
        self.num = num
        self.classes = classes
        self.lesson = lesson
        self.score = score

    def __str__(self) -> str:
        return f"{self.name} {self.score}"


# （2）创建一个列表存放3个学生和2名教师;
pers = [
    Student("stu1", 19, "男", 1001, "1911", "Python", 78),
    Student("stu2", 19, "男", 1003, "1911", "Python", 87),
    Student("stu3", 19, "男", 1002, "1911", "Python", 66),
    Teacher("t1", 31, "女", "0001", "Python", 17000),
    Teacher("t1", 33, "男", "0003", "Web大前端", 13000)
    # "asdasd",
    # 121211
]


# （3）编写方法，传入参数是（2）创建的列表，返回工资最高的教师和成绩最好的学员。
def max_teacher_stu(pers: list):
    max_t = None
    max_s = None

    # 检测列表中是否有老师或者学员 做最值的查找
    for i in range(len(pers)):
        # 判断类别
        if pers[i].__class__ is Teacher and (max_t is None or pers[i].salary > max_t.salary):
            max_t = pers[i]
        if type(pers[i]) == Student and (max_s is None or pers[i].score > max_s.score):
            max_s = pers[i]
    return max_t, max_s


# （4）打印出（3）返回的学员和教师信息。
# max_t, max_s = max_teacher_stu(pers)
# print(max_t, max_s)

#
# 13、程序中定义一个机器人类（Robot），该类中定一个静态数据成员__robot_count表示机器人人数，
# 以及一个类方法get_count来访问该字段。问题：如何做到机器人人数这个字段的值和产生的机器人对象数目保持一致。
#
class Robot:
    __robot_count = 0

    def __init__(self) -> None:
        super().__init__()
        Robot.__robot_count += 1

    @classmethod
    def get_count(cls):
        return cls.__robot_count


# Robot()
# Robot()
# Robot()
# Robot()
# Robot()
# print(Robot.get_count())
# 14、求以下表达式的值，写出您想到的一种或几种实现方法： 1-2+3-4+……+m(至少2种)
# 常规思路:循环求和
# 数学思维:1-2+3-4+5-6+7-8
# m若为偶数:恰好是m//2个-1：-m//2
# m为奇数:1-2+3-4+....-m-1 + m:-(m-1)//2+m
def task14(m):
    if m < 1:
        return
    sum = 0
    for i in range(1, m + 1):
        sum += (-1) ** (i + 1) * i
    return sum

# print(task14(10))
