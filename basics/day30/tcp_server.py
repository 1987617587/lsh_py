"""
# author Liu shi hao
# date: 2019/12/13 9:49
# file_name: tcp_server

"""
# import socket
#
# tcp_server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# tcp_server.bind(("192.168.18.22",1234))
#
#
# tcp_server.listen(10)
# print("服务器准备完毕，可以接收连接！")
# while 1:
#     socket_stream,c_addr = tcp_server.accept()
#     print(f"{c_addr}已连接服务器")
#     socket_stream.send("欢迎来到1911聊天室！".encode(encoding='utf-8'))
#

from multiprocessing import Process
from socket import *


def readprocess(cs, caddr):
    while True:
        receivebytes = cs.recv(1024)
        receivedata = receivebytes.decode("utf-8")
        print("收到%s from %s %d" % (receivedata, caddr[0], caddr[1]))


if __name__ == "__main__":
    ss = socket(AF_INET, SOCK_STREAM)
    saddr = ('127.0.0.1', 8989)
    ss.bind(saddr)
    ss.listen(50)
    while True:
        cs, caddr = ss.accept()
        readp = Process(target=readprocess, args=(cs, caddr))
        readp.start()
