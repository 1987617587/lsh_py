"""
# author Liu shi hao
# date: 2019/11/11 15:48
# file_name: def_func

"""

# 示例：
# 1.写一个函数，用于在商城中购买道具，若购买成功，返回购买成功，否则返回购买失败。结果
# def shop():
#     print("请选择商品")
#     num = input("1.购买，其他.放弃")
#     if num == "1":
#         return "购买成功"
#     else:
#         return "购买失败"
#
#
# result = shop()
# print(result)
import random


def buy(money):
    uers_money = 3000
    if uers_money >= money:
        uers_money -= money
        return True
    else:
        return True


print("购买成功") if buy(200) else print("购买失败")


# 2.写一个函数，用于释放战斗技能，若释放成功，返回技能伤害值，否则返回无伤害。
def skill():
    l_damage = 10  # 技能范围
    l_player = 12  # 双方距离
    if l_player - l_damage >= 0:
        return "达到攻击范围"
    else:
        return "攻击范围不足"


skill()

atk = 1000
SKILL_PER = 1.5
mp = 100
sk_mp = 150


def release():
    global mp
    if mp >= sk_mp:
        mp -= sk_mp
        return atk * SKILL_PER
    else:
        return 0


hurt = release()
print(f"减掉敌方{hurt}点血量")
# 3.写一个函数用于更换武器，一个函数用于更换头盔，一个函数更换铠甲，
# 一个函数更换护手，一个函数更换护腿，一个函数更换鞋子，这些函数均返回是否更换成功，
# 然后写一个更换套装的函数，用于更换所有的装备，并返回套装是否更换成功。背包
uer_backpack = ["武器", "头盔", "铠甲", "护手"]


def change_weapon():
    if "武器" in uer_backpack:
        print("武器模型切换")
        print("背包数据更新")
        return True
    return False


def change_helmet():
    if "头盔" in uer_backpack:
        print("头盔模型切换")
        print("背包数据更新")
        return True
    return False


def change_armour():
    if "铠甲" in uer_backpack:
        print("铠甲模型切换")
        print("背包数据更新")
        return True
    return False


def change_handguard():
    if "护手" in uer_backpack:
        print("护手模型切换")
        print("背包数据更新")
        return True
    return False


if change_weapon():
    print("武器已更新")


def change_all():
    if change_weapon() and change_helmet() and change_armour() and change_handguard():
        print("一件换装成功！背包数据更新完毕")
    elif not change_weapon():
        print("换装失败!背包内找不到武器")
    elif not change_weapon():
        print("换装失败!背包内找不到护手")


change_all()


# 1.读取用户输入的整数，如果用户输入的是数字,则返回输入的值,否则提示用户重新输入。
def in_int():
    while True:
        num = input("请输入整数：")
        if num.isdigit():
            return int(num)
        print("重新输入！")


r_num = in_int()
print(r_num)


# 2.查找两个整数中的最大值
def sch_max(a, b):
    return a if a >= b else b


print(sch_max(1, 3))
print(sch_max(random.randint(1, 100), random.randint(1, 100)))


def max_min_sum(a, b):
    max_num = a if a > b else b
    min_num = a if a < b else b
    sum_num = a + b
    return max_num, min_num, sum_num

print(max_min_sum(random.randint(1, 100), random.randint(1, 100)))

a,b,c = max_min_sum(random.randint(1, 100), random.randint(1, 100))
