"""
# author Liu shi hao
# date: 2019/12/6 17:57
# file_name: day25_task

"""
import datetime
import os

# 文件操作任务：
# 1  获取文件的大小
import random
import time

# print(os.path.getsize("E:\python1911A\day25\write_test2.date"))

# 2  获取文件扩展名

# print(os.path.splitext("E:\python1911A\day25\write_test2.date")[1])

# 3  获取文件上次修改时间

# print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(os.path.getmtime("."))))
# print(datetime.datetime.fromtimestamp(os.path.getmtime(r"F:\随堂视频\20191120\1.day11任务处理.mp4")))

# 4  创建和删除文件

# with open("write_test4.date", "w", encoding="utf-8") as io:
#     io.write("第一行数据\n")
#     io.writelines(["第二行数据\n", "第三行数据"])
# os.remove("write_test4.date")

# 5  生成随机文件名或文件夹名
# UUID的使用
# import uuid
#
# arr5 = [".mp4", ".wav", ".txt", ".ppt"]
# file_name = str(uuid.uuid4()).replace("-", "/") + str(arr5[random.randint(0, len(arr5))])
# dir_name = str(uuid.uuid4()).replace("-", "/")
# print(f"文件名:{file_name}")
# print(f"文件夹名:{dir_name}")

import datetime
import os
import uuid


# print(type(uuid.uuid4().hex))
# os.mkdir(uuid.uuid4().hex)

# 6  建立临时文件
# from tempfile import TemporaryFile
#
# with TemporaryFile('w+t') as f:
#     f.write('Hello World\n')
#     f.write('Testing\n')
#     data = f.readlines()
#     print(data)

# print(tempfile.mktemp(".tmp", uuid.uuid4().hex))
# print(tempfile.mkdtemp(".tmp", uuid.uuid4().hex))
# print(tempfile.mkstemp(".tmp", uuid.uuid4().hex))

# input()

# 7  根据日期动态建立文件

# file = str(datetime.datetime.strftime(datetime.datetime.now(),"%Y%m%d-%H%M%S"))
# file = str(datetime.datetime.now().strftime("%Y%m%d-%H%M%S"))
# os.close(os.open(file + ".txt", os.O_CREAT))


# 8  检查文件是否存在

# print(os.path.isfile("write_test2.date"))

# 9  获取文件夹下所有子文件夹及文件的名称
# print(os.listdir("E:\练习"))


#
# def func9():
#     for root, subs, files in os.walk("F:\随堂视频", False):
#         print("当前目录", root)
#         print("子目录们", subs)
#         print("子文件们", files)
#
#
# func9()

# 10 搜索文件

def search(dish, file_name):
    for root, subs, files in os.walk(dish):
        print("当前目录", root)
        print("子目录们", subs)
        print("子文件们", files)
        for file in files:
            if file == file_name:
                return os.path.join(root + file)
        return "找不到"


# print(search("F:\\", "1.py"))

# 11 修改文件或目录的名字

# os.close(os.open("2.txt", os.O_CREAT))  # 创建
# os.rename("2.txt", "1.txt")  # 重命名文件
# os.renames("1.txt", "aaa/2.txt")  # 移动文件
# os.renames("aaa", "bbb")  # 重命名文件夹

# 12 使用字节文件流复制大文件
import os
import time


# 13 批量复制文件
def copy_file(src, dest):
    with open(src, "rb") as read:
        with open(dest, "wb") as write:
            buffer_data = 4096
            while 1:
                data = read.read(buffer_data)
                if not data:
                    break
                write.write(data)


# "c:/aaa" "d:/rrr"
# "c:/aaa/bbb"
# ./aaa/bbb
# c:/aaa/bbb
# c:/aaa/bbb/ccc/ddd
def copy_dir(src_dir, dest_dir):
    if os.path.isdir(src_dir):
        for root, dirs, files in os.walk(src_dir):
            # root:../day25/aaa
            # 在dest的目录下创建新的root
            # 将src的目录进行切割
            if root == src_dir:
                dest_root = os.path.basename(root)
            else:
                dest_root = root[len(os.path.dirname(src_dir)) + 1:]
            # if dest_root.startswith("/"):
            #     dest_root = dest_root[1:]
            os.mkdir(os.path.join(dest_dir, dest_root))
            for file in files:
                copy_file(os.path.join(root, file), os.path.join(dest_dir, dest_root, file))


