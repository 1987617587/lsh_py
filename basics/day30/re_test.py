"""
# author Liu shi hao
# date: 2019/12/13 14:17
# file_name: re_test

"""
import re

# split 拆出算式中的运算符(返回分割列表)
print(re.split("\d+", "123+4-5*9/5")[1:-1])
# 拆出算式中的数字
print(re.split("[\+\-\*/]", "123+4-5*9/5"))

# print(re.match("^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$",input("请输入邮箱："))is not None)


# 匹配match
ret = re.match("123", "122324")  # 匹配后面的字符串是否已前面的字符串开头
print(ret)
if ret is not None:
    print(ret.group())  # 能匹配就返回匹配对象“123”

# 搜索字符串中第一个匹配的项(返回一个对应的match对象。如果没有匹配返回None.)
print(re.search("abc", "asabcabcacb"), re.search("abc", "asabcabcacb").span(), re.search("abc", "asabcabcacb").group())

# 完全匹配（完美匹配）fullmatch(返回一个对应的match对象。如果没有匹配返回None.)
print(re.fullmatch("abc,.", "abc,."))

# 找到所有的匹配项(返回列表)
print(re.findall("12", "ewe12c2e12fd12hby12"))

# split 剪切（一刀两段）maxsplit(切几刀)
print(re.split("he", "hello this is hello", maxsplit=2))

# re.sub（按模式替换） 使用repl替换pattern匹配到的内容，最多匹配count次
# sub(pattern, repl, string, count=0, flags=0)
result = re.sub("hello", "hi", "zzy hello china hello world hello zhengzhou", 2)
print(result, type(result))

# re.iterator  返回迭代器
# finditer(pattern, string, flags=0)
result = re.finditer("hello", "hello world hello china")
print(result)  # 可迭代，可直接next的迭代器
for i in result:
    print(i.group())
# print(next(result).group())
# print(next(result).group())


# re.compile  编译得到匹配模型(为了模式的复用，提高效率)
# compile(pattern, flags=0)
pat = re.compile("hello")
print(pat, type(pat))
result = pat.search("helloworld")
print(result, type(result))

# rex1 = re.compile("^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$")  # 预编译
# email1 = input("邮箱：")
# print(re.match(rex1, email1) is not None)
#
# email1 = input("邮箱：")
# print(re.match(rex1, email1) is not None)


# flags
# re.I 无视大小写
print(re.sub("s", "qiku", "SAsa", flags=re.I))

# 找到所有以abc开始的元素
# 默认的行模式：单行模式：将字符串看成一行 无视\n
print(re.findall("^abc", "asasda\nabcfeer\nefgh"))
print(re.findall("^abc", "asasda\nabcfeer\nefgh", flags=re.M))  # 多行

# 找到所有的单个字符
# .:任意字符
# 显示写出为单行模式 才能匹配\n
print(re.findall(".", "asd./,s\nda", flags=re.S))  # 把\n当作字符
print(re.findall(".", "asd./,s\nda", flags=re.M))  # 把\n当作换行符（不输出）
