"""
# author Liu shi hao
# date: 2019/11/27 18:01
# file_name: task

"""

# 1.去掉字符串中的所有空格
import calendar
import random
import re

from datetime import datetime


def func_1(s: str):
    li = s.split()
    return "".join(li)


# print(func_1("a b c d"))


# 2.根据完整的路径从路径中分离文件路径、文件名及扩展名
def func_2(s: str):
    path = s.rpartition("\\")
    filename = s[s.rfind("\\") + 1:s.rfind(".")]
    extend_name = s[s.rfind(".") + 1:len(s)]
    print(f"文件路径{path}文件名{filename}扩展名{extend_name}")


func_2("E:\python1911A\day15模块.jpg")


# 3.获取字符串中汉字的个数
def func_3(s: str):
    num = 0
    for i in range(len(s)):
        if "\u4e00" <= s[i] <= "\u9fa5":
            num += 1

    return num


# print(func_3("adsf 你是魔鬼中的天使f"))
# print("\u4e00")
# 汉字的范围
# print("\u9fa5")
def func_3_2(s):
    num = re.findall("[\u4e00,\u9fa5]]", s)
    return len(num)


# print(func_3_2("asd你好adff"))
# 4.对字符串进行加密与解密
def func_4():
    msg = input("请输入：")
    r_msg = ""
    x_msg = ""
    for i in range(len(msg)):
        r_msg += chr(ord(msg[i]) + 12)

    print(f"加密后：{r_msg}")
    for j in range(len(r_msg)):
        x_msg += chr(ord(msg[j]) - 12)

    print(f"解密后:{msg}")


# func_4()
def func_4_1():
    src = "abcdefghijklmnopqrstuvwxyz0123456789"
    tgt = "0123456789abcdefghijklmnopqrstuvwxyz"
    # 制作密码本
    encrypt = str.maketrans(src, tgt)
    name = input("用户名;")
    pwd = input("密码;")
    r_pwd = pwd.translate(encrypt)
    print(f"加密后:{r_pwd}")
    uname = input("登录用户名;")
    upwd = input("登录密码;")
    if uname == name and upwd.translate(encrypt) == pwd:
        print("登录成功")
    else:
        print("登录失败")


# func_4_1()

# 5.将字母全部转换为大写或小写
# string.upper()转换string中的小写字母为大写
# print(str.upper("asd"))
# string.lower()转换string中的大写字母为小写
# print(str.lower("ADd"))


# 6.根据标点符号对字符串进行分行
def func_6(s: str):  # 句号分行
    for i in range(len(s.split("."))):
        print((s.split(".")[i]), end="\n")


# func_6("afa,dagfwer,sgreg.asfa.dfge.")
# 7.去掉字符串数组中每个字符串的空格
def func_7(arr: list):
    r_list = []
    for i in range(len(arr)):
        r_list.append(func_1(arr[i]))
    return r_list


# print(func_7(["ad fg ", "sf gra th", " sf "]))


# 8.随意输入你心中想到的一个书名，然后输出它的字符串长度。  （len()属性:可以得字符串的长度）
def func_8():
    an = input("请输入你心中想到的一个书名：")
    return len(an)


# print(func_8())
# 9.两个学员输入各自最喜欢的游戏名称，判断是否一致,如果相等,则输出你们俩喜欢相同的游戏；如果不相同,则输出你们俩喜欢不相同的游戏。
def func_9():
    game1 = input("请学员1输入你喜欢的游戏名称：")
    game2 = input("请学员2输入你喜欢的游戏名称：")
    if game1 == game2:
        print("你们俩喜欢相同的游戏")
    print("你们俩喜欢不相同的游戏")


# func_9()
# 10.上题中两位同学输入 lol和 LOL代表同一游戏，怎么办?
def func_10():
    game1 = input("请学员1输入你喜欢的游戏名称：")
    game2 = input("请学员2输入你喜欢的游戏名称：")
    if game1.lower() == game2.lower():
        print("你们俩喜欢相同的游戏")
        return
    print("你们俩喜欢不相同的游戏")


# func_10()
# 11.让用户输入一个日期格式如“2008/08/08”，将 输入的日期格式转换为“2008年-8月-8日”。
def func_11():
    r_str = ""
    user_in = input("输入一个日期:")
    year = user_in[0:4]
    month = str(int(user_in[5:7]))
    day = str(int(user_in[8:10]))

    date = (year + "年-" + month + "月-" + day + "日")
    return date


# print(func_11())
# 12.接收用户输入的字符串，将其中的字符进行排序（升序），并以逆序的顺序输出，“cabed”→"abcde"→“edcba”。

def func_12():
    r_arr = []
    r_str = ""
    str_12 = input("请输入;")

    for i in range(len(str_12)):
        r_arr.append(ord(str_12[i]))
    r_arr.sort()
    # print(r_arr)
    for j in range(len(str_12) - 1, -1, -1):
        r_str += chr(r_arr[j])
    return r_str


