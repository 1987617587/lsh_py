"""
# author Liu shi hao
# date: 2019/11/13 20:16
# file_name: test_task

"""
import random

list_A_Z = [chr(65 + i) for i in range(26)]
list_a_z = [chr(97 + i) for i in range(26)]
list_0_9 = [chr(48 + i) for i in range(10)]
list_str = list_A_Z + list_a_z
# 选作：
# 11.编写一个程序，输入距离当前年月日的天数（可为负数） ，计算出差天数的年月日并显示出来。
#
#
import datetime

from day5.day5_task import in_int


def travel_days(days):
    travel_days = datetime.datetime.now() + datetime.timedelta(-days)
    return travel_days


# print(travel_days(10))


# 12.编写一个程序，输入两个字符串存储到2个字符串变量中，交换两个字符串的首尾两个字符并显示结果
# 例: abc ojk =>obk ajc
#
def procedure():
    r_str1 = ""
    r_str2 = ""
    str1 = input("字符串1：")
    str2 = input("字符串2：")
    r_str1 += str2[0]
    r_str2 += str1[0]
    for i in range(1, len(str1) - 1):
        r_str1 += str1[i]
    for j in range(1, len(str2) - 1):
        r_str2 += str2[j]
    r_str1 += str2[-1]
    r_str2 += str1[-1]
    print(f"转换前的字符串1：{str1}字符串2：{str1}。转换后的字符串1：{r_str1}字符串2：：{r_str2}。")


# procedure()
# 13.怪物boss血量100000，玩家使用某武器进行攻击，武器伤害值在121-344之间（随机产生伤害），求玩家攻击了多少次，怪物倒下。
#


# pk_boss(10000)
# 14.持续获取用户输入，直到用户输入的字符串全由字母组成。
#
def in_str():
    while True:
        str_14 = input("请输入：")
        for i in range(len(str_14)):
            if str_14[i] not in list_str:
                break
        else:
            return str_14


# print(in_str())
# 15.列出1-100之间的相邻质数的所有差值(相同得差值只显示一次)。
#

def prime_number_difference():
    list_prime_number = []
    list_difference = []
    for i in range(2, 101):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            list_prime_number.append(i)
    print(list_prime_number)
    for i in range(len(list_prime_number) - 1):
        list_difference.append(list_prime_number[i + 1] - list_prime_number[i])
    print(list_difference)
    print(set(list_difference))


# prime_number_difference()
# 16.为一个长度为100的字符列表随机赋值(a-z A-Z 0-9),然后判断’q’’i’’k’’u’这个字符序列是否在随机产生的列表中。
#
def qiku():
    list_100 = [" "] * 100
    q = i = k = u = 0
    for i in range(len(list_100)):
        list_100[i] = random.choice(list_0_9 + list_a_z + list_A_Z)
        if list_100[i] == "q":
            q = 1
        if list_100[i] == "i":
            i = 1
        if list_100[i] == "k":
            k = 1
        if list_100[i] == "u":
            u = 1
    if q == i == k == u == 1:
        return True


# print(qiku())

# 17.验证一个字符列表的字符序列是否出现在另外一个字符列表中。
#
list17_1 = ["asd","fg"]
list17_2 = ["asdfg","fg"]
def verify17(arr1:list,arr2:list):
    for i in range(len(list17_1)):
        for j in range(len(list17_2)):
            if list17_1[i] == list17_1[j]:
                return True


