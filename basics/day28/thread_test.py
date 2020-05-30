"""
# author Liu shi hao
# date: 2019/12/11 17:13
# file_name: thread_test

"""
import threading
from threading import Thread


class MyThread(Thread):
    _times = 10  # 进程独有，线程共享共用

    def run(self) -> None:
        # for i in range(MyThread._times):
        while MyThread._times > 0:
            print(threading.current_thread().name, MyThread._times)
            # print(threading.current_thread().name, i)
            MyThread._times -= 1


mt1 = MyThread(name='自定义类创建的线程1')
mt2 = MyThread(name='自定义类创建的线程2')
mt1.start()
mt2.start()
