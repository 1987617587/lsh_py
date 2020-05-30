"""
# author Liu shi hao
# date: 2019/11/19 11:18
# file_name: day11_task

"""

# 6、请编码实现动物世界的继承关系：
# 动物（Animal）具有行为：吃（eat）、睡觉（sleep）
# 动物包括：兔子（Rabbit），老虎（Tiger）
# 这些动物吃的行为各不相同（兔子吃草，老虎吃肉）
# 但睡觉的行为是一致的。
# 请通过继承实现以上需求，并进行测试。
#
import random

from day5.day5_task import in_int


class Animal:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name

    def eat(self):
        pass

    def sleep(self):
        print(f"{self.name}睡觉")
        pass


class Rabbit(Animal):

    def eat(self):
        print(f"{self.name}吃青草")


class Tiger(Animal):

    def eat(self):
        print(f"{self.name}吃肉")


an1 = Rabbit("兔子")
an1.eat()
an1.sleep()


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
#
class Note:

    def __init__(self, value) -> None:
        super().__init__()
        self.value = value


class High(Note):

    def __init__(self) -> None:
        super().__init__("高音")


class Low(Note):

    def __init__(self) -> None:
        super().__init__("低音")


class Medium(Note):
    def __init__(self) -> None:
        super().__init__("中音")


class Instrument():

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.notes = [High(), Low(), Medium()]

    def play(self):

        for i in range(len(self.notes)):
            print(f"{i + 1}.{self.notes[i].value}", end=" ")

        choice = input("请输入1-3进行曲调选择：")
        if choice in ["1", "2", "3"]:
            self.note = self.notes[int(choice) - 1]  # 得到列表中的类

        print(f"{self.name}演奏{self.note.value}")


class Wind(Instrument):

    def __init__(self) -> None:
        super().__init__("管乐器")


class Percussion(Instrument):
    def __init__(self) -> None:
        super().__init__("敲击乐器")

    pass


class Singed(Instrument):
    def __init__(self) -> None:
        super().__init__("弦乐器")

    pass


class Brass(Instrument):
    def __init__(self) -> None:
        super().__init__("铜管")

    pass


class Woodwind(Instrument):
    def __init__(self) -> None:
        super().__init__("木管")

    pass


# in1 = Instrument(Woodwind().play())


# def
# 8、有2个类：
# 员工类：属性：名字、工号、部门、工资 方法：涨工资
# 经理类继承自员工类 并多了一个属性：奖金
# 问题：
# 1).某公司有员工3人 经理2名 请用一个列表来管理他们 请自行产生这些对象
# 2.请输出所有员工的信息 格式：工号 部门 名字 工资
# 3.请统一的为所有员工涨一次工资 员工涨10% 经理比员工多涨10%
# 4.请输出所有员工涨工资后的信息 格式：工号 部门 名字 工资
#

class Employee:

    def __init__(self, name, number, department, salary) -> None:
        super().__init__()
        self.name = name
        self.number = number
        self.department = department
        self.salary = salary

    def pay_rise(self):
        self.salary *= 1.1

    def export(self):
        print(f"工号{self.number},部门{self.department} ,名字{self.name}, 工资{self.salary}")


class Manager(Employee):

    def __init__(self, name, number, department, salary, bonus) -> None:
        super().__init__(name, number, department, salary)
        self.bonus = bonus

    def pay_rise(self):
        self.salary *= 1.2


list_emps = [Employee("李四", "001", "研发部", 12000),
             Employee("王五", "006", "研发部", 14300),
             Employee("赵月", "011", "人事部", 10000),
             Manager("张三", "031", "研发部", 12000, 20000),
             Manager("陈东", "061", "财政部", 12000, 30000)]


def func_8():
    print("涨工资前：")
    for i in range(len(list_emps)):
        list_emps[i].export()
        list_emps[i].pay_rise()
    print("涨过工资后：")
    for j in range(len(list_emps)):
        list_emps[j].export()


# func_8()

# 9、计算1+2^2+3^3+4^4+...+n^n的值(^表示幂);
#
def func_9(n: int):
    # n = in_int()
    s = 0
    for i in range(1, n + 1):
        s += i ** i
    print(f"结果是：{s}")


# func_9()
# 10、求10000以下的水仙花数;
# 水仙花数是指一个 n 位数 ( n≥3 )，它的每个位上的数字的 n 次幂之和等于它本身。（例如：1^3 + 5^3+ 3^3 = 153）
# 要求：
# 1.先写一个函数 判断一个数是否是水仙花数
# 2.利用要求1中的函数求10000以下的水仙花数
#
def narcissistic_number(n):
    s = 0
    for i in range(len(str(n))):
        s += int(str(n)[i]) ** len(str(n))
        # print(s)
    if s == n:
        return True


# print(narcissistic_number(in_int()))


def func_10():
    list_narcissistic_number = []
    for i in range(100, 10000):
        if narcissistic_number(i):
            list_narcissistic_number.append(i)
    print(f"10000以下的水仙花数有：{list_narcissistic_number}")


func_10()


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

    def show(self, an):
        if an in [self.name, self.age, self.province, self.city]:
            print(self.__str__())


list_students = [Student("张三", 19, "河南", "郑州"),
                 Student("李四", 23, "浙江", "温州"),
                 Student("王五", 20, "新疆", "乌鲁木齐"),
                 ]


# for i in range(len(list_students)):
#     if "河南" == list_students[i].province:
#         print(f"名字:{list_students[i].name} 年龄:{list_students[i].age} 所属省份:{list_students[i].province} 所属市:{list_students[i].city}。")

