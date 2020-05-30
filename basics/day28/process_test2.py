"""
# author Liu shi hao
# date: 2019/12/11 14:51
# file_name: process_test2

"""
import os
import time
from multiprocessing import Process


def say(msg, **kwargs):
    count = kwargs.get("count")
    for i in range(count):
        print(f"{os.getpid()} 传入的消息{msg} 其他信息{kwargs}")
        time.sleep(0.1)


if __name__ == '__main__':
    p1 = Process(target=say, name="进程1", args=("你好",), kwargs={'count': 10})
    p2 = Process(target=say, name="进程2", args=("我不好",), kwargs={'count': 10})
    p1.start()
    p2.start()
    print(p1.is_alive())
    print(p2.is_alive())
    # p1.join()
    # p2.join()  # 括号内可以加主进程等待时间
    p2.terminate()
    p1.terminate()
    print(p1.is_alive())
    print(p2.is_alive())
    print(p1.name, p2.name, "子进程结束了")
