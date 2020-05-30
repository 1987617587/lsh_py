"""
# author Liu shi hao
# date: 2019/12/3 14:21
# file_name: math_text

"""
import math

# 数学模块math
# python中math模块中提供的基本数学函数
# 角度和弧度的换算
print(math.radians(180))
print(math.degrees(math.pi))
# sin(x) ：求x的正弦
print(math.sin(math.pi / 2))
# cos(x) ：求x的余弦
print(math.cos(math.pi))
# asin(x)：求x的反正弦
print(math.degrees(math.asin(1)))
# acos(x)：求x的反余弦
print(math.degrees(math.acos(1)))
# tan(x) ：求x的正切
print(math.tan(math.pi / 4))
# atan(x)：求x的反正切
print(math.atan(1))
# fmod(x,y)：求x/y的余数
print(math.fmod(5, 3))
# ceil(x) ：取不小于x的最小整数
print(math.ceil(1.1))
# floor(x)：求不大于x的最大整数
print(math.floor(1.1))
# fabs(x)：求绝对值
print(math.fabs(-1.1))
# pow(x,y) ：求x的y次幂
print(pow(3, 2))
# log10(x) ：求x的以10位底的对数
print(math.log10(100))
print(math.log2(4))
# sqrt(x) ：求x的平方根
print(math.sqrt(4))
# factorial(x) 求x的阶乘
print(math.factorial(4))
# trunc(x)  求x的整数部分 舍弃小数
print(math.trunc(1.9))
print(int(1.9))
