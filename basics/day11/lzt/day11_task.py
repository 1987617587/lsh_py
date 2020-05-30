# author:lzt
# date: 2019/11/20 8:51
# file_name: day11_task
# 6、请编码实现动物世界的继承关系：
# 动物（Animal）具有行为：吃（eat）、睡觉（sleep）
# 动物包括：兔子（Rabbit），老虎（Tiger）
# 这些动物吃的行为各不相同（兔子吃草，老虎吃肉）
# 但睡觉的行为是一致的。
# 请通过继承实现以上需求，并进行测试。


#
# 7、定义一个“曲调类”Note，value属性表示声音的高低
# Note的三个子类分别表示高音、低音和中音
# 定义一个“乐器类”Instrument
# 具有play()方法
# 子类：
# “管乐器类”Wind
# “敲击乐器类”Percussion
# “弦乐器类”Singed
# “铜管类”Brass
# “木管类”Woodwind
# 只写一个方法传入乐器和音调实现：
# Wind演奏高音
# Percussion演奏中音
# 铜管演奏中音
# 木管演奏低音
# 弦乐器演奏高音
# 敲击乐器演奏低音
import random


class Note:

    def __init__(self, value) -> None:
        super().__init__()
        # 表示声音的高低
        self.value = value

    def __str__(self) -> str:
        return self.value


class High(Note):

    def __init__(self) -> None:
        super().__init__("高音")


class Mid(Note):

    def __init__(self) -> None:
        super().__init__("中音")


class Low(Note):

    def __init__(self) -> None:
        super().__init__("低音")


class Instrument:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def play(self, note: Note):
        if issubclass(type(note), Note):
            print(f"{self.name}演奏了{note}")


class Wind(Instrument):

    def __init__(self) -> None:
        super().__init__("管乐器")


class Percussion(Instrument):

    def __init__(self) -> None:
        super().__init__("敲击乐器")


def music(ins: Instrument, note: Note):
    if issubclass(type(ins), Instrument) and issubclass(type(note), Note):
        ins.play(note)


# h = High()
# m = Mid()
# l = Low()
# w = Wind()
# p = Percussion()
#
# music(w, h)
# music(w, l)
# music(1,2)
#
#
# 8、有2个类：
# 员工类：属性：名字、工号、部门、工资 方法：涨工资
# 经理类继承自员工类 并多了一个属性：奖金
# 问题：
# 1).某公司有员工3人 经理2名 请用一个列表来管理他们 请自行产生这些对象
# 2.请输出所有员工的信息 格式：工号 部门 名字 工资
# 3.请统一的为所有员工涨一次工资 员工涨10% 经理比员工多涨10%
# 4.请输出所有员工涨工资后的信息 格式：工号 部门 名字 工资
class Emp:

    def __init__(self, name, empno, dp, salary) -> None:
        # 名字、工号、部门、工资
        super().__init__()
        self.__name = name
        self.__empno = empno
        self.dp = dp
        self._salary = salary

    @property
    def name(self):
        return self.__name

    @property
    def empno(self):
        return self.__empno

    @property
    def dp(self):
        return self.__dp

    @dp.setter
    def dp(self, value):
        self.__dp = value
        pass

    @property
    def salary(self):
        return self._salary

    # 涨工资
    def raise_salary(self, percent):
        self._salary += self._salary * percent
        pass

    def __str__(self) -> str:
        return f"{self.__empno} {self.__dp} {self.__name} {self._salary}"


class Manager(Emp):

    def __init__(self, name, empno, dp, salary, bonus) -> None:
        super().__init__(name, empno, dp, salary)
        self.bonus = bonus

    @property
    def bonus(self):
        return self.__bonus

    @bonus.setter
    def bonus(self, value):
        self.__bonus = value
        pass

    def raise_salary(self, percent):
        self._salary += self._salary * (0.1 + percent)


# emps = [
#     Emp("0001", "101", "研发部", 11000),
#     Emp("0003", "103", "研发部", 13000),
#     Emp("0002", "102", "研发部", 12000),
#     Manager("001", "10", "经理部", 25000, 15000),
#     Manager("002", "11", "经理部", 35000, 25000)
# ]
#
# for i in range(len(emps)):
#     print(emps[i])
#     emps[i].raise_salary(0.1)
#     print(emps[i])

#
# 9、计算1+2^2+3^3+4^4+...+n^n的值(^表示幂);
#
def task9(n):
    if n <= 0:
        return
    sum = 0
    for i in range(1, n + 1):
        sum += i ** i
    return sum


# print(task9(9))


