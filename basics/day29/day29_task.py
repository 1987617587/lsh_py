"""
# author Liu shi hao
# date: 2019/12/12 14:53
# file_name: day29_task

"""
# 7、使用线程互斥锁控制多个线程顺序执行：
# 	A线程负责打印0~99
# 	B线程负责打印100~199
# 	C线程负责打印200~299
import threading
import time

lock1 = threading.Lock()


def task1():
    time.sleep(0.1)
    if lock1.acquire(timeout=3):
        for i in range(100):
            print("A线程打印", i)
        lock1.release()


def task2():
    time.sleep(0.1)
    if lock1.acquire(timeout=3):
        for i in range(100, 200):
            print("B线程打印", i)
        lock1.release()


def task3():
    time.sleep(0.1)
    if lock1.acquire(timeout=3):
        for i in range(200, 300):
            print("C线程打印", i)
        lock1.release()


# threading.Thread(target=task1).start()
# threading.Thread(target=task2).start()
# threading.Thread(target=task3).start()

# 8、A、B两个线程，A打印100个数后换为B打印100个数，B打印100个后换A继续打印，如此往复

local1 = threading.local()
local2 = threading.local()


def taska():
    local1.num = 0
    while local1.num < 5:
        time.sleep(1)
        if lock1.acquire(timeout=3):
            for i in range(local1.num * 100, (local1.num + 1) * 100):
                print("A线程打印", i)
            lock1.release()
            local1.num += 1


def taskb():
    local2.num = 0
    while local2.num < 5:
        time.sleep(1)
        if lock1.acquire(timeout=3):
            for i in range(local2.num * 100, (local2.num + 1) * 100):
                print("B线程打印", i)
            lock1.release()
            local2.num += 1


# threading.Thread(target=taska).start()
# threading.Thread(target=taskb).start()


# 1、使用UDP协议实现，A用户给B用户发送消息，B用户负责将A发送的消息放到文本日志里
import socket
import threading


def run():
    # 创建一个用于接收和发送的服务端的socket
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # 绑定一个ip和端口号 必须是元组
    # 端口号最大值65535
    server_addr = ('127.0.0.1', 8888)
    server_socket.bind(server_addr)
    try:
        while 1:
            # 先收后发
            # 收数据
            data, c_addr = server_socket.recvfrom(512)
            print(f"收到{c_addr}发来的消息：{data.decode(encoding='utf-8')}")
            with open("user_write_test2.date", "a", encoding="utf-8") as io:
                io.write(f"收到{c_addr}发来的消息：{data.decode(encoding='utf-8')},时间{time.ctime()}")
                io.write("\n")

            # 回消息
            msg = input("请输入回复用户的消息")
            server_socket.sendto(msg.encode('utf-8'), c_addr)
            if msg == '88':
                break
    except:
        print("服务器异常")
    finally:
        server_socket.close()


def run1():
    # 创建一个用于接收和发送的用户端的socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # 发送的地址
    server_addr = ('127.0.0.1', 8888)
    # 发数据
    # msg = input("请输入要发送的数据：")
    try:
        while 1:
            msg = input("请输入要发给服务端的信息：")

            # sendto
            client_socket.sendto(msg.encode(encoding='utf-8'), server_addr)
            if msg == '88':
                break

            # # 接收服务端传回的数据
            ser_msg, s_addr = client_socket.recvfrom(512)
            print(f"收到{s_addr}发来的信息：{ser_msg.decode(encoding='utf-8')}")
            with open("user_write_test2.date", "a", encoding="utf-8") as io:
                io.write(f"收到{s_addr}发来的消息：{ser_msg.decode(encoding='utf-8')},时间{time.ctime()}")
                io.write("\n")
    except:
        print("用户端异常")
    finally:
        client_socket.close()


threading.Thread(target=run).start()
threading.Thread(target=run1).start()
