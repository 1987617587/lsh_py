# author:lzt
# date: 2019/12/13 15:35
# file_name: regular_test
# 正则的单字匹配
import re

# 匹配任意字符：.:在模式中
print(re.findall(".", "q21223asdasd"))

# 匹配可选的字符:[abcd....]:a|b|c|d|e|....
print(re.findall("[0123][bc]", "1230b 1c 2b"))
# 0b 0c 1b 1c 2b 2c 3b 3c

# 请找出字符串中所有的数字
print(re.findall("\d", "asdhajsgh78612asidgg8712tasgd87t"))

# 找出所有的非数字字符
print(re.findall("\D", "asdhajsgh78612asidgg8712tasgd87t"))

# 找出所有以空白开始的字符串
print(re.findall("\sabc", "abc abc1"))

# 找出所有非空白开始的字符串
print(re.findall("\Sabc", "abc abcabc abc"))

# 找出所有的单词字符
print(re.findall("\w", "123,asas*Zas dsa士大夫"))

# 找出所有的非单词字符
print(re.findall("\W", "123,asas*Zas dsa士大夫"))

# 数量级匹配
# *:0-n次
# print(re.findall("11*","1112112221111"))

# +:1-n
print(re.findall("12+", "11121111122"))

# ?:0-1
print(re.findall("ab?", "asdasabcabb"))

# {m}:必须重复m次 {m,}至少出现m次 {m,n}:出现m到n次
print(re.findall("1{5}", "111 11111 111111"))
print(re.findall("1{5,}", "111 11111 111111111"))
print(re.findall("1{1,5}", "111 11111 111111111"))

# 正则有两种搜索模式:贪婪模式：尽量多匹配 非贪婪模式：尽量少的匹配
# 默认贪婪模式
# print(re.findall("1{1,5}?", "111 11111 111111111"))
# 贪婪模式匹配he*:h/he/heeee...
print(re.findall("he*", "hee heeee heeeeee"))
print(re.findall("he*?", "hee heeee heeeeee"))
print(re.findall("he+", "hee heeee heeeeee"))
print(re.findall("he+?", "hee heeee heeeeee"))

# 注意事项:若贪婪或者非贪婪的模式后跟的有其他的模式 必须按整体的匹配度来匹配！！！
# print(re.findall("he*?a", "hea heea heeea"))


# 边界匹配
# ^:从字符串首位置开始匹配
print(re.findall("^123","abc 123 123 123"))
print(re.findall("^123","123abc 123 123 123"))
# $:一直匹配到末尾
print(re.findall("\w+\.txt$","asd 1111.txt\nasdasd 222.txt\nasdasd 333.txt",flags=re.M))


# 原始字符串:r
# 网页上有人询问如何换行
print(r"\n")

# \b
print(re.findall(r"\b123\b","123 a123a 123"))
# \B
print(re.findall(r"\B123\B","123 a123a 123"))

# 匹配上的任意的单词的项
# [abcd]:a/b/c/d
# abc|abd:abc/abd
print(re.findall(r"\bhello\b|\babc\b|\b123\b","hello1 abc1 1234"))

# 拆分邮件字符串
emails = re.match(".*?@.*?.com","lzt1234@163.com")
print(emails.group())
# 添加()
emails_group = re.match("(.*?)@(.*?.com)","lzt1234@163.com")
print(emails_group.group(1))
print(emails_group.group(2))
# print(emails_group.group(3))

# 数字(123)...字符(abc)...字符(abc)..数字(123)
# \d+\w+\w+\d+
# 123abcghj890
# (\d+)(\w+)\2\1
#   1    2
# abba
# abab
print(re.match(r"(\d+)(\w+)\2\1","1234abcdabcd1234").group(2))


# 按命名的方式为分组起名
# abccba
# a:序列111
# b:序列aaa
# c:序列222
ret = re.match(r"(?P<num1>\d+)(?P<chars1>\w+)(?P<num2>\d+)(?P=num2)(?P=chars1)(?P=num1)","111aaa222222aaa111")
print(ret)
print(ret.group("chars1"))
print(ret.group("num2"))













