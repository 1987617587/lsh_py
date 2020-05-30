"""
# author Liu shi hao
# date: 2019/12/3 16:36
# file_name: bank_test

"""


def atm():
    a = 10
    try:
        print("ATM服务")
        print("选择业务")
        server()
    except ZeroDivisionError as e:
        print("出现异常，本地服务器进行日志记录")
        print(e)
    finally:
        a = 100
        print("是否退出")
        return a


def server():
    try:
        print("进行数据查询")
        print("正在转向总部查询")
        end()
    except ZeroDivisionError as e:
        print("出现异常，中端服务器进行日志记录")
        raise e


def end():
    try:
        print("远端查询中...")
        print(1 / 0)
    except ZeroDivisionError as e:
        print("出现异常，远端服务器进行日志记录")
        raise e


if __name__ == '__main__':
    print(atm())
