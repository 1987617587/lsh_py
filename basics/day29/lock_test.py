"""
# author Liu shi hao
# date: 2019/12/12 11:13
# file_name: lock_test

"""
import threading
import time

num = 100


def fun1():
    global num
    while num > 0:
        mutex.acquire()
        if num > 0:
            print('窗口一买出票号', num)
            num -= 1
            time.sleep(0.1)
        mutex.release()


def fun2():
    global num
    while num > 0:
        mutex.acquire()
        if num > 0:
            print('窗口二买出票号', num)
            num -= 1
            time.sleep(0.1)
        mutex.release()


def fun3():
    global num
    while num > 0:
        mutex.acquire()
        if num > 0:
            print('窗口三买出票号', num)
            num -= 1
            time.sleep(0.1)
        mutex.release()


mutex = threading.Lock()
t1 = threading.Thread(target=fun1)
t2 = threading.Thread(target=fun2)
t3 = threading.Thread(target=fun3)
t2.start()
t1.start()
t3.start()


