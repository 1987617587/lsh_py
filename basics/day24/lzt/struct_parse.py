# author:lzt
# date: 2019/12/5 11:47
# file_name: struct_parse
# 结构间的互转
# 列转行
a = [1, 2, 3]
b = [1, 2, 3]
c = [1, 2, 3]
# zip1 = zip(a, b, c)
# for i in zip1:
#     print(i)

# 双列表转字典：
strs1 = ["a", "b", "c"]
strs2 = [1, 2]
print(dict(zip(strs1, strs2)))
