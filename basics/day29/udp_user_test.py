"""
# author Liu shi hao
# date: 2019/12/12 16:39
# file_name: udp_user_test

"""
import socket


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
    except:
        print("用户端异常")
    finally:
        client_socket.close()
