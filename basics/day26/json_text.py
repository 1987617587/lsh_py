"""
# author Liu shi hao
# date: 2019/12/9 11:41
# file_name: json_text

"""
# pickle可以很方便地序列化所有对象。不过json作为更为标准的格式，具有更好的可读性（pickle是二进制数据）和跨平台性。是个不错的选择。
# json使用的四个函数名和pickle一致。

# 内存中的序列化：
import json

# dic = {'age': 23, 'job': 'student'}
# dic_str = json.dumps(dic, indent=4)
# print(type(dic_str), dic_str)
# # out: <class 'str'> {"age": 23, "job": "student"}
#
# dic_obj = json.loads(dic_str)
# print(type(dic_obj), dic_obj)
# print(dic_obj['age'])
# # out: <class 'dict'> {'age': 23, 'job': 'student'}
#
# dic_obj = json.loads("[2,3,4,5,6]")  # 偏方
# print(type(dic_obj), dic_obj)

# json文件的序列化：


dic = {'user': [{'name': 'admin1', 'password': '123456'}, {'name': 'admin2', 'password': '000000'}]}
with open('abc.json', 'w', encoding='utf-8') as f:
    json.dump(dic, f, indent=4)

with open('abc.json', 'r', encoding='utf-8') as f:
    obj = json.load(f)
print(obj)
# print(dic.get("user")[0])
for i in dic.get("user"):
    print(i.get('name'), i.get('password'))
# 迭代出列表中的数据
for j in range(len(dic.get("user"))):
    print(dic.get("user")[j].get('name'), dic.get("user")[j].get('password'))

# print(dic.get("user")[0].get('name'), dic.get("user")[0].get('password'))
