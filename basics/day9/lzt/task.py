# author:lzt
# date: 2019/11/18 9:34
# file_name: task
# 9.
# 编写一个时间类My_Time，包含一个三个参数的初始化方法，3个属性hour,minute,second,
# 再加上一个转换成字符串的方法to_string。
# 注意：请注意时分秒的取值范围
class MyTime:

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
        if value < 0 or value >= 24:
            print("时间设定无效 已设定默认值0")
            self.__hour = 0
            return
        self.__hour = value
        pass

    @property
    def minute(self):
        return self.__minute

    @minute.setter
    def minute(self, value):
        if value < 0 or value >= 60:
            print("分钟设定无效 已设定默认值0")
            self.__minute = 0
            return
        self.__minute = value
        pass

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, value):
        if value < 0 or value >= 60:
            print("秒数设定无效 已设定默认值0")
            self.__second = 0
            return
        self.__second = value
        pass

    def to_string(self):
        return f"{self.__hour}:{self.__minute}:{self.__second}"


# mt1 = MyTime(5, 10, 6)
# print(mt1.to_string())
#
#
# 10.
# 编写一个日期类My_Date，包含一个初始化方法，3个属性year,month,day，再加上一个转换成字符串的方法to_string。
# 请注意月和日的取值范围
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
        if value <= 0:
            print("年份无效 已设定1")
            self.__year = 1
            return
        self.__year = value
        pass

    @property
    def month(self):
        return self.__month

    @month.setter
    def month(self, value):
        if value <= 0 or value > 12:
            print("月份设定无效 已设定默认值1")
            self.__month = 1
            return
        self.__month = value
        pass

    @property
    def day(self):
        return self.__day

    @day.setter
    def day(self, value):
        # value的异常数据:1.<=0 2.不允许超过本月最大的天数
        if value <= 0 or value > self.max_month_days():
            print("日期设定无效 已设定默认值1")
            self.__day = 1
            return
        self.__day = value
        pass

    def max_month_days(self):
        month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        # 判断是否闰年
        if self.__month == 2 and (self.__year % 4 == 0 and self.__year % 100 != 0 or self.__year % 400 == 0):
            return 29
        return month_days[self.__month - 1]

    def to_string(self):
        return f"{self.__year}/{self.__month}/{self.__day}"


# d1 = MyDate(2000, 4, 31)
# print(d1.to_string())

# 模拟简单的计算器。
# 定义名为Number的类，其中有两个整型数据对象n1和n2，声明为公有。
# 编写初始化方法，赋予n1和n2初始值，再为该类定义加（addition）、减（subtration）、
# 乘（multiplication）、除（division）等公有对象方法，分别对两个属性执行加、减、乘、除的运算。
# 创建Number类的对象，调用各个方法，并显示计算结果。
class Number:

    def __init__(self, n1, n2) -> None:
        super().__init__()
        self.n1 = n1
        self.n2 = n2

    def addition(self):
        return self.n1 + self.n2

    def subtration(self):
        return self.n1 - self.n2

    def multiplication(self):
        return self.n1 * self.n2

    def division(self):
        return self.n1 / self.n2 if self.n2 != 0 else "错误"


# num = Number(1, 0)
# print(num.addition())
# print(num.subtration())
# print(num.multiplication())
# print(num.division())

