"""
# author Liu shi hao
# date: 2019/11/5 20:01
# file_name: test

#"""
# 示例：
# 1.已知银行一年期整存整取的储蓄年利率为4.14%，在利率保持不变的情况下，经过多少年后，1000元存款能增值到2000元以上？
#
# per = 0.0414
# money = 1000
# years = 0
# while money < 2000:
#     money += money * per
#     years += 1
# print(years)
# 2.模拟两个玩家PK过程。
import random

player1 = "玩家1"
player2 = "玩家2"
MP1 = 500
MP2 = 500


# def pk():
#     blood_flow1 = 3000
#     blood_flow2 = 3000
#     while blood_flow1 > 0 and blood_flow2 > 0:
#         fis = random.randint(0, 1)
#         if fis == 0:
#             print(f"本回合，{player1}先出招")
#             blood_flow2 = blood_flow2 - MP1 if blood_flow2 - MP1 > 0 else 0
#             print(f"{player1}攻击{player2}，伤害是{MP1}，{player2}血量剩余：{ blood_flow2}")
#             if blood_flow1 <= 0 or blood_flow2 <= 0:
#                 break
#             blood_flow1 = blood_flow1 - MP2 if blood_flow1 - MP2 > 0 else 0
#             print(f"{player2}攻击{player1}，伤害是{MP2},{player1}血量剩余：{ blood_flow1}")
#         else:
#             print(f"本回合，{player2}先出招")
#             blood_flow1 = blood_flow1 - MP2 if blood_flow1 - MP2 > 0 else 0
#             print(f"{player2}攻击{player1}，伤害是{MP2},{player1}血量剩余：{ blood_flow1}")
#             if blood_flow1 <= 0 or blood_flow2 <= 0:
#                 break
#             blood_flow2 = blood_flow2 - MP1 if blood_flow2 - MP1 > 0 else 0
#             print(f"{player1}攻击{player2}，伤害是{MP1}，{player2}血量剩余：{ blood_flow2}")
#     print(f"{player1}死亡，游戏结束") if blood_flow1 < blood_flow2 else print(f"{player2}死亡，游戏结束")
#
# pk()
#
# 6.2015年培养学员10000人，每年增长25%，请问按此增长速度，到哪一年培训学员人数将达到20万人？
# students = 10000
# years = 2015
# while students< 200000:
#     students += students*0.25
#     years += 1
# print(years)
# 1.
# 求10的阶乘
# n! = n(n-1)(n-2).....2 * 1

n = int(input("请输入n:"))
proportion = 1
while n > 0:
    proportion *= n
    n -= 1
print(proportion)
# 2.
# 求1-100偶数的和
# sum1 = 0
# j = 0
# while j <= 100:
#     sum1 += j
#     j += 2
# print(sum1)

#
# 1.计算1-1000的和
# sum2 = 0
# for i in range(1001):
#     sum2 += i
# print(sum2)

# 2.打印如下
#
# **
# ****
# ******
#
# n = int(input("请输入打印行数："))
# for i in range(n + 1):
#     print("*" * 2 * i)
# 3.打印如下
# *
# ***
# *****
# *******
# n = int(input("请输入打印行数："))
# for i in range(n):
#     print("*" * (2 * i + 1))
# 4.如何遍历一个字符串查看字符串中的每一个字符
# str_in = input("请输入一个字符串:")
# for i in range(len(str_in)):
#     print(str_in[i], end=" ")

# 计算并输出100以内的所有素数(质数)。
# 素数：按照素数的定义，在大于1的自然数中，除了1和它自身以外，不能被其它数整除的数即为素数。
list1 = []
for i in range(100, 1, -1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        list1.append(i)
print(list1)

# 计算并输出100以内的所有合数
list2 = []
sum = 0
for i in range(100, 1, -1):
    for j in range(2, i):
        if i % j == 0:
            list2.append(i)
            sum += i
            break
print(list2)
print(sum)