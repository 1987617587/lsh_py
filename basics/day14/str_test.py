"""
# author Liu shi hao
# date: 2019/11/22 15:16
# file_name: str_test

"""
print([chr(i) for i in range(256)])
print(ord("中"))
print("\u4e00")
print("\u9fa5")
print(ord("국"))
print("你好，python世界".encode(encoding='UTF-8', errors='strict'))
print("你好，python世界".encode(encoding='gb2312'))
msg = "你好，python世界"
send_msg = msg.encode(encoding='UTF-8')  # 按照UTF-8的编码格式获取
print(send_msg.decode(encoding='UTF-8'))  # 按照UTF-8的编码格式解码
# 字节序列.decode(encoding='UTF-8', errors='strict')
# 如果设置为strict，代表遇到非法字符时抛出异常；
print(send_msg.decode(encoding='gb2312', errors='ignore'))
# 如果设置为ignore，则会忽略非法字符；
# 如果设置为replace，则会用?取代非法字符；
# 如果设置为xmlcharrefreplace，则使用XML的字符引用

file_path = "E模块"
print(file_path)
msg = '某人说:\'你好\''
print(msg)

msg = "asdghaAadddsasdasadsadfdEeas"

# print(msg.find("d"))
# print(msg.find("d",3,len(msg)))
# print(msg.find("d",9,len(msg)))
# print(msg.find("d",13,len(msg)))
# print(msg.find("d",17,len(msg)))
# print(msg.find("d",20,len(msg)))
# print(msg.find("d",22,len(msg)))

s = msg.find("d")
while s != -1:
    print(s)
    s = msg.find("d", s + 1)

r = msg.rfind("b")
while r != -1:
    print(r)
    if r == 0:
        break
    r = msg.rfind("b", 0, r)

print(msg.rfind("b", 0, -1))
# 常见操作 - 查找
# string.find(str, beg=0, end=len(string))
# 检测
# str
# 是否包含在
# string
# 中，如果
# beg
# 和
# end
# 指定范围，则检查是否包含在指定范围内，如果是返回开始的索引值，否则返回 - 1
# string.rfind(str, beg=0, end=len(string))
# 类似于
# find()
# 函数，不过是从右边开始查找.
# string.index(str, beg=0, end=len(string))
# 类似于
# find()
# 函数，但是找不到报异常.
# string.rindex(str, beg=0, end=len(string))
# 类似于
# rfind()
# 函数，但是找不到报异常.
#
# 常见操作 - 统计
# string.count(str, beg=0, end=len(string))
# 检测
# str
# 是否包含在
# string
# 中出现的次数，如果
# beg
# 和
# end
# 指定范围，则检查是否包含在指定范围内
#
# 常见操作 - 分割
# string.split(str="", num=string.count(str))
# 以
# str
# 为分隔符切片
# string，如果
# num有指定值，则仅分隔
# num
# 个子字符串
# string.splitlines([keepends])
# 按照行('\r', '\r\n', \n
# ')分隔，返回一个包含各行作为元素的列表，如果参数 keepends 为 False，不包含换行符，如果为 True，则保留换行符。
# string.partition(str)
# 有点像
# find()
# 和
# split()
# 的结合体, 从
# str
# 出现的第一个位置起, 把
# 字
# 符
# 串
# string
# 分
# 成
# 一
# 个
# 3
# 元
# 素
# 的
# 元
# 组(string_pre_str, str, string_post_str), 如果
# string
# 中不包含str
# 则
# string_pre_str == string.
#     string.rpartition(str)
# 类似于
# partition()
# 函数, 不过是从右边开始.
#
#     常见操作 - 判断
# string.startswith(obj, beg=0, end=len(string))
# 检查字符串是否是以
# obj
# 开头，是则返回
# True，否则返回
# False。如果beg
# 和
# end
# 指定值，则在指定范围内检查.
#     string.endswith(obj, beg=0, end=len(string))
# 检查字符串是否是以
# obj
# 结尾，是则返回
# True，否则返回
# False。如果beg
# 和
# end
# 指定值，则在指定范围内检查.
#     string.isalnum()
# 所有字符都是字母或数字则返回
# True, 否则返回
# False
# string.isalpha()
# 所有字符都是字母则返回
# True, 否则返回
# False
# string.isdigit()
# 所有字符都是数字则返回
# True, 否则返回
# False
# string.isupper()
# 所有字符都是大写则返回
# True, 否则返回
# False
# string.islower()
# 所有字符都是小写则返回
# True, 否则返回
# False
# string.isspace()
# 只包含空格则返回
# True, 否则返回
# False
#
# 常见操作 - 大小写
# string.capitalize()
# 把字符串的第一个字符大写
# string.upper()
# 转换
# string
# 中的小写字母为大写
# string.lower()
# 转换
# string
# 中的大写字母为小写
#
# 常见操作 - 对齐
# string.ljust(width)
# 返回一个原字符串左对齐, 并使用空格填充至长度
# width
# 的新字符串
# string.rjust(width)
# 返回一个原字符串右对齐, 并使用空格填充至长度
# width
# 的新字符串
# string.center(width)
# 返回一个原字符串居中, 并使用空格填充至长度
# width
# 的新字符串
#
# 常见操作 - 裁剪
# string.strip([obj])
# 删除
# string
# 字符串前后的的obj，如果不传参数，删除前后空格
# string.lstrip([obj])
# 删除
# string
# 字符串左面的obj，如果不传参数，删除左面空格
# string.rstrip([obj])
# 删除
# string
# 字符串右面的obj，如果不传参数，删除右面空格
#
# 常见操作 - 合并
# string.join(seq)以string作为分隔符，将seq中所有的元素(的字符串表示)合并为一个新的字符串
str1 = "asd/0sd/0d"
# print("-".join(str1))
# print(str1.)
# str1.split(str="/0",num = 3)