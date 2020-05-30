# author:lzt
# date: 2019/12/7 9:06
# file_name: copy_file_by_binary

# 复制文件:要求二进制读写
# 读写同时发生
# with能否嵌套
import time

s = time.time()
with open(r"D:\2019随堂\1911A\20191206\14.os.path获取文件属性.mp4", "rb") as read:
    with open(r"aaa\1.mp4", "wb") as write:
        read_count = 4096
        while 1:
            data = read.read(read_count)
            if not data:
                break
            write.write(data)
print(time.time() - s)
