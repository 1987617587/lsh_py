"""
# author Liu shi hao
# date: 2019/11/5 19:47
# file_name: test_666

"""
import random

# 任务8：
# 编程实现如下图列出的图形。
# *
# ***
# *****
# *******
#
# n_8 = int(input("请输入打印行数："))
# for i in range(n):
#     print("*" * (2 * i + 1))
# 任务9：
# 让用户输入一个数显示下面内容。
# *******       
# ******        
# *****          
# ****           
# ***            
# **             
# *           
#   
# n_9 = int(input("请输入打印行数："))
# for i in range(n_9, 0, -1):
#     print("*" * i)
# 任务10：
# 编程实现如下图列出的图形。
#
#   *              
#   ***        
#  *****    
# *******
#
# n_10 = int(input("请输入打印行数："))
# for i in range(1, n_10 + 1):
#     print(" " * (n_10 - i) + "*" * (2 * i - 1))
# 任务11：
# 编程实现如下图列出的图形。
#   *
#   ***
#  *****
# *******
#  *****
#  ***
#   *
# #
# # lines = int(input("行数:"))
# # if lines % 2 == 0:
# #     print("该图形必须为奇数行")
# # else:
# #     # 上半部分的行数:(lines+1)//2
# #     for i in range((lines + 1) // 2):
# #         for j in range((lines + 1) // 2 - 1 - i):
# #             print(" ", end="")
# #         for j in range(2 * i + 1):
# #             print("*", end="")
# #         print()
# #     for i in range(lines // 2):
# #         # i: 0 1 2
# #         # k: 1 2 3 i+1
# #         for j in range(i + 1):
# #             print(" ", end="")
# #         # *: 5 3 1
# #         #  2 1 0 (lines//2-1-i)*2+1
# #         for j in range((lines // 2 - 1 - i) * 2 + 1):
# #             print("*", end="")
# #         print()
#
#
# # 任务12：
# #  鸡兔同笼，从上面看有35个头，从下面看有94只脚，请问鸡有几只，兔有几只？
# # for i in range(47):
# #     for j in range(35):
# #         if i + j == 35 and i * 2 + j * 4 == 94:
# #             print(f"鸡有{i}只，兔有{j}只")
#
# # 任务13：
# # 玩家进来以后要买筹码；
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
#
# def stake():
#     chip = 50
#     while chip > 0:
#         print(f"欢迎进入掷骰子游戏，您的目前筹码为{chip}")
#         Stake = int(input("请输入下注金额："))
#         if chip < Stake:
#             print("筹码小于最小下注金额，强制玩家退出!")
#             break
#         dice_num = random.randint(1, 6)
#         result_num = "大" if dice_num > 3 else "小"
#         guess = input("请选择买大还是买小：")
#         if guess == result_num:
#             chip += Stake
#             print(f"骰子数是{dice_num}本次猜{guess}赢了，筹码为{chip}")
#
#         else:
#             chip -= Stake
#             print(f"骰子数是{dice_num}本次猜{guess}输了，筹码为{chip}")
#         an = input("玩家是否要退出游戏（y/n）:")
#         if an == "y":
#             print("已退出！")
#             break
#     else:
#         print("已退出！")
#
#
# # 可选任务：
# # 1.一个自然数与3的和是5的倍数,与3的差是6的倍数,这个自然数最小是几?
# # for i in range(100):
# #     if (i + 3) % 5 == 0 and (i - 3) % 6 == 0:
# #         print(f"自然数最小是{i}")
# #         break
#
# # 2.在400--500之间求一个数,它被2除余1,被5除余3,被9除余1,这个数是多少?
# # num_2 = 400
# # while 400 <= num_2 <= 500:
# #     if num_2 % 2 == 1 and num_2 % 5 == 3 and num_2 % 9 == 1:
# #         print(num_2)
# #         break
# #     else:
# #         num_2 += 1
#
# # 3.有一些四位数,百位数字都是3,十位数字都是6,并且它们既能被2整除,又能被3整除,
# # 求这样的四位数中最大的和最小的两数各是几?
# #
# # for i in range(1000, 10000):
# #     if i % 2 == 0 and i % 3 == 0 and (i // 10) % 10 == 6 and (i // 100) % 10 == 3:
# #         min_num_3 = i
# #         print(f"最小值{min_num_3}")
# #         break
# # for j in range(10000, 1000, -1):
# #     if j % 2 == 0 and j % 3 == 0 and (j // 10) % 10 == 6 and (j // 100) % 10 == 3:
# #         max_num_3 = j
# #         print(f"最大值{max_num_3}")
# #         break
#
# # 4.编程求一个四位自然数ABCD,它乘以A后变成DCBA
# for i in range(1000, 10000):
#     if ((i // 1000) % 10) * i == (i // 1000) % 10 + (i // 100) % 10 * 10 \
#             + (i // 10) % 10 * 100 + i % 10 * 1000:
#         num_4 = i
#         print(f"四位自然数为{num_4}")
#         # break
# 5.编程求出满足以下条件的三位数:它除以11所得的商等于它各位数字之和.
#
# for i in range(100, 1000):
#     if i / 11 == (i // 100) % 10 + (i // 10) % 10 \
#             + i % 10:
#         num_5 = i
#         print(f"三位数为{num_5}")
# break
# 6.某数被80除所得的商,不但是7的倍数,而且用2,3,4,5,6去除余数都是1,求这个自然数.  
#
# num_6 = 80
# while num_6 >= 80:
#     if (num_6 // 80) % 7 == 0 and (num_6 // 80) % 2 == 1 and (num_6 // 80) % 3 == 1 \
#             and (num_6 // 80) % 4 == 1 and (num_6 // 80) % 5 == 1 and (num_6 // 80) % 6 == 1:
#         print(f"这个自然数是{num_6}")
#         break
#     else:
#         num_6 += 1

