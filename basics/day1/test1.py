# author Liu shi hao
# date: 2019/11/5 10:48
# file_name:test1
import random

from math import ceil

print(abs(-100))
print(ceil(10.8))

print("ooo0000000000000000oooooooooooooooooo \
ooooooooooooooooooooooooooooooo \
ooooooooooooooooooooooooooooooooo")  # 你是谁
num_1 = 1
num_2 = "loi"
num_3 = 1.56
print(type(num_1))
print(type(num_2))
print(type(num_3))
vip_level = 4
pay = 100
t_f = vip_level > 4 and pay > 100
print(t_f)
vip_level = 8
print(t_f)
pay = 200
t_f = vip_level > 4 and pay > 100
print(t_f)

f_num = 2.11112111355
print(round(f_num, 10))

name = "刘四"
print(name[0], name[1])

print(len(name))

user_name = None
print(type(user_name))

random_num = random.randint(1, 100001)
str_random_num = str(random_num)
print(type(str_random_num))
print(len(str_random_num))

float_1 = 1.34
int_1 = 334
int_2 = int(float_1)
print(type(float_1))
print(int_2)
print(type(int_2))
float_2 = float(int_1)
print(float_2)
print(type(float_2))

str_11 = "1234"
print(int(str_11) + 1234)
print(float(str_11) + 0.11)
print(bool(str_11))
print(bool(None))
list_1 = ["j", "jij", "iutg"]
name = input("请输入姓名：")
age = int(input("请输入年龄："))
print(f"名字：{name},姓名：{age}")
print(f"""
1111111111111111
    1111{name}
22222222{age}
99999999999{list_1}
""")
print(str.format("名字：{0},年龄：{1}", name, age))
print(str.format("名字：{name},年龄：{age}", name=name, age=age))
value = input("此处填写提示信息：")
name = input("请输入您的名字：")
print(str.format("您的名字是{0}", name))
