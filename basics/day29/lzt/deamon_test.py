# author:lzt
# date: 2019/12/12 14:14
# file_name: deamon_test
# 守护线程 幽灵线程

# 为守护用户线程而生的线程
# 若用户线程未结束 守护线程会一直运行
# 若所有的用户线程全部结束了 守护线程持续一段时间后自动结束
import time
from threading import Thread


def deamon_run():
    while 1:
        print("-----------work---------------")
        time.sleep(0.1)


def user_run():
    for i in range(100):
        print(i)
        time.sleep(0.1)


deamon_t = Thread(target=deamon_run)
# 设定线程为守护线程
# 可以节约服务器资源
deamon_t.setDaemon(True)
# 启动守护线程
deamon_t.start()

# 启动用户线程
Thread(target=user_run).start()
