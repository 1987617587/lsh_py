"""
# author Liu shi hao
# date: 2019/11/15 18:42
# file_name: day9_task

"""
# 9.
# 编写一个时间类My_Time，包含一个三个参数的初始化方法，3个属性hour,minute,second,
# 再加上一个转换成字符串的方法to_string。
#
# 注意：请注意时分秒的取值范围
#
class MyTime:

    def __init__(self, hour, minute, second) -> None:
        super().__init__()
        self.hour = hour
        self.minute = minute
        self.second = second

    def to_string(self):
        if 0 <= self.hour <= 23 and 0 <= self.minute <= 59 and 0 <= self.second <= 59:
            return str(self.hour) + "时" + str(self.minute) + "分" + str(self.second) + "秒"
        else:
            print(f"时间格式错误，无法转换！")
            return False


my_time1 = MyTime(1, "2", 403)


print(my_time1.to_string())
#
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

    def to_string(self):  # 创建闰年，平年月份对应天数列表
        list_leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        list_common_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if self.year > 0 and 0 < self.month <= 12 and self.day > 0:
            if (self.year % 4 == 0 and self.year % 100 != 0 or self.year % 400 == 0) and \
                    self.day > list_leap_year[self.month - 1] or self.year % 4 != 0 and \
                    self.day > list_common_year[self.month - 1]:
                print(f"时间格式错误，无法转换！")
                return False
            else:
                return str(self.year) + "年" + str(self.month) + "月" + str(self.day) + "日"
        else:
            print(f"时间格式错误，无法转换！")
            return False


my_date1 = MyDate(2000, 2, 29)
print(my_date1.to_string())


#
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
        if self.n1 == 0 or self.n2 == 0:
            print("无法执行除运算！")
            return False
        else:
            division = self.n1 / self.n2
            return division


num1 = Number(1, 2)
# print(num1.addition())
# print(num1.division())
# print(num1.multiplication())
# print(num1.minus())
