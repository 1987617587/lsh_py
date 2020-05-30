"""
# author Liu shi hao
# date: 2019/12/2 18:25
# file_name: day21_str_task

"""

# 19.浮点数20.73，向上取整，向下取整，正弦值
import calendar
import time
from datetime import datetime, timedelta


def func_19(f1: str):
    arr = f1.split('.')
    if int(arr[1]) > (5 * 10 ** (len(arr[1]) - 1)):
        return int(arr[0]) + 1
    return int(arr[0])


# print(func_19("20.43"))


# 20.弧度π/4，π/2,对应的度数
def func_20(radian: str):
    arr = radian.split('/')
    if arr[0] == "π":
        dge = str(180 / (int(arr[1]))) + "度"
        return dge
    return "暂不支持其他格式！"


# print(func_20("π/3"))


# 21.输入一个日期，格式如：2010 10 24 ，判断这一天是这一年中的第几天。

# 直接使用函数
# in_time = input("请输入日期:")
# in_time = datetime.strptime(in_time, "%Y %m %d")
# start_time = datetime.strptime("2010 01 01", "%Y %m %d")
# print(((in_time - start_time).days + 1))
#
# # print(time.localtime().tm_year)
# t = (2010, 10, 24, 0, 0, 0, 0, 0, 0)
# print(time.localtime(time.mktime(t)).tm_yday)
# 22.已知2011年11月11日是星期五，输入日期 ，问YYYY年MM月DD日是星期几
def func22():
    in_time = input("请输入日期:")
    in_time = datetime.strptime(in_time, "%Y %m %d")
    dt = datetime.strptime("2011 11 11", "%Y %m %d")
    if dt <= in_time:
        print(((in_time - dt).days + 5) % 7) if ((in_time - dt).days + 5) % 7 != 0 else print(7)
    else:
        print(abs((in_time - dt).days + 5) % 7) if abs((in_time - dt).days + 5) % 7 != 0 else print(7)


# func22()

# 23.系统会随机给你一个日期（yyyy-MM-dd）字符串，你需要计算这个时间上一个月的最后一天的具体日期，最后以yyyy年MM月dd日的字符形式返回
def func_23():
    os = input("请输入:")
    os_time = datetime.strptime(os, "%Y-%m-%d")
    print(f"{os} 的上一个月的最后一天是 {os_time.year}年{os_time.month - 1}月", end="")
    print(f"{calendar.monthrange(os_time.year, os_time.month - 1)[1]}日", end="")  # 总天数(即当月的第几天)
    day = calendar.monthrange(os_time.year, os_time.month - 1)[1]  # 总天数(即当月的第几天)
    print(f"星期{calendar.weekday(os_time.year, os_time.month - 1, day) + 1}", end="")  # 星期几+1(中国)


# func_23()

def func_23_2():
    os = input("请输入:")
    os_time = datetime.strptime(os, "%Y-%m-%d")
    dt = os_time - timedelta(days=os_time.day)
    return dt.strftime("%Y{}%m{}%d{}").format("年", "月", "日")


# print(func_23_2())


# 24.输入两个日期,获得两个日期相差几天，几小时，几秒
def func_24():
    dt1 = datetime.strptime("2019-11-21 00:00:00", "%Y-%m-%d %H:%M:%S")
    dt2 = datetime.strptime("2019-11-20 00:00:00", "%Y-%m-%d %H:%M:%S")
    print(f"两个日期相差{(dt1 - dt2).days}天{(dt1 - dt2).seconds // 3600}小时"
          f"{(dt1 - dt2).seconds % 3600 // 60}分{(dt1 - dt2).seconds % 60}秒")  # 把不足一天的总秒数换成时分秒


# func_24()
# 1.	‘2019-7-22’去掉‘-’输出
def func_1():
    s = "2019-7-22"
    arr = s.split('-')
    print("".join(arr))


# func_1()

# 2.	统计字符串x中 1的个数 x=‘20191112’
def fun_2(x: str):
    return x.count("1")


# print(fun_2("20191112"))


# 3.	统计字符串中数字个数,如：“b2bc31b416u” ===> 输出6 [参看 ’2’.isdigit()]
def func_3(s: str):
    j = 0
    for i in s:
        if i.isdigit():
            j += 1
    return j


