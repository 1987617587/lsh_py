# 1、编写函数，传入一个列表，返回所有是7的倍数的数字的下标（友情提示：可使用列表返回）。(6分)
import datetime
import os
import random
import re
import time


def fun1(arr: list):
    r_arr = []
    if type(arr) == list:
        for i in range(len(arr)):
            if arr[i] % 7 == 0:
                r_arr.append(i)
        return r_arr
    return "格式错误！"


# print(fun1([1, 2, 7, 3, 14, 21]))


# print(fun1("12"))

#
# 2、编写函数求区间[n,m]内个位数字不是1,4,5，并且可以被3整除的所有数,并将所有数字放入合适的容器中返回。(6分)
#
def fun2(n: int, m: int):
    if type(n) == int and type(m) == int and m > n:
        return [i for i in range(n, m + 1) if i % 3 == 0 and str(i)[-1] not in ["1", "4", "5"]]
    return "格式错误！"


# print(fun2(1, 100))

# 3、编写函数，传入一个用户输入的行数，函数内打印如下图形:
#     ****
#    ***
#   **
#  *
# (6分)
#

def func3():
    n = input("请输入行数：")
    if n.isdigit():
        for i in range(int(n), -1, -1):
            print(i * " " + i * "*")


# func3()

# 4、编写函数，传入用户输入的字符串,函数内使用正则分离出数字和非数字，将所有数字和非数字各自连接成一个字符串并返回打印。(6分)
#
def func4():
    msg = input("请输入：")
    s1 = "".join(re.findall("\d+", msg))
    s2 = "".join(re.findall("\D+", msg))
    return s1, s2


# print(func4())

# 5、编写函数，传入用户需要的个数n和每个名字的长度name_len，在函数内产生n个由字母随机组成的名字，这些名字不能同名，
# 名字长度为name_len，请用合适的容器返回这些名字。(6分)
#
def func5(n: int, name_len: int):
    arr = []
    if type(n) == int and type(name_len) == int:
        while 1:
            name = "".join([chr(random.randint(97, 122)) for i in range(int(name_len))])
            arr.append(name)
            if len(set(arr)) == int(n):
                return arr


# print(func5(4, 3))

# 6、编写函数，传入字符串列表，该函数将每个字符串的小写字母变大写，将大写字母变小写并返回,比如[‘acB’,’Bca’,’cAb’]=》[‘ACb’,’bCA’,’CaB’]。(6分)
#

def func6(arr: list):
    if type(arr) == list:
        for i in range(len(arr)):
            s = ""
            for j in arr[i]:
                if j.isupper():
                    s += str.lower(j)
                if j.islower():
                    s += str.upper(j)
            arr[i] = s
    return arr


# print(func6(['acB', 'Bca', 'cAb']))

# 7、编写函数，传入列表生成式生成的10000个可重复数字的列表（提示:[i+随机数 …]），该函数统计每个数字的频次(出现的次数),并将(数字,频次)放入字典并返回。(6分)
#
def func7():
    arr1 = [random.randint(1, 1000) for i in range(10000)]
    return {i: arr1.count(i) for i in arr1}


# print(func7())


# 8、编写函数，传入一个文件的路径字符串，请将文件根目录、文件所在目录、文件后缀名返回。(6分)
# 例：
# 传入:”C:\a\b\c\d\9.rmvb”
# 返回:”C:\”  “d\”  “.rmvb”
#

def func8(s: str):
    try:
        split_text = os.path.splitext(s)
        s2 = os.path.split(split_text[0])[0]

        return s[:3], str(os.path.split(s2)[1]) + '\\', split_text[1]
    except:
        print("格式有误！")


# print(func8(r"C:\a\b\c\d\9.rmvb"))

# 9、编写函数，传入一个文件目录和数字n,函数内删除该文件目录中n天前不包括正好n天前创建的所有文件。(6分)
#
def func9(dir: str, n: int):
    for root, subs, files in os.walk(dir, False):
        for file in files:
            file_time = datetime.datetime.fromtimestamp(os.path.getctime(os.path.join(root, file)))
            if (datetime.datetime.now() - file_time).days < int(n):
                os.remove("/".join([root, file]))


# func9(r"e:\a\b\c\d", 4)


# 10、编写函数，传入一个多位数字的列表，使用sorted函数为其排序，排序依据为数字的各位之和。(6分)
# 例：
# 传入的列表：[119,121,234,511,521]
# 排序依据:
# 119=>1+1+9=11
# 121=>1+2+1=4
# ….
# 排序结果:[121,511,521,234,119]


def func10(arr: list):
    if type(arr) == list:
        return sorted(arr,
                      key=lambda i: [sum([int(i) for i in re.findall(".", str(arr[j]))]) for j in range(len(arr))])


print(func10([121, 511, 521, 234, 119]))
