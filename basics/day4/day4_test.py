"""
# author Liu shi hao
# date: 2019/11/8 10:11
# file_name: day4_test

"""
import math

# print([1,2] == [2,1])
# list = [3,4,5]
# for i in range(len(list)):
#     list[i] -= 3
# print(list)
#
# list = [i-3 for i in list]
# print(list)
# print(list -1)
# 11.今有四个人,他们得年龄各不相同,他们年龄总和是129,而其中有三个人的年龄是平方数,
# 若倒退15年,这四人中仍有三个人的年龄是平方数,求他们各自的年龄
# #
# list_11 = []
# for i in range(129):
#     for j in range(129):
#         for k in range(129):
#             for m in range(129):
#                 if i*i +j*j+k*k+m ==129 and i!= j and i!= k \
#                         and i!= m and j!= k and j!= m and i!= k and i!= m:
#                     # print( i*i ,j*j,k*k,m)if i*i >15 and j*j>15 and k*k>15and m>15else None
#                     a =i*i
#                     b =j*j
#                     c = k*k
#                     d = m
#                     for n in range(1, 13):  # a,b,c,最少有两个减去15还是平方数
#                         for x in range(1, 13):  # 无外乎两种可能
#                             if a ==n*n +15 and b ==x*x +15 or b ==n*n +15 and c ==x*x +15:
#                                 if a >15 and b>15 and c>15and d>15 :  # 此时结果已出，但顺序有多种可能，查重！
#                                     list_11.append(a)  # 查重！
#                                     if b not in list_11:
#                                         list_11.append(b)
#                                         if c not in list_11:
#                                             list_11.append(c)
#                                             # if d not  in list_11:
#                                             list_11.append(d)
#                                             print(list_11)
#                                             break

# n = 3
# for i in range(2*n):
#     # if i <= n:
#         for j in range(i):
#             if i <= j<= 2*n - i:
#                 print(j, end=" ")
#             else:
#                 print(i, end=" ")
#
#         print()


# for i in range(100,1,-1):
#     for j in range(2,i):
#         if i % j == 0:
#             break
#     else:
#         print(i)

# 画图如下
# 0  0 	0 	0 	0
# 0  1 	1 	1 	0
# 0  1 	2 	1 	0
# 0  1 	1 	1 	0
# 0  0 	0 	0 	0
# n = int(input("请输入行数："))
# for i in range(n):
#     for j in range(n):
#         print(min(i,j,n-i-1,n-j-1),end=" \t")
#     print()
# 5  5 	5 	5 	5
# 5  4 	4 	4 	5
# 5  4 	3 	4 	5
# 5  4 	4 	4 	5
# 5  5 	5 	5 	5
# m = int(input("请输入行数："))
# for i in range(1,m+1):
#     for j in range(1,m+1):
#         print(max(i,j,m-i+1,m-j+1),end=" \t")
#     print()



# 11.求1-100之间的所有差值为六的质数对。
# for i in range(2,101):
#     for j in range(2,i):
#         if i %j == 0:
#             break
#     else:
#         # print(i)
#         if i+6<101:
#             num = i+6
#             for k in range(2,num):
#                 if num %k == 0:
#                     break
#             else:
#                 print(i,num)
# 质数循环到开平方就ok
# for i in range(2,101):
#     for j in range(2,int(math.sqrt(i) +1)):
#         if i %j ==0:
#             break
#     else:
#         # print(i)
#         if i+6<101:
#             num = i+6
#             for k in range(2,int(math.sqrt(num) +1)):
#                 if num %k == 0:
#                     break
#             else:
#                 print(i,num)


# n = int(input("请输入行数："))
# for i in range(n):
#     for j in range(n):
#         print(min(i,j,n-i-1,n-j-1),end=" \t")
#     print()
#
# m = int(input("请输入行数："))
# for i in range(1,m+1):
#     for j in range(1,m+1):
#         print(max(i,j,m-i+1,m-j+1),end=" \t")
#     print()
#

# 编程：
# （1）在控制台上输出100~500之间的所有奇数，并计算它们的和。 
#
# sum_1 = 0
# for i in range(101,500,2):
#     sum_1 += i
# print(sum_1)

# （2）在控制台上输出100~200之间不能被3整除的所有数。
#

# （3）统计1~1000之内既能被5整除，也能被7整除的数的个数。 
#
# （4）从300开始，找出连续100个既能被3整数又能被5整除的数。 
# s = 300
# counts_4 = 0
# while counts_4 <100:
#     if s %3==0 and s%5==0:
#         counts_4+=1
#         print(s)
#         s+=1
#     else:
#         s+=1
# （5）计算s = 1! + 2! + 3! + ...+ n! （其中n是用户输入的正整数）。
#
# sum = 0
# f = 0
# n = int(input("请输入n:"))
# for i in range(n+1):
#     f *= i
#     sum += f
# print(sum)


# （6）计算出不大于1000 的10个最大的素数。
# counts = 0
# for i in range(1000, 1, -1):
#     for j in range(2, i):
#         if i % j == 0:
#             break
#     else:
#         counts += 1
#         if counts <= 10:
#             print(i)


m = 21000/(18*5)/7
print(m)




































