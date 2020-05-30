# author:lzt
# date: 2019/12/4 11:27
# file_name: list_create
# 生成全排列:"123"
import time

list1 = [a + b + c for a in "123" for b in "123" for c in "123"]
print(list1)
# 1.向列表[1, 2, 3, 4, 5]插入20，30，40
# append
# insert
# + extend
# list1 = [1, 2, 3, 4, 5]
# list1 += [20, 30, 40]
# print(list1)
# 2.从列表[1, 2, 3, 4, 5]删除4，5

# 3.找到列表[5,3,5,7,4,6,8,3,6]中第一个最小元素的下标
# list1 = [5, 3, 5, 7, 4, 6, 8, 3, 6]
# print(list1.index(min(list1)))

# 4.创建列表,元素为1-1000以内的偶数
# print([x for x in range(2, 1001, 2)])

# 5.将'My name is Jack, Your name is Rose'转换成列表
# (1)并截取里面的前10个字符
# (2)并截取里面的后4个字符
# str1 = 'My name is Jack, Your name is Rose'
# list1 = list(str1)
# print(list1[:10:])
# print(list1[-4::])

# 6.[1,2,4,5,6,7,3,2,6,3,2],打印出列表中每个数字出现的次数
# list1 = [1,2,4,5,6,7,3,2,6,3,2]
# list1_counts = [list1.count(i) for i in list1]
# print(list1_counts)

# 7.从['P','Y','T','H','O','N']挑出一个字母和['G','O','O','D']挑出一个字母有多少种组合,将各组合方式打印出来


# 8.列表[1,2,3,4,5],需要用户输入数字，然后删除列表中输入数字对应下标的元素
# 9.列表[100,33,55,2,56,66,22],依次打印每一个元素，然后从列表中删除，直到列表没有元素

# 10.将1-100以内的平方数放入列表，打印列表
# print([i * i for i in range(1, 11)])

# 11.创建列表，循环向列表依次中放入1个数字，达到100个后，依次删除所有的元素，
# 删除完后，继续循环向列表依次中放入1个数字，达到100个后，依次删除所有的元素.......依次类推
# list1 = []
# while 1:
#     for i in range(100):
#         list1.append(i)
#     # for i in range(100):
#     #     del list1[0]
#     # 清空列表
#     list1.clear()
#     print(list1)

# 12.arr1 = [2,4,6,8,10]和 arr2 = [5,4,2,6,7,8],编写程序求出l2和l1共有的元素
# arr1 = [2, 4, 6, 8, 10]
# arr2 = [5, 4, 2, 6, 7, 8]
# print([i for i in arr1 if i in arr2])

# 13.["book","shoe","bullet","brush","car"]将列表中所有包含字母"b"的单词放入新列表中，打印出来
# arr13 = ["book","shoe","bullet","brush","car"]
# print([i for i in arr13 if "b" in i])

# 14.用户输入字符串，将字符串转换成列表，如果字符超过5个，只打印用户输入的前5个字符
# msg = input("消息:")
# print(msg[:5])

# 15.列表【1，2，3，4，5】，循环删除列表的第一个元素，并将它放到列表的后面，打印每一次删除后列表的状态
# list1 = [1, 2, 3, 4, 5]
# while 1:
#     list1.append(list1.pop(0))
#     print(list1)
#     time.sleep(1)

# 16.['P','Y','T','H','O','N',"I","S","V","E","R","Y","G","O","O","D"]将列表中的所有"Y"替换成"*"
# list1 = ['P', 'Y', 'T', 'H', 'O', 'N', "I", "S", "V", "E", "R", "Y", "G", "O", "O", "D"]
# # 先将列表变为字符串:
# # 字符串不可变！！！
# str1 = "".join(list1)
# str1 = str1.replace("Y", "*")
# list1 = list(str1)
# print(list1)

# 17.['P','Y','T','H','O','N',"I","S","V","E","R","Y","G","O","O","D"]删除列表中出现次数最多的字母
# list1 = ['P','Y','T','H','O','N',"I","S","V","E","R","Y","G","O","O","D"]
# # 找到重复次数最多的字母
# counts = [list1.count(i) for i in list1]
# max_char = list1[counts.index(max(counts))]
# # list1 = [i for i in list1 if max_char != i]
# while max_char in list1:
#     list1.remove(max_char)
# print(list1)

# 18.[3,6,5,7,3,5,7,8,9,9] 删除列表中所有最大的元素
# 19.[4,5,7,3,6,7,8,6]编写程序查找程序中第二大的元素，打印出
# list1 = [3, 3, 3, 3, 3, 3]
# list2 = [i for i in list1 if i != max(list1)]
# if len(list2) != 0:
#     print(max(list2))
# else:
#     print("没有第二大的数据！")

# 20.["book","shoe","bullet","brush","car"]将列表中的每个元素重复5遍放入新的列表
# 21.[1,2,3,4,5,6,7,8,9]交换列表第一个和最后一个元素的位置
# 22.对[1,2,3,4,5,6,7,8,9]每一个元素和5求异或
# 23.[True,False,True,True,False]，对列表中每个元素取反
# 24.使用循环创建列表，如下[[1], [1,2] ,[1,2,3,],[1,2,3,4],[1,2,3,4,5] ]
list24 = [list(range(1, i + 1)) for i in range(1, 6)]
print(list24)
# 25.使用循环创建列表，如下[[1,2,3,4,5] ,[1,2,3,4],[1,2,3],[1,2],[1]]
list25 = [list(range(1, i+1)) for i in range(5, 0, -1)]
print(list25)
