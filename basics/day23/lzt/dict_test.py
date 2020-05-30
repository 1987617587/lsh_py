# author:lzt
# date: 2019/12/4 15:44
# file_name: dict_test

# 字典的生成
import random

dict1 = {1: 2, 2: 3, 3: 4, 5: "005", None: "6", "7": None}
print(dict1)

# 用字典类生成字典:字典参数！！！
dict2 = dict(张三=1, 李四=2, 王五=5)
print(dict2)

# 用字典创建字典
dict3_1 = {"1": 1, "2": 2}
dict3 = dict(**dict3_1)
print(dict3)


# 带字典参数的函数
def test_dict_parameter(**kwargs):
    print(type(kwargs))
    print(kwargs)


# 字典参数的传参
# test_dict_parameter({"1": 1, "2": 2})
test_dict_parameter(abc=1, bcd=2)
# 向字典参数传递字典:**:自动解包
dict_fun = {"1": 1, "2": 2}
test_dict_parameter(**dict_fun)

# 字典的操作:
# 增删改查
# 增加:
dict4 = {}
dict4["001"] = 123
dict4["002"] = 456
dict4["001"] = 1000
print(dict4)

# update
dict5 = {"004": 125}
dict4.update(**dict5)
print(dict4)

# print(dict4+dict5)
# 删除
# if "000" in dict4:
#     del dict4["000"]
#     dict4.pop("000")

# 修改:
dict4["008"] = 888
dict4["008"] = 999

# 查询
# [key]:会产生异常
# get(key):推荐！！！
# print(dict4[input("输入查询的key")])
# print(dict4.get(input("输入查询的key")))


# 字典的迭代
# 键的迭代
for i in dict4.keys():
    print(i)
# 值的迭代
for i in dict4.values():
    print(i)
# 键值对迭代
for k, v in dict4.items():
    print(k, v)

# print(dict4)

# 现有对象列表一个 需要优化查询速度？
import day23.set_test as st

stus = [
    st.Student(random.choice(["001", "002", "003"]), random.randint(19, 29), random.randint(1000, 9999)),
    st.Student(random.choice(["001", "002", "003"]), random.randint(19, 29), random.randint(1000, 9999)),
    st.Student(random.choice(["001", "002", "003"]), random.randint(19, 29), random.randint(1000, 9999)),
    st.Student(random.choice(["001", "002", "003"]), random.randint(19, 29), random.randint(1000, 9999)),
    st.Student(random.choice(["001", "002", "003"]), random.randint(19, 29), random.randint(1000, 9999))
]
for i in stus:
    print(i)
print("***********************")
# 依据对象列表生成对象的字典
stus_dict = {i.pid: i for i in stus}

# 根据列表筛选对象进入字典
stus_dict2 = {i.pid: i for i in stus if str(i.pid).startswith("3")}

print(stus_dict2.get(stus[0].pid))

# 键值反向
# 天气预报:
# {城市1:天气1，城市2：天气2，城市3：天气3，城市4：天气1}
# {天气1:[城市1，城市4],天气2:[城市列表]}
dict5 = {"郑州": "晴天", "上海": "晴天", "北京": "雾霾", "杭州": "小雨", "开封": "小雪"}

# dict6 = {v: [i for i in dict5.keys() if dict5.get(i) == v] for k, v in dict5.items()}
dict6 = {v: [k] for k, v in dict5.items()}
for k, v in dict5.items():
    # 得到所有的(城市:天气)
    # v == dict6的key相同
    city_list = dict6.get(v)
    if k not in city_list:
        city_list.append(k)
print(dict6)
