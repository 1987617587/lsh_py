"""
# author Liu shi hao
# date: 2019/12/3 15:45
# file_name: exception_test

"""


def create_except():
    print(1 / 0)
    print(int("asd"))
    print(a)


def call_except():
    create_except()


if __name__ == '__main__':
    try:
        call_except()
    except ZeroDivisionError:
        print("出现异常：0不能被除")
    except ValueError:
        print("出现异常：数字才能转换")
    except NameError:
        print("出现异常：名字未定义")
    print("执行了")
