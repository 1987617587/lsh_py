# author:lzt
# date: 2019/12/12 14:29
# file_name: threadlocal_test
# 让每个线程和进程一样 独享某些资源
import threading
from threading import Thread

local1 = threading.local()


# 线程1做的事
def db_con1():
    print("开启数据连接！")
    local1.db_con = "mysql连接"
    local1.username = "admin"
    query1()


# 线程1中的子函数
def query1():
    print("使用数据库连接进行查询")
    print(local1.db_con)
    print("当前用户", local1.username)


# 线程2做的事
def query2():
    print("开始查询：")
    if hasattr(local1, "db_con"):
        print(local1.db_con)
    else:
        print("该线程未连接数据库！")


Thread(target=db_con1).start()

Thread(target=query2).start()
