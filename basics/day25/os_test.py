"""
# author Liu shi hao
# date: 2019/12/6 10:44
# file_name: os_test

"""
import os

# 由于文件在操作系统的资源管理器上，so我们必须借助和操作系统相关的模块：os(operating system)

#
# # 1辨识操作系统：os.name
# print(os.name)
# 如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
#
# # 2环境变量:os.environ
# print(os.environ)
#
# # 3环境变量中某个特定数据:os.environ.get("key")
# print(os.environ.get("path"))
#
# # 4辨识目录权限
# os.access("new_dir", os.F_OK)  # 查看目录是否存在
# os.F_OK	:  是否存在
import time

print(os.access("asd", os.F_OK))
print(os.access(r"C:\Users\Administrator\Desktop\教室练习模板参考\gun_test.py", os.F_OK))
# os.R_OK	:  是否可读
print(os.access(r"C:\Users\Administrator\Desktop\教室练习模板参考\gun_test.py", os.R_OK))

# os.W_OK	:  是否可写
print(os.access(r"C:\Users\Administrator\Desktop\教室练习模板参考\gun_test.py", os.W_OK))
# os.X_OK	:  是否可执行
print(os.access(r"C:\Users\Administrator\Desktop\教室练习模板参考\gun_test.py", os.X_OK))
# # 5查看当前目录
print(os.getcwd())


#
# # 6更改当前目录:程序当次运行中有效
# os.chdir("..")
# print(os.getcwd())
#
# # 7创建单级目录：目录若已存在会报异常
# if not os.access("new_dir", os.F_OK):
#     os.mkdir("new_dir")
#
# # 8递归创建无限级目录：exist_ok为False若目录存在会报异常 默认False 建议True
# os.makedirs("mydir/sub1/sub2/sub3", exist_ok=True)
#
# # 9删除空目录
# if os.access("new_dir",os.F_OK):
#     os.rmdir("new_dir")
#
# # 10递归删除路径上的所有空目录
# os.removedirs("mydir/sub1/sub2/sub3")
#
# # 11创建文件 (若已存在，不覆盖，不创建)
# os.open("1.txt", os.O_CREAT)
# 为了防止资源泄露：创建后关闭对文件的连接
# os.close(os.open("2.txt", os.O_CREAT))
#
# time.sleep(3)

# # 12删除文件 只能删除文件 否则异常
# os.remove("2.txt")
#
# # 13重命名文件或目录
# os.rename("2.txt", "1.txt")
#
#
# # 14重命名文件或目录，可以带全路径一起修正(可移动)
# # 可以自动递归创建新目录 (禁止跨盘服务)
# os.renames("1.txt", "aaa/2.txt")
# os.renames("2.txt", "aaa/1.txt")
#
# # 15显示当前目录下所有的子文件及子目录
# print(os.listdir(".."))


#
# 递归遍历目录

def show_all(dir):
    print(dir)

    if os.path.isdir(dir):
        for i in os.listdir(dir):
            show_all("/".join([dir, i]))


# show_all(".")

# # 16显示当前目录中的所有内容（深度遍历）
# for root, subs, files in os.walk(".", True):
#     print("当前目录", root)
#     print("子目录：")
#     for i in subs:
#         print(root + "\\" + i)
#     print("子文件：")
#     for i in files:
#         print(root + "\\" + i)
#
# 思考并练习：
# 写一个函数，传入某个目录，将目录中的所有文件全部删除（包括子目录）
#
# os.close(os.open("1.txt", os.O_CREAT))
# os.close(os.open("2.txt", os.O_CREAT))
# os.renames("1.txt", "aaa/1.txt")
# os.renames("2.txt", "aaa/aab/2.txt")


def func():
    for root, subs, files in os.walk("aaa", False):
        print("当前目录", root)
        print("子目录们", subs)
        print("子文件们", files)
        for file in files:
            os.remove("/".join([root, file]))

        os.rmdir(root)


# func()

def func1():
    for root, subs, files in os.walk("F:\随堂视频", False):
        # print("当前目录", root)
        # print("子目录们", subs)
        # print("子文件们", files)
        for file in files:
            if file.endswith(".mp4"):
                print("/".join([root, file]))


func1()
