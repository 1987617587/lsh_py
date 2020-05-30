"""
# author Liu shi hao
# date: 2019/11/22 20:41
# file_name: base1

"""
import random


# 自己写的判断用户输入整数的函数
def in_int():
    while 1:
        num = input("请输入整数：")
        if not num.isdigit():
            continue
        return int(num)


# 1、编写函数，接收参数n，按如下规律显示如下图形：
# 例如：当n=4：
# 2
# 2 4
# 2 4 6
# 2 4 6 8
#

def func_1():
    lines = in_int()
    for i in range(lines):
        for j in range(i + 1):
            print(2 * (j + 1), end="\t")
        print()


# func_1()
# 2、创建一个长度为10的整型列表，并且用大于等于1且小于等于10的随机数初始化这个整型列表且列表内的数值不可重复。
#
def func_2():
    list_2 = []
    while len(list_2) < 10:
        j = random.randint(1, 10)
        if j not in list_2:
            list_2.append(j)
    return list_2


# print(func_2())
# 3、编写函数，接收一个整型列表,返回该列表中最大的质数。
#
def func_3(arr: list):
    arr.sort()  # 将整型列表从小到大排序
    for i in range(len(arr) - 1, -1, -1):  # 倒序遍历出最大的质数
        for j in range(2, arr[i]):
            if arr[i] % j == 0:
                break
        else:
            return arr[i]


# print(func_3([1, 9, 11, 13, 5, 2, 3, 4]))


# 4、计算一个字符串有几个子串（求出数字个数即可）？例如字符串"abc",就包含"a","b","c","ab","bc","abc"6个子串。
#
def func_4(str_4: str):
    return len(str_4) * 2


# print(func_4("abc"))


# 5、编写方法，接收一个表示上限的参数n，打印出0到n内能够被3整除的所有偶数。
#

def func_5():
    n = in_int()
    for i in range(n + 1):
        if i % 3 == 0 and i % 2 == 0:
            print(i)


# func_5()


# 6、编程求一个四位自然数ABCD,它乘以A后变成DCBA。
#
def func_6():
    for i in range(1000, 9999):
        if i * int(str(i)[0]) == int(str(i)[3] + str(i)[2] + str(i)[1] + str(i)[0]):
            print(i)


# func_6()

# 7、求100以内跨度最大的相邻的一对质数。
#
def func_7():
    list_7 = []
    for i in range(100, 1, -1):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            list_7.append(i)
    print(list_7)
    num_max = 0
    for k in range(1, len(list_7)):
        if list_7[k - 1] - list_7[k] > num_max:
            num_max = list_7[k - 1] - list_7[k]
    print(num_max)
    for j in range(1, len(list_7)):
        if list_7[j - 1] - list_7[j] == num_max:
            return list_7[j - 1], list_7[j]


# print(func_7())


# 8、编写函数，接收两个参数整数s和整数e,计算[s,e]中所有首位为奇数的数的和并返回。
def get_e():  # 为了规范操作，限定e为整数且大于s
    while 1:
        e = input("请输入大于s的整数：")
        if not e.isdigit():
            continue
        return int(e)


def func_8():
    s = in_int()  # 调用自己写的判定用户输入整数的函数
    e = get_e()
    num_sum = 0
    for i in range(s, e + 1):
        if str(i)[0] in [str(j) for j in range(1, 10, 2)]:
            num_sum += i

    return num_sum


# print(func_8())

# 9、输入一个日期，格式如：2010 10 24 ，打印输出为【2010年10月24日】，输出前请判断该日期是否合法。
#
def func_9():
    list_9_1 = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    list_9_2 = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    in_date = input("请输入日期:")
    years = in_date[0:4]
    months = in_date[5:7]
    days = in_date[8:10]
    if years.isdigit() and months.isdigit() and days.isdigit():
        years = int(years)
        months = int(months)
        days = int(days)
        if years > 0:
            if years % 4 == 0 and years % 100 != 0 or years % 400 == 0:
                if 0 < months < 13 and 0 < days <= list_9_2[months - 1]:
                    print(str(years) + "年" + str(months) + "月" + str(days) + "月")
                    return
            else:
                if 0 < months < 13 and 0 < days <= list_9_1[months - 1]:
                    print(str(years) + "年" + str(months) + "月" + str(days) + "月")
                    return
        print("日期不合法")


# func_9()
# 10、	编写函数，传入一个字符串，请将字符串中的数字和非数字进行分离，返回分离得到的纯数字字符串和非数字的字符串。
# 例如:传入：”1a2b35g”=>”1235”和”abg”
def func_10(str_10: str):
    no_number_str = ""
    number_str = ""
    for i in range(len(str_10)):
        if "a" <= str_10[i] <= "z":
            no_number_str += str_10[i]
        else:
            number_str += str_10[i]
    print(f"纯数字字符串{number_str},非数字的字符串{no_number_str}。")

# func_10("1a2b35g")
