"""
# author Liu shi hao
# date: 2019/12/11 17:53
# file_name: day28_task

"""
import threading
from threading import Thread

# 3，使用type创建对象Goods拥有id，name，getinfo（方法）三个属性
import os
import time
from multiprocessing import Process, Manager, Queue
from multiprocessing.dummy import Pool
from threading import Thread

Goods = type('A', (object,), {'name': '张三', 'id': '111', 'getinfo': lambda: print("这是类的方法")})
# 使用type创建Goods的子类对象Food 拥有type，getinfo（方法），getname（方法）
Food = type('A', (Goods,),
            {'type': 'class', 'getname': lambda: print(f"{Food.name}") if hasattr(Food, "name") else None})

# 实例化对象g1，f1 查看父子类方法的相互调用
# obj1 = Goods()
# f1 = Food()
# print(obj1.name)
# if hasattr(Food, "getinfo"):
#     Food.getinfo()
# if hasattr(Food, "getname"):
#     Food.getname()

# 4，使用元方法实现以下功能
# 将自定义类中所有属性名以attr结尾
# 新的类名为 New+元类名
from typing import Any


def type_function(class_name, tuple_supers, class_dict):
    class_name = "New" + class_name
    class_dict = {k + "attr": v for k, v in class_dict.items()}
    return type(class_name, tuple_supers, class_dict)


# class TypeTest(type):
#
#     def __new__(cls, class_name, tuple_supers, class_dict: dict) -> Any:
#         class_name = "New" + class_name
#         new_class_dict = {k + "attr": v for k, v in class_dict.items()}
#         return super().__new__(cls, class_name, tuple_supers, new_class_dict)


# class Yu(metaclass=TypeTest): # 元类的方式
class Yu(metaclass=type_function):  # 元函数的方式
    abc = 'abc'

    def __init__(self) -> None:
        super().__init__()


# n1 = Yu()
# print(Yu.__name__)
# if hasattr(Yu, "abcattr"):
#     print(Yu.abcattr)
# print(Yu.__dict__)


# 1、一个进程负责产生整数，一个进程负责打印偶数，一个进程负责打印奇数
# 进程应该完成的任务


# 进程的执行体
# 基数越大越不稳定
def run(q1: Queue):
    for i in range(10):
        print(f"1进程向Q1队列中产生整数{i}")
        q1.put(i)


def run1(q1: Queue):
    for i in range(10):
        if i % 2 == 0:
            data = q1.get()
            print(f"2进程向Q1队列中取出偶数{data}")


def run2(q1: Queue):
    for i in range(10):
        if i % 2 != 0:
            data = q1.get()
            print(f"3进程向Q1队列中取出奇数{data}")


# if __name__ == '__main__':
#     # 用自定义的类来创建子进程
#     q1 = Manager().Queue()
#     pool = Pool(3)
#     pool.apply_async(run, (q1,))
#     pool.apply_async(run1, (q1,))
#     pool.apply_async(run2, (q1,))
#     pool.close()
#     pool.join()


# 2、A进程负责向Q1队列发送数据，且从Q2队列读取数据；B进程负责向Q2队列发送数据，且从Q1队列读取数据
def A_2(q1: Queue, q2: Queue):
    for i in range(10):
        print(f"A进程向Q1队列中放入了数据{i}")
        q1.put(i)
        data1 = q2.get()
        print(f"A进程从Q2队列读取数据:{data1}")


def B_2(q1: Queue, q2: Queue):
    for i in range(10):
        q2.put(i)
        print(f"A进程从Q2队列放入了数据:{i}")
        data1 = q1.get()
        print(f"B进程从Q1队列读取数据:{data1}")


# if __name__ == '__main__':
#     q1 = Manager().Queue()
#     q2 = Manager().Queue()
#     pool = Pool(2)
#     pool.apply_async(A_2, (q1, q2))
#     pool.apply_async(B_2, (q1, q2))
#
#     pool.close()
#     pool.join()
#     print("消费和生产结束！")


# 3、A进程负责向Q1队列发送数据【整数】，B进程从Q1队列读取数据，将读出的每个数乘以2放进队列Q2，
# 	C进程从Q2队列读取数据，将取出的数据求平方，再打印出来
def A(q1: Queue):
    for i in range(10):
        print(f"A进程向Q1队列中放入了数据{i}")
        q1.put(i)


def B(q1: Queue, q2: Queue):
    for i in range(10):
        data1 = q1.get()
        print(f"B进程从Q1队列读取数据:{data1}")
        q2.put(data1 * 2)
        print(f"B进程向Q2队列中放入了数据{data1 * 2}")


def C(q2: Queue):
    for i in range(10):
        data1 = q2.get()
        print(f"C进程从Q2队列读取数据:{data1}")
        print(f"C进程从Q2队列读取数据求平方得:{data1 ** 2}")


# if __name__ == '__main__':
#     q1 = Manager().Queue()
#     q2 = Manager().Queue()
#     q3 = Manager().Queue()
#     pool = Pool(3)
#     pool.apply_async(A, (q1,))
#     pool.apply_async(B, (q1, q2))
#     pool.apply_async(C, (q1,))
#
#     pool.close()
#     pool.join()
#     print("消费和生产结束！")
# 4、利用进程池和队列编写以下功能:
# 	有队列q，进程a负责每3秒写入 ，进程b负责,每1秒读取
msg = ["消息" + str(i) for i in range(1, 11)]


# 生产者的任务
def producer(queue: Queue):
    for i in range(10):
        print(f"生产者向队列中放入了数据{msg[i]}")
        queue.put(msg[i])
        time.sleep(3)


# 消费者的任务
def consumer(queue: Queue):
    for i in range(10):
        data = queue.get()
        print(f"消费者消费掉数据:{data}")
        time.sleep(1)


# if __name__ == '__main__':
#     # 产生两个进程 一个进程生产 一个进程消费
#     # 产生一个通信的队列
#
#     # 进程池用的队列是Manager中的队列
#     q1 = Manager().Queue()
#     pool = Pool(2)
#     # pool.apply(producer, (q1,))
#     # pool.apply(consumer, (q1,))
#     pool.apply_async(producer, (q1,))
#     pool.apply_async(consumer, (q1,))
#
#     pool.close()
#     pool.join()
#     print("消费和生产结束！")


# 5、编写多线程程序，A线程每1秒打印一个'A'，B线程每2秒打印一个'B'
def prA():
    while 1:
        time.sleep(1)
        print(threading.current_thread().name, 'A')


def prB():
    while 1:
        time.sleep(2)
        print(threading.current_thread().name, 'B')


t3 = Thread(name="自定义线程的prA")
t4 = Thread(name="自定义线程的prB")
t3.run = prA
t4.run = prB


# t3.start()
# t4.start()


# 6、创建两一个线程负责打印偶数，一个线程负责打印奇数


def thread_run(times: int):
    for i in range(0, times, 2):
        print(threading.current_thread().name, i)


def run6(times: int):
    for i in range(1, times, 2):
        print(threading.current_thread().name, i)

# t1 = Thread(target=run6, name="自定义的线程1打印奇数", args=(10,))
# t1.start()
# t2 = Thread(target=thread_run, name="自定义的线程2打印偶数", args=(10,))
# t2.start()
