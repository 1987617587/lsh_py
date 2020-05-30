# author:lzt
# date: 2019/11/12 9:28
# file_name: task
# 1、编写函数，用户输入三个整数，将最大数和最小数输出
import math


def task1():
    num1 = int(input("整数:"))
    num2 = int(input("整数:"))
    num3 = int(input("整数:"))
    # print(max(num1, num2, num3), min(num1, num2, num3))
    return max(num1, num2, num3), min(num1, num2, num3)


# 测试1:
# 获取用户的三个数 找到最大最小值输出
# print(task1())
#
# # 获取用户的三个数 找到最大值最小值 求和
# max_num, min_num = task1()
# print(max_num + min_num)
#
# 2、编写函数将1~200末位数为5的整数求和返回
def task2():
    sum = 0
    for i in range(1, 201):
        if i % 10 == 5:
            sum += i
            pass
        pass
    return sum


# 测试2:
# print(task2())
#
# 3、编写函数将24的所有因子求积、求和
def task3():
    sum = 0
    mu = 1
    for i in range(1, 25):
        if 24 % i == 0:
            sum += i
            mu *= i
    return sum, mu


# print(task3())
#
# 4、输入学员的语文、数学和英语三门课的成绩，计算平均成绩输出。
def task4():
    ch = int(input("语文成绩："))
    math = int(input("数学成绩："))
    en = int(input("英语成绩："))
    return (ch + math + en) / 3


# print(task4())
#
# 5、输入一个圆的半径(int),并且输出这个圆的面积。
def area():
    r = int(input("半径:"))
    return math.pi * r * r


# print(area())
#
# 6、企业发放的奖金根据利润提成。利润(I)低于或等于1万元时，奖金可提10%；
# 利润高于1万元，低于2万元时，低于1万元的部分按10%提成，
# 高于1万元的部分，可提成7.5%；2万到4万之间时，高于2万元的部分，可提成5%；
# 4万到6万之间时高于4万元的部分，可提成3%；6万到10万之间时，高于6万元的部分，可提成1.5%，
# 高于10万元时，超过10万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？编写相应的函数？
def task6():
    sale = int(input("利润:"))
    if sale < 0:
        return
    if sale <= 10000:
        return sale * 0.1
    if sale <= 20000:
        return 10000 * 0.1 + (sale - 10000) * 0.075
    if sale <= 40000:
        return 10000 * 0.1 + 10000 * 0.075 + (sale - 20000) * 0.05
    if sale <= 60000:
        return 10000 * 0.1 + 10000 * 0.075 + 20000 * 0.05 + (sale - 40000) * 0.03
    if sale <= 100000:
        return 10000 * 0.1 + 10000 * 0.075 + 20000 * 0.05 + 20000 * 0.03 + (sale - 60000) * 0.015
    return 10000 * 0.1 + 10000 * 0.075 + 20000 * 0.05 + 20000 * 0.03 + 40000 * 0.015 + (sale - 100000) * 0.01


# print(task6())
#
# 7、超市收银系统规定，消费满500元的可以打9.8折，消费满800元可以打9.5折，消费满1000元可以打9折，
# 先要求输入消费数额，显示应收金额及折扣金额——“您合计收费***元  本次收***元  为您节省***元”
#
def task7():
    pay = float(input("消费的钱数:"))
    if pay < 0:
        return
    if pay < 500:
        return pay, pay
    if pay < 800:
        return pay, pay * 0.98
    if pay < 1000:
        return pay, pay * 0.95
    return pay, pay * 0.9


# pay1, pay2 = task7()
# print(f"您合计收费{pay1}元  本次收{pay2}元  为您节省{pay1 - pay2}元")
# 8、本金10000元存入银行，年利率是千分之三。每过1年，将本金和利息相加作为新的本金。
# 计算5年后，获得的本金是多少？
#
money = 10000
per = 0.003
years = 5


def task8():
    global money
    for i in range(years):
        money += money * per


# task8()
# print(money)

# 9、编写一个游戏级别评分器，循环录入每一局（共10局）的游戏得分，显示输出游戏级别。
# 评分标准：10局中如果90%达到80以上，为一级，如果60%达到80之上为二级，其余为三级。
def task9():
    count = 0
    for i in range(10):
        s = int(input("每局得分:"))
        if s > 80:
            count += 1
    if count >= 9:
        return "一级"
    if count >= 6:
        return "二级"
    return "三级"


# print(task9())

#
# 10、登录QQ时，QQ号和密码必须正确并且匹配才能够登录成功。
# 假设最多只允许用户输入三次，中间任何一次输入正确，则给出提示：登录成功。如第一次输入信息有误，
# 则给出提示：QQ号或密码输入有误，请重新输入，
# 您还有2次机会。第二次还输入有误，
# 则给出：QQ号或密码输入有误，请重新输入，
# 您还有1次机会。第三次如输入还有误，则给出提示：您三次输入都有误，请与管理员联系。
def task10():
    for i in range(3):
        qq_num = input("QQ号:")
        password = input("密码:")
        if qq_num == "123456" and password == "123456":
            return True
        print(f"QQ号或密码输入有误，请重新输入，您还有{2 - i}次机会。"
              if i != 2 else "您三次输入都有误，请与管理员联系。")
    return False


# if task10():
#     print("登录成功")
# else:
#     print("登录失败")
#
# 11、编写函数从键盘输入2016年的某个月份，得到当月的天数
def task11():
    year = 2016
    month = int(input("月份:(1-12)"))
    if month < 1 or month > 12:
        print("月份无效")
        return
    month_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return month_days[month - 1]


# days = task11()
# if days is not None:
#     print(days)
#
# 12、编写函数输入两个数m和n，分别输出这两个数的最大公约数和最小公倍数
def task12():
    m = int(input("m:"))
    n = int(input("n:"))
    min_num = min(m, n)

    for i in range(min_num, 0, -1):
        if m % i == 0 and n % i == 0:
            return m, n, i


# m1, n1, ret = task12()
# print(f"{m1}和{n1}的最大公约数是{ret},最小公倍数是{m1 * n1 / ret}")





