"""
# author Liu shi hao
# date: 2019/12/12 17:52
# file_name: udp_task2

"""

import socket
import threading
from multiprocessing import Queue
from multiprocessing.dummy import Pool

from day29.udp_user_test import run1

q1 = Queue()
# 创建一个用于接收和发送的服务端的socket
user_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定一个ip和端口号 必须是元组
# 端口号最大值65535
user_addr = ('127.0.0.1', 8988)
user_socket.bind(user_addr)

# # 收数据
# msg = input("请输入要发给服务端的信息：")
# # sendto
# user_socket.sendto(msg.encode(encoding='utf-8'), ('127.0.0.1', 8888))
# data, c_addr = user_socket.recvfrom(512)
# print(f"收到{c_addr}发来的消息：{data.decode(encoding='utf-8')}")
# q1.put(data.decode(encoding='utf-8'))


def get():
    while 1:
        data, c_addr = user_socket.recvfrom(512)
        print(f"收到{q1.get()}发来的消息：{data.decode(encoding='utf-8')}")


def send():
    while 1:
        # data, c_addr = user_socket.recvfrom(512)
        msg = input("请输入发给服务器的消息")
        user_socket.sendto(msg.encode('utf-8'), ('127.0.0.1', 8888))


try:
    msg = input("请输入发给服务器的消息")
    user_socket.sendto(msg.encode('utf-8'), ('127.0.0.1', 8888))
    threading.Thread(target=send).start()
    threading.Thread(target=get).start()


except:
    print("用户端异常")
finally:
    user_socket.close()
