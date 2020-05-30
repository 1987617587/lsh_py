"""
# author Liu shi hao
# date: 2019/11/12 14:29
# file_name: day6_task

"""
import datetime
import random


def in_int():
    while True:
        num = input("请输入整数：")
        if num.isdigit():
            return int(num)
        print("重新输入！")


# 必做：
# 1、写一个函数，在函数内依次打印出列表每个元素的值。

def list_print(in_list):
    for i in range(len(in_list)):
        print(in_list[i])


# list_1 = [1, 2, 3, 4, 5, 6]
# list_print(list_1)
# 2、写一个函数，计算列表所有元素的和(注意返回值)。
#
def list_sum(in_list):
    return sum(in_list)


# list_2 = [1, 2, 3, 4, 5, 6]
# print(list_sum(list_2))

# 3、写一个函数，计算列表所有奇数索引元素的和(注意返回值)。
#
def list_odd_sum(in_list):
    odd_sum = 0
    for i in range(1, len(in_list), 2):
        odd_sum += in_list[i]
    return odd_sum


# list_3 = [1, 2, 3, 4, 5, 6]
# print(list_odd_sum(list_3))
# 4、写一个函数，计算列表所有偶数索引元素的和(注意返回值)。
#
def list_even_sum(in_list):
    even_sum = 0
    for i in range(0, len(in_list), 2):
        even_sum += in_list[i]
    return even_sum


# list_3 = [1, 2, 3, 4, 5, 6]
# print(list_even_sum(list_3))
# 5、写一个函数可以计算两个数的和，想想这个函数有哪些参数，返回值是什么类型。
#

def sum_two_num(num1, num2):
    return num1 + num2


# print(sum_two_num(in_int(), in_int()))
# 6、写一个函数可以计算两个数的商(分母不能为0)，想想这个函数有哪些参数，返回值是什么类型。
#
def consult_two_num(num1, num2):
    return num1 / num2


# print(consult_two_num(in_int(), in_int()))
# 7、写一个函数将传入的天、小时、分钟、秒的总和转换为秒，
# 比如0天、2小时、5分、7秒，他们代表的总秒数为2*3600+5*60+7=7507秒。
# 想想这个函数有哪些参数，返回值是什么类型。
def time_seconds(days, hours, minutes, seconds):
    return days * 3600 * 24 + hours * 3600 + minutes * 60 + seconds


# print(time_seconds(0, 2, 46,40))
# 8、写一个函数交换整型列表中两个指定索引元素的值。想想这个函数有哪些参数，返回值是什么类型。
#
def list_change(in_list, a, b):
    in_list[a], in_list[b] = in_list[b], in_list[a]
    return in_list


list_8 = [1, 2, 3, 4, 5, 6]


# print(list_change(list_8,1,3))

# 9、写一个函数计算整型列表中所有能被3整除元素的个数。想想这个函数有哪些参数，返回值是什么类型。
#
def list_divide3(in_list):
    j = 0
    for i in range(len(in_list)):
        if in_list[i] % 3 == 0:
            j += 1
    return j


list_9 = [1, 2, 3, 4, 5, 6]


# print(list_divide3(list_9))

# 10、写一个函数将整型数字(int)转换为格式化的字符串(str)，现要求如下：
# a.可以指定转换后[字符串的长度];
# b.当数字的长度不足指定的长度，让这个字符串右对齐，指定[左边补的字符(char)];
# 例如，假设现在将指定的数字转换为固定长度为8的字符串，
# 如果长度不足，左边补'0'，那么27这个数字就会转换为字符串"00000027"。
# 根据要求，想想这个函数有哪些参数，返回值是什么类型。
#
def int_transform_str(num, lens, a=""):
    tran_str = a * (lens - len(str(num))) + str(num) if lens >= len(str(num)) else str(num)
    return tran_str


# print(int_transform_str(27, 8,"0"))

