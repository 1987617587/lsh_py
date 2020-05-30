"""
# author Liu shi hao
# date: 2019/12/12 16:32
# file_name: udp_server-test
服务端的UDP发送

"""
import socket
import threading

from day29.udp_user_test import run1


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

            # 回消息
            msg = input("请输入回复用户的消息")
            server_socket.sendto(msg.encode('utf-8'), c_addr)
            if msg == '88':
                break
    except:
        print("服务器异常")
    finally:
        server_socket.close()


threading.Thread(target=run).start()
threading.Thread(target=run1).start()
