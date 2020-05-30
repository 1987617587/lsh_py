"""
# author Liu shi hao
# date: 2019/12/7 10:52
# file_name: pickle

"""
# 内存上的序列化:
import pickle
#字典序列化
dic = {'age': 23, 'job': 'student'}
byte_data = pickle.dumps(dic)
# out -> b'\x80\x03}q\x00(X\x03\x00\x00\...'
print(byte_data)
#字典反序列化
obj = pickle.loads(byte_data)
print(obj)

# 借助文件的序列化：
# 序列化
with open('abc.txt', 'wb') as f:
    dic = {'age': 23, 'job': 'student'}
    pickle.dump(dic, f)
# 反序列化
with open('abc.txt', 'rb') as f:
    aa = pickle.load(f)
    print(aa)
    print(type(aa))  # <class 'dict'>