# 10、求10000以下的水仙花数;
# 水仙花数是指一个 n 位数 ( n≥3 )，它的每个位上的数字的 n 次幂之和等于它本身。（例如：1^3 + 5^3+ 3^3 = 153）
# 要求：
# 1.先写一个函数 判断一个数是否是水仙花数
# 2.利用要求1中的函数求10000以下的水仙花数
#
def task10(max_num):
    if max_num < 100:
        return
    for i in range(100, max_num):
        # 验证i是否为水仙花数
        # sum = 0
        # 拆分各个位置的数字
        # th = i // 1000
        # h = i % 1000 // 100
        # t = i % 100 // 10
        # u = i % 10
        # # 求数字的位数
        # num_len = len(str(i))
        # if i == th ** num_len + h ** num_len + t ** num_len + u ** num_len:
        #     print(i)
        sum = 0
        for j in range(len(str(i))):
            # 每位的数字:str(i)[j]
            sum += int(str(i)[j]) ** len(str(i))
        if sum == i:
            print(i)


# task10(100000)

# 11、编写一个学生类：
# 学生类包括：
# 属性：名字、年龄、所属省份、所属市
# 属性：请封装上述属性
# 题目要求：
# 11.1编写一个学生列表，长度为3，放入不同省市的3个学生对象。名字和年龄自定义即可。
# 11.2根据省份输出列表中该省份的所有学生信息。
# 11.3根据所属市输出列表中该市的所有学生信息。
#
class Student:

    def __init__(self, name, age, pro, city) -> None:
        super().__init__()
        self.__name = name
        self.age = age
        self.pro = pro
        self.city = city

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0 or value > 149:
            print("年龄无效 设定默认值18")
            self.__age = 18
            return
        self.__age = value
        pass

    @property
    def pro(self):
        return self.__pro

    @pro.setter
    def pro(self, value):
        self.__pro = value
        pass

    @property
    def city(self):
        return self.__city

    @city.setter
    def city(self, value):
        self.__city = value
        pass

    def __str__(self) -> str:
        return f"{self.__name} {self.__pro} {self.__city}"


stus = [
    Student("000", 19, "河南", "南阳"),
    Student("001", 19, "河北", "石家庄"),
    Student("002", 19, "山东", "日照"),
    111,
    "123123"
]


def query_by_pro(stus: list, pro):
    if type(stus) is not list:
        return
    for i in range(len(stus)):
        if type(stus[i]) is Student:
            if hasattr(stus[i], "pro"):
                if pro == stus[i].pro:
                    print(stus[i])


def query_by_city(stus: list, city):
    for i in range(len(stus)):
        if city == stus[i].city:
            print(stus[i])


# query_by_pro(stus, "河南")
# query_by_city(stus, "石家庄")

# 12、创建一个玩家类，玩家有名称、生命值、魔法值、攻击力、生存状态5个属性；生命值、魔法值、攻击力、
# 生存状态属性都是只读的；生命值、魔法值、攻击力的初值分别为800、100、50；
# 玩家类有一个攻击方法：def attack(player)。
# 玩家类有两个子类：野蛮人和魔法师。野蛮人每次攻击造成的伤害在[攻击力-10]
# 到[攻击力+10]之间（这个伤害值是一个随机值），另外野蛮人有一个被动技能（不消耗魔法），
# 有25%的几率产生1次暴击，每次暴击产生的伤害是原来的3倍；
# 魔法师每次攻击造成的伤害在攻击力的80%~100%之间（也是一个随机数），
# 魔法师每次攻击消耗18点魔法，它会额外减少对方12%的生命值。
# 现在分别创建一个野蛮人、魔法师对象，让他们进行PK，
# 就是你打我一下，我打你一下，直到有一方死亡为止；野蛮人先攻击。
#
class Player:

    def __init__(self, name) -> None:
        super().__init__()
        self.__name = name
        self.__hp = 800
        self._mp = 100
        self.__atk = 50
        self.__state = True

    @property
    def name(self):
        return self.__name

    @property
    def hp(self):
        return self.__hp

    @property
    def mp(self):
        return self._mp

    @property
    def atk(self):
        return self.__atk

    @property
    def state(self):
        return self.__state

    def attack(self, player):
        pass

    def be_hurt(self, hurt):
        # 死后不能被攻击
        if not self.__state:
            print("请尊重死者！")
            return
        # 减掉血量值
        self.__hp -= hurt
        # 血量值是否为负数
        if self.__hp <= 0:
            self.__hp = 0
            self.__state = False

    def __str__(self) -> str:
        return f"{self.__name} {self._mp} {self.__hp}"