# print(func_3("b2bc31b416u"))


# 4.	i am biter 逆置为：biter am i
def func_4(s: str):
    arr = s.split()
    arr.reverse()
    print(" ".join(arr))


# func_4("i am biter")
# 5.	删除字符串中所有的数字
def func_5(s: str):
    new_s = ""
    for i in s:
        if not i.isdigit():
            new_s += i
    return new_s


# print(func_5("b2bc31b416u"))

# 6.	写代码，有如下变量，请按照要求实现每个功能,name = " gouguoQ "
# (1)	将name变量对应的值中的"o"，替换为"p"，并输出结果
name = " gouguoQ "


# name = name.replace('o', 'p')
# print(name)
# (2)	将name变量对应的值根据"o"分割，并输出结果
# print(name.split("o"))
# (3)	移除name变量对应值的两边的空格，并输出移除后的内容
# print("".join(name.split()))
# (4)	判断name变量对应的值是否以"go"开头，并输出结果
# print(name.startswith("go"))
# (5)	判断name变量对应的值是否以"Q"结尾，并输出结果
# print(name.endswith("Q"))
# 7.	对给定的10个国家名，按其字母的顺序输出
def func_7(arr: list):
    list = []
    sort_list = []
    for i in range(len(arr)):
        list.append(arr[i][0].upper())
    list.sort()
    print(list)
    for j in range(len(arr)):
        for k in range(len(arr)):
            if list[j] == arr[k][0].upper():
                sort_list.append(arr[k])
    return sort_list


# print(func_7(["Madf", "Casd", "jAD"]))

# 8.	求输入英文句子单词的平均长度。
def func_8(s: str):
    li = s.split()
    num = 0
    for i in range(len(li)):
        num += len(li[i])
    return num / len(li)


# print(func_8("asd asf af asfe asd"))

# 9.	判断一个数是否是回文数。若一个数（首位不为零）从左到右与从右到左都是一样的，我们将之称为回文数。例如：121。
def func_9(n: str):
    lisr_n = list(n)
    lisr_n.reverse()
    if n[0] != "0" and lisr_n == list(n):
        return True
    return False


# print(func_9("121"))

# 10.	开发敏感词语过滤程序， 提示用户输入内容，如果用户输入的内容中包含特殊的字符：
# 如 "老牛很邪恶" "你是大笨蛋"，则将(邪恶、笨蛋)等内容替换为 ***
def func_10():
    in_str = input("请输入:")
    if "邪恶" in in_str:
        s = in_str.replace('邪恶', '**')
        if "笨蛋" in s:
            r_s = s.replace('笨蛋', '**')
            return r_s
        return s
    if "笨蛋" in in_str:
        w = in_str.replace('笨蛋', '**')
        return w


# print(func_10())

# 11.	请用代码实现：
# 　　a.利用下划线将列表的每一个元素拼接成字符串,li＝"alexericrain"
def func_a(li: list):
    r_str = ""
    for i in range(len(li[0])):
        r_str += li[0][i]
        if i == len(li[0]) - 1:
            return r_str
        r_str += "_"


# print(func_a(["ascwh"]))


# 　　b.利用下划线将列表的每一个元素拼接成字符串,li＝['alex','eric','rain']
def func_b(li: list):
    r_str = ""
    for i in range(len(li)):
        r_str += li[i]
        if i == len(li) - 1:
            return r_str
        r_str += "_"


# print(func_b(['alex', 'eric', 'rain']))

# 12.	制作趣味模板程序
# 需求：等待用户输入名字、地点、爱好，根据用户的名字和爱好进行任意现实
# 如：尊敬可亲的 xxx，最喜欢在 xxx 地方干 xxx
def func_12():
    user_input = input("请输入名字、地点、爱好:")
    user_list = user_input.split("、")
    print(f"尊敬可亲的 {user_list[0]}，最喜欢在 {user_list[1]} 地方干 {user_list[2]}")


# func_12()

# 13.	把my-short-string形式的字符串转化成myShortString形式的字符串
def func_13(s: str):
    li_s = s.split("-")
    r_s = ""
    r_s += li_s[0]
    for i in range(1, len(li_s)):
        r_s += li_s[i].capitalize()
    return r_s


