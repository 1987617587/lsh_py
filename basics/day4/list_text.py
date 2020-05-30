"""
# author Liu shi hao
# date: 2019/11/8 17:27
# file_name: list_text

"""
str1 = "siaihdfaiojdfm"
str1_list = list(str1)
print(str1_list)
list_num = list(range(10))
print(list_num)
list_x2 = list(x*2 for x in range(3))
print(list_x2)
# 语法糖
arr_7 = ["a"]*15
print(arr_7)
# 操作列表
print(len(arr_7))

print(list_x2[2])
# 求元素个数
# 访问元素
for i in range(len(list_x2)):
    print(list_x2[i],end=" ")
print()
list_x2.append(3)
print(list_x2)
list_x2.insert(1,5)
print(list_x2)
del list_x2[3]
print(list_x2)
list_x2.remove(5)
print(list_x2)
if 0 in list_x2:
    list_x2.remove(0)
    print(list_x2)
list_x2[1] = 45
print(list_x2)

# 其他










