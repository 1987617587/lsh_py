"""
# author Liu shi hao
# date: 2019/12/11 16:18
# file_name: process_queue_test

"""
import queue
import time
from multiprocessing import Queue, Process, Manager
from multiprocessing.dummy import Pool

q1 = Queue(2)
q1.put('第一个数据')
q1.put('第二个数据')
# 阻塞模式放入 当队列满的时候 停止等待
# q1.put('第三个数据')
# 非阻塞模式
# print(q1.put('第三个数据', False))
# print(q1.put('第三个数据', timeout=3))
try:
    q1.put_nowait('第三个数据')
except queue.Full:
    print("队列满了")
print(q1.get())
print(q1.get())


# print(q1.get())
# # 非阻塞模式（不等待模式）
# print(q1.get(False))
# print(q1.get(timeout=3))
# print(q1.get_nowait())

def producer(queue: Queue):
    for i in range(10):
        print(f"生产者放入数据{i}")
        queue.put(i)
        time.sleep(0.3)


def consumer(q1: Queue):
    for i in range(10):
        date = q1.get()
        print(f"消费者消费掉数据{date}")
        time.sleep(0.3)


if __name__ == '__main__':
    # queue = Queue
    # p = Process(target=producer, args=(queue,))
    # c = Process(target=consumer, args=(queue,))
    # c.start()
    # p.start()
    # c.join()
    # p.join()
    # print("finish")

    # 进程池(用的队列必须是Manager中的队列)
    queue = Manager().Queue()
    pool1 = Pool(2)

    pool1.apply_async(producer, (queue,))  # 异步
    pool1.apply_async(consumer, (queue,))  # 异步
    # pool1.apply(producer,(queue,))  # 同步
    # pool1.apply(consumer,(queue,))  # 同步

    pool1.close()
    pool1.join()
    print('finish')
