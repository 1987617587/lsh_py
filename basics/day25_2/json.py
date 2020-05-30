"""
# author Liu shi hao
# date: 2019/12/7 10:53
# file_name: json

"""
# pickle可以很方便地序列化所有对象。不过json作为更为标准的格式，具有更好的可读性（pickle是二进制数据）和跨平台性。是个不错的选择。
# json使用的四个函数名和pickle一致。
#
# 内存中的序列化：
import json

dic = {'age': 23, 'job': 'student'}
dic_str = json.dumps(dic)
print(type(dic_str), dic_str)
# out: <class 'str'> {"age": 23, "job": "student"}

dic_obj = json.loads(dic_str)
print(type(dic_obj), dic_obj)
# out: <class 'dict'> {'age': 23, 'job': 'student'}

# json文件的序列化：
import json

dic = {'age': 23, 'job': 'student'}
with open('abc.json', 'w', encoding='utf-8') as f:
    json.dump(dic, f)

with open('abc.json', encoding='utf-8') as f:
    obj = json.load(f)
    print(obj)
