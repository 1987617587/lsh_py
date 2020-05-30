# author:lzt
# date: 2019/12/11 16:18
# file_name: process_queue_test
# 进程间的通信

# 进程外独立的队列
import time
from multiprocessing import Queue
from multiprocessing import Process
from multiprocessing import Pool
from multiprocessing import Manager

# q1 = Queue(4)
# q1.put("第一个数据")
# q1.put("第二个数据")
# q1.put("第三个数据")
# q1.put("第四个数据")
# # 阻塞模式放入 当队列满的时候 停止并等待
# # q1.put("第五个数据")
# # 非阻塞模式
# # q1.put("第五个数据",False)
# # q1.put("第五个数据", timeout=3)
# try:
#     q1.put_nowait("第五个数据")
# except:
#     print("队列满了！")
# print(q1.get())
# print(q1.get())
# print(q1.get())
# 非阻塞模式 不等待模式
# print(q1.get(False))
# print(q1.get(timeout=3))
# print(q1.get_nowait())

msg = ["消息" + str(i) for i in range(1, 11)]


# 生产者的任务
def producer(queue: Queue):
    for i in range(10):
        print(f"生产者向队列中放入了数据{msg[i]}")
        queue.put(msg[i])
        time.sleep(0.3)


# 消费者的任务
def consumer(queue: Queue):
    for i in range(10):
        data = queue.get()
        print(f"消费者消费掉数据:{data}")
        time.sleep(0.3)


if __name__ == '__main__':
    # 产生两个进程 一个进程生产 一个进程消费
    # 产生一个通信的队列
    # q1 = Queue()
    # p = Process(target=producer, args=(q1,))
    # c = Process(target=consumer, args=(q1,))
    #
    # p.start()
    # c.start()
    # p.join()
    # c.join()

    # 进程池用的队列是Manager中的队列
    q1 = Manager().Queue()
    pool = Pool(2)
    pool.apply(producer, (q1,))
    pool.apply(consumer, (q1,))

    pool.close()
    pool.join()
    print("消费和生产结束！")
