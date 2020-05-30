"""
# author Liu shi hao
# date: 2019/11/18 14:22
# file_name: person_students

"""


class Person:
    def __init__(self, name, age) -> None:
        super().__init__()
        self.name = name
        self.age = age

    def eat(self):
        print(f"{self.name}胡吃海喝")


class Students(Person):
    def __init__(self, name, age) -> None:
        super().__init__(name, age)
        # self.name =

    def eat(self):
        # print("吃学生餐")
        super().eat()


s1 = Students("001", 19)
s1.eat()


class Bonze(Person):
    def __init__(self, name, age, tall) -> None:
        super().__init__(name, age)
        self.name = "八戒"
        self.tall = "tall"

    def eat(self):
        print(f"{self.name}不准吃肉，不准破戒")


b1 = Bonze("和尚1", 67, 187)
b1.eat()


class Father:

    def __init__(self, year, money) -> None:
        super().__init__()
        self.year = year
        self.money = money

    def marr(self):
        print(f"{self.year}年结婚，需要手电筒，缝纫机，自行车")

    def pay(self,pay_money):
        self.money -= pay_money


class Son(Father):


    def __init__(self, year, money,son_money) -> None:
        super().__init__(year, money)
        self.son_money = son_money

    def marr(self):
        print(f"{self.year}年结婚，需要汽车洋房，彩礼20万，三金")

    def pay(self,pay_money):
        if self.son_money < pay_money:
            super().pay(pay_money)
        else:
            self.son_money -= pay_money

son = Son(2020,10000,1000)
son.marr()
son.pay(8000)
print(son.money)
print(son.son_money)














