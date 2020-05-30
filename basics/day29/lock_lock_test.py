"""
# author Liu shi hao
# date: 2019/12/12 11:57
# file_name: lock_lock_test

"""
import threading
import time

lock1 = threading.Lock()
lock2 = threading.Lock()


def task1():
    if lock1.acquire(timeout=3):
        print("锁一 被任务1锁定")
        print("任务1需要锁二锁定")
        time.sleep(0.1)
        if lock2.acquire(timeout=3):
            print("锁二 被任务1锁定")
            lock2.release()
        lock1.release()


def task2():
    if lock2.acquire(timeout=3):
        print("锁二 被任务2锁定")
        print("任务2需要锁一锁定")
        time.sleep(0.1)
        if lock1.acquire(timeout=3):
            print("锁一 被任务2锁定")
            lock1.release()
        lock2.release()


threading.Thread(target=task1).start()
threading.Thread(target=task2).start()
