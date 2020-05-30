# author:lzt
# date: 2019/12/11 17:12
# file_name: thread_test
# 线程的创建方式:
# 1.每个进程默认自带一个主线程！！！

import threading
# 系统定义的创建线程的类
from threading import Thread


# print(threading.current_thread())


# 2.使用Thread类完成线程的自定义创建
def thread_run(times: int):
    for i in range(times):
        print(threading.current_thread().name, i)


def run():
    for i in range(10):
        print(i)


t1 = Thread(target=lambda: print("线程运行了"))
t1.start()
t2 = Thread(target=thread_run, name="自定义的线程2", args=(10,))
t2.start()

# 3.使用Thread对象指定run来完成线程的创建:只能指定无参的run
t3 = Thread(name="自定义线程的run")
t3.run = run
t3.start()


# 4.使用自定义的类完成线程的创建
class MyThread(Thread):
    _times = 10

    def run(self) -> None:
        # for i in range(MyThread._times):
        while MyThread._times > 0:
            print(threading.current_thread().name, MyThread._times)
            MyThread._times -= 1


# mt1 = MyThread(name="自定义类创建的线程1")
# mt1.start()
# mt2 = MyThread(name="自定义类创建的线程2")
# mt2.start()