# print(func_13("my-short-string"))


# 14.	 去除字符串中的重复字符,例如:’abcdefgahx’ ==> ‘bcdefghx’
def func_14(str1: str):
    # r_s = ""
    # for i in range(len(s)):
    #     for j in range(len(s)):
    #         if s[i] == s[j]:
    #             pass
    #         else:
    #             r_s += s[j]
    #     return r_s
    # 列表生成式
    ret_list = [str1[index] for index in range(len(str1)) if str1.count(str1[index]) == 1]
    return "".join(ret_list)


print(func_14("abcdefgahx"))


# 15.	字符串转化（压缩） “aabbccdaa” -> “a2b2c2d1a2”
def func_15(s: str):
    j = 1
    r_s = ""
    for i in range(1, len(s)):
        if s[i - 1] == s[i]:
            j += 1
            if i == len(s) - 1:
                r_s += (s[i - 1] + str(j))
        else:
            r_s += (s[i - 1] + str(j))
            j = 1
    return r_s


print(func_15("aabbccdaa"))


# 16.	定义一个字符串str='abcdefghijklmnopqrstuvwxyz'，在每个字符串前面加上序号。比如‘1a2b3c.....26z’
def func_16(s):
    r_s = ""
    for i in range(len(s)):
        r_s += (str(ord(s[i]) - 96) + s[i])
        # r_s += (str(i + 1) + s[i])

    return r_s


# print(func_16("abcdefghijklmnopqrstuvwxyz"))

# 17.	一位作家正在写最新的诗，图灵和机器。聘请你来帮忙找出诗歌中出现次数最多的这个词。你可以通过反复调用input()来读取诗的每一行，其中最后一行包含三个字符 ###。
# 每一行都是由单个空格分隔的单词组成的，没有数字或标点符号。请你将所有的单词转换成小写，并打印出现次数最多的那个单词,例如输入如下：
# Here is a line like sparkling wine
# Line up fast or be the last
# ###
#
def func_17():
    li = ""
    while "###" not in li:
        li += (input("请输入：").lower())

    li = li.split()
    char_counts = [li.count(ch) for ch in li]
    print(li[char_counts.index(max(char_counts))])
    return li


# print(func_17())


# 18.	小明有N个字符串，他想将这些字符串分类，他认为两个字符串A和B属于同一类需要满足以下条件：
# A中交换任意位置的两个字符，最终可以得到B，交换的次数不限。比如：abc与bca就是同一类字符串。现在小明想知道这N个字符串可以分成几类。
# (1)	输入描述:
# 首先输入一个正整数N（1 <= N <= 10），接下来输入N个字符串，每个字符串长度不超过10。
# (2)	输出描述:输出一个整数表示分类的个数。d
def in_int():
    while True:
        num = input("请输入正整数N（1 <= N <= 10）：")
        if num.isdigit() and 1 <= int(num) <= 10:
            return int(num)
        print("重新输入！")


def func_18():
    n = in_int()
    s_name = 0
    li = []
    while s_name < n:
        s = input("请输入：")
        if 0 < len(s) <= 10:
            s_name += 1
            li.append(s)
    print(li)
    p = 0
    d = 0
    for i in range(len(li)):
        for j in range(len(li)):
            if len(li[i]) == len(li[j]) and i != j:
                for k in range(len(li[i])):
                    if li[i].count(li[i][k]) == li[j].count(li[i][k]):
                        p += 1
                if p == len(li[j]):
                    p = 0
                    print(f"本组同类{li[i]},{li[j]}")
                    d += 0.5
                else:
                    p = 0

    return d


# func_18()


def func_18_2(n=in_int()):
    s_name = 0
    li = []
    while s_name < n:
        s = input("请输入：")
        if 0 < len(s) <= 10:
            s_name += 1
            s = list(s)
            s.sort()
            li.append(s)
    print(li)
    arr = []

    for i in range(len(li)):
        if li[i] not in arr and li.count(li[i]) > 1:
            arr.append(li[i])
            arr.append(li.count(li[i]))
        else:
            if li.count(li[i]) == 1:
                arr.append(li[i])
                arr.append(li.count(li[i]))
    print(f"分类的个数{len(arr) / 2}")
    print(f"分类组合：{arr}")


func_18_2()