# print(verify17(list17_1, list17_2))
# 18.根据用户输入的行数打印出类似下面的图形：
# 例：7行
#    *
#   **
#  ***
# ****
#  ***
#   **
#    *
#
def task18():
    n = in_int()
    for i in range(n):
        if i < n // 2:
            print(" " * (n // 2 - i) + "*" * (i + 1))
        else:
            if n % 2 != 0:
                print(" " * (i - n // 2) + "*" * (n - i))
            else:
                print(" " * (i - n // 2 + 1) + "*" * (n - i))

# task18()


# 19.写一个函数将一个列表合并到另外一个列表中的指定位置。
#
list_19_1 = [1,2]
list_19_2 = [1,2,3,4,5]
def list_combine(arr1:list,arr2:list,arr3:int):
    list_19_combine = []
    for i in range(arr3):
        list_19_combine.append(list_19_2[i])
    for k in range(len(list_19_1)):
        list_19_combine.append(list_19_1[k])
    for j in range(arr3,len(list_19_2)):
        list_19_combine.append(list_19_2[j])
    return list_19_combine


# print(list_combine(list_19_1, list_19_2, 3))

# 20.有一个长度为30的整型列表，请按照下面的规律为其进行赋值：
#      1、1、2、3、5、8、13、21、34......
#
def task20(n):
    list_2 = [1, 1, 2, 3, 5, 8, 13, 21, 34]
    for i in range(n - len(list_2)):
        list_2.append(list_2[-1] + list_2[-2])
    print(list_2)

# task20(30)
# 21.假设有n个人坐成一圈，从某个人开始报数，数到m的人出圈，接着从出圈的下一个人开始重新报数，
# 数到m的人再次出圈，如此反复，直到所有人都出圈，请列出出圈顺序。
# list_man = [i for i in range(n)]
# list_man = ["ren1","ren2","ren3","ren4"]
# r_list_man = []
# while True:
#     m = 4
#     print(f"本次出圈人：{list_man[4 % 4 - 1]}")
#     r = list_man.index(list_man[4 % 4 - 1])
#     del list_man[4 % 4 - 1]
#     for i in range(r,len(list_man)):
#         r_list_man.append(list_man[i])
#     for k in range(r):
#         r_list_man.append(list_man[k])
#     print(list_man)
#     print(r_list_man)
#     list_man =r_list_man
#     # break
#     if len(list_man) == 2 :
#         print(f"倒数第二个出圈人：{list_man[1]}")
#         break



# 可选任务： 
# 任务1：
# 用户输入了一个矩阵的行和列
# 请检测用户输入的是否为数字并打印出回形矩阵
#
def back_matrix():
    n = in_int()
    m = in_int()
    for i in range(n):
        for j in range(m):
            print(min(i, j, n - i - 1, m - j - 1), end=" \t")
        print()

# back_matrix()
# 画图如下  方形图案参考
# 0  0 	0 	0 	0
# 0  1 	1 	1 	0
# 0  1 	2 	1 	0
# 0  1 	1 	1 	0
# 0  0 	0 	0 	0
# n = int(input("请输入行数："))
# for i in range(n):
#     for j in range(n):
#         print(min(i,j,n-i-1,n-j-1),end=" \t")
#     print()
# 5  5 	5 	5 	5
# 5  4 	4 	4 	5
# 5  4 	3 	4 	5
# 5  4 	4 	4 	5
# 5  5 	5 	5 	5
# m = int(input("请输入行数："))
# for i in range(1,m+1):
#     for j in range(1,m+1):
#         print(max(i,j,m-i+1,m-j+1),end=" \t")
#     print()

# 任务2： 
# 将一个整型列表中元素按照从小到大的顺序排列。 
# 比较过程中如果发现前数比后数大 交换两个位置的值
#
def task2(arr: list):
    r_arr = []
    # 列表不能为None 为空
    if arr is None or len(arr) == 0:
        return False
    for i in range(len(arr)-1,-1,-1):
        r_arr.append(max(arr))
        arr.remove(max(arr))

    return r_arr

# print(task2([1, 2, 3, 4, 2, 1]))
# 任务3： 
# 判断一个字符串是否是一个回文字符串（正着读反着读都一样）？ 
#
def task3(arr: str):
    # 列表不能为None 为空
    if arr is None or len(arr) == 0:
        return False
    for i in range(len(arr) // 2):
        # i,len(arr)-1-i
        if arr[i] != arr[len(arr) - 1 - i]:
            return False
        pass
    return True


# print(task3("123454321"))
# 任务4： 
# 每局有十轮 
# 球道上有10个球瓶 
# 第1~9轮，每次可以投掷1~2次 
# 第10轮，可以投掷2~3次 
# 计分规则： 
# 全中(strike):一次碰倒10个，这一轮的得分=10+接下来两次碰倒瓶子的个数 
# 补中(spare)两次碰倒10个，这一轮的得分=10+下一次碰倒瓶子的个数 
# 失误(fault)两次碰倒的个数小于10，这一轮的得分=碰倒瓶子的个数 
# 最后一次(第10轮)： 
# 全中，1+2 
# 补中，2+1 
# 失误，2 
#
# 10、10、10、10、10、10、10、10、10、10、10、10 
# 300 
# 0、2|7、3|10|1、4|5、2|10|6、2|8、2|4、1|7、3、8 
# 2+20+15+5+7+18+8+14+5+18 
#
# list4_1 = [0,2]  # 2
# list4_2 = [7,3]  # 10+7+3
# list4_3 = [10]  # 10+1+4
# list4_4 = [1,4]
# list4_5 = [5,2]
# list4_6 = [10]
# list4_7 = [6,2]
# list4_8 = [8,2]
# list4_9 = [4,1]
# list4_10 = [7,3,8]

# 任务5：
# 四格猜数游戏
# 1.每一个格子的数各不相同
# 2.如果数字和位置都对 1A    提示
# 3.如果数字在四格内但是位置不对 1B
# 4.九次机会 
# 5.  1234     3256   1A1B
# 6.重复玩
# 7.无论对错 请告知答案


def answer():
    list_answer = []
    while len(list_answer) < 4:
        num = random.randint(0, 9)
        if num not in list_answer:
            list_answer.append(num)
    return list_answer


def guess():
    list_guess = []
    for i in range(4):
        while True:
            num = input(f"请猜第{i}个数：")
            if num.isdigit() and 0 <= int(num) <= 9:
                list_guess.append(int(num))
            print("请重新输入！")
    return list_guess

# def hint():
#     answer()
#     guess()
#     for i in range(4):
#         if list_guess[i] ==list_answer[i]:
#             list_guess.
