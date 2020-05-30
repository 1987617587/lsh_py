"""
# author Liu shi hao
# date: 2019/11/25 9:48
# file_name: str_test

"""

#
# 常见操作 - 查找string.find(str, beg=0, end=len(string))检测str是否包含在string中，
# 如果beg和end指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回 - 1
from numpy.core.defchararray import expandtabs

str1 = "adgsdgSHAERHGDFASFAsdgsdf\nhtyj"
print(str1.find("dg"))
# string.rfind(str, beg=0, end=len(string))
# 类似于find()函数，不过是从右边开始查找.\
print(str1.rfind("d"))
# string.index(str, beg=0, end=len(string))类似于find()函数，但是找不到报异常.
# string.rindex(str, beg=0, end=len(string))类似于rfind()函数，但是找不到报异常.
#
# 常见操作 - 统计string.count(str, beg=0, end=len(string))
# 检测str是否包含在string中出现的次数，如果beg和end
# 指定范围，则检查是否包含在指定范围内
#
print(str1.count("d"))
# 常见操作 - 分割
# string.split(str="", num=string.count(str))
# 以str为分隔符切片string，如果num有指定值，则仅分隔num个子字符串
print(str1.split("d"))

# string.splitlines([keepends])
# 按照行('\r', '\r\n', \n')分隔，返回一个包含各行作为元素的列表，
# 如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
print(str1.splitlines(False))
print(str1.splitlines(True))
# string.partition(str)有点像find()和split()的结合体, 从str出现的第一个位置起, 把字符串string分成一个3元素
# 的元组(string_pre_str, str, string_post_str), 如果string中不包含str则string_pre_str == string.
print(str1.partition("d"))
# string.rpartition(str)类似于partition()函数, 不过是从右边开始.
#
print(str1.partition("A"))
print(str1.rpartition("A"))
# 常见操作 - 判断
# string.startswith(obj, beg=0, end=len(string))检查字符串是否是以obj开头，是则返回True，否则返回False。
print(str1.startswith("a"))
# 如果beg和end指定值，则在指定范围内检查.
# string.endswith(obj, beg=0, end=len(string))检查字符串是否是以obj结尾，是则返回True，否则返回False。
# 如果beg和end指定值，则在指定范围内检查.
print(str1.endswith("f"))
# string.isalnum()所有字符都是字母或数字则返回True, 否则返回False

str2 = "61613"
str3 = "asfa"
str4 = "asADfa"
print(str1.isalnum())
print(str2.isalnum())
print(str3.isalnum())
print(str4.isalnum())
# string.isalpha()所有字符都是字母（除数字和特殊字符）则返回True, 否则返回False
print(str3.isalpha())
# string.isdigit()所有字符都是数字则返回True, 否则返回False
print(str2.isdigit())
# string.isupper()所有字符都是大写则返回True, 否则返回False
print(str4.isupper())
# string.islower()所有字符都是小写则返回True, 否则返回False
print(str1.islower())
# string.isspace()只包含空格则返回True, 否则返回False
print(str1.isspace())
# 判断是否是标题（只有首字母大写）
print("Asdf".istitle())
#
# 常见操作 - 大小写string.capitalize()把字符串的第一个字符大写(转标题)
print(str.capitalize("asd"))
# string.upper()转换string中的小写字母为大写
print(str.upper("asd"))
# string.lower()转换string中的大写字母为小写
print(str.lower("ADd"))
#
# 常见操作 - 对齐string.ljust(width)
# 返回一个原字符串左对齐, 并使用空格填充至长度width的新字符串
print(str3.ljust(5))
# string.rjust(width)
# 返回一个原字符串右对齐, 并使用空格填充至长度width的新字符串
print(str3.rjust(5))
# string.center(width)
# 返回一个原字符串居中, 并使用空格填充至长度width的新字符串
print(str3.center(6))
#
# 常见操作 - 裁剪
# string.strip([obj])删除string字符串前后的的obj，如果不传参数，删除前后空格
import string

s = " asd gdf asd asda "
j = "asd gdf asd asda"
print(s.strip())
print(j.strip())

# string.lstrip([obj])删除string字符串左面的obj，如果不传参数，删除左面空格
print(j.lstrip("a"))
# string.rstrip([obj])删除string字符串右面的obj，如果不传参数，删除右面空格
print(j.rstrip("a"))
#
# 常见操作 - 合并
# string.join(seq)以string作为分隔符，将seq中所有的元素(的字符串表示)合并为一个新的字符串
#
print("|".join("asddf"))

s = "  a  b  c d"
li = s.split() # 删除空格
# li = s.lstrip() # 删除字符串左边空格
# li = s.rstrip() # 删除字符串末尾空格
print(",".join(li))  # 用符号","把字符隔开

print("137a9041".isdecimal())  # 检查字符串是否只包含十进制字符，如果是返回 true，否则返回 false。

# maketrans() 创建字符映射的转换表，对于接受两个参数的最简单的调用方式
# ，第一个参数是字符串，表示需要转换的字符，第二个参数也是字符串表示转换的目标。

# translate(table, deletechars="")
# 根据 str 给出的表(包含 256 个字符)转换 string 的字符, 要过滤掉的字符放到 deletechars 参数中
"""
maketrans()
字符串一种映射关系（对应关系、对照关系）
两个参数 第一个参数是字符串，是需要转换的字符串
第一个参数是字符串，是需要转换成为的字符串

两个字符串的长度必须相等

translate()
"""
src = "abcdefghijklmnopqrstuvwxyz0123456789"
tgt = "0123456789abcdefghijklmnopqrstuvwxyz"

#制作密码本
encrypt = str.maketrans(src,tgt)
print(encrypt)

name = input("请输入用户名：")
pwd = input("密码：")
pwd = pwd.translate(encrypt)
print("加密之后：",pwd)

































































































