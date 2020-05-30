# author:lzt
# date: 2019/11/14 9:14
# file_name: word2_task
# 附加作业：
# 1.获取一个用户输入的3位数字，若用户输入的不是数字，提示重新输入，直到数值合理。
import random


def task1():
    while 1:
        # 获取用户的三位数字
        num = input("三位数字:")
        # 必须为三位
        if len(num) != 3:
            print("必须为三位！")
            continue
        # 必须全部是数字
        if not num.isdigit():
            print("必须全部为数字")
            continue
        # 检测转换后数字是否为三位数
        if len(str(int(num))) != 3:
            print("前缀数字不能为0！")
            continue
        return int(num)


# print(task1())
#
# 2.计算出字符串中的p-z的字母个数。
def task2(str1):
    count = 0
    for i in range(len(str1)):
        if "p" < str1[i] < "z":
            count += 1
    return count


# print(task2("asdkjghkasgdk"))
#
# 3.根据用户输入的行数，输出下面的效果：
# #1
# #1
# ##2
# ###3
# #####5
# ########8 以此类推
def task3(lines):
    if lines <= 0:
        return
    # # 得到斐波那契数列表
    # f_list = []
    # for i in range(lines):
    #     if i == 0 or i == 1:
    #         f_list.append(1)
    #     else:
    #         f_list.append(f_list[i - 1] + f_list[i - 2])
    #
    # # 遍历列表 打印列表中元素数字对应的图形个数
    # for i in range(len(f_list)):
    #     print("#" * f_list[i])

    # 直接计算当前行的#数目
    # if lines == 1:
    #     print("#")
    # elif lines == 2:
    #     print("#")
    #     print("#")
    # else:
    before_before = 1
    before = 1
    for i in range(lines):
        if i == 0 or i == 1:
            print("#")
        else:
            # 计算当前行的#数目
            current = before + before_before
            print("#" * current)
            before_before = before
            before = current


# task3(10)
#
# 4.反转字符串中的指定部分的字符序列。
# 例：
# “12345”,2,3=>”12435”
def task4(str1, start, end):
    # 开始和结束的检测
    # start和end都应该在0-len-1 start<end
    if start < 0 or start >= len(str1) or end < 0 or end >= len(str1) or start > end:
        return str1
    # 将字符串拆分成三个部分:
    # 0-start
    # start-end
    # end-len(str1)-1
    str1_1 = ""
    str1_2 = []
    str1_3 = ""
    for i in range(len(str1)):
        if i < start:
            str1_1 += str1[i]
        elif i <= end:
            str1_2.append(str1[i])
        else:
            str1_3 += str1[i]
    # 反转start-end的字符串
    str1_2.reverse()

    return str1_1 + "".join(str1_2) + str1_3


# print(task4("123456789", 4, 2))
#
# 5.计算出1-1000中完全数的个数。
# 完全数：完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
# 它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
# 如果一个数恰好等于它的因子之和，则称该数为“完全数”。
def task5():
    count = 0
    for i in range(2, 100001):
        # 找到i的所有的因子
        sum = 1
        for j in range(2, i):
            if i % j == 0:
                sum += j
        if sum == i:
            print(i)
            count += 1
    return count


# print(task5())
#
# 6.去除字符串中的重复字符，重复的字符只保留一个.
def task6(str1):
    ret = ""
    for i in range(len(str1)):
        # 判断ret中是否已经含有str1[i]
        if str1[i] not in ret:
            ret += str1[i]
            pass
        pass
    return ret


# print(task6("aaadddbvvbfjhjjhsa"))

#
# 7.怪物boss血量10000，玩家使用某武器进行攻击，武器伤害值在100-212之间（随机产生伤害），
# 求玩家攻击了多少次，怪物倒下。
def task7(boos_hp):
    times = 0
    while boos_hp > 0:
        boos_hp -= random.randint(100, 212)
        times += 1
    return times


# print(task7(10000))
#
# 8.持续获取用户输入，直到用户输入的字符串一半是字母一半是数字。
def task8():
    while 1:
        msg = input("一半字母一半数字的消息:")
        # 统计字母数和数字数
        char_count = 0
        num_count = 0
        for i in range(len(msg)):
            if "0" <= msg[i] <= "9":
                num_count += 1
            if "A" <= msg[i] <= "Z" or "a" <= msg[i] <= "z":
                char_count += 1
        if char_count != 0 and char_count == num_count and char_count + num_count == len(msg):
            return msg
        print("请重新输入！")


# print(task8())
#
# 9.请输出33-250之间的最小素数和最大素数的和。
def task9(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


min_prime = 0
for i in range(33, 251):
    if task9(i):
        min_prime = i
        break
max_prime = 0
for i in range(250, 32, -1):
    if task9(i):
        max_prime = i
        break


# print(min_prime + max_prime)
#
# 10.随机产生1000次1-6之间的数，求其中重复次数最多的数，输出该数和其重复的次数。
def task10():
    # 找一个列表保存数字的重复次数
    # [0,0,0,0,0,0]
    #  0 1 2 3 4 5
    times = [0] * 100
    for i in range(1000):
        times[random.randint(1, 100) - 1] += 1

    return times.index(max(times)) + 1, max(times)

print(task10())

