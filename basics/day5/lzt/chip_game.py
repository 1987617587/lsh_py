# author:lzt
# date: 2019/11/12 11:09
# file_name: chip_game
# 任务13：
# 玩家进来以后要买筹码；
# 在每次掷骰子前，
#     要下注（50~手里剩余的筹码）;
#     接着要选择买大小；
#     程序要模仿掷骰子，产生一个1~6的随机数
#     根据掷骰子的结果，判断玩家的输赢，改变玩家的手里的筹码
#         如果买大，4~6是赢，1~3是输
#         如果小，1~3是赢，4~6是输
#         如果赢了，玩家的筹码+=下注金额
#         如果输了，玩家的筹码-=下注金额    
#     提示玩家是否要退出游戏
#     玩家手里的筹码小于最小下注金额，要强制玩家退出
# 注意 ：先理清楚思路，从宏观上考虑流程，不要考虑每个步骤的细节。
# 流程搞清楚以后，再琢磨每个步骤的细节。然后写代码。
import random

import day5.fun_return_test

# 准备数据
# 玩家的资金
money = 5000
# 玩家的筹码数
user_chips = 0
# 骰子数
dice = 0
# 玩家的大小
b_s = None


def buy_chip():
    """
    购买筹码
    :return: None
    """
    # 声明访问全局变量
    global user_chips
    global money
    while 1:
        # 输入要购买的筹码数:必须为0以上的整数
        buy_chips = day5.fun_return_test.get_int()
        # 0以上的判断
        if buy_chips <= 0:
            print("请重新购买！")
            continue
        # 资金是否足够
        if buy_chips > money:
            print("资金不足 请重新兑换！")
            continue
        # 玩家的筹码数增加 资金减少
        money -= buy_chips
        user_chips += buy_chips
        # 玩家的筹码总数必须大于等于50
        if user_chips < 50:
            print(f"筹码不足一局，请重新购买！资金余额:{money}")
            continue
        break
    pass


def put_chips():
    """
    开始下注
    :return: 下注的数字
    """
    global user_chips
    while 1:
        # 请下注:(50及以上)
        put_chip = day5.fun_return_test.get_int()
        # 判断必须50以上
        if put_chip < 50:
            print("下注数必须在50以上 请重新下注！")
            continue
        # 判断玩家的筹码数是否足够
        if put_chip > user_chips:
            print("筹码数不足！请重新下注！")
            continue
        # 减少玩家的筹码数
        user_chips -= put_chip
        return put_chip

    pass


def game():
    global dice
    global b_s
    global user_chips
    # 购买筹码
    buy_chip()
    print(user_chips)
    while 1:
        # 下注
        pcs = put_chips()
        print(f"玩家的下注数:{pcs}")
        # 摇骰子
        dice = random.randint(1, 6)
        # 大小的答案
        dice_b_s = "大" if dice > 3 else "小"
        # 买大小
        b_s = "大" if input("1.大 其他.小") == "1" else "小"
        # 判断输赢
        # 显示骰子数
        print(f"开出的结果为{dice} {dice_b_s}")
        if dice_b_s == b_s:
            print("You Win！")
            # 筹码数增加
            user_chips += pcs * 2
        else:
            print("You Lose!")

        # 显示当前的状态
        print(f"当前剩余筹码:{user_chips}")

        # 判断筹码数是否足够下一局 不够 请出去
        if user_chips < 50:
            print("请下次再来！")
            break
        # 询问是否继续
        if input("退出-y 其他-继续") == "y":
            break


# 游戏开始
game()
