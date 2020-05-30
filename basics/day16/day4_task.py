"""
# author Liu shi hao
# date: 2019/11/28 15:06
# file_name: day4_task

"""
import random


# 预留问题
def bubble_sort(arr: list):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def func():
    li = [55, "j", 457, "c", 435, "s", 234]
    for i in range(len(li)):
        if str(li[i]).isdigit():
            pass
        else:
            li[i] = ord(li[i])
    r_li = bubble_sort(li)

    li = [55, "j", 457, "c", 435, "s", 234]

    for j in range(len(r_li)):
        if chr(r_li[j]) in li:
            r_li[j] = chr(r_li[j])
    return r_li


print(func())


# 12.接收用户输入的字符串，将其中的字符进行排序（升序），并以逆序的顺序输出，“cabed”→"abcde"→“edcba”。

def func_12():
    r_arr = []
    r_str = ""
    str_12 = input("请输入;")

    for i in range(len(str_12)):
        r_arr.append(ord(str_12[i]))
    r_arr.sort()
    # print(r_arr)
    for j in range(len(str_12) - 1, -1, -1):
        r_str += chr(r_arr[j])
    return r_str


# print(func_12())


# 13.接收用户输入的一句英文，将其中的单词以反序输出，“hello c sharp”→“sharp c hello”。

def func_13(s: str):
    r_s = s.split(" ")
    r_s.reverse()
    print(r_s)
    # print(r_s[::-1])


func_13("hello c sharp")


# 14.从请求地址中提取出用户名和域名
# http://www.163.com?userName=admin&pwd=123456
def func_14(s: str):
    name = s[s.find("="):s.rfind("=")]
    domain_name = s[s.rfind("="):len(s)]
    print(f"用户名{name}域名{domain_name}")


# func_14("http://www.163.com?userName=admin&pwd=123456")


# 15.有个字符串数组，存储了10个书名，书名有长有短，现在将他们统一处理，
# 若书名长度大于10，则截取长度8的子串并且最后添加“...”，加一个竖线后输出作者的名字。
def func_15():
    s = ("asdhfjdhd", "wrtreeryhfrjtyrth", "afda")
    r_s = []
    for i in range(len(s)):
        if len(s[i]) > 10:
            r_s.append(s[i][0:8] + "..." + "|")
        else:
            r_s.append(s[i])
    return r_s


# print(func_15())

# 16.让用户输入一句话,找出所有"呵"的位置。
def func_16():
    msg = input("请输入：")
    s = msg.find("呵")
    while s != -1:
        print(s)
        s = msg.find("呵", s + 1)


# func_16()
# 17.让用户输入一句话,找出所有"呵呵"的位置。
def func_17():
    msg = input("请输入：")
    s = msg.find("呵呵")
    while s != -1:
        print(s)
        s = msg.find("呵呵", s + 1)


# func_17()
# 18.让用户输入一句话,判断这句话中有没有邪恶,如果有邪恶就替换成这种形式然后输出,
# 如:“老牛很邪恶”,输出后变成”老牛很**”;
def func_18():
    s = input("请输入：")
    if "邪恶" in s:
        return s.replace("邪恶", "**")


# print(func_18())


# 19.如何判断一个字符串是否为另一个字符串的子串
def func_19(s1: str, s2: str):
    if s1 in s2:
        return True
    return False


# print(func_19("s", "ads"))


# 20.如何验证一个字符串中的每一个字符均在另一个字符串中出现过
def func_20(s1: str, s2: str):
    j = 0
    for i in range(len(s1)):
        if s1[i] in s2:
            j += 1
    if j == len(s1):
        return True
    return False


# print(func_20("asd", "abcsd"))
# 21.如何随机生成无数字的全字母的字符串
def func_21(n: int):
    s = ""
    for i in range(n):
        if random.randint(0, 1) == 0:
            s += chr(random.randint(65, 90))
        else:
            s += chr(random.randint(97, 122))
    return s


# print(func_21(4))

# 22.如何随机生成带数字和字母的字符串
def func_22(n: int):
    s = ""
    for i in range(n):
        r = random.randint(0, 2)
        if r == 0:
            s += chr(random.randint(65, 90))
        elif r == 1:
            s += chr(random.randint(97, 122))
        else:
            s += chr(random.randint(48, 57))
    return s


print(func_22(4))


# 23.如何判定一个字符串中既有数字又有字母
def func_23(s: str):
    j = m = 0
    for i in range(len(s)):
        if s[i].isdigit():
            j = 1
        if s[i].islower() or s[i].isupper():
            m = 1
    if j == m == 1:
        return True
    return False


# print(func_23("asd123"))
# 24.字符串内的字符排序（只按字母序不论大小写）
#
# print(min("asdas"))
# print(min("Asdas"))

