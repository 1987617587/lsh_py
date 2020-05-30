# author:lzt
# date: 2019/12/11 15:26
# file_name: process_class_test
# 用自定义的类来完成进程的创建:

# 自定义的类继承自Process
import os
import time
from multiprocessing import Process


class MyProcess(Process):
    _num = 0

    # 进程的执行体
    def run(self) -> None:
        for i in range(10):
            MyProcess._num += 1
            print(os.getpid(), MyProcess._num)
            time.sleep(1)



if __name__ == '__main__':
    # 用自定义的类来创建子进程
    p1 = MyProcess()
    p2 = MyProcess()
    p3 = MyProcess()
    p1.start()
    p2.start()
    p3.start()
    p1.join()
    p2.join()
    p3.join()
    print(MyProcess._num)
