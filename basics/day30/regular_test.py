"""
# author Liu shi hao
# date: 2019/12/13 15:37
# file_name: regular_test

"""
import re

# 匹配单字符的相关格式
# 匹配任意字符：. :在模式中
# print(re.findall(".", "q123werqasd"))
#
# # 匹配可选的字符：【abcd..】:a|b|c|d|e|...
# print(re.findall("[0123][bc]", "123ob 1c 2b"))
#
# # 找出字符串所有数字
print(re.findall(r"\d", "afsafgs2356758d/'.ghedf"))
print(re.findall(r"\D", "afsafgs2356758dghe'.】df"))
#
# # 找出所有以空白开始的字符串（空白即空格）
# print(re.findall(r"\sabc", "abc bc1 abc"))
# # 找出所有以非空白开始的字符串
# print(re.findall(r"\Sabc", "1abc bc1 abc"))
#
# # 找出所有单词字符（非标点符号W）
# print(re.findall(r"\w", "123,./*+-'][;koiajdf分段收费"))
# # 找出所有非单词字符（只含标点符号）
# print(re.findall(r" \W ", "123,./*+-'][;koiajdf分段收费"))

# 匹配多个字符的相关格式r
# 数量级匹配(之和前面一位的字符关联)
# *：0-n次
# result = re.findall("i*", "hi china hello china")
# print(result)
result = re.findall("hi*", "hi china hello china")
print(result)
# +：1-n次
result = re.findall("hi+", "hi china hello chiina")
print(result)
# ?：0-1次
result = re.findall("hi?", "hi china hello chiina")
print(result)
# {m}:必须重复m次
result = re.findall("11{2}", "111 c11a h1lo 111")
print(result)
# {m,}:至少出现m次
result = re.findall("hi{2,}", "hi china hello chiina")
print(result)
# {m,n}:出现m到n次
result = re.findall("hi{1,2}", "hi china hello chiiina")
print(result)

# 特殊贪婪字符 ？
# 正则匹配默认贪婪模式即匹配尽可能多个字符
result = re.findall("he*", "hee heeeee zzheee0 e ee")
print(result)
# 结果为 ['hee', 'heeeee', 'heee']
# 当?出现在+、*、{m}之后开启非贪婪模式
result = re.findall("he*?", "hee heeeee zzheee0 e ee")
print(result)
# 结果为 ['h', 'h', 'h']
result = re.findall("he+?", "hee heeeee zzheee0 e ee")
print(result)
# 结果为 ['he', 'he', 'he']
result = re.findall("he{2,}?", "hee heeeee zzheee0 e ee")
print(result)
# 结果为 ['hee', 'hee', 'hee']

# 注意事项：若贪婪或者非贪婪的模式后跟的有其他的模式 必须按整体的匹配度来匹配！！！
print(re.findall("he*?a", "ha,hea,heea,heeeea"))

print("*" * 30)
# 边界匹配
# ^: 从字符串首位开始匹配
print(re.findall("^123", "abc 123n 123 123"))
print(re.findall("^123", "123a 123n 123 123"))
# $: 从字符串末尾结束匹配
print(re.findall(r"\w+\.txt$", "abc.123.txt\n.123s.txt\n1234.txt", flags=re.M))
# \w+ 字符一个到多个 \.字符后面紧跟着一个点. 紧跟着txt 得到txt文件格式

# 原始字符串：r
print('\n')
print(r'\n')
# 边界匹配
# \b
print(re.findall(r"\babc\b", "123 abc 1abc abc"))  # abc两旁没字符可以匹配成功
print(re.findall(r"\Babc\b", "123 abc 1abc abc"))  # abc左边有字符右边没字符可以匹配成功
print(re.findall(r"\Babc\B", "123 abc 1abc1 abc"))  # abc两旁都字符可以匹配成功

# 匹配上的任意的单词的项
print(re.findall(r"\bhello\b|\babc\b|\b123\b", "hello abc 123"))
print(re.findall(r"\bhello\b|\babc\b|\b123\b", "hello 1abc 123"))

# 拆分邮件字符串
emails = re.match(".*?@.*?.com", "lzt1234@163.com")
print(emails.group())
emails = re.match("(.*?)@(.*?.com)", "lzt1234@163.com")
# 加括号实现分组，上述按@分为两组
print(emails.group(1))
print(emails.group(2))

# 数字（123）字符（abc）字符（abc）数字（123）
# \d+\w+\w+\d+
# 1=(\d+) 2 =(\w+) 引用分组匹配到的字符串
print(re.match(r"(\d+)(\w+)\2\1", "123abcabc123").group())
print(re.match(r"(\d+)(\w+)\1\2", "123abc123abc").group())

# 按命名的方式为分组起名
# abba格式
ret = re.match(r"(?P<num1>\d+)(?P<chars1>\w+)(?P=chars1)(?P=num1)", "123abcabc123")
print(ret)
print(ret.group("chars1"))
# abccba格式
ret = re.match(r"(?P<num1>\d+)(?P<chars1>\w+)(?P<num2>\d+)(?P=num2)(?P=chars1)(?P=num1)", "123abc321321abc123")
print(ret)
print(ret.group("num2"))
