"""
# author Liu shi hao
# date: 2019/12/13 8:46
# file_name: say_online2

"""
# author:lzt
# date: 2019/12/12 16:31
# file_name: udp_client
# UDP的客户端

import socket

# 创建一个用于发送数据的socket
import threading, time

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client_socket.bind(("127.0.0.1", 8888))
# # 直接发送数据
# # 发送的地址
#
# server_addr = ("127.0.0.1", 6666)
try:
    print("提示：您可 win+r 输入命令行‘ipconfig’查询ip")
    client_addr_ip = input("请输入您的ip:")
    print("提示：您可 自定义端口号（0-65535）")
    client_addr_o = input("请输入您的端口号:")
    name = input("请设定一个用于聊天的昵称：")
    client_addr = (client_addr_ip, int(client_addr_o))
    client_socket.bind(client_addr)
    server_addr_ip = input("请输入对方的ip:")
    server_addr_o = input("请输入对方的端口号:")
    server_addr = (server_addr_ip, int(server_addr_o))


    def send():
        while 1:
            # 将需要发送的数据发送出去
            msg = input("请输入要发送的数据:")
            # sendto
            client_socket.sendto(msg.encode("utf-8"), server_addr)
            if msg == "88":
                break
        return


    def get():
        while 1:
            # 接收服务端传回的数据
            ser_msg, s_addr = client_socket.recvfrom(512)
            print(f"收到{s_addr}发来的信息:{ser_msg.decode('utf-8')}")
            with open("user_write_test2.date", "a", encoding="utf-8") as io:
                io.write(f"收到{s_addr}发来的消息：{ser_msg.decode(encoding='utf-8')},时间{time.ctime()}")
                io.write("\n")
            if ser_msg.decode(encoding='utf-8') == "88":
                return False


    try:
        # 手动输入消息进行回复
        msg = input("请输入发送的消息:")
        client_socket.sendto(msg.encode("utf-8"), server_addr)
        if msg != '88':
            threading.Thread(target=send).start()
            threading.Thread(target=get).start()
    except:
        print("客户端异常")
except:
    print("出现故障！")
