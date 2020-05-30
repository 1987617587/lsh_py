"""
# author Liu shi hao
# date: 2019/11/22 18:43
# file_name: day14_task14

"""


# 1.去掉字符串中的所有空格
import pygame


def func_1(arr: str):
    str_1 = ""
    # str_in = input("请输入字符串：")
    for i in range(len(arr)):
        if arr[i] != " ":
            str_1 += arr[i]
    return str_1


# print(func_1("asd  efr  rtg"))

# 2.对字符串进行简单加密与解密
def func_2():
    msg = input("请输入：")
    # send_msg = msg.encode(encoding='gb2312') # 按照UTF-8的编码格式获取
    # print(send_msg)
    # print(send_msg.decode(encoding='gb2312'))  # 按照UTF-8的编码格式解码
    r_msg = ""
    x_msg = ""
    for i in range(len(msg)):
        r_msg += chr(ord(msg[i]) + 12)

    print(f"加密后：{r_msg}")
    for j in range(len(r_msg)):
        x_msg += chr(ord(msg[j]) - 12)

    print(f"解密后{msg}")


func_2()


# 3.将字母全部转换为大写或小写
# string.upper()
# 转换
# string
# 中的小写字母为大写
# string.lower()
# 转换
# string
# 中的大写字母为小写
def func_3_1():
    an = input("请输入：")
    r_str = ""
    for i in range(len(an)):
        if an[i] in [chr(j) for j in range(65, 91)]:
            r_str += chr(ord(an[i]) + 32)
        else:
            r_str += an[i]
    return r_str


def func_3_2():
    an = input("请输入：")
    r_str = ""
    for i in range(len(an)):
        if an[i] in [chr(j) for j in range(97, 122)]:
            r_str += chr(ord(an[i]) - 32)
        else:
            r_str += an[i]
    return r_str


# print(func_3_1())
# print(func_3_2())
# 4.根据标点符号对字符串进行分行


# func_4("good!")
# 5.去掉字符串列表中每个字符串的空格：注意方法复用
def func_5(arr: list):
    r_list = []
    for i in range(len(arr)):
        r_list.append(func_1(arr[i]))
    return r_list


# print(func_5(["asfg  sdfg","arf ae ert"]))

# 6.随意输入你心中想到的一个书名，然后输出它的字符串长度。  （len(字符串)可以得字符串的长度）
def func_6():
    an = input("请输入你心中想到的一个书名：")
    return len(an)


# print(func_6())
# 7.两个学员输入各自最喜欢的游戏名称，判断是否一致,如果相等,则输出你们俩喜欢相同的游戏；如果不相同,则输出你们俩喜欢不相同的游戏。
def func_7():
    game1 = input("请学员1输入你喜欢的游戏名称：")
    game2 = input("请学员2输入你喜欢的游戏名称：")
    if game1 == game2:
        print("你们俩喜欢相同的游戏")
    print("你们俩喜欢不相同的游戏")


# func_7()
# 8.让用户输入一个日期格式如“2008/08/08”，将 输入的日期格式转换为“2008年-8月-8日”。
def func_8():
    r_str = ""
    user_in = input("输入一个日期:")
    for i in range(10):
        if user_in[i].isdigit():
            r_str += user_in[i]
        else:
            if i == 4:
                r_str += "年-"
            if i == 7:
                r_str += "月-"

    r_str += "日"
    x_str = ""
    for j in range(len(r_str)):
        if j < 5:
            x_str += r_str[j]
        else:
            if r_str[j] == "0":
                pass
            else:
                x_str += r_str[j]

    print(r_str)
    print(x_str)


# func_8()

# 9.接收用户输入的字符串，将其中的字符进行排序（升序），并以逆序的顺序输出，“cabed”→"abcde"→“edcba”。

# 10.接收用户输入的一句英文，将其中的单词以反序输出，“hello c sharp”→“sharp c hello”。
list_words = []
list_1 = []
while 1:
    str_1 = input("请输入单词(用空格结束单词):")
    if " " in str_1:
        list_1.append(str_1)
    elif "." in str_1:  # 用户输入“.”结束
        break
list_1.reverse()
print(list_1)
# 11.从请求地址中提取出用户名和域名
# http://www.163.com?userName=admin&pwd=123456

# 12.让用户输入一句话,判断这句话中有没有邪恶,如果有邪恶就替换成这种形式然后输出,如:“老牛很邪恶”,输出后变成”老牛很**”;
# 13.如何判断一个字符串是否为另一个字符串的子串
# 14.如何验证一个字符串中的每一个字符均在另一个字符串中出现过
# 15.如何随机生成无数字的全字母的字符串
# 16.如何随机生成带数字和字母的字符串
# 注意：如何判定一个字符串中既有数字又有字母
# 17.字符串内的字符排序（只按字母序不论大小写）
# 18.字符串的补位操作
# 1  =》001
# 2  =》002
# 10=》010
# pygame.
