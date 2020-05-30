"""
# author Liu shi hao
# date: 2019/12/12 14:20
# file_name: deamon_test
守护线程，幽灵线程
"""
import time
from threading import Thread


def deamon_run():
    while True:
        print("----work-----")


def user_run():
    for i in range(100):
        print(i)
        time.sleep(0.1)


deamon_t = Thread(target=deamon_run)

deamon_t.setDaemon(True)
Thread(target=user_run).start()
deamon_t.start()

