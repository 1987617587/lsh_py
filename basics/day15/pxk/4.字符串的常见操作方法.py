# 字符串的查找
# s = "谁爱像一阵风，吹完它就走，这样的节奏，谁都无可奈何"
# print(s.find("谁"))#find返回的是从左向右第一次出现的位置
# print(s.rfind("谁"))#find返回的是从右向左第一次出现的位置
# print(s.find("亚"))#找不到返回-1
#
# print(s.index("谁"))
# print(s.rindex("谁"))
# # print(s.rindex("亚"))找不到报错

# 统计
# l = len(s)
# print(l)
# count()返回查找的字符的次数
# print(s.count("谁"))

# s = "谁爱像一阵风,吹完它就走,这样的节奏,谁都无可奈何"
# 将字符串拆分3段
# t = s.partition("风")
# print(t)
# print(len(t))
# print(t[0])
# print(t[1])
# print(t[2])
# for i in t:
#     print(i)

# split 按照指定字符拆分
# sub_str = s.split(",")
# print(sub_str)

s = "Hellopython哈尼123"
s2 = "WORLD"
s3 = "123"
s4 = " "
# 一系列判断
# print(s.islower())#判断是否全小写

# name = input("请输入：")
# if name.islower():
#     print("请输入全大写")

# print(s2.isupper())#判断是否全大写

# print(s.istitle())#只有首字母大写  判断是否是标题

# print(s3.isdigit())#判断是否全数字

# data = input("请输入数字：")
# if data.isdigit():
#     print("输入成功！")

print(s.isalpha())  # 判断字母和汉字

# print(s4.isspace())#判断是否空格

# print(s3.isalnum())#字母or数字or数字and字母and汉字

# print(s.startswith("h"))#判断以什么开头

# email = input("请输入邮箱：")
# if email.endswith("@qq.com")
#     print("格式正确")

# print(s.endswith("13"))#判断以什么结尾

# url = input("路径：")
# if url.startswith("https://"):
#     print("网址输入正确！")

# s2= "WORLD"
# print(s2.lower())#转小写
# s5 = "hello"
# print(s5.upper())#转大写

# res = input("游戏结束按Q键退出")
# if res.upper() == "Q":
#     print("游戏结束！")

# s6 = "hello"
# print(s6.capitalize())#Hello 转标题

# s7 = "hi"
# print(s7.ljust(20,"*"))
# print(s7.rjust(20,"*"))
# print(s7.center(35,"*"))

# 迭代  for
s8 = "a b c d e"
li = s8.split(" ")
print(li)
print(",".join(li))  # join拼接

# name = input("请输入用户名：")
# uname = input("请登录：")
# if uname.strip() == name.strip():
#     print("登录成功！")
# else:
#     print("登录失败！")


s = ['aaa', 'ddd', 'eee', 'bbb', ]
s1 = ['a', 'c', 'b']
new = sorted(s, key=lambda i: i[0])
print(new)
