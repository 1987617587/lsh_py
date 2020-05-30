"""
# author Liu shi hao
# date: 2019/11/11 17:55
# file_name: day5_task

"""

#
import random

import math

# 定义in_int()函数，提示用户一直输入正确的整数为止
def in_int():
    while True:
        num = input("请输入整数：")
        if num.isdigit():
            return int(num)
        print("重新输入！")


# 1、编写函数，用户输入三个整数，将最大数和最小数输出
# def max_min(a, b, c):
#     if a > b and a > c:
#         num_max = a
#     elif b > a and b > c:
#         num_max = b
#     else:
#         num_max = c
#     if a < b and a < c:
#         num_min = a
#     elif b < a and b < c:
#         num_min = b
#     else:
#         num_min = c
#     return num_max, num_min


# print(max_min(a = in_int(),b = in_int(),c = in_int()))
# 2、编写函数将1~200末位数为5的整数求和返回
#
def bottom_num5():
    list = []
    for i in range(5, 200, 10):
        list.append(i)
    # print(list)
    return sum(list)


# print(bottom_num5())


# 3、编写函数将24的所有因子求积、求和
#
def factor_4():
    product = 1
    sum_factor = 0
    for i in range(1, 25):
        if 24 % i == 0:
            # print(i)
            product *= i
            sum_factor += i
    return product, sum_factor


# print(factor_4())


# 4、输入学员的语文、数学和英语三门课的成绩，计算平均成绩输出。
def in_score():
    while True:
        score = input("请输入成绩：")
        if score.isdigit() and 0 <= int(score) <= 100:
            return int(score)
        print("重新输入！")


def score_3(c, m, e):
    return (c + m + e) / 3


# print(score_3(in_score(), in_score(), in_score()))


# 5、输入一个圆的半径(int),并且输出这个圆的面积。
# #
def ircle_area():
    return in_int() ** 2 * math.pi


#
#
# print(f"圆的面积:{ircle_area()}")
# 6、企业发放的奖金根据利润提成。利润(I)低于或等于1万元时，奖金可提10%；
# 利润高于1万元，低于2万元时，低于1万元的部分按10%提成，高于1万元的部分，可提成7.5%；
# 2万到4万之间时，高于2万元的部分，可提成5%；4万到6万之间时高于4万元的部分，可提成3%；
# 6万到10万之间时，高于6万元的部分，可提成1.5%，
# 高于10万元时，超过10万元的部分按1%提成，从键盘输入当月利润I，求应发放奖金总数？编写相应的函数？
#
def bonus():
    profit = in_int()
    if profit < 0:
        return
    if profit <= 10000:  # if return 使用相当于elif
        return profit * 0.1
    if profit <= 20000:
        return 10000 * 0.1 + (profit - 10000) * 0.075
    if profit <= 40000:
        return 10000 * 0.1 + 10000 * 0.075 + (profit - 20000) * 0.05
    if profit <= 60000:
        return 10000 * 0.1 + 10000 * 0.075 + 20000 * 0.05 + (profit - 40000) * 0.03
    if profit <= 100000:
        return 10000 * 0.1 + 10000 * 0.075 + 20000 * 0.05 + 20000 * 0.03 + (profit - 60000) * 0.015
    return 10000 * 0.1 + 10000 * 0.075 + 20000 * 0.05 + 20000 * 0.03 + 40000 * 0.015 + (profit - 100000) * 0.01


# print(f"应发放奖金总数:{bonus()}")
# 7、超市收银系统规定，消费满500元的可以打9.8折，消费满800元可以打9.5折，
# 消费满1000元可以打9折，先要求输入消费数额，
# 显示应收金额及折扣金额——“您合计收费***元  本次收***元  为您节省***元”
#
# def collect_money():
#     pay_money = in_int()
#     if pay_money >=500:
#         discount = 0.98
#     elif pay_money >=800:
#         discount = 0.95
#     elif pay_money >=1000:
#         discount = 0.9
#     else:
#         discount = 1
#     discount_money = discount * pay_money
#     # return pay_money,discount_money,pay_money-discount_money
#     print(f"您合计收费{pay_money}元  本次收{discount_money}元  为您节省{pay_money-discount_money}元")
#
#
# collect_money()
# 8、本金10000元存入银行，年利率是千分之三。每过1年，将本金和利息相加作为新的本金。计算5年后，获得的本金是多少？
#
# principal = 10000
# for i in range(5):
#     principal+=principal*0.003
#
# print(principal)
# 9、编写一个游戏级别评分器，循环录入每一局（共10局）的游戏得分，显示输出游戏级别。
# 评分标准：10局中如果90%达到80以上，为一级，如果60%达到80之上为二级，其余为三级。
#
# def grade():
#     j = 0
#     for i in range(10):
#         if in_score()>80:
#             j+=1
#     print("一级")if j >=9  else print("二级")if 6<=j<=8 else print("三级")
#
# grade()

