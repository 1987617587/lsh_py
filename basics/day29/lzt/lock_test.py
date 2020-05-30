# author:lzt
# date: 2019/12/12 10:50
# file_name: lock_test
# 有100张票 3个窗口同时开卖 每卖出一张 票数-1 直到100张票卖完为止
from threading import Thread
import time
import threading

tickets = 100

# 获取一把锁
lock1 = threading.Lock()


def window1():
    global tickets
    while tickets > 0:
        lock1.acquire()
        # 二次判断：检测数据有没有在等待期间发生变化
        if tickets > 0:
            # 打印票面
            print("window1卖出票号:", tickets)
            # time.sleep(0.02)
            # 票数-1
            tickets -= 1
        lock1.release()


def window2():
    global tickets
    while tickets > 0:
        lock1.acquire()
        if tickets > 0:
            # 打印票面
            print("window2卖出票号:", tickets)
            # time.sleep(0.1)
            # 票数-1
            tickets -= 1
        lock1.release()


def window3():
    global tickets
    while tickets > 0:
        lock1.acquire()
        if tickets > 0:
            # 打印票面
            print("window3卖出票号:", tickets)
            # time.sleep(0.05)
            # 票数-1
            tickets -= 1
        lock1.release()


t1 = Thread(target=window1)
t2 = Thread(target=window2)
t3 = Thread(target=window3)

t1.start()
t2.start()
t3.start()
