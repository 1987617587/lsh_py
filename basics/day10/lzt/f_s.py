# author:lzt
# date: 2019/11/18 14:39
# file_name: f_s
class Father:

    def __init__(self, money) -> None:
        super().__init__()
        self.__money = money

    @property
    def money(self):
        return self.__money

    def pay(self, pay_money):
        self.__money -= pay_money

    def marr(self):
        print("老三件:缝纫机、手电筒、自行车")


class Son(Father):

    def __init__(self, money, son_money) -> None:
        super().__init__(money)
        self.son_money = son_money

    def marr(self):
        print("新三件:房子、车子、票子")

    def pay(self, pay_money):
        if self.son_money < pay_money:
            super().pay(pay_money)
        else:
            self.son_money -= pay_money


son = Son(100000, 10000)
son.marr()
son.pay(2000)
print(son.money)
print(son.son_money)