# print(func_12())


# 13.接收用户输入的一句英文，将其中的单词以反序输出，“hello c sharp”→“sharp c hello”。

def func_13(s: str):
    r_s = s.split(" ")
    r_s.reverse()
    print(r_s)


func_13("hello c sharp")


# 14.从请求地址中提取出用户名和域名
# http://www.163.com?userName=admin&pwd=123456
def func_14(s: str):
    name = s[s.find("="):s.rfind("=")]
    domain_name = s[s.rfind("="):len(s)]
    print(f"用户名{name}域名{domain_name}")


# func_14("http://www.163.com?userName=admin&pwd=123456")


# 15.有个字符串数组，存储了10个书名，书名有长有短，现在将他们统一处理，
# 若书名长度大于10，则截取长度8的子串并且最后添加“...”，加一个竖线后输出作者的名字。
def func_15():
    s = ("asdhfjdhd", "wrtreeryhfrjtyrth", "afda")
    r_s = []
    for i in range(len(s)):
        if len(s[i]) > 10:
            r_s.append(s[i][0:8] + "..." + "|")
        else:
            r_s.append(s[i])
    return r_s


# print(func_15())

# 16.让用户输入一句话,找出所有"呵"的位置。
def func_16():
    msg = input("请输入：")
    s = msg.find("呵")
    while s != -1:
        print(s)
        s = msg.find("呵", s + 1)


# func_16()
# 17.让用户输入一句话,找出所有"呵呵"的位置。
def func_17():
    msg = input("请输入：")
    s = msg.find("呵呵")
    while s != -1:
        print(s)
        s = msg.find("呵呵", s + 1)


# func_17()
# 18.让用户输入一句话,判断这句话中有没有邪恶,如果有邪恶就替换成这种形式然后输出,
# 如:“老牛很邪恶”,输出后变成”老牛很**”;
def func_18():
    s = input("请输入：")
    if "邪恶" in s:
        return s.replace("邪恶", "**")


# print(func_18())


# 19.如何判断一个字符串是否为另一个字符串的子串
def func_19(s1: str, s2: str):
    if s1 in s2:
        return True
    return False


# print(func_19("s", "ads"))


# 20.如何验证一个字符串中的每一个字符均在另一个字符串中出现过
def func_20(s1: str, s2: str):
    j = 0
    for i in range(len(s1)):
        if s1[i] in s2:
            j += 1
    if j == len(s1):
        return True
    return False


# print(func_20("asd", "abcsd"))
# 21.如何随机生成无数字的全字母的字符串
def func_21(n: int):
    s = ""
    for i in range(n):
        if random.randint(0, 1) == 0:
            s += chr(random.randint(65, 90))
        else:
            s += chr(random.randint(97, 122))
    return s


# print(func_21(4))

# 22.如何随机生成带数字和字母的字符串
def func_22(n: int):
    s = ""
    for i in range(n):
        r = random.randint(0, 2)
        if r == 0:
            s += chr(random.randint(65, 90))
        elif r == 1:
            s += chr(random.randint(97, 122))
        else:
            s += chr(random.randint(48, 57))
    return s


# print(func_22(4))
# 23.如何判定一个字符串中既有数字又有字母
def func_23(s: str):
    j = m = 0
    for i in range(len(s)):
        if s[i].isdigit():
            j = 1
        if s[i].islower() or s[i].isupper():
            m = 1
    if j == m == 1:
        return True
    return False


# print(func_23("asd123"))
# 24.字符串内的字符排序（只按字母序不论大小写）
#
# print(min("asdas"))
# print(min("Asdas"))

# 大写优先
def func_24():
    # max_arr = []
    # min_arr = []
    r_str = ""
    str_12 = list(input("请输入;"))

    for i in range(len(str_12)):
        r_str += min(str_12)
        str_12.remove(min(str_12))
    return r_str


print(func_24())


# 25.字符串的补位操作
# 1  =》001
# 2  =》002
# 10=》010
def func_25(s: str):
    return s.rjust(3, "0")


# print(func_25("1"))

# 22.已知2011年11月11日是星期五，输入日期 ，问YYYY年MM月DD日是星期几
def func22():
    in_time = input("请输入日期:")
    in_time = datetime.strptime(in_time, "%Y{0}%m{1}%d{2}".format("年", "月", "日"))
    dt = datetime.strptime("2011年11月11日", "%Y{0}%m{1}%d{2}".format("年", "月", "日"))
    if dt <= in_time:
        print(((in_time - dt).days+5)%7)
    else:
        print(abs((in_time - dt).days + 5) % 7)


func22()

# def func22_1():
#     str_date = "2019年12月25日"
#     dt = datetime.strftime((str_date,"%Y年%m月%d月"))
#     print(calendar.weekday(2019, 12, 4)+1)
