# author:lzt
# date: 2019/12/13 10:39
# file_name: tcp_thread_test
import socket
from threading import Thread

tcp_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定ip和端口号
tcp_server.bind(("192.168.18.38", 9999))

# 启动监听
# 等待的队列数目
# 最大的服务的客户端:当前程序的进程数+线程数+10
tcp_server.listen(50)

print("服务器准备妥当 可以接受客户端连接！")

users = []


def t_run(user):
    while 1:
        try:
            c_stream = user[0]
            c_addr = user[1]
            data = c_stream.recv(512).decode("utf-8")
            # 收到某客户端发来的消息
            # 将该客户端的消息转发到其他用户
            for client in users:
                if client != user:
                    client[0].send(f"{c_addr}:{data}".encode("utf-8"))
        except:
            print("聊天异常！")
            break
    pass


while 1:
    # 不停的获取客户端的连接
    # client:(stream,c_addr)
    client = tcp_server.accept()

    print(f"{client[1]}上线")
    # 将客户端进行容器的保存
    users.append(client)

    # 开启线程为客户端服务！
    Thread(target=t_run, args=(client,)).start()

