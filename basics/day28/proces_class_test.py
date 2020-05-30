"""
# author Liu shi hao
# date: 2019/12/11 15:26
# file_name: proces_class_test

"""
# 封装类继承Process类并在内部创建run方法
from multiprocessing import Process
import os


class MyProcess(Process):
    _num = 0

    def run(self):
        for i in range(10):
            MyProcess._num += 1
            print(os.getpid(), MyProcess._num)


if __name__ == '__main__':
    p1 = MyProcess()
    p2 = MyProcess()
    p3 = MyProcess()

    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print("finish", MyProcess._num)
