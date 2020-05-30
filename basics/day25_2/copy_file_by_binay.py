"""
# author Liu shi hao
# date: 2019/12/7 9:07
# file_name: copy_file_by_binay

"""
# 复制文件(二进制读写)
import os
import time


def copy_file():
    s = time.time()
    with open(r"C:\Users\Administrator\Desktop\作业.txt", "rb") as read:
        with open(r"作业.txt", "wb") as write:
            read_count = 4096
            while 1:
                data = read.read(read_count)
                if not data:
                    break
                write.write(data)

    print(time.time() - s)


copy_file()


def copy_files():
    s = time.time()
    for root, subs, files in os.walk(r"E:\python1911A\day25\bbb", False):
        for file in files:
            file = ("/".join([root, file]))
            with open(file, "rb") as read:
                with open(file, "wb") as write:
                    read_count = 4096
                    while 1:
                        data = read.read(read_count)
                        if not data:
                            break
                        write.write(data)

        print(time.time() - s)
