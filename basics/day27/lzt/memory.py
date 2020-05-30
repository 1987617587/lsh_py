# author:lzt
# date: 2019/12/10 9:31
# file_name: memory
# = 的复制性 复制0级引用保存的地址
# a = 10
# b = a
# arr = [1, 2, 3, 4]
# arr2 = arr
# arr2.append(5)
# print(arr)

# copy模块
import copy

# copy中的copy：复制0及1级内存区的内容
# arr = [1, 2, 3, 4]
# arr2 = copy.copy(arr)
# arr2[0] = 111
# print(arr[0])

# 深度拷贝
# arr = [1, 2, 3]
# arr2 = [4, 5, 6]
#
# arr_arr = [arr, arr2]
# # arr_arr2 = copy.copy(arr_arr)
# arr_arr2 = copy.deepcopy(arr_arr)
# arr_arr2[0][0] = 111
# print(arr_arr2)
# print(arr_arr)

# 小练习
dict_copy = {"list": [1, 2, 3], "dict": {"a": 1}, "tup": ([1, 2, 3],)}

dict1 = dict_copy
dict2 = copy.copy(dict_copy)
dict3 = copy.deepcopy(dict_copy)

dict_copy["list"][0] = 111
dict_copy["dict"]["a"] = 3
dict_copy["tup"][0][1] = 222

print(dict1)
print(dict2)
print(dict3)
