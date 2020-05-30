import socket
import threading
import time
import re

from day12_17 import login


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
            print('新兵报道！', client[1])
            # 创建线程 处理请求
            threading.Thread(target=self.recv, args=[client[0]]).start()

    def recv(self, client: socket.socket):
        reshtml = """<!DOCTYPE html>
                        <html>
                            <head>
                                <meta charset="utf-8">
                                <title></title>
                            </head>
                            <body>
                            {}
                            </body>
                        </html> """
        while True:
            try:
                recvData = client.recv(1024).decode('utf-8')


            except:
                print('%s 下线' % (client.getpeername()))
                break
            else:
                if len(recvData) != 0:
                    print(client.getpeername(), '接受数据为：', recvData)
                    temp = recvData.splitlines()[-1]
                    print('post 请求的数据：', temp)
                    # print("注册"())
                    if "hidden1=" in temp:
                        print('请求注册')
                        # end = re.fullmatch('userName=(.*?)&pwd=(.*?)&text1=(.*)', temp)
                        end = re.fullmatch('userName=(.{6,18}?)&pwd=(.{6,18}?)&text1=(.*)', temp)
                        # print("注册信息：",end.groups())
                        if end is not None:
                            username = end.groups()[0]
                            userpwd = end.groups()[1]

                            if not login.query_by_name(username):
                                login.write_json(username, userpwd)
                                print("注册成功！")
                                client.send(reshtml.format("注册成功！").encode('utf-8'))
                                print("用户名：", username)
                                print("密码：", userpwd)
                            else:
                                print("用户名已存在！")
                                client.send(reshtml.format("用户名已存在！").encode('utf-8'))
                        else:
                            print("格式有误！")
                            client.send(reshtml.format("格式有误！").encode('utf-8'))
                    else:
                        print('请求登录')
                        end = re.fullmatch('user_name=(.*?)&user_pwd=(.*?)', temp)
                        user_name = end.groups()[0]
                        user_pwd = end.groups()[1]
                        if login.query_by_name_pwd(user_name, user_pwd) is not None:
                            print("用户名：", user_name)
                            print("密码：", user_pwd)
                            print("登录成功！")
                            client.send(reshtml.format("登录成功！").encode('utf-8'))
                        else:
                            print("登录失败！")
                            client.send(reshtml.format("登录失败！").encode('utf-8'))

                    time.sleep(1)
                    client.close()
                    break
                else:
                    client.close()
                    break


# *************************************************************

Server()
