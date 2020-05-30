# author:lzt
# date: 2019/11/13 15:47
# file_name: word1_task

# 1.输出像下面显示的图形（行数由用户输入指定）
# *
#       ***
# *****
#   *******
# *********
import random


def task1(lines: int):
    if lines <= 0:
        return
    for i in range(lines):
        # i:0 1 2 3 4 5
        # *:1 3 5 7 9 11 2*i+1
        #  :偶数下标的行没有空格
        #  :奇数行:
        #  :0 8 0 4 0 0
        # 最大的列-当前行的*数
        # 2*lines-1 - (2*i+1)
        if i % 2 != 0:
            print(" " * (2 * lines - 1 - (2 * i + 1)), end="")
        print("*" * (2 * i + 1))


task1(7)

# #
# # 2.请依次输出0-99之间能把99整除的数字。
# # def task2():
# #     for i in range(1, 100):
# #         if 99 % i == 0:
# #             print(i)
#
#
# # task2()
# #
# # 3.声明一个列表，为列表的每一个索引位置赋值，赋值要求：1-100之间的随机数，
# # 可以重复，赋值完毕后，求50这个数字是不是在列表中出现。若出现输出true，否则输出false。
# def task3():
#     nums = []
#     for i in range(100):
#         nums.append(random.randint(1, 100))
#     return 50 in nums
#
#
# # print(task3())
# #
# # 4.写一个函数，参数为字符串类型，返回值也为字符串类型，函数内对传入的字符串进行遍历，
# # 找出所有的大写字母并连接成新的字符串，遍历结束后将新连接成的字符串返回。
# def task4(str1: str):
#     ret = ""
#     for i in range(len(str1)):
#         # if "A" <= str1[i] <= "Z":
#         if str1[i].isupper():
#             ret += str1[i]
#     return ret
#
#
# # print(task4("asdfJGJSGDjasdfgJGJHasda"))
# #
# # 5.持续获取用户输入，直到用户输入的字符串中既有字母又有数字。
def task5():
    while 1:
        str1 = input("输入一个既有字母又有数字的消息:")
        # 做检测
        is_have_char = False
        is_have_num = False
        for i in range(len(str1)):
            if "0" <= str1[i] <= "9":
                is_have_num = True
            if "A" <= str1[i] <= "Z" or "a" <= str1[i] <= "z":
                is_have_char = True
            # 为了性能 提前中断
            if is_have_char and is_have_num:
                break
        else:
            continue
        break
    return str1
#
#
# # print(task5())
# #
# # 6.有一个长度为62的字符列表，请为这个列表随机赋值(a-z A-Z 0-9)要求每个下标位置的字符都不重复。
# def task6():
#     chars = []
#     while len(chars) != 62:
#         # 随机出62个字符当中的一个
#         # ord(字符)可以得到该字符的数字表示
#         random_char_num = random.randint(ord("0"), ord("z"))
#         # 48-57 65-90 97-122
#         if ord("9") < random_char_num < ord("A") or ord("Z") < random_char_num < ord("a"):
#             continue
#         # chr(数字)->字符
#         char = chr(random_char_num)
#         if char not in chars:
#             chars.append(char)
#     return chars
#
#
# # print(task6())
# #
# # 7.写一个函数将整型数字(int 不含0)转换为汉字大写格式。例：111=>壹佰壹拾壹
# # 167891111
# # 使用列表:
# # 汉字列表:["零","壹","贰","叁","肆","伍","陆","柒","捌","玖"]
# #            0    1    2    3    。。。。                 9
# # "167891111"=>"1"->汉字[int("1")]
# # 单位:["圆", "拾", "佰", "仟", "萬", "拾", "佰", "仟", "亿", "拾", "佰", "仟", "萬"]
# #        0    1    2     3   4    5    6    7.....
# # "167891111"
# #  012345678
# #  876543210:len-1-i:单位[len-1-i]
# def task7(num):
#     # 做数字位数的限定
#     if len(str(num)) > 13:
#         print("暂时不支持13位以上的转换！")
#         return
#     # 准备汉字和单位列表
#     zhs = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
#     units = ["圆", "拾", "佰", "仟", "萬", "拾", "佰", "仟", "亿", "拾", "佰", "仟", "萬"]
#     # 设定转换后的字符串
#     ret = ""
#     num_str = str(num)
#     for i in range(len(num_str)):
#         ch = num_str[i]
#         ret += zhs[int(ch)] + units[len(num_str) - 1 - i]
#     return ret
#
#
# # print(task7(123456789))
#
# #
# # 8.根据用户输入的行数打印出类似下面的图形：
# # 例：4行
# #    *
# #   **
# #  ***
# # ****
# def task8(lines):
#     for i in range(lines):
#         # i:0 1 2 3
#         # *:1 2 3 4 i+1
#         #  :3 2 1 0 lines-1-i
#         print(" " * (lines - 1 - i), end="")
#         print("*" * (i + 1))
#
#
# # task8(4)
# # 9.写一个函数传入字符串参数，获取字符串中所有的数字。
# def task9(str1):
#     ret = ""
#     for i in range(len(str1)):
#         if str1[i].isdigit():
#             ret += str1[i]
#     return ret
#
#
# # print(task9("asdasd87as6d86asd687as6"))
#
# #
# # 10.写一个函数，传入两个整型列表，函数将两个列表进行合并，并返回合并后的列表。
# def task10(arr1, arr2):
#     return arr1 + arr2
#
#
# print(task10([1, 2, 3], [4, 5, 6]))
