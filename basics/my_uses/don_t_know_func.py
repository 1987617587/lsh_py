"""
# author Liu shi hao
# date: 2019/11/13 20:23
# file_name: don_t_know_func
# 本模块放置本人不熟练的内置函数，多用多练多记
"""
# 插入元素到指定位置，位置可以为负：
# nums =[1,2,3,4,5]
# nums.insert(1, 9)
# print(nums)
# 插入元素到指定位置，位置可以为负：
# nums.insert(1, 9)
#
# 追加列表：
# nums.extend([8, 9, 10, 11])
#
# 删除：
# 删除位置上的数据：del nums[2]
# 删除某个数据(只删除找到的第一个)：nums.remove(7)
#
# 修改:
# nums[0] = 0
#
# 查询:找不到会报错
# 会找到第一个6的索引
# index = nums.index(6)
#
# 反序
# nums.reverse()
# [7, 6, 5, 4, 3, 2, 1]
# 追加列表：
# nums.extend([8, 9, 10, 11])
#
# 删除：
# 删除位置上的数据：del nums[2]
# 删除某个数据(只删除找到的第一个)：nums.remove(7)
#
# 修改:
# nums[0] = 0
#
# 查询:找不到会报错
# 会找到第一个6的索引
# index = nums.index(6)
#
# 反序
# nums.reverse()
# [7, 6, 5, 4, 3, 2, 1]

# 冲突场景
# 1.函数内修改全局变量
# 会被解释器认为新声明了一个局部变量
#
# 例：
# num = 10
#
#
# def set_num(in_num):
#     num = in_num
#     pass
#
#
# set_num(111)
# print(num)
# 结果:10

# 解决办法：global关键字
# num = 10
#
#
# def set_num(in_num):
#     global num
#     num = in_num
#     pass
#
#
# set_num(111)
# print(num)
# # 结果:111
#
#
# # 2.在函数内新声明的局部变量和全局变量同名，但是又想使用全局变量
# discount = 0.9  # 全场9折
#
#
# def pay(money):
#     discount = 0.8  # 折上折
#     print("请pay:", money * discount * discount)
#     pass
#
#
# pay(10000)
# 结果：请pay: 6400.0


# 解决办法：globals()函数
# discount = 0.9  # 全场9折
#
#
# def pay(money):
#     discount = 0.8  # 折上折
#     print("请pay:", money * globals()["discount"] * discount)
#     pass
#
#
# pay(10000)
# 结果：请pay: 7200.0

# 切片
mystr = 'helloworld'
mystr = mystr[1:5]  # 截取字符串索引【1-5】直接的字符串
# print(mystr)

# format
mystr2 = 'welcome, dear {name}'
mystr2 = mystr2.format(name="haha")
# print(mystr2)

# join
mystr3 = ['luo', 'bo', 'da', 'za']
mystr3 = '-'.join(mystr3)  # 可用join将列表转换为字符串输出
# print(mystr3)

# replace
mystr4 = 'haha-lala'
mystr4 = mystr4.replace('haha', 'good')  # 后面的字符串“good” 取代前面“haha”
# print(mystr4)

# split
mystr5 = 'lala,haha'
mystr5 = mystr5.split('h')  # 劈开:把“h”当作劈开符，把字符串分割为多个字符串
# print(mystr5)
# print('-'.join(mystr5))

# 删除元素
# del：根据下标进行删除
# pop：删除最后一个元素
# remove：根据元素的值进行删除

# 排序
mylist5 = [1, 9,11,5, 2, 3, 4]
mylist5.sort()
# print(mylist5)
# mylist5.reverse()
print(mylist5)

# 如何判断输入的字符串是int/float
# s = "12"
# if type(eval(s)) == int:
#     print(int(s))
#
s = "1.2.3"
if type(eval(s)) == float:
    print(float(s))
    print(float(s) * 4)
