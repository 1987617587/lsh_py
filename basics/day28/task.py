"""
# author Liu shi hao
# date: 2019/12/11 20:41
# file_name: task

"""
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
from multiprocessing import Process
from multiprocessing.dummy import Pool
from threading import Thread

Goods = type('A', (object,), {'name': '张三', 'id': '111', 'getinfo': lambda: print("这是类的方法")})
# 使用type创建Goods的子类对象Food 拥有type，getinfo（方法），getname（方法）
Food = type('A', (Goods,),
            {'type': 'class', 'getname': lambda: print(f"{Food.name}") if hasattr(Food, "name") else None})

# 实例化对象g1，f1 查看父子类方法的相互调用
obj1 = Goods()
f1 = Food()
print(obj1.name)
if hasattr(Food, "getinfo"):
    Food.getinfo()
if hasattr(Food, "getname"):
    Food.getname()

# 4，使用元方法实现以下功能
# 将自定义类中所有属性名以attr结尾
# 新的类名为 New+元类名
from typing import Any


def type_function(class_name, tuple_supers, class_dict):
    class_name = "New" + class_name

    new_class_dict = {k + "attr": v for k, v in class_dict.items()}

    return type(class_name, tuple_supers, new_class_dict)


class TypeTest(type):

    def __new__(cls, class_name, tuple_supers, class_dict: dict) -> Any:
        class_name = "New" + class_name

        new_class_dict = {k + "attr": v for k, v in class_dict.items()}

        return super().__new__(cls, class_name, tuple_supers, new_class_dict)


# class Yu(metaclass=TypeTest): # 元类的方式
class Yu(metaclass=type_function):  # 元函数的方式
    abc = 'abc'

    def __init__(self) -> None:
        super().__init__()


n1 = Yu()
print(Yu.__name__)
if hasattr(Yu, "abcattr"):
    print(Yu.abcattr)
print(Yu.__dict__)

# 1、一个进程负责产生整数，一个进程负责打印偶数，一个进程负责打印奇数
# 进程应该完成的任务
i = 0


def task():
    global i
    i += 1

    time.sleep(1)


def pr_j():
    if i % 2 == 1:
        print(os.getpid(), i)


def pr_o():
    if i % 2 == 0:
        print(os.getpid(), i)


if __name__ == '__main__':
    # 创建指定数量的进程的进程池
    pool1 = Pool(3)
    for i in range(3):
        pool1.apply(task)
        pool1.apply(pr_j)
        pool1.apply(pr_o)

    # 进程池安排完毕 需要关闭
    pool1.close()
    pool1.join()
    print("进程池完成所有的任务！")

# 2、A进程负责向Q1队列发送数据，且从Q2队列读取数据；B进程负责向Q2队列发送数据，且从Q1队列读取数据


# 3、A进程负责向Q1队列发送数据【整数】，B进程从Q1队列读取数据，将读出的每个数乘以2放进队列Q2，
# 	C进程从Q2队列读取数据，将取出的数据求平方，再打印出来

# 4、利用进程池和队列编写以下功能:
# 	有队列q，进程a负责每3秒写入 ，进程b负责,每1秒读取

# 5、编写多线程程序，A线程每1秒打印一个'A'，B线程每2秒打印一个'B'

# while 1:
#     t1 = Thread(target=lambda: print("A"))
#     t2 = Thread(target=lambda: print("B"))
#     t1.start()
#     time.sleep(1)
#     t2.start()
#     time.sleep(1)
# 6、创建两一个线程负责打印偶数，一个线程负责打印奇数



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