copy_dir("../day25", "./")
print(os.path.join("./", "aaa/bbb"))


# 14 判断文件是否正在被使用(文件被打开时不可改名)
# os.open("111.py", os.O_CREAT)
#
# try:
#     os.renames("111.py", "11.py")
# except PermissionError:
#     print("文件正被使用！")
# else:
#     os.rename("11.py", "111.py")
def is_use(file_name: str):
    try:
        os.rename(file_name, file_name)
    except PermissionError:
        return False
    return True


os.open("111.py", os.O_CREAT)
if not is_use("111.py"):
    print("文件正被使用！")

# 15 根据文件内容进行比较

import filecmp


#
# true if 2 files are the same
# with open("2.txt", "w", encoding="utf-8") as io:
#     io.write("第一行数据\n")
# io.writelines(["第二行数据\n", "第三行数据"])
#
# result = filecmp.cmp("1.txt", "2.txt")
# print(result)

# 16 如何将订单对象存入文件中 并实现增删改查功能
#
class Student:

    def __init__(self, name, gender, stu_num, pid) -> None:
        super().__init__()
        self.stu_num = stu_num
        self.gender = gender
        self.name = name
        self.pid = pid

    def __lt__(self, other):
        return self.pid < other.pid

    def __gt__(self, other):
        return self.pid > other.pid

    def __eq__(self, other):
        return self.pid == other.pid

    def __str__(self) -> str:
        return f"姓名{self.name}\t性别{self.gender}\t学号{self.stu_num}\t身份证号{self.pid}"


stus = [
    Student("sfs", "男", "001", 123),
    Student("fsg", "男", "002", 322),
    Student("ret", "女", "003", 192),
    Student("sdf", "男", "004", 222),
    Student("sdf", "女", "005", 333)

]


# 按对象列表添加
def add_students(arr: list):
    with open("Students.date", "w", encoding="utf-8") as io:
        for i in range(len(arr)):
            io.writelines(str(arr[i]) + "\n")


# add_students(stus)


# 按身份证号删除
def del_students(pid_num):
    nums = len(stus)
    for i in range(nums):
        if stus[i].pid == pid_num:
            del stus[i]
            break

    with open("Students.date", "w", encoding="utf-8") as io:
        for j in range(len(stus)):
            io.writelines(str(stus[j]) + "\n")


# del_students(222)

# 按身份证号查询，进行修改
def revamp_students(pid_num, self):
    nums = len(stus)
    for i in range(nums):
        if stus[i].pid == pid_num:
            stus[i] = self
            break

    with open("Students.date", "w", encoding="utf-8") as io:
        for j in range(len(stus)):
            io.writelines(str(stus[j]) + "\n")


# revamp_students(222, Student("sdf", "女", "004", 222))  # 把上面222的性别改为女


# 从文件按对象查询
def query_students(self):
    with open("write_test2.date", "r", encoding="utf-8") as read_io:

        while True:  # 按原行数读取
            data = read_io.readline(len(str(self)))
            # print(data, len(data))
            # print(self,len(str(self)))
            if data == str(self):
                return f"找到对象：{self}"
            if not data:
                return None


# print(query_students(Student("sdf", "男", "004", 222)))

def load_all_stus(stus_file):
    ret = []
    with open(stus_file, "r", encoding="utf-8") as read_list:
        str_list = read_list.readlines()
        for i in str_list:
            name = i.split("\t")[0]
            gender = i.split("\t")[1]
            stu_num = i.split("\t")[2]
            pid = i.split("\t")[3][:-1:]
            ret.append(Student(name, gender, stu_num, int(pid)))
    return ret

# for i in load_all_stus("E:\python1911A\day25\Students.date"):
#     print(i)
