"""
# author Liu shi hao
# date: 2019/12/3 17:04
# file_name: exception_class

"""


# 异常是一个类,用户定义的异常一般继承自Exception：
#   '''自定义的异常类'''
class ShortInputException(Exception):
    def __init__(self, length, atleast):
        super().__init__()
        self.length = length
        self.atleast = atleast


def main():
    try:
        s = input('请输入 --> ')
        if len(s) < 3:
            # raise引发一个你定义的异常
            raise ShortInputException(len(s), 3)
    # x这个变量被绑定到了错误的实例
    except ShortInputException as result:
        print(result)
        print('ShortInputException: 输入的长度是{result.length},长度至少应是 {result.atleast}')
    else:
        print('没有异常发生.')


if __name__ == '__main__':
    main()