# for i in range(len(list_students)):
#     list_students[i].show("乌鲁木齐")
# 12、创建一个玩家类，玩家有名称、生命值、魔法值、攻击力、生存状态5个属性；生命值、魔法值、攻击力、生存状态属性都是只读的；
# 生命值、魔法值、攻击力的初值分别为800、100、50；玩家类有一个攻击方法：public void attack(Player player)。
# 玩家类有两个子类：野蛮人和魔法师。野蛮人每次攻击造成的伤害在[攻击力-10] 到[攻击力+10]之间（这个伤害值是一个随机值），
# 另外野蛮人有一个被动技能（不消耗魔法），有25%的几率产生1次暴击，每次暴击产生的伤害是原来的3倍；
# 魔法师每次攻击造成的伤害在攻击力的80%~100%之间（也是一个随机数），魔法师每次攻击消耗18点魔法，它会额外减少对方12%的生命值。
# 现在分别创建一个野蛮人、魔法师对象，让他们进行PK，就是你打我一下，我打你一下，直到有一方死亡为止；野蛮人先攻击。
#

class Player:

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self._hp = 800
        self._mp = 100
        self._atk = 50
        self._state = True

    @property
    def hp(self):
        return self._hp

    @property
    def mp(self):
        return self._mp

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


class Human(Player):
    def __init__(self, name) -> None:
        super().__init__(name)

    def attack(self, player):
        if not self._state:
            print("请安息！")
            return
        # 获取当前玩家的基础伤害值
        hurt = self._atk + random.randint(-10, 10)
        # 附加伤害值
        if 1 <= random.randint(1, 100) <= 25:
            hurt *= 3
        # 减掉对方的血量值
        print(f"{self.name}打出伤害{hurt}")
        player.be_hurt(hurt)


class Magic(Player):
    def __init__(self, name) -> None:
        super().__init__(name)

    def attack(self, player):
        if not self._state:
            print("请安息！")
            return
        # 获取当前玩家的基础伤害值
        hurt = self._atk * random.uniform(0.8, 1)
        # 附加伤害值
        if self._mp >= 18:
            self._mp -= 18
            hurt += player._hp * 0.12
        # 减掉对方的血量值
        print(f"{self.name}打出伤害{hurt}蓝量{self._mp}")
        player.be_hurt(hurt)


h = Human("野蛮人")
m = Magic("法师")


def pk():
    while h.state and m.state:
        h.attack(m)
        if m.state:
            m.attack(h)
    print("野蛮人 win" if h.state else "法师 win")


pk()


# 13、写一个Ticket类,有一个距离属性(本属性只读,在初始化方法中赋值),不能为负数,有一个价格属性,价格属性只读,并且根据距离计算价格(1元/公里):
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
        self.__distance = distance
        self.__price = 1

    @property
    def distance(self):
        return self.__distance

    @property
    def price(self):
        return self.__price

    def show(self):
        if self.__distance <= 0:
            self.__price = 0
        elif self.distance <= 100:
            self.__price = 1
        elif self.__distance <= 200:
            self.__price = 0.95
        elif self.distance <= 300:
            self.__price = 0.9
        else:
            self.__price = 0.8

        print(f"距离:{self.__distance},计算价格:{self.__price}元/公里,应付{self.__distance * self.__price}元")


t1 = Ticket(340)


# t1.show()
# 16、定义一个Vehicle汽车类，类中包含一个Person类型的数据成员拥有者owner、车轮数、车重、品牌等；
# 定义一个Car类，它是Vehicle的子类，其中添加属性：核载人数和实载人数。
# 定义VehicleManage汽车管理这个类：
# 该类包含一个属性：管理的车辆列表
# 该类包含两个方法：
# 1.获取到某个人拥有的所有车辆，并显示其名下所有车辆的信息
# 2.查看某车是否超载，并显示车辆和车主信息。
# 测试方案：测试汽车管理类中的方法
class Vehicle:
    def __init__(self, owner, wheels_nums, car_weight, brand) -> None:
        super().__init__()
        self.owner = owner
        self.wheels_nums = wheels_nums
        self.car_weight = car_weight
        self.brand = brand


class Car(Vehicle):
    def __init__(self, owner, wheels_nums, car_weight, brand, nuclear_nums, actual_nums) -> None:
        super().__init__(owner, wheels_nums, car_weight, brand)
        self.nuclear_nums = nuclear_nums
        self.actual_nums = actual_nums


class VehicleManage:

    def __init__(self) -> None:
        super().__init__()
        self.cars = [Car("小王", "4", 30000, "宝马", 5, 6),
                     Car("小赵", "4", 20000, "丰田", 5, 3),
                     Car("小赵", "4", 40000, "福特", 5, 6),
                     Car("小刘", "4", 50000, "牧马人", 5, 7),
                     Car("小黄", "8", 1200000, "奔驰", 2, 2),
                     ]

    def owner_cars(self, an):
        for i in range(len(self.cars)):
            if an == self.cars[i].owner:
                print(f"拥有者:{self.cars[i].owner} 车轮数{self.cars[i].wheels_nums}、"
                      f"车重{self.cars[i].car_weight}、品牌{self.cars[i].brand}。")

    def check(self):
        for i in range(len(self.cars)):
            if self.cars[i].nuclear_nums < self.cars[i].actual_nums:
                print(f"本车超载！拥有者:{self.cars[i].owner} 车轮数{self.cars[i].wheels_nums}、车重{self.cars[i].car_weight}、"
                      f"品牌{self.cars[i].brand},核载人数{self.cars[i].nuclear_nums}实载人数{self.cars[i].actual_nums}。")

VehicleManage().owner_cars("小赵")
VehicleManage().check()
