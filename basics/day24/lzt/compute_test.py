# author:lzt
# date: 2019/12/5 10:42
# file_name: compute_test
# 1+2+3+4
from queue import LifoQueue
expression = input("请输入一个运算的式子:")
print(eval(expression))

# expression = input("请输入一个加法的式子:")

# # 拆分数字和符号
# # 数字的列表:
# nums = expression.split("+")
# # 符号的列表
# ops = ["+"] * (len(nums) - 1)
# # 产生两个栈
# num_stack = LifoQueue()
# op_stack = LifoQueue()
# # 数字和符号进栈
# for i in nums:
#     num_stack.put(int(i))
# # 符号进栈
# for i in ops:
#     op_stack.put(i)
# # 运算过程：
# while not op_stack.empty():
#     # 运算数弹出两个
#     num1 = num_stack.get()
#     num2 = num_stack.get()
#     # 弹出运算符
#     op = op_stack.get()
#     # 按运算符运算
#     ret = num1 + num2
#     # 将结果压回运算数栈
#     num_stack.put(ret)
# print(num_stack.get())

