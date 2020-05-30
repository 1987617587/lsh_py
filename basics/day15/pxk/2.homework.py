# 1.去掉字符串中的所有空格
# s = "s f f f f"
# s = s.replace(" ","")
# print(s)
# s="a s d f g h"
# list1=s.replace(" ","")
# print(list1)


# print("".join(s.split(" ")))
# s="a s d f gg h"
# a=s.split(" ")
# a_list="".join(a)
# print(a_list)
# 2.根据完整的路径从路径中分离文件路径、文件名及扩展名
path = r"D:\pyteach\py1911\day04\2.homework.py"
d=path.rpartition("\\")
print(d[2])
c=d[2].rpartition(".")
print(c[2])
# temp = path.rpartition("\\")
# print(temp)
# print("文件路径：",temp[0])
# print("文件名：",temp[2].split(".")[0]+"."+temp[2].split(".")[1])
# print("扩展名：",temp[2].split(".")[2])
# 3.获取字符串中汉字的个数
# import re
# #正则表达式
# s = "hello你好"
# l = re.findall("[\u4e00-\u9fa5]",s)
# print(l,len(l))
# 4.对字符串进行加密与解密
#maketrans  translate
# 5.将字母全部转换为大写或小写
# 6.根据标点符号对字符串进行分行
# s = "s,s,ss,s"
# # # temp = s.split(",")
# # # print(temp)
# # # for i in temp:
# # #     print(i)
# # print(s.replace(",", "\n"))
# s = "sds\ndsds\ndsd\ndsd\n"
# s2 = "bmsdnmsbsm"
# print(s)
# print(s.splitlines(False))

# 7.去掉字符串数组中每个字符串的空格 #array  list列表
# 8.随意输入你心中想到的一个书名，然后输出它的字符串长度。
# （len()属性:可以得字符串的长度）
# 9.两个学员输入各自最喜欢的游戏名称，判断是否一致,如果相等,
# 则输出你们俩喜欢相同的游戏；如果不相同,则输出你们俩喜欢不相同的游戏。
# name = input("请输入")
# name2 = input("请输入：")
# if name == name2:
#     print(name)
# else:
#     print(name,name2)
# 10.上题中两位同学输入 lol和 LOL代表同一游戏，怎么办?
# 11.让用户输入一个日期格式如“2008/08/08”，将 输入的日期格式转换
# 为“2008年-8月-8日”。
# s = "2008/08/08"
# temp = s.split("/")
# print(temp)
# print("转化后的格式为：{}年-{}月-{}日".format(temp[0],int(temp[1]),int(temp[2])))
#


