# author:lzt
# date: 2019/11/8 9:25
# file_name: txt_task
# 基础语法：
# 1.编写一个程序，输入四个字符串存储到四个变量中，变量一,三交换 变量二,四交换，显示交换的结果。
# s1 = input("字符串:")
# s2 = input("字符串:")
# s3 = input("字符串:")
# s4 = input("字符串:")
#
# s1, s3 = s3, s1
# s2, s4 = s4, s2
# print(f"s1={s1} s2={s2} s3={s3} s4={s4}")
#
# 2.请输入一个圆的半径,求圆的面积和周长
# import math
#
# r = float(input("半径:"))
# print(f"半径为{r}的圆的面积为{math.pi * r * r} 周长为{2 * math.pi * r}")
#
# 3.求公元222年到公元2100年中所有的闰年 请从大到小依次打印
# for i in range(2100,221,-1):
#     # 判断是否为闰年
#     if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
#         print(i)

#
# 4.老师问学生,这道题你会做了吗?如果学生答"会了(y)",则可以放学.如果学生不会做(n),则老师再讲一遍,再问学生是否会做了......
# 直到学生会为止,才可以放学.
# 直到学生会或老师给他讲了10遍还不会,都要放学
#
# 5.请打印出九九乘法表.
# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6 3*3=9
# ....
#
# 6.2015年培养学员10000人，每年增长25%，请问按此增长速度，到哪一年培训学员人数将达到20万人？
#
# 7.已知两个三位数abc和cba之和为1333（即abc+cba=1333）求 a、b、c
# for a in range(1, 10):
#     for b in range(10):
#         for c in range(1, 10):
#             if a * 100 + 10 * b + c + c * 100 + b * 10 + a == 1333:
#                 print(a, b, c)
# for abc in range(100, 1000):
#     # a = abc // 100
#     # b = abc % 100 // 10
#     # c = abc % 10
#     a = int(str(abc)[0])
#     b = int(str(abc)[1])
#     c = int(str(abc)[2])
#     if a * 100 + 10 * b + c + c * 100 + b * 10 + a == 1333:
#         print(a, b, c)

#
# 8.人猿泰山第一天摘了桃子若干 每天吃掉前一天的一半多一个 到第10天发现只剩一个了
# 求泰山一共摘了多少桃子
# 纯程序思维:不停的试验试吃
# p_count = 10
#
# is_con = True
# while is_con:
#     # 试验数据
#     left = p_count
#     # 怎么试吃
#     for i in range(9):
#         left = left // 2 - 1
#
#     # 怎么检证是否正确
#     if left == 1:
#         print("试验成功！")
#         print(p_count)
#         is_con = False
#     else:
#         # 试验的数据应该+1
#         p_count += 1

# y x
# x = y//2-1
# y = (x+1)*2
# x = 1
# for i in range(9):
#     x = (x+1)*2
# print(x)


#
# 9.30人用餐 其中男人每人消费3元 女人每人2元 每个孩子1元 一共花了50美元 求男、女、小孩个几人
#
# 10.随机产生4个在[11-100]之间各不相同的随机数。
# import random
#
# eq = True
# while eq:
#     num1 = random.randint(11, 100)
#     num2 = random.randint(11, 100)
#     num3 = random.randint(11, 100)
#     num4 = random.randint(11, 100)
#
#     if num1 != num2 and num1 != num3 and num1 != num4 \
#             and num2 != num3 and num2 != num4 \
#             and num3 != num4:
#         eq = False
# print(num1, num2, num3, num4)

#
# 11.求1-100之间的所有差值为六的质数对。
#
# 12.韩信带兵不足百人，三人一行多一人，七人一行少两人，五人一行正好，求韩信点了多少兵？
for i in range(1000000):
    if i % 3 == 1 and i % 7 == 5 and i % 5 == 0:
        print(i)
