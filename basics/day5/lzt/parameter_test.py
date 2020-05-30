# author:lzt
# date: 2019/11/12 14:20
# file_name: parameter_test

# 参数的定义
# 形参:a,b


def add(a: int, b: int):
    """
    为a和b求和
    :param a: 数据a
    :param b: 数据b
    :return: 两个数据的和
    """
    return a + b


# 函数执行
# c = "a"
# d = "b"
# # 实参:c,d
# print(add(c, d))

# 1.写一个函数根据用户的按键不同角色播放不同的动画。
def doaction(key):
    """
    根据key做出不同的动画效果
    :param key:用户的按键
    :return:None
    """
    # 根据按键做动画播放
    if key == "w":
        print("播放前进动画")
    elif key == "d":
        print("播放右移动画")
    elif key == "a":
        print("左移动画")
    elif key == "s":
        print("后退动画")
    else:
        print("不支持该按键！")


# while 1:
#     doaction(input("请按键"))

# 2.写一个函数，传入攻击者的攻击力，技能加成系数，被攻击者的防御力，计算出伤害值。
def hurt(atk, sk_per, h_def, dis_per):
    """
    计算伤害值并返回
    :param atk:主动攻击方的攻击力
    :param sk_per:本次的技能伤害
    :param h_def:被攻击方的防御力
    :param dis_per:防御力的抵伤系数
    :return:本次的真实伤害值
    """
    hurt = atk * sk_per - h_def * dis_per
    return 1 if hurt < 0 else hurt


# 测试伤害函数
# e_atk = 1500
# e_sk_per = 2
# e_h_def = 1200
# e_dis_per = 0.2
# print(f"本次伤害值为:{hurt(e_atk, e_sk_per, e_h_def, e_dis_per)}")
# print(f"本次伤害值为:{hurt(2000, 1.7, 1800, 0.3)}")


# 位置参数:按次序摆放的形参
def print_nums(arg1, arg2, arg3):
    """
    输出传入的参数
    :param arg1:第一个参数
    :param arg2:第二个参数
    :param arg3:第三个参数
    :return:None
    """
    print(arg1)
    print(arg2)
    print(arg3)


# 实参传入并执行
# print_nums(1, 2, 3)
# print_nums(2, 1, 3)
# print_nums(3, 1, 2)
# 位置参数可以按照名字来传参
# print_nums(arg2=10, arg3=5, arg1=6)
# print_nums(1, arg3=2, arg2=1)

# 银行的开卡
# 以默认值的方式写的参数 可以免于传递
def create_card(name, pid, gender="男", tel="123456", addr=None, b_g=None):
    """
    为开卡输入用户数据
    :param name:真实姓名
    :param pid:身份证号
    :param gender:性别
    :param tel:电话号码
    :param addr:住址
    :param b_g:男女朋友
    :return:None
    """
    print(f"开卡的用户{name} 身份证号：{pid} 性别:{gender} 电话:{tel} 住址:{addr}  有没有朋友:{b_g}")


# 进行单据的填写
# create_card("002", "1234")
# create_card("002", "12345", "女")
# create_card("002", "123456", "女", "12312312312")
# create_card("001", "121xxxxxxx", "男", "16666666xxx")
# create_card(pid="123123", name="123", gender="女")

# 命名关键字参数:*
def print_args(arg1, arg2, *, arg3, arg4):
    print(arg1, arg2, arg3, arg4)


# print_args(1, 2, 3, 4)
# print_args(1, 2, arg4=4, arg3=3)

# def be_hurt():
#     print("未命中目标")
#
#
# def be_hurt(player1):
#     print("未命中目标")
#
#
# def be_hurt(player1, player2):
#     print("未命中目标")

# 可变参数列表
# 1. 可变参数列表是否可以和其他参数形式混杂
# def be_hurt(player, *args):
#     """
#     减掉AOE释放技能伤害的角色的血量值
#     :param player:主动攻击的角色
#     :param args:被命中的角色
#     :return:None
#     """
#     # 查看一下args的类型
#     print(type(args))
#     # 遍历args这个容器 查看被打中的角色
#     for i in range(len(args)):
#         print(f"{player}击中了{args[i]}！")


# be_hurt("悟空")
# be_hurt("悟空", "阿珂")
# be_hurt("悟空", "阿珂", "嬴政")
# be_hurt("悟空", "阿珂", "嬴政", "妲己")

# 2.可变参数列表一般情况下位于目前参数的末尾
def be_hurt(*args, player):
    """
    减掉AOE释放技能伤害的角色的血量值
    :param player:主动攻击的角色
    :param args:被命中的角色
    :return:None
    """
    # 查看一下args的类型
    print(type(args))
    # 遍历args这个容器 查看被打中的角色
    for i in range(len(args)):
        print(f"{player}击中了{args[i]}！")


# be_hurt("1", "2", "3", player="4")

# 3.可变参数列表和*是互不见面的状态
# def be_hurt(*, args1, arg2, *args):
#     pass
# be_hurt(args1=1,arg2=2,a="1",b="2")

# 参数的打包和解包
# 参数的打包：*args **args方式来完成打包
# def nums(*args):
#     pass


# nums(1, 2, 3, 4, 5, 6, 7, 8)

# 参数的解包
nums = [1, 2, 3, 4, 5, 6, 7]


def show_nums(a, b, c, d, e, f, g):
    print(a, b, c, d, e, f, g)


# show_nums(*nums)


# 函数内的修正对实参有无影响？
# def swap(a, b):
#     a, b = b, a
#     print(f"a={a} b={b}")


# c = 1
# d = 2
# swap(c, d)
# print(f"c={c} d={d}")

# def swap(arr):
#     # 交换列表中0和1位置
#     arr[0], arr[1] = arr[1], arr[0]
#     print(f"函数内的列表:{arr}")
#     pass
#
#
# arr_obj = [1, 2]
# swap(arr_obj)
# print(arr_obj)

# 可变和不可变类型
# str1 = "bcd"
# print(id(str1))
# str1 = "abc"
# print(id(str1))

# 不可变类型的传参
def change(str1, num, bool1):
    str1 = "1111"
    num = 1234
    bool1 = False


# 传入不可变类型的实参:函数内的修改不会影响实参
# s1 = "ok"
# num1 = 123
# bool11 = True
# change(s1, num1, bool11)
# print(s1, num1, bool11)

# 可变类型的传参:影响的程度:1.若可变类型的下属的值发生改变 可以影响到实际参数 2.若整体发生了改变 不影响实参
def change_list(arr):
    # arr[3] = 10
    arr = [100, 1000]


arr2 = [1, 2, 3, 4]
change_list(arr2)
print(arr2)
