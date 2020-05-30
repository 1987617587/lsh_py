"""
# author Liu shi hao
# date: 2019/12/11 15:43
# file_name: process_pool_test
进程池
"""
import os
import time
from multiprocessing.pool import Pool


# 进程应该完成的任务
def task():
    for i in range(3):
        print(os.getpid(), i)
        time.sleep(0.2)


if __name__ == '__main__':

    pool1 = Pool(3)
    for i in range(15):
        # pool1.apply_async(task)  # 异步
        pool1.apply(task)  # 同步

    pool1.close()
    pool1.join()
    print('finish')
