# author:lzt
# date: 2019/12/12 16:31
# file_name: udp_server
# 服务器端的UDP发送


# socket
import socket,time

# 创建一个用于接收和发送的服务端的socket
import threading


server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# 绑定一个ip和端口号 必须为元组
# 端口号的最大值:65535
server_addr = ("192.168.18.22", 8888)
server_socket.bind(server_addr)
c_addr = ("192.168.18.9", 8989)


def send():
    while 1:
        # 手动输入消息进行回复
        msg = input("请输入回传的消息:")
        server_socket.sendto(msg.encode("utf-8"), c_addr)
        if msg == "88":
            return


def get():
    while 1:
        # 收数据
        data, c_addr = server_socket.recvfrom(512)
        # 解码显示收到的数据
        print(f"收到{c_addr}发来的信息:{data.decode('utf-8')}")
        with open("user_write_test2.date", "a", encoding="utf-8") as io:
            io.write(f"收到{c_addr}发来的消息：{data.decode(encoding='utf-8')},时间{time.ctime()}")
            io.write("\n")
        if data.decode(encoding='utf-8') == "88":
            return



try:

    # 接收服务端传回的数据
    ser_msg, s_addr = server_socket.recvfrom(512)
    print(f"收到{s_addr}发来的信息:{ser_msg.decode('utf-8')}")
    with open("user_write_test2.date", "a", encoding="utf-8") as io:
        io.write(f"收到{c_addr}发来的消息：{ser_msg.decode(encoding='utf-8')},时间{time.ctime()}")
        io.write("\n")
    if ser_msg.decode(encoding='utf-8') != "88":
        threading.Thread(target=send).start()
        threading.Thread(target=get).start()

except:
    print("服务器异常！")

