"""
# author Liu shi hao
# date: 2019/12/10 9:07
# file_name: copy_test

"""
# copy模块
import copy


# 浅拷贝 深拷贝
# 1.‘=’ 一般意义的复制 复制0级内存区
# 复制0级引用保存的地址（共同管理一块地址）
# list1 = [1, 2, [3, 4]]
# print(list1)
# list2 = list1
# print(list2)
# list1.append(5)  # 任意一个管理者修改地址内容
# print(list1, list2)  # 地址发生改变，都受影响
# list1[2].append(3.5)
# print(list1, list2)

# 2.浅拷贝copy 复制0及1级内存区


# list1 = [1, 2, [3, 4]]
# print(list1)
# list2 = copy.copy(list1)
# print(list2)
# list1.append(5)  # 此时互不影响（复制0及1级内存区）
# print(list1,list2)
#
# list1[2].append(3.5)  # 此时互相影响（无法复制2级内存区）
# print(list1, list2)

# 3.深拷贝 deepcopy 复制每级内存区

#
# list1 = [1, 2, [3, 4]]
# print(list1)
# list2 = copy.deepcopy(list1)
# print(list2)
# list1.append(5)  # 此时互不影响（复制任意级内存区）
# print(list1,list2)
# list1[2].append(3.5)  # 此时互不影响（复制任意级内存区）
# print(list1, list2)


# 新建字典对象，
class Hero:

    def __init__(self, name, hp, atk) -> None:
        super().__init__()
        self.name = name
        self.hp = hp
        self.atk = atk


# 字典对象中有键名list，值为列表
# 有键名dict，值为对象
# 有键名tup，值为元组
dict1 = {'list': [1, 2, 3, 4], 'dict': {Hero('关羽', 123, 200)}, 'tup': (99, 87, 56, 23)}
# 使用复制，浅拷贝，深拷贝得到3个对象
a1 = dict1
a2 = copy.copy(dict1)
a3 = copy.deepcopy(dict1)
print(a1,a2, a3)
# 改变原始对象中键dict、list、tup的值
dict1['list'][0] = 2  # 此时修改二级（会受影响）
# dict1['list'] = [1, 1, 1, 1]  # 此时修改一级（不会受影响）
dict1['dict'] = {Hero('张飞', 1000, 20)}
dict1['tup'] = (10, 10, 10, 10)
print(a1,a2, a3)

# 查看新对象的值是否发生改变
# 要求：给与输出结果详细解说
