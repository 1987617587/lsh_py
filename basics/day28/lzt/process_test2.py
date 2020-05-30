# author:lzt
# date: 2019/12/11 14:43
# file_name: process_test2
# 了解Process的参数
import time
from multiprocessing import Process
import os


# 进程主体带参
def say(msg, msg2, **kwargs):
    count = kwargs.get("count")
    print(msg2)
    for i in range(count):
        print(f"{os.getpid()} 传入的消息:{msg} 其他参数:{kwargs}")
        time.sleep(0.1)


if __name__ == '__main__':
    p1 = Process(target=say, name="进程1", args=("你好", "请回答"), kwargs={"count": 3})
    # 多进程使用同一块代码块作为进程主体
    # 进程间相互独立 互不影响
    p2 = Process(target=say, name="进程2", args=("我不好", "88"), kwargs={"count": 3})
    p3 = Process(target=say, args=("我不好", "死去"), kwargs={"count": 3})
    p1.start()
    p2.start()
    # print(p1.is_alive())
    # print(p2.is_alive())
    # p1.join()
    # p2.join()
    # time.sleep(0.1)
    # p1.terminate()
    # p2.terminate()
    print(p1.name, p2.name, p3.name, "结束了")
    # print(p1.is_alive())
    # print(p2.is_alive())
