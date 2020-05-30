"""
￥200
# author Liu shi hao
# date: 2019/11/11 10:01
# file_name: test

"""

# ctrl+r 查找替换快捷键
# jion:以分隔符连接的方式连接到列表中的所有元素
import random
#
# names = ["a", "b", "c"]
# f_names = "?".join(names)
# print(f_names)
# print("?".join(names))
#
# # 反转函数
# # 1.列表反转函数 reverse
# names.reverse()
# print(names)
# # 2.内置函数 reversed
# names = list(reversed(names))
# print(names)
# # 3:切片
# msg = names[::-1]
# print(msg)
#
#
# def list9_9():
#     for i in range(1, 10):
#         for j in range(1, i + 1):
#             print(f"{j}*{i}=={i * j}", end="\t")
#         print()
#
#
# list9_9()
#
#
# def return_none(a):
#     return None
#
#
# def num_sum(a, b):
#     """
#     对两个参数求和
#     :param a: 参数1
#     :param b: 参数二
#     :return: a+b
#     """
#     return a + b
#
#
# def list_sum(arr):
#     return sum(arr)
#
#
# print(num_sum(1, 2))


def stake(chip):

    while chip > 0:
        print(f"欢迎进入掷骰子游戏，您的目前筹码为{chip}")
        Stake = int(input("请输入下注金额："))
        if chip < Stake:
            print("筹码小于最小下注金额，强制玩家退出!")
            break
        dice_num = random.randint(1, 6)
        result_num = "大" if dice_num > 3 else "小"
        guess = input("请选择买大还是买小：")
        if guess == result_num:
            chip += Stake
            print(f"骰子数是{dice_num}本次猜{guess}赢了，筹码为{chip}")

        else:
            chip -= Stake
            print(f"骰子数是{dice_num}本次猜{guess}输了，筹码为{chip}")
        an = input("￥￥￥￥￥￥￥玩家是否要退出游戏（y/n）:")
        if an == "y":
            print("*****************已退出！*****************")
            break

    else:
        print("*****************已退出！*****************")
        pass

# stake(50)


def in_char():
    list_a_z = ["a","b","c"]
    list_A_Z = ["A","B","C"]
    while True:
        list_char = list(input("请输入一段字符："))
        print(list_char)
        for i in range(len(list_char)-1):
            if list_char[i] in list_a_z:
                print("zhix")
                list_char[i]= list_A_Z[list_a_z.index(list_char[i])]
            if list_char[i] in list_A_Z:
                list_char[i] = list_a_z[list_A_Z.index(list_char[i])]
        print(str(list_char))
        return
in_char()