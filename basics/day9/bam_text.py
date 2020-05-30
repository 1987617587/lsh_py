"""
# author Liu shi hao
# date: 2019/11/15 14:29
# file_name: bam_text

"""


class Account:
    def __init__(self, name, money) -> None:
        super().__init__()
        self.__money = money
        self.name = name

    def get_money(self, money):
        if money <= 0:
            return "无法操作！"
        if money >= self.__money:
            return "余额不足！"
        self.__money -= money
        return money

    def save_money(self, money):
        if money <= 0:
            return
        self.__money += money

    def show_money(self):
        return self.__money


# acc1 = Account("小二", 1000)
# print(acc1.name)
# acc1.save_money(240)
# print(acc1.name, acc1.get_money(1200))
# print(acc1.show_money())
#