# 10、登录QQ时，QQ号和密码必须正确并且匹配才能够登录成功。
# 假设最多只允许用户输入三次，中间任何一次输入正确，则给出提示：登录成功。
# 如第一次输入信息有误，则给出提示：QQ号或密码输入有误，请重新输入，您还有2次机会。
# 第二次还输入有误，则给出：QQ号或密码输入有误，请重新输入，您还有1次机会。
# 第三次如输入还有误，则给出提示：您三次输入都有误，请与管理员联系。
#
def register():
    in_next = 3
    for i in range(3):
        user_name = input("请输入用户名：")
        user_pwd = input("请输入密码：")
        if user_name != "admin" or user_pwd != "88888":
            print(f"QQ号或密码输入有误，请重新输入，您还有{2 - i}次机会。") if i != 2 else print("您三次输入都有误，请与管理员联系")
        else:
            print("登录成功")
            return


# register()


# 11、编写函数从键盘输入2016年的某个月份，得到当月的天数
#

# def days_month():
#
#     month = in_int()
#     if month in [1, 3, 5, 7, 8, 10, 12]:
#         print("这个月的天数为31")
#     elif month in [4, 6, 9, 11]:
#         print("这个月的天数为30")
#     elif month == 2:
#         print("这个月的天数为29")
# days_month()

# def years_months_days(years=in_int(), months=in_int()):
#     days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
#         days[1] = 29
#
#     return days[months - 1]
#
# print(f"这个月的天数为{years_months_days()}")
# 12、编写函数输入两个数m和n，分别输出这两个数的最大公约数和最小公倍数

def common_num(a,b):
    c= a if a<b else b
    for i in range(c,a*b+1):
        if i%a==0 and i%b ==0:
            # common_multiple= i
            print(f"最小公倍约数:{i}")
            break
    for j in range(c,0,-1):
        if a%j==0 and b%j ==0:
            # common_divisor= j
            print(f"最大公约数:{j}")
            break
# common_num(in_int(),in_int())

# 玩家进来以后要买筹码；
# # 在每次掷骰子前，
# #     要下注（50~手里剩余的筹码）;
# #     接着要选择买大小；
# #     程序要模仿掷骰子，产生一个1~6的随机数
# #     根据掷骰子的结果，判断玩家的输赢，改变玩家的手里的筹码
# #         如果买大，4~6是赢，1~3是输
# #         如果小，1~3是赢，4~6是输
# #         如果赢了，玩家的筹码+=下注金额
# #         如果输了，玩家的筹码-=下注金额    
# #     提示玩家是否要退出游戏
# #     玩家手里的筹码小于最小下注金额，要强制玩家退出
# # 注意 ：先理清楚思路，从宏观上考虑流程，不要考虑每个步骤的细节。流程搞清楚以后，再琢磨每个步骤的细节。然后写代码。
#
def in_pay():
    while True:
        num = input("请输入下注金额：")
        if num.isdigit():
            return int(num)
        print("重新输入下注金额！")


def stake(chip):
    while chip > 0:
        print(f"欢迎进入掷骰子游戏，您的目前筹码为{chip}")
        Stake = in_pay()
        if chip < Stake:
            print("筹码小于最小下注金额，强制玩家退出!")
            break
        dice_num = random.randint(1, 6)
        result_num = "大" and "9" if dice_num > 3 else "小" and "0"
        guess = input("请选择买大(9)还是买小(0)：")
        if guess == result_num:
            chip += Stake
            print(f"￥+￥+ 骰子数是{dice_num}本次猜{guess}赢了，筹码为{chip}")
        else:
            chip -= Stake
            print(f"￥-￥- 骰子数是{dice_num}本次猜{guess}输了，筹码为{chip}")
        an = input("￥0￥0 玩家是否要退出游戏（y/n）:")
        if an == "y":
            print("*****************已退出！*****************")
            break
    else:
        print("<<<<<筹码不足已退出游戏！您可前往商城充值后再次进入游戏>>>>>")



