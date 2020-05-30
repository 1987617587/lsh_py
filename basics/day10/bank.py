"""
# author Liu shi hao
# date: 2019/11/16 11:39
# file_name: bank

"""
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
import random


class Account:

    def __init__(self, name, password, person_id, email, balance) -> None:
        super().__init__()
        self.__id = str(random.randint(1000000000000000, 99999999999999999))
        self.__name = name
        self.password = password
        self.__person_id = person_id
        self.email = email
        self._balance = balance   # 下面的储蓄账号和信用卡需要继承。信用卡方法需要对余额修改，所以使用单下划线。

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
        return self._balance

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        if len(value) != 6:
            print("密码必须为6位！设定为默认值000000")
            self.__password = "000000"
            return
        if not str(value).isdigit():
            print("只支持数字密码! 已设定默认值000000")
            self.__password = "000000"
            return
        # self.__password = value
        self.__password = value
        pass

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, value):
        if "@" not in value:
            print("邮箱格式错误！")
            self.__email = None
            return
        self.__email = value
        # self.__email = value
        pass

    # 存款
    def deposit(self, money):
        if money <= 0:
            print("存款异常")
            return
        self._balance += money
        print(f"本次交易金额为:{money},账户余额为:{self._balance}")

    # 取款
    def withdraw(self, money):
        if money <= 0:
            print("取款异常")
            return 0
        if money > self._balance:
            print("余额不足！")
            return 0
        self._balance -= money
        print(f"本次交易金额为:{money},账户余额为:{self._balance}")
        return money


class SavingAccount(Account):

    def __init__(self, name, password, person_id, email, balance) -> None:
        super().__init__(name, password, person_id, email, balance)


class CreditAccount(Account):

    def __init__(self, name, password, person_id, email, balance, ceiling) -> None:
        super().__init__(name, password, person_id, email, balance)
        self.ceiling = ceiling

    @property
    def ceiling(self):
        return self.__ceiling

    @ceiling.setter
    def ceiling(self, value):
        if value <= 0:
            print("透支额度必须大于0")
            if self.__ceiling == 0:
                print("首次修改透支额度 默认设置1000")
                self.__ceiling = 1000
            return
        self.__ceiling = value
        pass

    def withdraw(self, money):
        choice_type = input("请选择支付类型 1-余额支付 其他-信用卡支付:")
        if str(money).isdigit() and "1" == choice_type and self._balance >= money:
            self._balance -= float(money)
            print(f"本次交易金额为:{money},账户余额为:{self._balance},透支额度剩余:{self.ceiling}")
            return

        if "1" != choice_type and self.__ceiling >= money > 0 and str(money).isdigit():
            self.__ceiling -= float(money)
            print(f"本次交易金额为:{money},账户余额为:{self.balance},透支额度剩余:{self.__ceiling}")
            return
        print("交易失败！")
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
        print("欢迎您到本银行开户！")
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
            self.__accounts.append(SavingAccount(name, pwd1, pid, email, 0))
        else:
            self.__accounts.append(CreditAccount(name, pwd1, pid, email, 0, 10000))

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
            # return
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
            # return
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
bank2 = Bank()
bank1.create_account()
print("信用卡，卡2开户")
bank2.create_account()
bank1.login()
bank1.save()
bank1.get()
print("信用卡，卡2取钱")
bank2.get()
bank1.total()
bank2.ceiling(3000)

