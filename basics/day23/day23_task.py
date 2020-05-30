"""
# author Liu shi hao
# date: 2019/12/4 15:21
# file_name: day23_task

"""

# 1. 两个列表进行合并操作
# arr1 = [1, 2, 3]
# arr2 = [1, 2, 3]
# print(arr1 + arr2)
# arr1.extend(arr2)
# print(arr1)
# 2. 使用列表判断一个列表是否在另外一个列表中
import random


def func2(arr1: list, arr: list):
    j = 0
    for i in range(len(arr1)):
        if arr1[i] in arr:
            j += 1
    if j == len(arr1):
        return True
    return False


# print(func2([1], [1, 2, 3]))

# 3. 列表的反转
# arr3 = [1, 2, 3]
# arr3.reverse()
# print(arr3)
# 4. 列表的排序
# arr4 = [2, 3, 2, 5, 1]
# arr4.sort()
# print(arr4)
# 5. 实现对列表的增删改查功能
arr5 = [1, 2, 3, 4]
arr5.append(6)
arr5.extend([7])
arr5.remove(7)
arr5.pop()
del arr5[0]
arr5.index(2)
arr5[0] = 7

# 6. 如何将0-10 随机存入列表中
# arr6 = [i for i in range(1, 11)]
# random.shuffle(arr6)
# print(arr6)

# 7. 求出元组(90,34,-23,18,12) 中的最大值和最小值
print(max(90, 34, -23, 18, 12))
print(min(90, 34, -23, 18, 12))

# 8.如何用队列实现约瑟夫环
# 约瑟夫环：假设有n个人坐成一圈，从某个人开始报数，数到m的人出圈，接着从出圈的下一个人开始重新报数，数到m的人再次出圈，如此反复，直到所有人都出圈，请列出出圈顺序。
# def func8(n, m):
#     for i in range(1, n + 1):
#         qu.put(f"第{i}个人")
#
#     count = 0
#     while qu.qsize() != 0:
#         date = qu.get()
#         count += 1
#         if count % m == 0:
#             print(f"{date}out")
#         else:
#             qu.put(date)
#
#
# func8(5, 3)

# 9.用栈实现加法式子的运算
# 1+2+3+4
from queue import LifoQueue


def func9(msg: str):
    num = LifoQueue()
    add = LifoQueue()
    li = msg.split("+")
    print(li, len(li))
    for i in li:
        num.put(i)
    for j in range(len(li) - 1):
        add.put("+")
    while 1:
        add.get()
        num.put(int(num.get()) + int(num.get()))
        if add.empty() and num.qsize() == 1:
            break
    print(num.get())


# func9("1+2+3+4")

msg = input("请输入式子：")
print(eval(msg))  # 字符串直接转运算

# 10.为集合追加不重复的100个值，且每个值都是1-100之间的随机数，问哪个数字重复的次数最多，重复了多少次？


def func10():
    set1 = [int(random.randint(1, 100) * i / i) for i in range(1, 101)]
    num_dict = {i: set1.count(i) for i in set1}
    print(num_dict)
    for k, v in num_dict.items():
        if v == max(num_dict.values()):
            print(f"数字{k}重复的次数最多，重复了{v}次")


func10()

# 11.假定书籍的种类有5种，设计何种的数据结构可以达到快速查询某类所有书籍的功能
dic = {"科幻": [{"书名": "三体"}, {"书名": "未来是什么"}], "文学": [{"书名": "西游记"}, {"书名": "红楼梦"}],
       "医学": [{"书名": "针灸大法"}, {"书名": "起死回生"}],
       "地理学": [{"书名": "敦煌游记"}, {"书名": "地质地理"}], "历史学": [{"书名": "唐朝那些事"}, {"书名": "隋唐秘史"}]}


# print(dic["科幻"])


class Book:

    def __init__(self, name, book_type) -> None:
        super().__init__()
        self.name = name
        self.book_type = book_type

    def __eq__(self, o) -> bool:
        return self.name == o.name

    def __hash__(self) -> int:
        return self.name.__hash__()

    def __str__(self) -> str:
        return f"书名{self.name}，种类{self.book_type}"


books = [
    Book("三体", "科幻"),
    Book("未来是什么", "科幻"),
    Book("针灸大法", "医学"),
    Book("隋唐秘史", "历史学"),
    Book("敦煌游记", "地理学"),
    Book("西游记", "文学")
]

book_idct = {i.name: i.book_type for i in books}
# print(book_idct)
books_type_idct = {v: [i for i in book_idct.keys() if book_idct.get(i) == v] for k, v in book_idct.items()}
print(books_type_idct)
print(books_type_idct.get("科幻"))


# 12.判断一篇英文文章出现了哪些字母，以及每个字母出现的个数
def func12(art: str):
    msg = []
    for j in art:
        if "a" <= j <= "z" or "A" <= j <= "Z":
            msg.append(j)

    dict12 = dict.fromkeys([chr(i + 64) for i in range(1, 27)] + [chr(i + 96) for i in range(1, 27)], 0)
    for i in msg:
        dict12[i] = dict12[i] + 1
    print(dict12)
    for k, v in dict12.items():
        if v > 0:
            print(f"出现字母{k}，{v}次")


# func12("afweRTGEGH wewe rSGFREGwtw t")

# 方法二去除花里胡哨一步到位
def func12_2(msg: str):
    return {i: msg.count(i) for i in msg}


print(func12_2("afweRTGEGH wewe rSGFREGwtw t"))
#
# 选作：
# 1.如何实现一个单向链表
# 列表方法使得列表可以很方便的作为一个堆栈来使用，堆栈作为特定的数据结构，最先进入的元素最后一个被释放（后进先出）
# 。用 append() 方法可以把一个元素添加到堆栈顶。用不指定索引的 pop() 方法可以把一个元素从堆栈顶释放出来。
# 例如：
# arr_1 = [2, 3, 4, 5]
# # 进栈
# arr_1.append(6)
# # 出栈
# arr_1.pop()
# arr_1.pop()
# arr_1.pop()
# print(arr_1)

# 2.解析用户输入的一个算数表达式 算出其结果(选作)
# 2-1.没有括号和负号（中等难度）
# 2-2.带括号和负号（高难度）
