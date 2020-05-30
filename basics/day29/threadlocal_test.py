"""
# author Liu shi hao
# date: 2019/12/12 14:37
# file_name: threadlocal_test

"""
import threading

local1 = threading.local()


def db_con1():
    print("开启数据连接")
    local1.db_con = "Mysql连接"
    query1()


def query1():
    print("使用数据库连接进行查询")
    print(local1.db_con)


def query2():
    print("另一个地方开始查询")
    if hasattr(local1, "db_con"):
        print(local1.db_con)
    else:
        print("该线程暂无数据库连接")


threading.Thread(target=db_con1).start()
threading.Thread(target=query2).start()
