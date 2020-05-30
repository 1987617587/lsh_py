"""
# author Liu shi hao
# date: 2019/12/12 17:34
# file_name: udp_task

"""

import socket
import threading
from multiprocessing import Queue

q1 = Queue()
q2 = Queue()
# 创建一个用于接收和发送的服务端的socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定一个ip和端口号 必须是元组
# 端口号最大值65535
server_addr = ('127.0.0.1', 8888)
server_socket.bind(server_addr)

# data, c_addr = server_socket.recvfrom(512)
# print(f"收到{c_addr}发来的消息：{data.decode(encoding='utf-8')}")
# q1.put(data.decode(encoding='utf-8'))
# msg = input("请输入要发给服务端的信息：")
#
# # sendto
# server_socket.sendto(msg.encode(encoding='utf-8'), ('127.0.0.1', 8988))


def get():
    while 1:
        data, c_addr = server_socket.recvfrom(512)
        print(f"收到{q1.get()}发来的消息：{data.decode(encoding='utf-8')}")


def send():
    while 1:
        data, c_addr = server_socket.recvfrom(512)
        msg = input("请输入发给用户的消息")
        server_socket.sendto(msg.encode('utf-8'), c_addr)


try:
    data, c_addr = server_socket.recvfrom(512)
    print(f"收到{q1.get()}发来的消息：{data.decode(encoding='utf-8')}")
    threading.Thread(target=send).start()
    threading.Thread(target=get).start()


except:
    print("服务器异常")
finally:
    server_socket.close()