# 大写优先
def func_24():
    # max_arr = []
    # min_arr = []
    r_str = ""
    str_12 = list(input("请输入:"))

    for i in range(len(str_12)):
        r_str += min(str_12)
        str_12.remove(min(str_12))
    return r_str


print(func_24())


# 25.字符串的补位操作
# 1  =》001
# 2  =》002
# 10=》010

def func_25(s: str):
    # return s.rjust(3, "0")  # 或者
    return s.zfill(3)


print(func_25("1"))


# 1.两个列表进行合并操作  extend
def func_1(arr_1: list, arr_2: list):
    arr_1.extend(arr_2)
    return arr_1


# print(func_1([1, 2, 3], [4, 5, 6]))
# 2.使用列表判断一个列表是否在另外一个列表中
def func_2(arr_1: list, arr_2: list):
    if arr_1 in arr_2:
        return True
    return False


# print(func_2([1, 2, 3], [4, 5, 6]))
# 3.列表的反转
def func_3(arr: list):
    arr.reverse()
    return arr


# print(func_3([1, 2, 3]))
# 4.列表的排序
# 冒泡排序

# print(bubble_sort(arr1))
# 选择排序
def selection_sort(arr: list):
    for i in range(len(arr) - 1):
        min_num = i
        for j in range(i + 1, len(arr)):
            if arr[min_num] > arr[j]:
                min_num = j
        arr[min_num], arr[i] = arr[i], arr[min_num]
    return arr


# print(selection_sort([3, 2, 4, 1]))
# 二分法查找
def dichotomy(arr: list, num: int):
    start = 0
    end = len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] == num:
            return True
        if arr[mid] > num:
            end = mid
        else:
            start = mid + 1
    return False


# print(dichotomy([1, 2, 3, 4, 5], 0))

# 5.实现对列表的增删改查功能
arr_5 = [1, 2, 3, 4, 5]

# arr_5.insert(1, 34)  # 在所给索引值的前面增加新元素
# arr_5.append(9)  # 在末尾追加新元素
# arr_5.extend([3,4,6])  # 在末尾追加列表
# arr_5.remove(2)  # 按列表中的值删除
# arr_5.pop()  # 删除最后一个元素
# del(arr_5[1])  # 按列表中的索引删除对应元素
# arr_5[3] =30  # 改变指定索引位置的元素
# print(arr_5.index(3))  # 查找所给元素的索引位置

print(arr_5)


# 6.如何将0-10随机存入列表中,不重复
def func_6():
    arr = [i for i in range(11)]
    random.shuffle(arr)
    return arr


# print(func_6())
# 7.求出元组(90,34,-23,18,12)中的最大值和最小值
# t1 = (90,34,-23,18,12)
# print(max(t1))
# print(min(t1))
# 8.	针对列表[90,34,-23,18,12]从小到大进行排序，然后输出排序后结果
# arr_8 = [90,34,-23,18,12]
# arr_8.sort()
# print(arr_8)
# 9.	编程输出【所有】的三位水仙花数 水仙花数:各位数字的立方数相加等于该数本身
# 例如 153  1*1*1+5*5*5+3*3*3=153  153就是一个三位水仙花数
#
def int_3():
    while True:
        s = input("请输入：")
        if s.isdigit() and len(s) == 3:
            return s
        else:
            print("格式错误！")


def func_8():
    s = int_3()
    add_num = 0
    for i in range(len(s)):
        add_num += int(s[i]) ** len(s)
    if add_num == int(s):
        return True
    return False


# print(func_8())

#
# 9.1.根据班级名称 ，书写一个随机点名程序，可以多次点名。
#
def call(arr: list, n: int):
    for i in range(n):
        print(arr[random.randint(0, len(arr))])


# call(["李四","王五","张龙","赵虎"],3)
# 10.为哈希表追加不重复的10个值，且每个值都是1-10之间的随机数，问哪个数字重复的次数最多，重复了多少次？
#
def func_10():
    arr_10 = [None] * 10
    num = [0] * 10
    print(num)
    print(arr_10)
    for i in range(10):
        s = random.randint(1, 10)
        num[s - 1] += 1
        arr_10[i] = s
    print(arr_10)
    print(num)
    return f"{num.index(max(num)) + 1}数字重复的次数最多,重复的次数:{max(num)}"

# print(func_10())


# 11.假定书籍的种类有5种，设计何种的数据结构可以达到快速查询某类所有书籍的功能（提示：用Dictionary<K,V>）
# {"科幻":[{"书名":"三体"},{"书名":"未来是什么"}]}
#
#
# 思考题：
# 如何用队列实现约瑟夫环
# 约瑟夫环：假设有n个人坐成一圈，从某个人开始报数，数到m的人出圈，
# 接着从出圈的下一个人开始重新报数，数到m的人再次出圈，如此反复，直到所有人都出圈，请列出出圈顺序。
