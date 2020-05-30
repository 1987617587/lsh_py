"""
# author Liu shi hao
# date: 2019/12/5 17:01
# file_name: digui_test

"""


# 思考：一对小兔子一年后长成大兔子，一对大兔子每半年生一对小兔子，假定第一年年初投放了一对小兔子，请编程实现，第Ｎ年年末总共有多少对兔子，Ｎ由键盘输入！
# 
# 特殊到一般 归纳规律
# 半年数:  0  1     2     3     4     5     6
# 大兔子   0  0     1     1     1     2     3
# 中兔子   0  1     0     0     1     1     1
# 小兔子   1  0     0     1     1     1     2
# 
# 前半年期的大中小兔子数:a  b  c
# 
# temp = a;
# a += b;
# b=c;
# c =temp;


def func(half_years: int):
    if half_years == 0:
        return 0, 0, 1

    a, b, c = func(half_years - 1)
    temp = a
    a += b
    b = c
    c = temp
    return a, b, c


print(func(4))  # 半年数
