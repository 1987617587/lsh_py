# author:lzt
# date: 2019/12/13 14:15
# file_name: re_test

import re

# # 正则的引子
# # 123+456+7890*3/2-1000
# # 拆出所有的符号
# ops = re.split("\d+", "123+456+7890*3/2-1000")
# # print(ops[1:len(ops)-1])
# # 获取所有的数据
# print(re.split("[\+\-\*/]", "123+456+7890*3/2-1000"))
#
# # 请用户输入邮箱地址
# # 验证用户的输入是否正常！！！
# # 111@qq.com
# print(re.match("^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$",input("请输入邮箱：")) is not None)


# re模块中的常用方法
# match:匹配
# ret = re.match("1234","123456546456adasd")
# print(ret)
# # 打印匹配的结果
# print(ret.group())

# search:搜索字符串第一个匹配的项
print(re.search("abc", "123abc1abc1abc").group())

# fullmatch:完全匹配 完美匹配
print(re.fullmatch("abcde", "abcde").span()[0])

# findall:找到所有的匹配项
print(re.findall("123", "123 123 4123 a123 b123"))

# split:按模式分割
print(re.split("he", "hello this is hello", maxsplit=3))

# sub:按模式替换
print(re.sub("123", "abc", "123 123 123 123 123", count=2))

# iterator
it = re.finditer("123", "123 123 123 123 123 123 123 123 123")
# print(it)
# print(next(it).group())
# print(next(it).span()[0])
for i in it:
    print(i.group())

# 为了模式的复用 请预编译 也可以提高匹配效率
# 匹配邮件的模式
rex1 = re.compile("^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$")

# email1 = input("邮箱：")
# print(re.match(rex1, email1) is not None)
#
# email1 = input("邮箱：")
# print(re.match(rex1, email1) is not None)
#
# email1 = input("邮箱：")
# print(re.match(rex1, email1) is not None)

# re.I:无视大小写
print(re.sub("s", "qiku", "SADasdaJGJGjas", flags=re.I))

# 找到所有以abc开始元素
# 模式的行模式:单行模式(re.S)：将字符串看成一行的数据 无视\n
print(re.findall("^abc", "asa123\nabc123\n09asd"))
print(re.findall("^abc", "asa123\nabc123\n09asd", flags=re.M))

# 找到所有的单个字符:
# .：任意字符
# 显式写出为单行模式 才能匹配\n
print(re.findall(".", "hello,.\nasd", flags=re.S))
print(re.findall(".", "hello,.\nasd", flags=re.M))
