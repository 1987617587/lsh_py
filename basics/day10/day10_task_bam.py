"""
# author Liu shi hao
# date: 2019/11/15 19:44
# file_name: day10_task_bam

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
#
import random


class Account:

    def __init__(self, password, name, person_id, email, balance) -> None:
        super().__init__()
        self.__acc_id = str(random.randint(100000, 999999))
        self.password = password
        self.__name = name
        self.__person_id = person_id
        self.email = email
        self.__balance = balance

    @property
    def id(self):
        return self.__acc_id

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

    def deposit(self, money):
        if money > 0 and str(money).isdigit():
            self.__balance += float(money)
        else:
            print("存款失败！")
            return

    def withdraw(self, money):
        if self.__balance >= money > 0 and str(money).isdigit():
            self.__balance -= float(money)
            print(f"取款金额为{money},余额为{self.__balance}")
        else:
            print("取款失败！")
            return

        # acc1 = Account( "6666", "siri", "41165", "@qq123.com", 90000.0)


# acc1.withdraw(699)
# print(acc1.balance)
# acc1.deposit(699)
# print(acc1.balance)


class SavingAccount(Account):
    pass


class CreditAccount(Account):

    def __init__(self, password, name, person_id, email, balance, ceiling) -> None:
        super().__init__(password, name, person_id, email, balance)
        self.ceiling = ceiling

    @property
    def ceiling(self):
        return self.__ceiling

    @ceiling.setter
    def ceiling(self, value):
        if value >= 0 and str(value).isdigit():
            self.__ceiling = value
        else:
            print("额度设置异常")
            return

    def withdraw(self, money):
        if self.__ceiling >= money > 0 and str(money).isdigit():
            self.__ceiling -= float(money)
        else:
            print("取款失败！")
            return

        # c_acc1 = CreditAccount(8765, "88888", "jake", "412725", "@qq666.com", 9.0, 10000)


# c_acc1.withdraw(699)
# print(c_acc1.balance)
# c_acc1.deposit(699)
# print(c_acc1.balance)
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
#
# 用户会通过调用Bank对象以上的方法来操作自己的账户,请分析各个方法需要的参数
# 测试你写的类
class Bank:

    def __init__(self) -> None:
        super().__init__()
        self.__accounts = []
        self.__login = None

    def create_account(self):
        while 1:
            pwd = input("请输入要设定的密码：")
            re_pwd = input("请重复输入要设定的密码：")
            if pwd == re_pwd:
                break
            else:
                print("两次密码输入不一致，请重设密码！")
        name = input("请输入您的真实姓名：")
        pid = input("请输入您的身份证号：")
        email = input("请输入您的邮箱地址：")
        choice_type = input("请选择开户类型 1-储蓄账户 其他-信用账户：")
        # acc_id = random.randint(100000, 999999)
        if choice_type == "1":
            self.__accounts.append(SavingAccount(pwd, name, pid, email, 0))
            # print(f"储蓄卡开户成功，您的卡号为{self.__acc_id}")
        else:
            self.__accounts.append(CreditAccount(pwd, name, pid, email, 0, 5000))
            # print(f"信用卡开户成功，您的卡号为{self.__acc_id},透支额度为{5000}")

        for i in range(len(self.__accounts)):
            print(self.__accounts[i].acc_id)
        # 验证：遍历数据库中的开户卡号，验证开户成功，数据传入数据库。

    def login(self):
        for j in range(3):
            # 检测是否已经登录
            if self.__login is not None:
                print("请勿重复登录！")
                return
            acc_id = input("请输入卡号：")
            pwd = input("请输入密码：")
            # 验证：遍历数据库中的账户，验证卡号和密码正确
            for i in range(len(self.__accounts)):
                if str(self.__accounts[i].acc_id) == acc_id and self.__accounts[i].pwd == pwd:
                    self.__login = self.__accounts[i]
                    print("登录成功！ 请选择服务项目")
                    break
            else:
                print("卡号或密码错误！" if j != 2 else "账户锁定，请联系客服！")

    def save(self):
        # 检测是否已经登录
        if self.__login is not None:
            print("请先登录！")
            self.login()
            return
        set_money = input("请输入存钱金额：")
        if int(set_money) > 0 and str(set_money).isdigit():
            self.__login.deposit(set_money)
            print(f"当前余额为:{self.__login.balance}")
        else:
            print("存款失败！")

    def get(self):
        # 检测是否已经登录
        if self.__login is not None:
            print("请先登录！")
            self.login()
            return
        get_money = input("请输入取款金额：")
        if int(get_money) > 0 and str(get_money).isdigit():
            get_money = self.__login.withdraw(get_money)
            print(f"本次交易金额为:{get_money},账户余额为:{self.__login.balance}")
        else:
            print("交易失败！")

    def total(self):
        t = 0
        for i in range(len(self.__accounts)):
            t += self.__accounts[i].balance
        print(f"当前银行所有存款为:{t}")


bank = Bank()
bank.create_account()
# bank.login()
# bank.save()
# bank.get()
# bank.total()
