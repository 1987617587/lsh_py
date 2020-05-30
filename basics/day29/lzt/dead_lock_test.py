# author:lzt
# date: 2019/12/12 11:44
# file_name: dead_lock_test
import threading
import time
from threading import Thread

# 两把锁
lock1 = threading.Lock()
lock2 = threading.Lock()


def task1():
    # 先锁定lock1
    if lock1.acquire(timeout=3):
        print("锁一被任务1锁定！")
        print("需求第二把锁")
        time.sleep(0.1)
        if lock2.acquire(timeout=3):
            print("锁二被任务一锁定")
            lock2.release()
        lock1.release()


def task2():
    # 先锁定lock1
    if lock2.acquire(timeout=3):
        print("锁二被任务二锁定！")
        print("需求第一把锁")
        time.sleep(0.1)
        if lock1.acquire(timeout=3):
            print("锁一被任务二锁定")
            lock1.release()
        lock2.release()


Thread(target=task1).start()
Thread(target=task2).start()
