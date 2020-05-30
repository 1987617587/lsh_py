# author:lzt
# date: 2019/12/9 9:12
# file_name: day25_task
# 1  获取文件的大小
# 2  获取文件扩展名
# 3  获取文件上次修改时间
# 4  创建和删除文件
# import os
#
# os.close(os.open("task4.txt", os.O_CREAT))
# os.remove("task4.txt")

# 5  生成随机文件名或文件夹名
# UUID的使用
import datetime
import os
import uuid
# print(type(uuid.uuid4().hex))
# os.mkdir(uuid.uuid4().hex)

# 6  建立临时文件
import tempfile


# print(tempfile.mktemp(".tmp", uuid.uuid4().hex))
# print(tempfile.mkdtemp(".tmp", uuid.uuid4().hex))
# print(tempfile.mkstemp(".tmp", uuid.uuid4().hex))

# input()

# 7  根据日期动态建立文件
# file_name = datetime.datetime.now().strftime("%Y-%m-%d %H-%M-%S")
# os.open(file_name, os.O_CREAT)

# 8  检查文件是否存在
# 9  获取文件夹下所有子文件夹及文件的名称
# for i in os.listdir(".."):
#     print(i)


# 10 搜索文件
# for root, dirs, files in os.walk(".."):
#     for file in files:
#         if file == "base1.py":
#             print(os.path.join(root, file))

# 11 修改文件或目录的名字


# 12 使用字节文件流复制大文件


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
                dest_root = root[len(os.path.dirname(src_dir)):]
            if dest_root.startswith("/"):
                dest_root = dest_root[1:]
            os.mkdir(os.path.join(dest_dir, dest_root))
            for file in files:
                copy_file(os.path.join(root, file), os.path.join(dest_dir, dest_root, file))


# copy_dir("../day25", "./")
# print(os.path.join("./","aaa/bbb"))


# 14 判断文件是否正在被使用
def is_use(file_name: str):
    try:
        os.rename(file_name, file_name)
    except PermissionError:
        return False
    return True


# os.open("use.txt", os.O_CREAT)
# if is_use("use.txt"):
#     print("可以对文件操作")
# else:
#     print("文件正在占用中！")

# 15 根据文件内容进行比较
with open("use.txt", "rb") as read1:
    with open("__init__.py", "rb") as read2:
        print(read1.read() == read2.read())

# 16 如何将订单对象存入文件中 并实现增删改查功能
