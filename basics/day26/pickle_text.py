"""
# author Liu shi hao
# date: 2019/12/9 11:23
# file_name: pickle_text

"""
# 内存上的序列化:
import pickle

# 字典序列化
# dic = {'age': 23, 'job': 'student'}
# byte_data = pickle.dumps(dic)
#
# print(byte_data)
# # 字典反序列化
# obj = pickle.loads(byte_data)
# print(obj)
#
# arr1 = [1, 2, 3, 4]
# set1 = {2, 3, 4, 6}

# list_data = pickle.dumps(arr1)
# re_arr = pickle.loads(list_data)
# print(re_arr)

# set_data = pickle.dumps(set1)
# re_set = pickle.loads(set_data)
# print(re_set)


# 借助文件的序列化：
# 序列化
with open('abc.txt', 'wb') as f:
    dic = {'age': 23, 'job': 'student'}
    set1 = {1, 2, 3}
    arr1 = [2, 3, 4]
    pickle.dump(dic, f)
    pickle.dump(set1, f)
    pickle.dump(arr1, f)

# 反序列化
with open('abc.txt', 'rb') as f:
    aa = pickle.load(f)
    bb = pickle.load(f)
    cc = pickle.load(f)
print(aa, bb, cc)
print(type(aa))  # <class 'dict'>
