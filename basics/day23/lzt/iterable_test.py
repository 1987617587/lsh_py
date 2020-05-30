# author:lzt
# date: 2019/12/4 11:00
# file_name: iterable_test

# 迭代一切
# 迭代字符串:
str1 = "asdhjasjdgj"
# for i in str1:
#     print(i)


# 迭代列表
list1 = [1, 2, 3, 4]
# for i in list1:
#     print(i)

# 迭代元组
t = (1, 2, 3, 4)
for i in t:
    print(i)

# 迭代中带序号
for index, i in enumerate(t, 0):
    print(index, i)

# 迭代中能否修正容器的内容
# 不要修正迭代变量的指向！！！
# 不要用迭代删除！！结果会不正常！！！
# 迭代的作用：查询数据用
for index,i in enumerate(list1,0):
    # list1.remove(i)
    print(i)
    list1[index] = 10
print(list1)


