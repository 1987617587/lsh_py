# author:lzt
# date: 2019/11/15 14:21
# file_name: bam

class Account:

    def __init__(self,money,name) -> None:
        super().__init__()
        # 成员变量名前缀没有_：公有变量 所有的位置都可以访问
        # _前缀的成员变量多用于继承关系内
        # __前缀是将数据变量封装在类内部的一种手段：禁止外部直接访问！！！
        # 产生成员变量的时候 为成员变量名+_或者__
        self.__money = money
        self.__name = name

    # 编写获取和设定钱数的成员方法：访问内部数据的接口
    def get_money(self,money):
        # 内部的约束流程
        if money <= 0:
            return "请不要开这种玩笑！"
        if money > self.__money:
            return "余额不足!"
        self.__money -= money
        return money

    def save_money(self,money):
        if money <= 0:
            return
        self.__money += money

    # 查看余额
    def show_money(self):
        return self.__money

# 创建一个具体的账户
acc1 = Account(10000,"123")
# acc1.__money = 500
# acc1.__name = "123"
# print(acc1.__money)
# # print(acc1.__name)
acc1.save_money(0)
print(acc1.show_money())
print(acc1.get_money(-10000))
print(acc1.show_money())


