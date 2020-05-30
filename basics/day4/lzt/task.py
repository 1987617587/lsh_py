# author:lzt
# date: 2019/11/8 10:15
# file_name: task
# 任务5：
# 提示用户输入用户名，然后再提示输入密码，如果用户名是“admin”并且密码是“88888”，则提示正确，
# 否则，提示用户“用户名或者密码错误”，但如果错误达到3次，则提示用户"您的账户已被冻结"，退出程序。
# for i in range(3):
#     user_name = input("用户名:")
#     password = input("密码:")
#
#     if user_name == "admin" and password == "88888":
#         print("验证通过！")
#         break
#     else:
#         print("用户名或者密码错误" if i != 2 else "您的账户已被冻结")
#
# 任务6：
# 求1-100间的所有奇数和。
# sum = 0
# for i in range(1, 101, 2):
#     sum += i
#     pass
# print(sum)
#
# 任务7：
# 求1-100间的所有能被3整除的数的和。
# sum = 0
# for i in range(0, 101, 3):
#     sum += i
#     pass
# print(sum)
#
# 任务8：
# 编程实现如下图列出的图形。
# *
# ***
# *****
# *******
#
# 任务9：
# 让用户输入一个数显示下面内容。
# *******       
# ******        
# *****          
# ****           
# ***            
# **             
# *   
# 行数由用户指定
lines = int(input("行数:"))
# for i in range(lines):
#     # i:0 1 2 3 4 5 6....lines-1
#     # *:7 6 5 4 3 2 1
#     # 7-i=>lines-i
#     print("*"*(lines-i))

#    
# 任务10：
# 编程实现如下图列出的图形。
#
#    *              
#   ***        
#  *****    
# *******
# for i in range(lines):
#     # i:0 1 2 3 4...lines-1
#     #  :3 2 1 0:3-i=>lines-1-i
#     print(" " * (lines - 1 - i), end="")
#     # *:1 3 5 7:2*i+1=>2*i+1
#     print("*" * (2 * i + 1))
#
# 任务11：
# 编程实现如下图列出的图形。
#    *
#   ***
#  *****
# *******
#  *****
#   ***
#    *
# 判断用户的行数是否可以打印图形
if lines % 2 == 0:
    print("该行数下图形无法输出！")
else:
    # 行数为7：
    # 上半部分:4行
    # 下半部分:3行
    # 行数为lines：
    # 上半部分:(lines+1)/2行
    for i in range((lines + 1) // 2):
        # 打印空格
        # i:0 1 2 3
        #  :3 2 1 0:3-i=>(lines+1)/2-1-i
        print(" " * ((lines + 1) // 2 - 1 - i), end="")
        # 打印*
        # *:1 3 5 7:2*i+1
        print("*" * (2 * i + 1))
        pass
    # 下半部分:(lines-1)/2行
    d = (lines - 1) // 2
    for i in range(d):
        # 空格
        # i:0 1 2
        #  :1 2 3:i+1
        print(" " * (i + 1), end="")
        #   2 1 0: d-i
        # *:5 3 1: 2*(d-i)+1
        print("*"*(2*(d-i)+1))
        pass