# stake(50000)
# 选作：
# 1、输入一段字符判断是大写，还是小写。若是小写，转换为大写，若是大写，转换为小写
#
list_a_z = [chr(i) for i in range(97, 123)]
list_A_Z = [chr(i) for i in range(65, 91)]
def in_char():
    while True:
        list_char = list(input("请输入一段字符："))
        for i in range(len(list_char)-1):
            if list_char[i] in list_a_z:
                list_char[i]= list_A_Z[list_a_z.index(list_char[i])]
            if list_char[i] in list_A_Z:
                list_char[i] = list_a_z[list_A_Z.index(list_char[i])]
        print(str(list_char))
        return
# in_char()
# 2、一列数的规则如下: 1、1、2、3、5、8、13、21、34...... 求第30位数
# 是多少， 用递归算法实现。
#
# list_2 = [1,1,2,3,5,8,13,21,34]
# for i in range(30-len(list_2)):
#     list_2.append(list_2[-1] + list_2[-2])
# print(list_2)


# 3、请编程实现对一个数组的排序，结果从大到小
#
def int_rank():
    num_list = [1,8,4,3,9]
    rank_list=[]
    num_list.append(in_int())
    for i in range(len(num_list)):
        rank_list.append(max(num_list))
        num_list.remove(max(num_list))
    print(rank_list)
# int_rank()
# 4、接收一个整数(1-26之间),打印A-Z之间图形。如接收26，则打印如下图形
#      (char)65-->A   (char)66-->B
#      以此类推
#                                    A
#                                   BBB
#                                  CCCCC
#                                 DDDDDDD
#                                EEEEEEEEE
#                               FFFFFFFFFFF
#                              GGGGGGGGGGGGG
#                             HHHHHHHHHHHHHHH
#                            IIIIIIIIIIIIIIIII
#                           JJJJJJJJJJJJJJJJJJJ
#                          KKKKKKKKKKKKKKKKKKKKK
#                         LLLLLLLLLLLLLLLLLLLLLLL
#                        MMMMMMMMMMMMMMMMMMMMMMMMM
#                       NNNNNNNNNNNNNNNNNNNNNNNNNNN
#                      OOOOOOOOOOOOOOOOOOOOOOOOOOOOO
#                     PPPPPPPPPPPPPPPPPPPPPPPPPPPPPPP
#                    QQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQQ
#                   RRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRRR
#                  SSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS
#                 TTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTTT
#                UUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUUU
#               VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV
#              WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW
#             XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
#            YYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY
#           ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ
#
def in_1_26():
    while True:
        score = input("请输入1-26（打印行数）：")
        if score.isdigit() and 1 <= int(score) <= 26:
            return int(score)
        print("重新输入！")
def figure_A_Z():
    n = in_1_26()
    for i in range(1, n + 1):
        print(" " * (n - i) + chr(64 + i) * (2 * i - 1))
# figure_A_Z()
# 5. 键盘输入一个整数(0-9之间)，显示如下图形(n=5)
#     12345
#      2345
#       345
#        45
#         5
#
# def figure_0_9():
#     n_5 = in_int()
#     if n_5 >9 or n_5<0:
#             print("暂只能满足0-9之间打印！")
#     else:
#         for j in range(5):
#             for i in range(j, 6):
#                 if i <= j:
#                     print(" " * j, end="")
#                 else:
#                     print(chr(48 + i), end="")
#             print()
# figure_0_9()
# 6、输入一个奇数显示以下图型（如：num=5）
#  *****            " ",0,*,5
#   ***            " ",1,*,3
#    *            " ",2,*,1
#   ***            " ",1,*,3
#  *****            " ",0,*,5
# def figure_odd():
#     n_11 = in_int()
#     if n_11 % 2 == 0:
#         print("输入值非奇数无法打印！")
#     else:
#         for i in range(n_11):
#             if i <= n_11 // 2:
#                 print(" " * i + "*" * (n_11 - i * 2))
#             else:
#                 print(" " * (n_11 - i - 1) + "*" * (i * 2 - n_11 + 2))
#             pass
#         pass


# 编程实现如下图列出的图形。(放在此处作为上题参考！)
#   *
#  ***
#  *****
# *******
#  *****
#   ***
#   *
# n_11 = int(input("请输入奇位行数："))
# if n_11 % 2==0:
#     print("无法打印！")
# else:
#     for i in range(n_11):
#         if i <= n_11 // 2:
#             print(" " * (n_11 // 2 - i) + "*" * (2 * i + 1))
#         else:
#             print(" " * (i - n_11 // 2) + "*" * ((n_11 - i) * 2 - 1))
#         pass
#     pass
