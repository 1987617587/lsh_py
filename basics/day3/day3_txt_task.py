"""
# author Liu shi hao
# date: 2019/11/7 16:02
# file_name: text_test

"""
import random

import math
# 基础语法：
# 1.编写一个程序，输入四个字符串存储到四个变量中，变量一,三交换 变量二,四交换，显示交换的结果。
#
# str_1 = input("请输入变量一：")
# str_2 = input("请输入变量二：")
# str_3 = input("请输入变量三：")
# str_4 = input("请输入变量四：")
# str_1,str_3 =str_3,str_1
# str_2,str_4 =str_2,str_4
# print(f"变量一:{str_1}变量二:{str_2}变量三:{str_3}变量四:{str_4}")
# 2.请输入一个圆的半径,求圆的面积和周长
#

# r = int(input("请输入圆的半径;"))
# print(f"圆的面积为：{r ** 2 * math.pi}周长为：{2 * r * math.pi}")
# 3.求公元222年到公元2100年中所有的闰年 请从大到小依次打印
#
# for i in range(2100,222,-1):
#     # if (i % 4 == 0 and i % 100 != 0 )or i % 400 == 0:
#     #     print(i)
#     print(i)if (i % 4 == 0 and i % 100 != 0 or i % 400 == 0)else None
# 4.老师问学生,这道题你会做了吗?如果学生答"会了(y)",则可以放学.如果学生不会做(n),则老师再讲一遍,再问学生是否会做了......
# 直到学生会为止,才可以放学.
# 直到学生会或老师给他讲了10遍还不会,都要放学
#

# for i in range(9):
#      an = input("这道题你会做了吗?(y/n):")
#      if an == "y":
#          print("可以放学")
#          break
#      else:
#          print("老师再讲一遍")
# print("放学")
# 5.请打印出九九乘法表.
# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6 3*3=9
# ....
#

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j}x{i}={i * j}", end="\t")
#     print()

# 7.已知两个三位数abc和cba之和为1333（即abc+cba=1333）求 a、b、c
# for i in range(100,1000):
#     str_i = str(i)
#     print(f"{i}")if int(str_i[2]) * 100 + int(str_i[1]) * 10 + int(str_i[0]) + i == 1333 else None


# 8.人猿泰山第一天摘了桃子若干 每天吃掉前一天的一半多一个
# 到第10天发现只剩一个了 求泰山一共摘了多少桃子
#
# peach_count = 1
# for i in range(9):
#     peach_count = (peach_count + 1) * 2
# print(peach_count)
# 9.30人用餐 其中男人每人消费3元 女人每人2元 每个孩子1元 一共花了50美元 求男、女、小孩个几人
#
# for i in range(31):
#     for j in range(25):
#         for k in range(11):
#             if i + j * 2 + k * 3 == 50 and i + j + k == 30:
#                 print(f"男{k}、女{j}、小孩{i}")
#
#                 break
# 10.随机产生4个在[11-100]之间各不相同的随机数。
#
list_10 =[]
for i in range(4):
    num_1 = random.randint(11, 100)
    list_10.append(num_1)
    if num_1 not in list_10:
        list_10 = list_10.append(random.randint(11, 100))
print(list_10)
# 11.求1-100之间的所有差值为六的质数对。
list11 = []
for i in range(100, 1, -1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        list11.append(i)
print(list11)
for i in range(len(list11)):
    if list11[i - 1] - list11[i] == 6:
        print(list11[i - 1], list11[i])

# 12.韩信带兵不足百人，三人一行多一人，七人一行少两人，五人一行正好，求韩信点了多少兵？
# for i in range(100):
#     if i % 3 == 1 and i % 7 == 5 and i % 5 == 0:
#         print(f"韩信点了{i}兵")
