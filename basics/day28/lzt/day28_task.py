# author:lzt
# date: 2019/12/12 9:24
# file_name: day28_task
# 使用元方法实现以下功能
# 将自定义类中所有属性名以attr结尾
# 新的类名为 New+元类名
import time


def type_method(class_name, t_supers, class_dict):
    print("拦截到一个类的生成！")
    # print(class_name)
    class_name = "New" + class_name
    # class_dict = {k + "_attr": v for k, v in class_dict.items()}
    user_key = []
    for i in class_dict:
        if not str(i).startswith("__"):
            user_key.append(i)
    for i in user_key:
        class_dict[i + "_attr"] = class_dict[i]
        class_dict.pop(i)
    return type(class_name, t_supers, class_dict)


class A(metaclass=type_method):
    count = 0
    age = 0
    count2 = 0

    def __init__(self, name) -> None:
        super().__init__()
        self.name = name


#
# A("测试")
# print(A.__dict__)
# print(A.__name__)
# 1、一个进程负责产生整数，一个进程负责打印偶数，一个进程负责打印奇数
from multiprocessing import Queue
from multiprocessing import Process


# 负责向队列生产整数
def task1(qu: Queue):
    for i in range(100):
        print(f"task1放入数据:{i}")
        qu.put(i)


# 从队列中取得奇数并打印
def task2(qu: Queue):
    # 50-100
    for i in range(100):
        try:
            data = qu.get(timeout=10)
        except:
            print("队列已空 程序结束！")
            break
        if data % 2 == 0:
            # 拿到偶数的话 再次将数据放回队列中
            qu.put(data)
        else:
            print("task2", data)


# 消费偶数
def task3(qu: Queue):
    # 50-100
    for i in range(100):
        try:
            data = qu.get(timeout=10)
        except:
            print("队列已空 程序结束！")
            break
        if data % 2 != 0:
            # 拿到奇数的话 再次将数据放回队列中
            qu.put(data)
        else:
            print("task3", data)


# if __name__ == '__main__':
#     q1 = Queue()
#     p1 = Process(target=task1, args=(q1,))
#     p2 = Process(target=task2, args=(q1,))
#     p3 = Process(target=task3, args=(q1,))
#
#     p1.start()
#     p2.start()
#     p3.start()
#
#     p1.join()
#     p2.join()
#     p3.join()
#     print("任务已结束")

# 2、A进程负责向Q1队列发送数据，且从Q2队列读取数据；B进程负责向Q2队列发送数据，且从Q1队列读取数据
def task2_1(q1: Queue, q2: Queue):
    for i in range(100):
        print("A进程放入数据", i)
        q1.put(i)
        print("A进程取得数据", q2.get())


def task2_2(q1: Queue, q2: Queue):
    for i in range(100):
        print("B进程取得数据", q1.get())
        print("B进程放入数据", i)
        q2.put(i)


# if __name__ == '__main__':
#     q1 = Queue()
#     q2 = Queue()
#     a_p = Process(target=task2_1, args=(q1, q2))
#     b_p = Process(target=task2_2, args=(q1, q2))
#
#     a_p.start()
#     b_p.start()
#
#     a_p.join()
#     b_p.join()
#
#     print("任务结束！")
# 3、A进程负责向Q1队列发送数据【整数】，B进程从Q1队列读取数据，将读出的每个数乘以2放进队列Q2，
# 	C进程从Q2队列读取数据，将取出的数据求平方，再打印出来
# 4、利用进程池和队列编写以下功能:
# 	有队列q，进程a负责每3秒写入 ，进程b负责,每1秒读取
from multiprocessing import Manager


def a_run(q):
    for i in range(10):
        print("a进程放入数据", i)
        q.put(i)
        time.sleep(3)


def b_run(q):
    for i in range(10):
        print("b进程取得数据", q.get())
        time.sleep(1)


# from multiprocessing import Pool
# if __name__ == '__main__':
#     q = Manager().Queue()
#     pool = Pool(2)
#     pool.apply_async(a_run,(q,))
#     pool.apply_async(b_run,(q,))
#
#     # 进程池关闭
#     pool.close()
#     pool.join()
#
#     print("进程池执行完毕！")

# 5、编写多线程程序，A线程每1秒打印一个'A'，B线程每2秒打印一个'B'
def t_run1():
    while 1:
        print("A")
        time.sleep(1)


def t_run2():
    while 1:
        print("B")
        time.sleep(2)


from threading import Thread


# Thread(target=t_run1).start()
# Thread(target=t_run2).start()

# 6、创建两一个线程负责打印偶数，一个线程负责打印奇数
def print_even():
    for i in range(0, 1000, 2):
        print("偶数线程", i)


def print_odd():
    for i in range(1, 1000, 2):
        print("奇数线程", i)


Thread(target=print_even).start()
Thread(target=print_odd).start()