class Human(Player):

    def attack(self, player):
        if not self.state:
            print("请先安息")
            return
        # 野蛮人每次攻击造成的伤害在[攻击力 - 10]
        # 到[攻击力+10]之间（这个伤害值是一个随机值），
        hurt = self.atk + random.randint(-10, 10)
        # 另外野蛮人有一个被动技能（不消耗魔法），
        # 有25%的几率产生1次暴击，每次暴击产生的伤害是原来的3倍；
        # 1-100 1-25:暴击
        if random.randint(1, 100) <= 25:
            hurt *= 3
        # 减掉对方的血量
        player.be_hurt(hurt)


class Master(Player):

    def attack(self, player):
        if not self.state:
            print("请先安息")
            return
        # 魔法师每次攻击造成的伤害在攻击力的80 % ~100 % 之间（也是一个随机数），
        hurt = self.atk * random.uniform(0.8, 1)
        # 魔法师每次攻击消耗18点魔法，它会额外减少对方12%的生命值。
        if self._mp >= 18:
            self._mp -= 18
            hurt += player.hp * 0.12

        # 减掉对方的血量
        player.be_hurt(hurt)


# h = Human("野蛮人")
# m = Master("法师")
#
# while h.state and m.state:
#     h.attack(m)
#     print(h)
#     print(m)
#     m.attack(h)
#     print(h)
#     print(m)
#
# print("野蛮人获胜" if h.state else "法师获胜")

# 13、写一个Ticket类,有一个距离属性(本属性只读,在初始化方法中赋值),不能为负数,有一个价格属性,价格属性只读,
# 并且根据距离计算价格(1元/公里):
# 0-100公里 票价不打折
# 101-200公里 总额打9.5折
# 201-300公里 总额打9折
# 300公里以上 总额打8折
# 有一个方法,可以显示这张票的信息.
# 测试上面的类.
#
class Ticket:

    def __init__(self, distance) -> None:
        super().__init__()
        if distance < 0:
            distance = 0
        self.__distance = distance
        if self.__distance <= 100:
            self.__price = self.__distance
        elif self.__distance <= 200:
            self.__price = self.__distance * 0.95
        elif self.__distance <= 300:
            self.__price = self.__distance * 0.9
        else:
            self.__price = self.__distance * 0.8

    @property
    def distance(self):
        return self.__distance

    @property
    def price(self):
        return self.__price

    def __str__(self) -> str:
        return f"{self.__distance} {self.__price}"


# t1 = Ticket(100)
# print(t1)
# print(t1.price)

# 14、定义一个Vehicle汽车类，类中包含一个Person类型的数据成员拥有者owner、车轮数、车重、品牌等；定义一个Car类，
# 它是Vehicle的子类，其中添加属性：核载人数和实载人数。
# 定义VehicleManage汽车管理这个类：
# 该类包含一个属性：管理的车辆列表
# 该类包含两个方法：
# 1.获取到某个人拥有的所有车辆，并显示其名下所有车辆的信息
# 2.查看某车是否超载，并显示车辆和车主信息。
# 测试方案：测试汽车管理类中的方法
class Person:

    def __init__(self, name, d_id) -> None:
        super().__init__()
        self.name = name
        self.d_id = d_id

    def __str__(self) -> str:
        return f"{self.name} {self.d_id}"


class Vehicle:

    def __init__(self, owner, w_count, weight, sign) -> None:
        # owner、车轮数、车重、品牌
        super().__init__()
        if issubclass(type(owner), Person):
            self.owner = owner
        else:
            self.owner = None
        self.w_count = w_count
        self.weight = weight
        self.sign = sign

    def __str__(self) -> str:
        return f"{self.owner} {self.w_count} {self.weight} {self.sign}"


class Car(Vehicle):

    def __init__(self, owner, w_count, weight, sign, load_count, cur_count) -> None:
        super().__init__(owner, w_count, weight, sign)
        self.load_count = load_count
        self.cur_count = cur_count

    def __str__(self) -> str:
        return super().__str__() + f" {self.load_count} {self.cur_count}"


class VehicleManage:

    def __init__(self) -> None:
        super().__init__()
        self.cars = [
            Car(Person("张三", "10009008"), 4, 1.29, "BMW", 2, 5),
            Car(Person("张三2", "100090081"), 4, 1.39, "BMW", 5, 5),
            Car(Person("张三3", "100090082"), 4, 1.49, "BMW", 5, 6),
            Car(Person("张三4", "100090083"), 4, 1.59, "BMW", 5, 5)
        ]

    def query_by_name(self, name):
        for i in range(len(self.cars)):
            if name == self.cars[i].owner.name:
                print(self.cars[i])

    def check_load(self, d_id):
        for i in range(len(self.cars)):
            if d_id == self.cars[i].owner.d_id:
                if self.cars[i].cur_count > self.cars[i].load_count:
                    print("此车超载！")
                    print(f"驾照为{d_id}已登记 请及时缴费")


vm = VehicleManage()
vm.query_by_name("张三")
vm.check_load("10009008")
