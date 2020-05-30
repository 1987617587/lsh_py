# author : liuShiHao
# Date : 2020/5/29 23:24
# 经典问题：对于一个m*n的网格，从左上角的方格到右下角的方格，共有多少条路径（只允许向右和向下）
# 向右走（x+1，y）
# 向下走（x，y-1）

# 找出规律
# Start	1	    1	    1
# 1	    2	    3	    4
# 1	    3	    6	    10
# 1	    4	    10  	20
# 1 	5       15     35  Finish   

# 方法一：递归
def func1(m, n):
    # 起始位置（0，0）目标(m,n)

    # # m行 # n列

    if m == 1 or n == 1:
        return 1
    return func1(m-1,n) + func1(m,n-1)


print(func1(3, 5))

# 方法二：非递归实现
import numpy as np


def left_to_right(m, n):
    d = np.zeros(dtype=int, shape=(m, n))
    d[0][0] = 0
    for i in range(1, m):
        d[i][0] = 1
    for j in range(1, n):
        d[0][j] = 1
    for i in range(1, m):
        for j in range(1, n):
            d[i][j] = d[i - 1][j] + d[i][j - 1]
    return d[m - 1][n - 1]


if __name__ == '__main__':
    # res=left_to_right(7,5)
    res = left_to_right(3, 5)
    print(res)
