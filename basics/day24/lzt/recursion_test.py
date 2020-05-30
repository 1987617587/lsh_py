# author:lzt
# date: 2019/12/5 16:51
# file_name: recursion_test

# 阶乘
n = 5


# n = 1*2*3*4*...n-1*n
def fac(n):
    """
     求某数阶乘
    :param n:某数
    :return:阶乘值
    """
    # 结束条件:
    if n == 1:
        return 1
    else:
        return fac(n - 1) * n


def fibona(n):
    if n == 1 or n == 2:
        return 1
    return fibona(n - 1) + fibona(n - 2)


def rabbit(half_years: int):
    """
    求某半年期的兔子数
    :param half_years:半年期数
    :return:大兔子数 中兔子数 小兔子数
    """
    if half_years == 0:
        return 0, 0, 1
    # 求前半年期的兔子数
    a, b, c = rabbit(half_years - 1)
    temp = a
    a += b
    b = c
    c = temp
    return a, b, c


print(rabbit(40))
