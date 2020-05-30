# author:lzt
# date: 2019/12/13 9:57
# file_name: tcp_client
import socket

# 创建tcp的对应的socket
from threading import Thread

tcp_clinet = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_clinet.connect(("192.168.18.38",9999))


def c_run():
    while 1:
        data = tcp_clinet.recv(512)
        print(data.decode("utf-8"))
    pass


Thread(target=c_run).start()


def c_s_run():
    while 1:
        msg = input("输入消息：")
        tcp_clinet.send(msg.encode("utf-8"))
    pass


Thread(target=c_s_run).start()



# tcp_clinet.close()
