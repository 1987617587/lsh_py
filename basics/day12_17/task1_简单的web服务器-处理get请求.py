import socket
import threading
import time
import re


class Server:

    def __init__(self, ip='', port=80) -> None:
        self.ser = socket.socket(2, 1)
        self.ser.bind((ip, port))
        self.ser.listen(100)
        print('web服务器 开启！！')
        # 创建线程 处理每一个人的链接
        threading.Thread(target=self.accept).start()

    def accept(self):
        while True:
            client = self.ser.accept()
            print('新兵报道！', client[1])
            # 创建线程 处理请求
            threading.Thread(target=self.recv, args=[client[0]]).start()

    def recv(self, client: socket.socket):
        while True:
            try:
                recvData = client.recv(1024).decode('utf-8')


            except:
                print('%s 下线' % (client.getpeername()))
                break
            else:
                if len(recvData) != 0:
                    print(client.getpeername(), '接受数据为：', recvData.splitlines()[0])
                    temp = recvData.splitlines()[0].split(" ")[1]
                    if '?' in temp:
                        print('请求注册', temp.split("?")[1])
                        # end=re.fullmatch('userName=(.*?)&userPwd=(.*?)',temp.split("?")[1])
                        # end=re.fullmatch('userName=(.*?)&pwd=(.*?)&text1=(.*)',temp.split("?")[1])
                        end = re.fullmatch('userName=(.*?)&pwd=(.*?)', temp.split("?")[1])
                        print("用户名：", end.groups()[0])
                        print("密码：", end.groups()[1])

                    time.sleep(1)
                    client.close()
                    break
                else:
                    client.close()
                    break


# *************************************************************

Server()
