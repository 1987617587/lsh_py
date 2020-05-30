"""
# author Liu shi hao
# date: 2019/12/11 14:27
# file_name: process

"""
import os
import time
from multiprocessing import Process


def process_run1():
    for i in range(5):
        print(os.getpid(), i,"第一个")
        time.sleep(1)


def process_run2():
    for j in range(5):
        print(os.getpid(), j,"第二个")
        time.sleep(1)


if __name__ == '__main__':
    my_process1 = Process(target=process_run1)
    my_process2 = Process(target=process_run2)
    my_process1.start()
    my_process2.start()
    # my_process1.join()  # 等待子进程完成再运行主进程
    # my_process2.join()
    print(my_process1.pid)  # 主进程
    print(my_process2.pid)  # 主进程
