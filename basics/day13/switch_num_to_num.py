"""
# author Liu shi hao
# date: 2019/11/21 14:19
# file_name: switch_num_to_num

"""
def in_int_n():
    while True:
        num = input("请输入要转换的n进制n(暂支持36进制):")
        if num.isdigit() and 2<=int(num)<37:
            return int(num)
        print("重新输入！")

# n进制转10进制
def switch():
    x = in_int_n()
    str1 = input("输入符合n进制的规范数：")
    sum = 0
    for i in range(len(str1) - 1, -1, -1):
        if str1[i].isdigit():
            sum += int(str1[i]) * x ** int(len(str1) - i - 1)
        else:
            sum += (ord(str1[i]) - 55) * x ** int(len(str1) - i - 1)
    return sum


print(switch())

# 10进制转n进制


def in_int_m():
    while True:
        num = input("请输入要转换整数m:")
        if num.isdigit():
            return int(num)
        print("重新输入！")


def conversion_base():
    m = in_int_m()
    n = in_int_n()
    str1 = ""
    while m != 0:
        if m % n >n:
            str1 =  str(chr(m % n+55))  + str1
        # str1 = "|"+str(m % n) +"|"+ str1  # 取余数，按位数累加到字符串
        else:
            if m % n > 9:
                str1 = str(chr(m % n + 55)) + str1
            else:
                str1 = str(m % n)  + str1
        m = m // n  # 取商做下一次的除数
    return str1


print(conversion_base())