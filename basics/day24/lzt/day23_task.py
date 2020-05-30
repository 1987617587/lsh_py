# author:lzt
# date: 2019/12/5 11:58
# file_name: day23_task
# 为集合追加不重复的100个值，且每个值都是1-100之间的随机数，问哪个数字重复的次数最多，重复了多少次？
import random

nums = set()

# 统计的列表
counts = [0] * 100

while len(nums) != 100:
    num = random.randint(1, 100)
    nums.add(num)
    counts[num - 1] += 1

# 求最大值和数字
# print(counts.index(max(counts)) + 1, max(counts))


# 假定书籍的种类有5种，设计何种的数据结构可以达到快速查询某类所有书籍的功能
books = {
    "计算机": ["计算机原理", "操作系统", "数据结构和算法", "离散数学"],
    "编程": {"C": [""], "c++": [""], "面向对象思想": [""], "Java从入门到放弃": [""], "Python的黑客之路": [""]},
    "美食": ["厨房宝典", "美食天下"]
}

query_book_type = input("请输入要查询的书目种类:")
query_books = books.get(query_book_type)

if query_books is not None:
    for i in query_books:
        print(i)
