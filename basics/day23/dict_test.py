"""
# author Liu shi hao
# date: 2019/12/4 15:48
# file_name: dict_test

"""

# dict1 = {1: 2, "2": 3, "asd": 4}
# print(dict1)
# dict2 = {"2": 3, "asd": 4}
# dict3 = dict(**dict2)
# print(dict3)
# dict4 = dict(张三=1, 李四=2)
# print(dict4)
# print(id(dict1), id(dict2), id(dict3), id(dict4))
#


_dict = dict.fromkeys([1, 2, 3, 4, 5], 1)
print(_dict)
for i in _dict:
    print(i)

for i in _dict.values():
    print(i)

for k, v in _dict.items():
    print(k, ":", v)

print(_dict.pop(1))
print(_dict.get(1))

print({k:v for k, v in [1, 2, 3, 4, 5], [1, 2, 3, 4, 5]})