# 11.用函数实现找出一个整型列表中最大值和最小值 
def list_max_min(in_list):
    return max(in_list), min(in_list)


list_11 = [1, 2, 3, 4, 5, 6]


# print(list_max_min(list_11))
# 12.判断一个数是否是质数(素数)？该如何声明函数？
#
def prime_number(num):
    for i in range(2, num):
        if num % i == 0:
            return False  # 判断是质数就返回原来值，不是质数返回False
    else:
        return num


# print(prime_number(14))
# 13. 将指定的秒数转变为几小时几分几秒。
#
def seconds_time(seconds):
    days = seconds // (3600 * 24)
    hours = ((seconds - seconds // (3600 * 24) + days) // 3600) % 24
    minutes = ((seconds - (seconds - seconds // (3600 * 24)) // 3600 + hours) // 60) % 60
    r_seconds = (seconds - (seconds - (seconds - seconds // (3600 * 24)) // 3600) // 60 + minutes) % 60
    return (f"{days}天{hours}小时{minutes}分{r_seconds}秒")


# print(seconds_time(10000))
# 14.使用Random类给一个列表的所有元素随机赋初值（不重复）。
#
def no_repeat_list(n):
    list_no_repeat = []
    while len(list_no_repeat) < n:
        num = random.randint(0, 99999)
        if num not in list_no_repeat:
            list_no_repeat.append(num)
    return list_no_repeat


def value_random(*args):
    return args


# print(value_random(no_repeat_list(4)))


# 15.判断一个整型列表是否是对称的。所谓对称就是第一个元素等于最后一个元素，第二个元素等于倒数第二个元素，
# 依次类推，例如【7，3，1，3，7】就是对称的。
#
def symmetry_list(in_list):
    for i in range(len(in_list) // 2):
        if in_list[i] != in_list[len(in_list) - 1 - i]:
            return False
    return True


list_15 = [7, 3, 2, 1, 2, 3, 7]


# print(symmetry_list(list_15))
# 16.打印一个列表的所有值。
#
def list_print_all(in_list):
    for i in range(len(in_list)):
        print(in_list[i])


# list_print_all([2,3,4,7])
# 17.查找一个列表中某个值是否存在，如果存在返回这个值的索引，否则返回-1。
#
def list_indexes(in_list, n):
    for i in range(len(in_list)):
        if n == in_list[i]:
            return i
    return -1


list_17 = [7, 3, 2, 1, 2, 3, 7]
# print(list_indexes(list_17, 1))
# 18.将一个列表反转过来，比如【2，3，1，4，7】转换为【7，4，1，3，2】 
#
list_18 = [2, 3, 1, 4, 7]


def flip(in_list):
    r_list = []
    for i in range(len(in_list) - 1, -1, -1):
        r_list.append(in_list[i])
    return r_list


# print(flip(list_18))
# 19.求一个列表的最大值。
#
list_19 = [2, 3, 1, 4, 7]


def list_max(in_list):
    return max(in_list)


# print(list_max(list_19))
# 20.求一个列表的最小值。
#
list_20 = [2, 3, 1, 4, 7]


def list_min(in_list):
    return min(in_list)


# print(list_min(list_20))
# 21.写一个函数，实现在列表中指定的的位置前插入一个值。
#
list_21 = [2, 3, 1, 4, 7]


def list_insert(adds, num):
    list_21.insert(adds, num)
    return list_21


# print(list_insert(1,5))
# 22.写一个函数，删除列表中指定位置的元素。 
#
def list_del(in_list, n):
    list = []
    for i in range(len(in_list)):
        if n - 1 != i:
            list.append(in_list[i])
    return list


list_22 = [2, 3, 1, 4, 7]


# print(list_del(list_22, 3))
# 23.猜数游戏
# 1.随机出现一个数(范围自定义) 作为答案
# 2.提示用户输入并根据答案和用户输入的大小关系输出大了? 小了?
# 3.5次机会
# 4.可以重复玩
# 5.根据猜对的次数进行评价
# 6.无论对错 请告知答案
#
def repeat_play():  # 定义重复玩函数
    while True:
        guess_nums()
        an = input("是否退出游戏？(y/n)")
        if an == "y":
            return False


def guess_nums():  # 猜数游戏
    i = 0
    game_answer = random.randint(0, 100)
    while i < 5:
        user_answer = in_int()
        # print(game_answer)
        i += 1
        if user_answer == game_answer:
            break
        print(f"第{i}次你猜{user_answer}大了") if user_answer > game_answer else print(f"第{i}次你猜{user_answer}小了")
    print(f"本轮随机答案为：{game_answer}")
    print(f"{i}次猜对，欧皇附体！") if i == 0 else print(f"{i}次猜对，运气真好！") \
        if i == 1 else print(f"{i}次猜对，猜的不错！") if 4 > i > 1 else print(f"{i}次猜对，太及时了！") \
        if i == 4 else print("本次游戏未猜中，继续努力！")


# guess_nums()
# repeat_play()


# 1.输出像下面显示的图形（行数由用户输入指定）
# *
#       ***
# *****
#   *******
# *********
#
def figure_1(n):
    for i in range(n):
        if i % 2 == 0:
            print("*" * (2 * i + 1))
        else:
            print(" " * (2 * n - (2 * i + 1)) + "*" * (2 * i + 1))


# figure_1(6)
# 2.请依次输出0-99之间能把99整除的数字。
def exact_division(num=99):
    for i in range(1, num + 1):
        if num % i == 0:
            print(i)


# exact_division()
# 3.声明一个列表，为列表的每一个索引位置赋值，赋值要求：1-100之间的随机数，可以重复，
# 赋值完毕后，求50这个数字是不是在列表中出现。若出现输出true，否则输出false。
#
list_3 = [1, 2, 3, 4]


def func_3():
    for i in range(len(list_3)):
        list_3[i] = random.randint(1, 100)
    print(list_3)
    if 50 in list_3:
        return True
    else:
        return False


# print(func_3())
# 4.写一个函数，参数为字符串类型，返回值也为字符串类型，函数内对传入的字符串进行遍历，
# 找出所有的大写字母并连接成新的字符串，遍历结束后将新连接成的字符串返回。
#
list_A_Z = [chr(65 + i) for i in range(26)]
list_a_z = [chr(97 + i) for i in range(26)]
list_0_9 = [chr(48 + i) for i in range(10)]


# print(list_A_Z)
def func_4(a=""):
    b = ""
    for i in range(len(a)):
        if a[i] in list_A_Z:
            b += a[i]
    return b


# print(func_4(a="ADAJOI8987jihj"))
# 5.持续获取用户输入，直到用户输入的字符串中既有字母又有数字。
#
list_str = list_A_Z + list_a_z


def in_str_int():
    while True:
        str_5 = input("请输入：")
        for i in range(len(str_5)):
            for j in range(len(str_5)):
                if str_5[i] in list_0_9 and str_5[j] in list_str:
                    return True


# print(in_str_int())
# 6.有一个长度为62的字符列表，请为这个列表随机赋值(a-z A-Z 0-9)要求每个下标位置的字符都不重复。
#
list_str_62 = list_str + list_0_9


def str_62():
    str_62 = []
    while True:
        a = random.choice(list_str_62)
        if a not in str_62:
            str_62.append(a)
            if len(str_62) == 62:
                return str_62


# print(str_62())
# 7.写一个函数将整型数字(int 不含0)转换为汉字大写格式。例：111=>壹佰壹拾壹
def in_1_9():
    list_1_9 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    while True:
        str_7 = input("请输入不含零整数(最高13位)：")
        for i in range(len(str_7)):
            if str_7[i] not in list_1_9:
                break
        else:
            return str_7


def transform_Chinese():
    list_1_9 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    list_Chinese_1_9 = ["壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
    list_format = ["", "拾", "佰", "仟", "万", "拾", "佰", "仟", "亿", "拾", "佰", "仟", "万"]
    str = ""
    # num = list(input("整型数字,最高13位:"))
    num = list(in_1_9())
    for i in range(len(num)):
        for j in range(9):
            if num[i] == list_1_9[j]:
                num[i] = list_Chinese_1_9[j]
    for i in range(len(num)):
        str += (num[i] + list_format[len(num) - i - 1])
    print(str)


# transform_Chinese()
#
def task7(num):  # 优化函数（方法2）
    # 做数字位数的限定
    if len(str(num)) > 13:
        print("暂时不支持13位以上的转换！")
        return
    # 准备汉字和单位列表
    zhs = ["零", "壹", "贰", "叁", "肆", "伍", "陆", "柒", "捌", "玖"]
    units = ["圆", "拾", "佰", "仟", "萬", "拾", "佰", "仟", "亿", "拾", "佰", "仟", "萬"]
    # 设定转换后的字符串
    ret = ""
    num_str = str(num)
    for i in range(len(num_str)):  # 1-9转换到大写有优化，对应数字，两个列表的索引是相同的
        ch = num_str[i]  # 拿到数字1-9的索引，转换为int型,直接为大写数字使用。
        ret += zhs[int(ch)] + units[len(num_str) - 1 - i]  # 同方法1加上单位即可完成
    return ret


# print(task7(123456789))

# 8.根据用户输入的行数打印出类似下面的图形：
# 例：4行
#    *
#   **
#  ***
# ****
def figure_8(n):
    for i in range(1, n + 1):
        print(" " * (n - i) + "*" * i)


# figure_8(in_int())
# 9.写一个函数传入字符串参数，获取字符串中所有的数字。
#
def get_0_9():
    r_str_9 = ""
    str_9 = list(input("请传入字符串："))
    for i in range(len(str_9)):
        if str_9[i] in list_0_9:
            r_str_9 += str_9[i]
    return r_str_9


# print(get_0_9())


# 10.写一个函数，传入两个整型列表，函数将两个列表进行合并，并返回合并后的列表。
#
def merge(a, b):
    return a + b


lis_10_1 = [1, 2, 3]
lis_10_2 = [4, 5, 6]


# print(merge(lis_10_1, lis_10_2))

# 附加作业：
# 1.获取一个用户输入的3位数字，若用户输入的不是数字，提示重新输入，直到数值合理。
#
def in_int3():
    while True:
        num = input("请输入整数：")
        if num.isdigit() and len(num) == 3:
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
        if num_str[i] in list_p_z:
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
    sum_factor = 0
    for j in range(a, b + 1):
        factor_4(j)
        if j == factor_4(j):
            list_perfect_num.append(j)

    return list_perfect_num


# print(perfect_num_1_1000(1,1000))


# 6.去除字符串中的重复字符，重复的字符只保留一个.
def del_repetition():
    r_str = ""
    str = input("请输入：")
    for i in range(len(str)):
        if str[i] not in r_str:
            r_str += str[i]

    print(r_str)


# del_repetition()

# 7.怪物boss血量10000，玩家使用某武器进行攻击，武器伤害值在100-212之间（随机产生伤害），
# 求玩家攻击了多少次，怪物倒下。
#
import random

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
    list_weapon = ["木棒", "砍刀", "步枪", "火箭筒"]

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
    list = []
    for i in range(a, b + 1):
        if prime_num(i):
            list.append(i)
    return max(min(list), max(list))


# print(sum_min_max_prime_num(4, 10))
# 10.随机产生1000次1-6之间的数，求其中重复次数最多的数，输出该数和其重复的次数。
def task10(next):
    list10 = []
    s1, s2, s3, s4, s5, s6 = [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6]
    for i in range(next):
        list10.append(random.randint(1, 6))
    for j in range(next):
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

