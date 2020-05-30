"""
# author Liu shi hao
# date: 2019/12/6 15:17
# file_name: os_path_test

"""
import datetime
import os

# os.path有四大职责：
# 1.格式化文件或目录路径
import time

print(os.path.abspath("aaa"))
print(os.path.abspath("."))
print(os.path.abspath(".."))
print(os.path.abspath("../.."))

# import os.path
# import time
#
# # 1.格式化文件或目录路径
# # 获取绝对路径
# print(os.path.abspath("."))
# # 返回一个路径的当前目录或文件名(最后一个分隔符后的名字)
print(os.path.basename(r"aaa\2.txt"))
# # 返回一个路径的父目录(最后一个分隔符前的名字)
print(os.path.dirname(r"aaa\rfr\2.txt"))
# # os.path.join(path1[, path2[, ...]])	把目录和文件名合成一个路径
print(os.path.join("c:\\", "aaa", "1.txt"))
print(os.path.join("e:\\", "som", "aaa", "1.txt"))
# # 规范path字符串形式
print(os.path.normpath(r"./aaa\bbb/ccc\1.txt"))
print(os.path.normpath(r"./aa/a\bb\b/cc\c\1.txt"))

#
# # 2.文件属性获取
# # 得到得到文件的大小(字节大小)
print(os.path.getsize("aaa/1.txt"))
# # 返回最近访问时间
print(datetime.datetime.fromtimestamp(os.path.getatime(r"F:\随堂视频\20191120\1.day11任务处理.mp4")))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getatime("."))))

# # 返回最近文件修改时间
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime("."))))
print(datetime.datetime.fromtimestamp(os.path.getmtime(r"F:\随堂视频\20191120\1.day11任务处理.mp4")))

# # 返回文件 path 创建时间
# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getctime("."))))
print(datetime.datetime.fromtimestamp(os.path.getctime(r"F:\随堂视频\20191120\1.day11任务处理.mp4")))

#
# # 3.辨识路径（存在or不存在、绝对or相对、目录or文件等）
# # 判断路径是否存在
# print(os.path.exists(r".\aaa"))
# # 判断是否为绝对路径
# print(os.path.isabs(r"F:\随堂视频\20191120\1.day11任务处理.mp4"))
# print(os.path.isabs(r"c:/abs."))
# print(os.path.isabs(r"abs"))
# # 判断路径是否为文件(不存在的返回False)
# print(os.path.isfile("."))
# print(os.path.isfile("aaa/1.txt"))
# print(os.path.isfile("aaa/2.txt"))
# # 判断路径是否为目录(不存在的返回False)
# print(os.path.isdir("."))
# print(os.path.isdir("aaa"))

# # 4.拆分路径:获得的是元组
# # 路径拆分为两部分，后一部分总是最后级别的目录或文件名(按最后一个分隔\符切开)
print(os.path.split(r"aaa\bbb\2.txt"))
print(os.path.split(r"aaa\bbb"))
# # 路径拆分为两部分，后一部分总是文件的后缀名(按最后一个分隔符.切开,保留.)
print(os.path.splitext(r"aaa\bbb\2.mp4"))
dir = r"aaa\bbb\2.txt"
split_text = os.path.splitext(dir)
print(os.path.split(split_text[0])[0])
print(os.path.split(split_text[0])[1])

print(split_text[1])


#
# 思考并练习:
# 编写一个函数，传入一个目录路径，将该目录中的文件进行相同后缀名的分组归档：比如所有.txt的放入txt目录中，所有.py的放入py目录中等等，注意不处理子目录
#
def func(root_dir):
    for root, subs, files in os.walk(root_dir, False):
        # print("当前目录", root)
        # print("子目录们", subs)
        # print("子文件们", files)
        for file in files:
            endwith = os.path.splitext(file)[1][1:]
            print(endwith)
            os.renames(os.path.join(root, file), os.path.join(root_dir, endwith, file))
            # print(os.path.join(root_dir,endwith, file))


func("F:\新建文件夹 (3)")


def group_files(dir):
    if os.path.isfile(dir):
        return
    for i in os.listdir(dir):
        if os.path.isfile(os.path.join(dir, i)):
            ext = os.path.splitext(i)[1][1:]
            print(ext)
            os.renames(os.path.join(dir, i), os.path.join(dir, ext, i))

# group_files("F:\新建文件夹")
