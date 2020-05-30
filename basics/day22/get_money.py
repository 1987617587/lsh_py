"""
# author Liu shi hao
# date: 2019/12/3 17:26
# file_name: get_money

"""
# 在定义银行类时,若取钱数大于余额则作为异常处理
# (InsufficientFundsException).
# 思路:产生异常的条件是余额少于取额,  因此是否抛出异常
# 要判断条件
# 取钱是Withdrawal 方法中定义的动作,因此在该方法中产生
# 异常.
# 处理异常安排在调用Withdrawal 的时候,因此Withdrawal
# 方法要声明异常,由上级方法调用
# 要定义好自己的异常类
# 要求：捕捉到的异常对象内有余额和取额的信息

class GetmoneyError(Exception):

    def __init__(self, acc, get_money) -> None:
        super().__init__()
        self.acc = acc
        self.get_money = get_money

    def __str__(self) -> str:
        return f"异常发生的账户是{self.acc.acc_id}，" \
            f"情况为取款金额{self.get_money}，超出账户余额{self.acc.money}"


class Account:

    def __init__(self, acc_id, money) -> None:
        super().__init__()
        self.acc_id = acc_id
        self.money = money

    def withdraw(self, get_money):
        if 0 < get_money < self.money:
            return get_money
        else:
            # print("余额不足")
            # pass
            raise GetmoneyError(self, get_money)


if __name__ == '__main__':
    try:
        acc = Account("001", 123)
        acc.withdraw(244)
    except GetmoneyError as e:
        print(e)


# 作业一
# 自定义一个学生类，属性有 姓名 年龄，如果用户在给学生年龄赋值时，
# 年龄小于0抛出一个AgeLT0Exception，大于150  抛出一个AgeGT150Exception
class AgeLT0Exception(Exception):

    def __init__(self, name, set_age) -> None:
        super().__init__()
        self.name = name
        self.set_age = set_age

    def __str__(self) -> str:
        return f"异常发生的学生姓名是{self.name}，" \
            f"情况为赋值年龄{self.set_age}小于0"


class AgeGT150Exception(Exception):

    def __init__(self, name, age) -> None:
        super().__init__()
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"异常发生的学生姓名是{self.name}，" \
            f"情况为赋值年龄{self.age}大于150"


class Student:
    def __init__(self, name, age=0) -> None:
        super().__init__()
        self.__name = name
        self.__age = age

    @property
    def name(self):
        return self.__name

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 0:
            self.__age = 0
            raise AgeLT0Exception(self.name, value)
        if value > 150:
            self.__age = 0
            raise AgeGT150Exception(self.name, value)
        self.__age = value


s = Student("sa")
if __name__ == '__main__':
    try:
        s.age = 199
    except AgeGT150Exception as e:
        print(e)
    except AgeLT0Exception as e:
        print(e)
