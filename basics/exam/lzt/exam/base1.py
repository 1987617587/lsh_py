# 编写函数，接收参数n，按如下规律显示如下图形：
# 例如：当n=4：
# 2
# 2 4
# 2 4 6
# 2 4 6 8
import random


def test1(n: int):
    if n < 1:
        return
    for i in range(n):
        for j in range(i + 1):
            print(2 * (j + 1), end=" ")
        print()


# test1(4)

#
# 2、创建一个长度为10的整型列表，并且用大于等于1且小于等于10的随机数初始化这个整型列表且列表内的数值不可重复。
# nums = list(range(1, 11))
# random.shuffle(nums)
# print(nums)


#
# 3、编写函数，接收一个整型列表,返回该列表中最大的质数。
def is_prime(num: int):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


def test3(num_list: list):
    max_prime = 2
    for i in range(len(num_list)):
        if is_prime(num_list[i]) and num_list[i] > max_prime:
            max_prime = num_list[i]
    return max_prime


# print(test3([1, 3, 11, 22, 66, 79, 97, 34, 13]))
#
# 4、计算一个字符串有几个子串（求出数字个数即可）？
# 例如字符串"abc",就包含"a","b","c","ab","bc","abc"6个子串。
def test4(str1: str):
    return sum(list(range(1, len(str1) + 1)))


# print(test4("abcdef"))
#
# 5、编写方法，接收一个表示上限的参数n，打印出0到n内能够被3整除的所有偶数。
def test5(n: int):
    print(list(range(0, n + 1, 6)))


# test5(24)

#
# 6、编程求一个四位自然数ABCD,它乘以A后变成DCBA。
# for A in range(1, 10):
#     for B in range(10):
#         for C in range(10):
#             for D in range(1, 10):
#                 if int(str(A) + str(B) + str(C) + str(D)) * A == int(str(D) + str(C) + str(B) + str(A)):
#                     print(str(A) + str(B) + str(C) + str(D))

#
# 7、求100以内跨度最大的相邻的一对质数。
def test7():
    # 初始化差值和上一个质数
    # 2 3 为差值最小 并记录3这个质数 为求下一个差值做准备
    max_dis = 1
    before_prime = 3
    for i in range(4, 101):
        # 复用上面第三题已写的函数
        if is_prime(i):
            # 判断差值是否发现更大的
            if i - before_prime > max_dis:
                max_dis = i - before_prime
            # 无论是否发现更大差值都需要更新上一个质数
            before_prime = i
    return before_prime - max_dis, before_prime


# print(test7())
#
# 8、编写函数，接收两个参数整数s和整数e,计算[s,e]中所有首位为奇数的数的和并返回。
def test8(s: int, e: int):
    if s > e:
        return
    sum = 0
    for i in range(s, e + 1):
        if int(str(i)[0]) % 2 == 1:
            sum += i
    return sum


# print(test8(10, 9))
# print(test8(10, 10))
# print(test8(2, 11))
#
# 9、输入一个日期，格式如：2010 10 24 ，打印输出为【2010年10月24日】，输出前请判断该日期是否合法。
def test9(date_str: str):
    if len(date_str) != 10:
        return
    if date_str[4] != " " or date_str[7] != " ":
        return
    year = date_str[0] + date_str[1] + date_str[2] + date_str[3]
    month = date_str[5] + date_str[6]
    day = date_str[8] + date_str[9]
    # 检测年 不支持公元前
    if not year.isdigit() or int(year) < 1:
        return

    # 检测月:
    if not month.isdigit() or int(month) < 1 or int(month) > 12:
        return

        # 检测日期：
    if not day.isdigit():
        return

    month_days = [31,
                  29 if int(year) % 4 == 0 and int(year) % 100 != 0 or int(year) % 400 == 0 else 28,
                  31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if int(day) < 1 or int(day) > month_days[int(month) - 1]:
        return

    return f"{year}年{month}月{day}日"


# print(test9("123123321"))
# print(test9("yyyy mm dd"))
# print(test9("-111 13 12"))
# print(test9("1900 aa 12"))
# print(test9("1900 13 12"))
# print(test9("1900 02 29"))
# print(test9("1900 02 28"))

#
# 10、	编写函数，传入一个字符串，请将字符串中的数字和非数字进行分离，返回分离得到的纯数字字符串和非数字的字符串。
# 例如:传入：”1a2b35g”=>”1235”和”abg”
def test10(str1: str):
    ret_nums = ""
    ret_strs = ""
    for i in range(len(str1)):
        if str1[i].isdigit():
            ret_nums += str1[i]
        else:
            ret_strs += str1[i]
    return ret_nums, ret_strs


# print(test10("1231928asjdghasgh;as'd;as[]as"))
