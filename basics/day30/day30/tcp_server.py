# author:lzt
# date: 2019/12/13 9:48
# file_name: tcp_server

import socket

# 创建tcp的对应的socket
from multiprocessing import Process


def client_run(socket_stream, c_addr):
    while 1:
        try:
            socket_stream.send("欢迎来到1911的聊天室！".encode("utf-8"))
            msg = socket_stream.recv(512)
            print(c_addr,msg.decode("utf-8"))
        except:
            print("连接已关闭！")
            break
        pass


if __name__ == '__main__':

    tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # 绑定ip和端口号
    tcp_server.bind(("192.168.18.38", 9999))

    # 启动监听
    # 等待的队列数目
    # 最大的服务的客户端:当前程序的进程数+线程数+10
    tcp_server.listen(50)

    print("服务器准备妥当 可以接受客户端连接！")

    while 1:
        # 阻塞等待客户端的连接
        # (连接两端的socket流，客户端的地址)
        socket_stream, c_addr = tcp_server.accept()

        print(f"{c_addr}已连接到服务器！")

        # 可以开启进程或线程为之进行服务！
        client_process = Process(target=client_run, args=(socket_stream, c_addr))
        client_process.start()
        # try:
        #     socket_stream.send("欢迎来到1911的聊天室！".encode("utf-8"))
        #     msg = socket_stream.recv(512)
        #     print(msg.decode("utf-8"))
        # except:
        #     print("客户端异常！")
