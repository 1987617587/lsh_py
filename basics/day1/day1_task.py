"""
# author Liu shi hao
# date: 2019/11/5 18:47
# file_name: day1_task
今日小结：
语言发展史；
代码的组织结构：建立项目，项目里面可以放包，模块。
模块里面应该遵守约束和约定，自上而下，先在三引号内写上模块说明性文字。
再看有没有需要添加的第三方库，之后定义一下常量，变量用代码实现函数，类等。
编程规范：遵守约束和约定，一般ctrl+alt+L即可搞定

"""
# 必做任务：
# 任务1：
# 模仿Hello world案例，写一个方法向控制台输出字符串"Hello Python！"。
# print("Hello Python！")
# # 任务2：
# # 在你的方法中定义变量，用这些变量存储游戏中一个敌人应该有的一些属性（比如用户名，等级，经验值，血量，魔法值等），定义尽可能多的变量。
# name = "典韦"
# grade = 15
# EXP = 100
# blood_flow = 2500
# MP = 500
# # 任务3：
# # 提示用户输入籍贯，当用户输入籍贯后，向用户显示"欢迎您来到某某" ，某某是用户输入的籍贯地。
# ad = input("请输入籍贯：")
# print("欢迎您来到", ad)
# # 任务4：
# # 编写一个控制台应用程序，要求用户输入4个int值，并显示他们的乘积。
# a = int(input("请输入第一个值："))
# b = int(input("请输入第二个值："))
# c = int(input("请输入第三个值："))
# d = int(input("请输入第四个值："))
# print("成绩为：", a * b * c * d)
# 任务5：
# 让用户分别输入姓名，语文，数学，英语 三门课的成绩，然后给用户显示：XX，你的总成绩为XX分，平均成绩为XX分。
# name_1 = input("请输入姓名：")
# ch = int(input("请输入语文成绩："))
# math = int(input("请输入数学成绩："))
# english = int(input("请输入英语成绩："))
# total_points = english + math + ch
# average = total_points / 3
# print(f"{name_1}，你的总成绩为{total_points}分，平均成绩为{average}分",)

# 任务6：
# 编写一个程序，输入梯形的上底 下底 和高 ，计算出来梯形的面积并显示出来。
#     梯形的面积=（上底+下底）*高 /2
# upper_base = int(input("请输入上底："))
# down_base = int(input("请输入下底："))
# tall = int(input("请输入高："))
# proportion = ((upper_base + down_base) * tall) / 2
# print(f"梯形面积为：{proportion}")
# 任务7：
# 编程实现计算指定的天数(如46天)是几周零几天。
# 由用户输入天数 
# days = int(input("请输入天数："))
# weeks = days // 7
# day = days % 7
# print(f"{days}天是{weeks}周零{day}天")
# 任务8：
# 接受用户输入的两个整数，存储到两个变量里面，交换变量存储的值。

# n1 = int(input("整数:"))
# n2 = int(input("整数:"))
# # python独有的语法
# n1, n2 = n2, n1
# print("n1=", n1, "n2=", n2)
# 1.临时变量：万能交换法：适配所有的数据类型
# temp = n1
# n1 = n2
# n2 = temp
# print("n1=", n1, "n2=", n2)
# 2.求和法：只能适配数字
# n1 = n1 + n2
# n2 = n1 - n2
# n1 = n1 - n2
# print("n1=", n1, "n2=", n2)
# 异或：只能适配整数
# n1 = n1 ^ n2
# n2 = n1 ^ n2
# n1 = n1 ^ n2
# print("n1=", n1, "n2=", n2)

# 可选任务：
# 任务9：
# 写一个方法，传递两个参数，分别代表年份和月份，计算这个月的天数（可选）。
# 注：闰年的 2 月有 29 天；能被 4 整除同时不能被 100 整除即为闰年；如果能被 400 整除的是闰年，除此两种条件，其他都是非闰年。
years = int(input("请输入年份："))
months = int(input("请输入月份："))
if (years % 4 == 0 and years % 100 != 0) or years % 400 == 0:
    if months in [1, 3, 5, 7, 8, 10, 12]:
        print("这个月的天数为31")
    elif months in [4, 6, 9, 11]:
        print("这个月的天数为30")
    elif months == 2:
        print("这个月的天数为29")
else:
    if months in [1, 3, 5, 7, 8, 10, 12]:
        print("这个月的天数为31")
    elif months in [4, 6, 9, 11]:
        print("这个月的天数为30")
    elif months == 2:
        print("这个月的天数为28")

# 任务10：
# 从键盘输入一个三位的正整数，把百分位十分位个位数字的相反顺序输出。
num = int(input("请输入一个三位数："))
num_2 = num // 100 + ((num - (num // 100) * 100) // 10) * 10 + (num % 10) * 100
print(num_2)

str_num = input("请输入一个三位数:")
print(str_num[2], str_num[1], str_num[0])
# 思考题:
# 如何为大小写混杂的字符串排序？
# 例如: CabD=>abCD; 









