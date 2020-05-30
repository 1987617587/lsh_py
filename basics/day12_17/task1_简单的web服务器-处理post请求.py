import random
import socket
import threading
import time
import re


class Server:

    def __init__(self, ip='', port=80) -> None:
        self.ser = socket.socket(2, 1)
        self.ser.bind((ip, port))
        self.ser.listen(100)
        # self.pid_get = random.randint(11111,55555)
        print('web服务器 开启！！')
        # 创建线程 处理每一个人的链接
        threading.Thread(target=self.accept).start()

    def accept(self):
        while True:
            client = self.ser.accept()
            print('用户上线！', client[1])
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
                if len(recvData)!=0:
                    print(client.getpeername(), '接受数据为：', recvData)
                    temp = recvData.splitlines()[-1]
                    print('post 请求的数据：',temp)

                    print('请求注册')
                    # end=re.fullmatch('userName=(.*?)&userPwd=(.*?)',temp)
                    # end=re.fullmatch('text1=(.*?)&text2=(.*?)',temp)
                    end = re.fullmatch('userName=(.*?)&pwd=(.*?)&text1=(.*)', temp)

                    print("用户名：", end.groups()[0])
                    print("密码：", end.groups()[1])

                    print(end.groups())

                    time.sleep(1)
                    client.close()
                    break
                else:
                    client.close()
                    break


# *************************************************************

Server()
