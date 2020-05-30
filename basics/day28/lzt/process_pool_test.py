# author:lzt
# date: 2019/12/11 15:43
# file_name: process_poll_test

# 用进程池完成进程要完成的任务
import os
import time
from multiprocessing import Pool


# 进程应该完成的任务
def task():
    for i in range(3):
        print(os.getpid(), i)
        time.sleep(1)


if __name__ == '__main__':
    # 创建指定数量的进程的进程池
    pool1 = Pool(3)
    # 追加任务到进程池
    for i in range(15):
        # 异步执行进程池中的进程
        # pool1.apply_async(task)
        # 同步执行进程池中的进程（互相等待对方完成)
        pool1.apply(task)

    # 进程池安排完毕 需要关闭
    pool1.close()
    pool1.join()
    print("进程池完成所有的任务！")