# 7.有一种最简真分数,它们的分子与分母的乘积都是140,把所有这样的真分数从小到大打印出来
#
# for i in range(140):
#     for j in range(140):
#         if i * j == 140 and i < j:
#             print(f"这样的真分有{i}/{j}")
# 8.一个五位数,若在它的后面写上一个7,得到一个六位数A,若在它前面写上一个7,
# 得到一个六位数B,B是A的五倍,求此五位数.
#
# for i in range(10000, 100000):
#     str_i = str(i)
#     num_8a = int(str_i + "7")
#     num_8b = int("7" + str_i)
#     if num_8b / num_8a == 5:
#         # print(num_8a)
#         # print(num_8b)
#         print(f"此五位数为{i}")
#         break

# 9.把123456789这个数乘以一个什么数,能使它的结果不但不含零,而且仍然是  
#  由1,2,3,4,5,6,7,8,9这九个数字组成的,只是顺序不同而已.
#
# str_9 = "123456789"
# for i in range(2, 10):
#     str_num9 = str(int(str_9) * i)
#     if "1" and "2" and "3" and "4" "1" and "5" and "6" and "7" and "9" in str_num9:
#         print(f"乘以{i},结果为{str_num9}")

# 10.验证:任意一个大于9的整数减去它的各位数字之和所得的差,一定能被9整除.
#
# num_10 = 10
# sum_10 = 0
# while num_10 > 9:
#     str_10 = str(num_10)
#     for i in range(len(str_10)):
#         sum_10 += int(str_10[i])
#     # print(sum_10)
#     # print(num_10)
#     if (num_10 - sum_10) % 9 == 0:
#         # print(f"验证成功！，整数为{num_10},和为{sum_10}")
#         sum_10 = 0
#
#     else:
#         print(f"验证失败！，整数为{num_10},和为{sum_10}")
#     num_10 += 1

# 11.今有四个人,他们得年龄各不相同,他们年龄总和是129,而其中有三个人的年龄是平方数,
# 若倒退15年,这四人中仍有三个人的年龄是平方数,求他们各自的年龄
#
for i in range(129):
    for j in range(3,129):
        for k in range(3,129):
            for m in range(3,129):
                if i*i +j*j+k*k+m ==129 and i!= j and i!= k \
                        and i!= m and j!= k and j!= m and i!= k and i!= m:
                    print(i,j,k,m)


# 12.如果两个素数之差为2,这样的两个素数就叫作"孪生数",找出100以内的所有"孪生数".

list12 = []
for i in range(100, 1, -1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        list12.append(i)
print(list12)
for i in range(len(list12)):
    if list12[i-1] - list12[i] == 2:
        print(list12[i - 1],list12[i])











