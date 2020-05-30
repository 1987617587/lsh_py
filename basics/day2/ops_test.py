"""
# author Liu shi hao
# date: 2019/11/6 10:35
# file_name: ops_test

"""
# age = int(input("年龄："))
# print(0 < age < 100)
# num1 = int(input("第一个数："))
# num2 = int(input("第二个数："))
# num3 = int(input("第三个数："))
# print(num1 > (num2 and num3))
# 字符串的比较方式
# 从左到右依次比较
# “0”-“9”<“A”-“Z”<"a"-"z"
#   48-57       65-90      97-122

# num1 = input("第一个数：")
# num2 = input("第二个数：")
# num3 = input("第三个数：")
# print(num1 > (num2 and num3))
#
# num1 = ""
# print(num1 is None)
# num2 = None
# print(num2 is None)


# 任意进制转换
# def pares():
#     pares_str = ""
#     num3 = int(input("请输入数字:"))
#     base = int(input("请输入转换进制n:"))
#     while num3 != 0:
#         pares_str += str(num3 % base)
#         num3 //= base
#     print(pares_str)
#
#
# pares()
#
# pwd = int(input("请输入登录密码："))
# key = 123456
# # 密码加密
# encrypt_pwd = pwd ^ key
# pwd_in = int(input("请输入密码:"))
# print(encrypt_pwd == pwd_in ^ key)

# is_boy = input("请问你是男生吗（y/n）:")
# if is_boy == "y":
#     is_1911 = input("请问你是1911的学生吗（y/n）")
#     if is_1911 == "y":
#         print("come in!")
#         pass
#     else:
#         print("out!")
#     pass
# print("ok!")
#
# 输入用户年龄：
# 18岁以下是未成年人
# 否则是成年人

# age = int(input("请输入年龄："))
# if 0 < age < 149:
#     if 0 < age < 18:
#         print("未成年")
#     else:
#         print("成年")
# else:
#     print("年龄不合法！")


# 1.
# 输入用户年龄：
# 16岁以下（包含16岁）是少年
# 17到40是青年
# 41到60是中年人
# 剩下的是老年人
import random


# age = int(input("请输入用户年龄："))
# if 0 < age < 150:
#     if age <= 16:
#         print("少年")
#     elif age <= 40:
#         print("青年")
#     elif age <= 60:
#         print("中年人")
#     else:
#         print("老年人")
# else:
#     print("年龄非人类！")
#
# print(random.randint(1, 10))  # 产生 1 到 10 的一个整数型随机数
# print(random.random())  # 产生 0 到 1 之间的随机浮点数
# print(random.uniform(1.1, 5.4))  # 产生  1.1 到 5.4 之间的随机浮点数，区间可以不是整数
# print(random.choice('tomorrow'))  # 从序列中随机选取一个元素
# print(random.randrange(1, 100, 2))  # 生成从1到100的间隔为2的随机整数
# print(random.randint(1, 2))


# 三元表达式
# guess = random.choice("123")
# guess = "石头" if guess == "1" else("剪刀"if guess == "2" else "布")
# print(guess)
# 2.
# 猜拳游戏：
# 使用判断语句，完成石头剪刀布的猜拳游戏。
#
# def finger_guessing():
#     guess1 = input("请用户选择输入石头, 剪刀, 布：")
#     # guess1 = random.choice(["石头", "剪刀", "布"])
#     guess2 = random.choice(["石头", "剪刀", "布"])
#     player1 = "用户玩家"
#     player2 = "电脑玩家"
#     # 80%
#     # random [1,1000] 1-200人赢
#     r = random.randint(1, 1000)
#     if 1 < r < 800:
#         print("用户玩家出石头，电脑玩家出剪刀,用户玩家赢")  # 假装游戏正规运行,偷改省略
#     else:
#         if guess1 == "石头" and guess2 == "剪刀":
#             print(f"{player1}出{guess1}，{player2}出{guess2},{player1}赢")
#         elif guess1 == "剪刀" and guess2 == "布":
#             print(f"{player1}出{guess1}，{player2}出{guess2},{player1}赢")
#         elif guess1 == "布" and guess2 == "石头":
#             print(f"{player1}出{guess1}，{player2}出{guess2},{player1}赢")
#         elif guess1 == guess2:
#             print(f"{player1}出{guess1}，{player2}出{guess2},平局")
#         else:
#             print(f"{player1}出{guess1}，{player2}出{guess2},{player2}赢")
#
#
# n = int(input("你要玩几次猜拳游戏："))
# for i in range(n):
#     finger_guessing()
# # 押注
# user_choice = input("请选择押注玩家（1/2）：")

# print(random.choice(["石头", "剪刀", "布"]))   # 从序列中随机选取一个元素
# 3.根据1,2,3,4,5,6,7 输出星期一到星期天
# in_num = int(input("请输入1-7："))
# for i in range(7):
#     if in_num == i:
#         print(f"星期{in_num}")

# 4.根据用户按键，做出不一样的动作响应
# key_num = input("请选择输入按键")
# if key_num == "j":
#     print("一技能")
# elif key_num == "i":
#     print("二技能")
# elif key_num == "o":
#     print("三技能")
# elif key_num == "k":
#     print("大招")
# else:
#     print("原地不动")


# 1.打印九九乘法:
# 1*1=1
# 1*2=2 2*2=4
# 1*3=3 2*3=6 3*3=9
#

# for i in range(1, 10):
#     for j in range(1, i + 1):
#         print(f"{j}X{i} = {i * j}\t", end=" ")
#     print()
# 2.打印下面的图形：
#
# *
#  **
#   ***


# 3.根据给定的整数n，生成一个n×n的单位矩阵（即主对角线上的元素值均为1，其余元素值均为0的矩阵），并显示输出
# n:5
# 1 0 0 0 1
# 0 1 0 1 0
# 0 0 1 0 0
# 0 1 0 1 0
# 1 0 0 0 1
# i:行数
# j:列数
# 为1的位置的行列值：
# 0,0
# 0,4
# 1,1
# 1,3
# 2,2
# 3,1
# 3,3
# 4,0
# 4,4
# // 若要为1：i==j or i+j==n-1



# for i in range(7):
#     for j in range(8):
#         print("$",end="\t")
#     print()



# 2.打印下面的图形：
#
# *
#  **
#   ***
# n_2 = int(input("请输入行数："))
# for i in range(n_2 ):
#     # for j in range(2*i+1):
#     print(" "*(i+1)+"*"*(i+1))

# 3.根据给定的整数n，生成一个n×n的单位矩阵（即主对角线上的元素值均为1，
# 其余元素值均为0的矩阵），并显示输出
# n:5
# 1 0 0 0 1
# 0 1 0 1 0
# 0 0 1 0 0
# 0 1 0 1 0
# 1 0 0 0 1
# i:行数
# j:列数
# 为1的位置的行列值：
# 0,0
# 0,4
# 1,1
# 1,3
# 2,2
# 3,1
# 3,3
# 4,0
# 4,4
# // 若要为1：i==j or i+j==n-1
# n_3 = int(input("请输入行数："))
# for i in  range(n_3):
#     for j in range(n_3):
#         print("1"if i==j or i+j==n_3 - 1 else"0",end=" ")
#         # if i==j or i+j==4:
#         #     print("1")
#         # else:
#         #     print("0")
#     print()









