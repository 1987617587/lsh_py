"""
# author Liu shi hao
# date: 2019/12/9 10:50
# file_name: copy_dir_files

"""
# 13 批量复制文件
import os


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
                dest_root = root[len(os.path.dirname(src_dir)) :]
            if dest_root.startswith("/"):
                dest_root = dest_root[1:]
            os.mkdir(os.path.join(dest_dir, dest_root))
            for file in files:
                copy_file(os.path.join(root, file), os.path.join(dest_dir, dest_root, file))


copy_dir(r"F:\随堂视频", r"E:\新建文件夹")
print(os.path.join("./", "aaa/bbb"))
