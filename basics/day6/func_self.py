"""
# author Liu shi hao
# date: 2019/11/12 10:07
# file_name: func_self

"""


# 1.写一个函数根据用户的按键不同角色播放不同的动画。
def animation(key):
    if key == "w":
        return "前进"
    if key == "a":
        return "左移"
    if key == "s":
        return "后退"
    if key == "d":
        return "右移"
    if key == "j":
        return "一骑当千"
    if key == "i":
        return "单刀赴会"
    if key == "o":
        return "刀锋铁骑"
    return "普攻/补刀"


# print(animation(input("按键：")))


# 2.写一个函数，传入攻击者的攻击力，技能加成系数，被攻击者的防御力，计算出伤害值。

def aggressor(atk, coefficient, phy):
    if atk * coefficient > phy:
        return atk * coefficient - phy
    return "miss"


# print(aggressor( 5, 2, phy =8))

# 银行开卡
# def creat_card(name,pid,gender,tel,adds = None,g_b= None):
#     print(f"开卡的用户{name} 身份证号{pid} 性别{gender} 电话{tel} 地址{adds} 伴侣{g_b}")
#
# creat_card("a",43424,"男","1214")
# creat_card("b",4345464,"男","1454","9009","sxas")
#
# def be_hurt(player, *args):
#     for i in range(len(args)):
#         print(f"{player}打中了{args[i]}")


# be_hurt("武则天", "王昭君", "兰陵王", "曜")

def be_hurt(player, *args):
    for i in range(len(args)):
        print(f"{player}打中了{args[i]}")


be_hurt("武则天", "王昭君", "兰陵王", "曜")


# 参数的打包和解包
#

def num_s(*args):
    pass
num_s(1, 2, 3, 4, 5)
# 解包
nums = [1, 2, 3, 4, 5]

def show_nums(a, b, c, d, e):
    print(a, b, c, d, e)

# 14.使用Random类给一个列表的所有元素随机赋初值（不重复）。

# show_nums(*nums)
# 冲突场景
# 1.函数内修改全局变量
# 会被解释器认为新声明了一个局部变量
#
# 例：
num = 10


def set_num(in_num):
    num = in_num
    pass


set_num(111)
print(num)
# 结果:10
# 解决办法：global关键字
num = 10


def set_num(in_num):
    global num
    num = in_num
    pass


set_num(111)
print(num)
# 结果:111


# 2.在函数内新声明的局部变量和全局变量同名，但是又想使用全局变量
discount = 0.9  # 全场9折


def pay(money):
    discount = 0.8  # 折上折
    print("请pay:", money * discount * discount)
    pass


pay(10000)


# 结果：请pay: 6400.0
#
# 解决办法：globals()函数
# discount = 0.9  # 全场9折


def pay(money):
    discount = 0.8  # 折上折
    print("请pay:", money * globals()["discount"] * discount)
    pass


pay(10000)


def change_list(arr):  # 传参的过程只是实参把内存地址告诉形参，并不是替换掉（可改变实参下属参数）
    arr = [1, 2, 3]


arr2 = [000.000]
change_list(arr2)
print(arr2)
