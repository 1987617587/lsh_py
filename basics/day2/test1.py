"""
# author Liu shi hao
# date: 2019/11/5 18:50
# file_name: test1

"""

import random

# 1.让用户输入一个月份，判断这个月是哪个季节？假定3到4月是春季，5到8月是夏季，9到10是秋季，11、12、1、2月是冬季。
#
# list_month = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# month = int(input("请输入一个月份："))
# if month not in list_month:
#     print("月份非法！")
# elif 3 <= month <= 4:
#     print("春季")
# elif 5 <= month <= 8:
#     print("夏季")
# elif 9 <= month <= 10:
#     print("秋季")
# else:
#     print("冬季")

# 2.让用户输入小强的语文、数学和英语成绩，输出以下判断是否正确，正确输出true，错误输出false
# a.语文、英语和数学成绩都大于85分；
# b.语文、英语和数学至少有一门大于95分；
# c.语文和英语至少有一门大于90分且数学不低于80分。
# language = int(input("请输入语文成绩："))
# math = int(input("请输入数学成绩："))
# english = int(input("请输入英语成绩："))
# print(language > 85 and math > 85 and english > 85)
# print(language > 95 or math > 95 or english > 95)
# print((language > 90 or math > 90) and english > 80)

# 3.完成一个简单的计算器程序，用户输入两个数字，用四则运算符计算结果并显示在控制台上。
# num1 = int(input("请输入第一个数字："))
# list_op = ["+", "-", "*", "/"]
# op = input("+、-、*、/:")
# if op in list_op:
#     num2 = int(input("请输入第二个数字："))
#     if op == "+":
#         print("计算结果为:", num1 + num2)
#     elif op == "-":
#         print("计算结果为:", num1 - num2)
#     elif op == "*":
#         print("计算结果为:", num1 * num2)
#     elif op == "/" and num2 != 0:
#         print("计算结果为:", num1 / num2)
#     else:
#         print("输入格式非法！")
# else:
#     print("输入格式非法！")
# 4.请用户输入两次，每次输入一个数字，如果用户输入的第一个数大就输出第一个数，如果用户输入的第二个数大就输出第二个数。
# num1 = int(input("请输入第一个数字："))
# num2 = int(input("请输入第二个数字："))
# print(num1 if num1 > num2 else num2)
# 5.请用户输入一个字符串，根据这个字符串的长度得出如下结果:
# s = "1234"  字符串的长度:len(s)
# 长度：0-56之间: 输出：短消息
# 长度：57-128之间: 输出：一般消息
# 长度：129-192之间: 输出：长消息
# 长度：193-256之间: 输出：超长消息
# 长度：其他情况：长度超过可发送上限
str1 = input("请输入一个字符串：")
if 0 < len(str1) < 56:
    print("短消息")
elif len(str1) <= 128:
    print("一般消息")
elif len(str1) <= 192:
    print("长消息")
elif len(str1) <= 256:
    print("超长消息")
else:
    print("长度超过可发送上限")
# 6.随机产生一个0-5之间的数：
# 随机产生的数：0：输出：进入战斗
# 随机产生的数：1：输出：捡到宝箱
# 随机产生的数：2：输出：捡到武器
# 随机产生的数：3：输出：捡到弹药
# 随机产生的数：4：输出：踩到陷阱
# 随机产生的数：5：输出：无事件


rand_num = random.randint(0, 5)
if rand_num == 0:
    print("进入战斗")
elif rand_num == 1:
    print("捡到宝箱")
elif rand_num == 2:
    print("捡到武器")
elif rand_num == 3:
    print("捡到弹药")
elif rand_num == 4:
    print("踩到陷阱")
else:
    print("无事件")

# 7.老师问学生,这道题你会做了吗?如果学生答"会了(y)",则可以放学.如果学生不会做(n),则老师再讲一遍
#
# an = input("会了么? y-会了 n-不会")
# if an == "y":
#     print("放学！")
# else:
#     print("再讲一遍")
# 8.提示用户输入年龄，如果大于等于18，则告知用户可以查看，如果小于10岁，则告知不允许查看，如果大于等于10岁并且小于18，则提示用户是否继续查看（yes、no），如果输入的是yes则提示用户请查看，否则提示"退出,你放弃查看"。
age = int(input("年龄:(0-149)"))
if 0 <= age <= 149:
    if age >= 18:
        print("随意查看")
    elif age < 10:
        print("不可查看！")
    else:
        an = input("是否继续?yes-继续 其他-放弃")
        if an == "yes":
            print("请查看")
        else:
            print("退出 放弃查看")
else:
    print("你是妖怪吧！")

# 9.请用户输入自身的血压值（高压和低压） 请依据下面标准血压 判断出用户的血压是否正常 若正常 显示血压正常 否则显示用户血压不正常
#   标准：成人：收缩压：90-140mmHg 舒张压：60-90mmHg
h_pa = int(input("高压:"))
l_pa = int(input("低压:"))
print("血压不正常") if h_pa < 90 or h_pa > 140 or l_pa < 60 or l_pa > 90 else print("血压正常")

# 10.某商店T恤的价格为35元/件（2件9折，3件以上8折）,裤子的价格为120元/条（2条以上9折）.小明在该店买了3件T恤和2条裤子,请计算并显示小明应该付多少钱?
t_count = int(input("T恤的件数:"))
tr_count = int(input("裤子的条数"))

dis1 = 0.9 if t_count == 2 else (1 if t_count == 1 else 0.8)
dis2 = 0.9 if tr_count > 2 else 1

print(35 * t_count * dis1 + 120 * tr_count * dis2)
