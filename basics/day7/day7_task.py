"""
# author Liu shi hao
# date: 2019/11/13 21:48
# file_name: day7_task

"""
import random

list_A_Z = [chr(65 + i) for i in range(26)]
list_a_z = [chr(97 + i) for i in range(26)]
list_0_9 = [chr(48 + i) for i in range(10)]
list_str = list_A_Z + list_a_z


# 附加作业：
# 1.获取一个用户输入的3位数字，若用户输入的不是数字，提示重新输入，直到数值合理。
#
def in_int3():
    while True:
        num = input("请输入整数：")
        if num.isdigit() and len(num) == 3 and len(str(int(num))) == 3:
            return int(num)
        print("重新输入！")


# print(in_int3())
# 2.计算出字符串中的p-z的字母个数。
#
list_p_z = [chr(i) for i in range(112, 123)]


# print(list_p_z)
def num_str_p_z():
    j = 0
    num_str = input("请输入：")
    for i in range(len(num_str)):
        # if num_str[i] in list_p_z:  # 和下行代码等同
        if "p" <= num_str[i] <= "z":
            j += 1
    return j


# print(num_str_p_z())


# 3.根据用户输入的行数，输出下面的效果：
# #
# #
# ##
# ###
# #####
# ######## 以此类推
#


def in_effect(n):
    list_2 = [1, 1, 2]
    for i in range(n - len(list_2)):
        list_2.append(list_2[-1] + list_2[-2])
    # print(list_2)
    for i in range(n):
        print("#" * int(list_2[i]))


# in_effect(in_int())

def task3(lines):
    if lines <= 0:
        return
    f_list = []
    for i in range(lines):
        if i == 0 or i == 1:
            f_list.append(i)
        else:
            f_list.append(f_list[i - 1] + f_list[i - 2])
    for i in range(len(f_list)):
        print("#" * f_list[i])


task3(10)


# 4.反转字符串中的指定部分的字符序列。
# 例：
# “12345”,2,3=>”12435”["1","2","3","4","5"]
#
def reversal_str(in_str, a, b):
    r_str = ""
    in_str = list(in_str)
    in_str[a], in_str[b] = in_str[b], in_str[a]
    for i in range(len(in_str)):
        r_str += in_str[i]
    return r_str


# print(reversal_str("12345", 2, 3))
# 5.计算出1-1000中完全数的个数。
# 完全数：完全数（Perfect number），又称完美数或完备数，是一些特殊的自然数。
# 它所有的真因子（即除了自身以外的约数）的和（即因子函数），恰好等于它本身。
# 如果一个数恰好等于它的因子之和，则称该数为“完全数”。
#
def factor_4(n):
    """

    :param n:
    :return: 判断它是不是完全数
    """
    sum_factor = 0
    for i in range(1, n):
        if n % i == 0:
            sum_factor += i
    if sum_factor == n:
        return n


# print(factor_4(in_int()))
def perfect_num_1_1000(a, b):
    list_perfect_num = []
    for j in range(a, b + 1):
        factor_4(j)
        if j == factor_4(j):
            list_perfect_num.append(j)

    return list_perfect_num


# print(perfect_num_1_1000(1,1000))


# 6.去除字符串中的重复字符，重复的字符只保留一个.
def del_repetition():
    r_str = ""
    in_str = input("请输入：")
    for i in range(len(in_str)):
        if in_str[i] not in r_str:
            r_str += in_str[i]

    print(r_str)


# del_repetition()

# 7.怪物boss血量10000，玩家使用某武器进行攻击，武器伤害值在100-212之间（随机产生伤害），
# 求玩家攻击了多少次，怪物倒下。
#


player1 = "玩家1"
player2 = "玩家2"
MP1 = 500
MP2 = 500


def pk():
    blood_flow1 = 3000
    blood_flow2 = 3000
    while blood_flow1 > 0 and blood_flow2 > 0:
        fis = random.randint(0, 1)
        if fis == 0:
            print(f"本回合，{player1}先出招")
            blood_flow2 = blood_flow2 - MP1 if blood_flow2 - MP1 > 0 else 0
            print(f"{player1}攻击{player2}，伤害是{MP1}，{player2}血量剩余：{blood_flow2}")
            if blood_flow1 <= 0 or blood_flow2 <= 0:
                break
            blood_flow1 = blood_flow1 - MP2 if blood_flow1 - MP2 > 0 else 0
            print(f"{player2}攻击{player1}，伤害是{MP2},{player1}血量剩余：{blood_flow1}")
        else:
            print(f"本回合，{player2}先出招")
            blood_flow1 = blood_flow1 - MP2 if blood_flow1 - MP2 > 0 else 0
            print(f"{player2}攻击{player1}，伤害是{MP2},{player1}血量剩余：{blood_flow1}")
            if blood_flow1 <= 0 or blood_flow2 <= 0:
                break
            blood_flow2 = blood_flow2 - MP1 if blood_flow2 - MP1 > 0 else 0
            print(f"{player1}攻击{player2}，伤害是{MP1}，{player2}血量剩余：{blood_flow2}")
    print(f"{player1}死亡，游戏结束") if blood_flow1 < blood_flow2 else print(f"{player2}死亡，游戏结束")


# pk()
def pk_boss():
    boss_blood_volume = 10000
    # list_weapon = ["木棒", "砍刀", "步枪", "火箭筒"]

    hurt_nums = 0
    while boss_blood_volume > 0:
        weapon_hurt = random.randint(100, 212)
        boss_blood_volume -= weapon_hurt
        hurt_nums += 1
    print(f"玩家攻击了{hurt_nums}次，怪物倒下")


# pk_boss()
# 8.持续获取用户输入，直到用户输入的字符串一半是字母一半是数字。
#
def in_str_and_int():
    while True:
        k, m = 0, 0
        str_5 = input("请输入：")
        for i in range(len(str_5)):
            if str_5[i] in list_0_9:
                k += 1
        for j in range(len(str_5)):
            if str_5[j] in list_str:
                m += 1
        if k == m > 0:
            return str_5


# print(in_str_and_int())
# 9.请输出33-250之间的最小素数和最大素数的和。


def prime_num(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return a


def sum_min_max_prime_num(a, b):
    in_list = []
    for i in range(a, b + 1):
        if prime_num(i):
            in_list.append(i)
    return max(min(in_list), max(in_list))


# print(sum_min_max_prime_num(4, 10))
# 10.随机产生1000次1-6之间的数，求其中重复次数最多的数，输出该数和其重复的次数。
def task10(n):
    list10 = []
    s1, s2, s3, s4, s5, s6 = [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6]
    for i in range(n):
        list10.append(random.randint(1, 6))
    for j in range(n):
        if list10[j] == 1:
            s1[0] += 1
        elif list10[j] == 2:
            s2[0] += 1
        elif list10[j] == 3:
            s3[0] += 1
        elif list10[j] == 4:
            s4[0] += 1
        elif list10[j] == 5:
            s5[0] += 1
        else:
            s6[0] += 1
    a = max(s1[0], s2[0], s3[0], s4[0], s5[0], s6[0])
    b = s1[1] if s1[0] == a else s2[1] if s2[0] == a else s3[1] if s3[0] == a \
        else s4[1] if s4[0] == a else s5[1] if s5[0] == a else s6[1]
    print(f"随机产生{next}次1-6之间的数,其中重复次数最多的数{b}，其重复的次数{a}")


# task10(1000)

# 简单的方法
def task10_2():
    times = [0] * 6
    for i in range(1000):
        times[random.randint(1, 6) - 1] += 1

    return times.index(max(times)) + 1, max(times)


# print(task10_2())