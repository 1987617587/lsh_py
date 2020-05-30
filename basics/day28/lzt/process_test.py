# author:lzt
# date: 2019/12/11 14:16
# file_name: process_test
# 进程的创建:
# 1.手动运行一个程序
# 2.使用Process类创建对象 这个对象就是一个进程
# 3.使用类继承Process来完成进程的创建
# 4.使用进程池来创建进程
import os

# 获取当前进程的id的
# print(os.getpid())
# input()

# 创建子进程
# 请在顶级模块的判断中创建
# 导入模块
import time
from multiprocessing import Process


# 进程的活动函数
# 进程体
def process_run1():
    for i in range(5):
        print(os.getpid(), i)
        time.sleep(1)


def process_run2():
    for i in range(5):
        print(os.getpid(), i)
        time.sleep(1)


if __name__ == '__main__':
    # 新创建进程对象
    my_process1 = Process(target=process_run1)
    my_process2 = Process(target=process_run2)
    # 启动进程对象
    my_process1.start()
    my_process2.start()
    # 请主进程等待子进程完成后再继续！
    my_process1.join()
    my_process2.join()
    # 主进程
    print(my_process1.pid)
    print(my_process2.pid)
