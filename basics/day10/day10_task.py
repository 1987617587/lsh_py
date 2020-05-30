"""
# author Liu shi hao
# date: 2019/11/15 18:40
# file_name: day10_task

"""

import random


# 9.
# 编写一个时间类My_Time，包含一个三个参数的初始化方法，3个属性hour,minute,second,
# 再加上一个转换成字符串的方法to_string。
#
# 注意：请注意时分秒的取值范围
class Mytiime:

    def __init__(self, hour, minute, second) -> None:
        super().__init__()
        self.hour = hour
        self.minute = minute
        self.second = second

    @property
    def hour(self):
        return self.__hour

    @hour.setter
    def hour(self, value):

        if value < 0 or value > 23 or not str(value).isdigit():
            print("时 格式错误，已设定默认值0！")
            self.__hour = 0
        else:
            self.__hour = value
        pass

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, value):
        if value < 0 or value > 59 or not str(value).isdigit():
            print("分 格式错误，已设定默认值0！")
            self.__minute = 0
        else:
            self.__minute = value
        pass

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, value):
        if value < 0 or value > 59 or not str(value).isdigit():
            print("秒 格式错误，已设定默认值0！")
            self.__second = 0
        else:
            self.__second = value
        pass

    def to_string(self):

        return str(self.__hour) + "时" + str(self.__minute) + "分" + str(self.__second) + "秒"


time1 = Mytiime(11, 10, 1)

# print(time1.to_string())


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

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        if value >= 0 and str(value).isdigit():
            self.__year = value
        else:
            print("年 格式错误，已设定默认值0！")
            self.__year = 0
        pass

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        if 12 >= value >= 0 and str(value).isdigit():
            self.__month = value
        else:
            print("月 格式错误，已设定默认值0！")
            self.__month = 0

        pass

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        if value > 0 and str(value).isdigit():
            if self.__year % 4 == 0 and self.__year % 100 != 0 or self.__year % 400 == 0:
                list_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            else:
                list_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

            if value <= list_days[self.__month - 1]:
                self.__day = value
            else:
                print("日 格式错误，已设定默认值0！")
                self.__day = 0
        else:
            print("日 格式错误，已设定默认值0！")
            self.__day = 0


    def to_string(self):

        return str(self.__year) + "年" + str(self.__month) + "月" + str(self.__day) + "日"


my_date1 = MyDate(2020, 2, 39)


# print(my_date1.to_string())

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

    @property
    def n1(self):
        return self.__n1

    @n1.setter
    def n1(self, value):
        if type(eval(str(value))) == int:
            self.__n1 = int(value)
        elif type(eval(str(value))) == float:
            self.__n1 = float(value)
        else:
            print("n1格式错误,无法计算！")

        pass

    @property
    def n2(self):
        return self.__n2

    @n2.setter
    def n2(self, value):
        if type(eval(str(value))) == int:
            self.__n2 = int(value)
        elif type(eval(str(value))) == float:
            self.__n2 = float(value)
        else:
            print("n2格式错误,无法计算！")

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
        if self.n2 == 0:
            return "无法执行除运算！"
        else:
            division = self.n1 / self.n2
            return division


num1 = Number(10.5, 3)

# print(num1.n1)
num2 = Number(1, -0.2)
print(num1.addition())
print(num2.division())
print(num1.division())
print(num1.multiplication())


# 12.
# 银行账户管理系统（BAM）
# 写一个账户类(Account)：
# 属性: id:账户号码 长整数
# password:账户密码
# name:真实姓名
# person_id:身份证号码 字符串类型
# email:客户的电子邮箱
# balance:账户余额
# 方法:
# deposit: 存款方法,参数是浮点数型的金额
# withdraw:取款方法,参数是浮点数型的金额
# 初始化方法:
# 1.将Account类作成完全封装,注意:要辨别每个属性的是否需要公开
# 2.添加新的银行的客户类：储蓄账户(Saving_Account)和信用账户(Credit_Account),区别在于储蓄账户不允许透支,而信用账户可以透支,并允许用户设置自己的透支额度.
# 注意:Credit_Account需要多一个属性 ceiling 透支额度
#


class Account:

    def __init__(self, name, password, person_id, email, balance) -> None:
        super().__init__()
        self.__id = str(random.randint(1000000000000000, 99999999999999999))
        self.__name = name
        self.password = password
        self.__person_id = person_id
        self.email = email
        self.__balance = balance

    @property
    def id(self):
        return self.__id

    @property
    def name(self):
        return self.__name

    @property
    def person_id(self):
        return self.__person_id

    @property
    def balance(self):
        return self.__balance

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        self.__password = value
        pass

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        self.__email = value
        pass

    # 存款
    def deposit(self, money):
        if money <= 0:
            print("存款异常")
            return
        self.__balance += money
        print(f"本次交易金额为:{money},账户余额为:{self.__balance}")

    # 取款
    def withdraw(self, money):
        if money <= 0:
            print("取款异常")
            return 0
        if money > self.__balance:
            print("余额不足！")
            return 0
        self.__balance -= money
        print(f"本次交易金额为:{money},账户余额为:{self.__balance}")
        return money


