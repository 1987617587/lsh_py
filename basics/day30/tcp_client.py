"""
# author Liu shi hao
# date: 2019/12/13 9:48
# file_name: tcp_client

"""
# import socket
#
# tcp_client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# tcp_client.connect(("192.168.18.22",1234))


from socket import *

# data = tcp_client.recv(512)
# print(data.decode('utf-8'))
# tcp_client.close()
while True:
    tcp_client = socket(AF_INET, SOCK_STREAM)
    saddr = ('192.168.18.22',9999)
    tcp_client.connect(saddr)
    senddata = input("输入要发送的数据")
    if senddata.__eq__("exit"):
        tcp_client.close()
        break
    sendbytes = senddata.encode("utf-8")
    tcp_client.send(sendbytes)
    receivebytes = tcp_client.recv(1024)
    receivedata = receivebytes.decode("utf-8")
    print(receivedata)
tcp_client.close()