class SavingAccount(Account):
    pass


class CreditAccount(Account):

    def __init__(self, name, password, person_id, email, balance, ceiling) -> None:
        super().__init__(name, password, person_id, email, balance)
        self.ceiling = ceiling

    @property
    def ceiling(self):
        return self.__ceiling

    @ceiling.setter
    def ceiling(self, value):
        if value < 0:
            print("额度设置异常")
            return
        self.__ceiling = value
        pass

    # 修改父类中的取款方法
    def withdraw(self, money):
        choice_type = input("请选择支付类型 1-余额支付 其他-信用卡支付:")
        if "1" == choice_type and self.__balance >= money > 0 and str(money).isdigit():
            self.__balance -= float(money)
            print(f"本次交易金额为:{money},账户余额为:{self.__balance},透支额度剩余:{self.ceiling}")

        if "1" != choice_type and self.__ceiling >= money > 0 and str(money).isdigit():
            self.__ceiling -= float(money)
            print(f"本次交易金额为:{money},账户余额为:{self.balance},透支额度剩余:{self.__ceiling}")
        else:
            print("取款失败！")
            return


#
# 12-2.编写Bank类
# 属性:
# 1.当前所有的账户对象存放在列表中
# 2.当前登录用户
#
# 方法:
# 1.用户开户,由用户输入需要的参数:id,密码,密码确认,姓名,身份证号码,邮箱,账户类型(int),将新创建的Account对象放入账户列表中
# 2.用户登录,从用户输入中获取:id,密码 提示 检测用户列表内是否有此用户，若登录成功，将匹配到的对象放入当前登录用户中
# 3.用户存款,判断用户是否登录，若登录，输入:存款数额,修改当前登录的Account对象，若未登录，提示登录
# 4.用户取款,判断用户是否登录，若登录，输入:取款数额,修改当前登录的Account对象，若未登录，提示登录
# 5.统计银行所有账户余额总数
class Bank:

    def __init__(self) -> None:
        super().__init__()
        self.__accounts = \
            [
                # 预存数据库 Bank()

            ]
        self.__login = None

    def create_account(self):
        name = input("请输入您的真实姓名:")
        pid = input("请输入您的身份证号:")
        email = input("请输入您的邮箱地址:")
        choice_type = input("请选择开户类型 1-储蓄账户 其他-信用账户:")
        while True:
            pwd1 = input("请输入要设定的密码:")
            re_pwd = input("请重复输入要设定的密码:")
            if pwd1 == re_pwd:
                break
            else:
                print("两次密码输入不一致，请重设密码！")
        if "1" == choice_type:
            self.__accounts.append(SavingAccount(name, pwd1, pid, email, 0.0))
        else:
            self.__accounts.append(CreditAccount(name, pwd1, pid, email, 0.0, 10000.0))

        for i in range(len(self.__accounts)):
            print(self.__accounts[i].id)

    def login(self):
        # 检测是否已登录
        if self.__login is not None:
            print("请勿重复登录！")
            return
        for j in range(3):
            acc_id = input("请输入卡号:")
            pwd = input("请输入密码:")
            # 遍历所有的账户
            for i in range(len(self.__accounts)):
                if self.__accounts[i].id == acc_id and self.__accounts[i].password == pwd:
                    self.__login = self.__accounts[i]
                    print("登录成功！ 请选择服务项目！")
                    return
            else:
                if j == 2:
                    print("您已被禁止登录，请联系客服！")
                    return
                print(f"你输入的卡号或密码有误，还有{2 - j}次登录机会")

    def save(self):
        # 检测是否已经登陆
        if self.__login is None:
            print("请先登录！")
            self.login()
            return
        set_money = input("请输入存钱金额：")
        if str(set_money).isdigit() and int(set_money) > 0:
            self.__login.deposit(int(set_money))
            # print(f"当前余额为:{self.__login.balance}")
        else:
            print("存款失败！")

    def get(self):
        # 检测是否已经登陆
        if self.__login is None:
            print("请先登陆！")
            self.login()
            return
        get_money = input("请输入取款金额：")
        if str(get_money).isdigit() and int(get_money) > 0:
            self.__login.withdraw(int(get_money))
            # print(f"本次交易金额为:{get_money},账户余额为:{self.__login.balance},透支额度剩余:{self.__login.ceiling}")
        else:
            print("交易失败！")

    def total(self):
        t = 0
        for i in range(len(self.__accounts)):
            t += self.__accounts[i].balance
        print("当前银行所有存款:", t)


# 用户会通过调用Bank对象以上的方法来操作自己的账户,请分析各个方法需要的参数
# 测试你写的类
bank1 = Bank()
bank1.create_account()
bank1.login()
bank1.save()
bank1.get()
bank1.total()
# bank2 = Bank()
# bank1.get()
# bank2.save()
print(bank1.accounts)