# author:lzt
# date: 2019/12/9 14:37
# file_name: blog_manager
# pickle方式操作文件
import os
import pickle

# 定义文章保存路径和文件名
contents_file = "contents.objs"

# 判断文件是否存在
if not os.path.exists(contents_file):
    os.close(os.open(contents_file, os.O_CREAT))


# 预定义文章:有编写文章功能

class Content:

    def __init__(self, title, author, content, ctime) -> None:
        super().__init__()
        self.title = title
        self.author = author
        self.content = content
        self.ctime = ctime

    def __str__(self) -> str:
        return f"{self.title} {self.author} {self.content} {self.ctime}"

    def __eq__(self, other):
        return self.title == other.title and self.content == other.content \
               and self.author == other.author and self.ctime == other.ctime


# 追加新文章的功能
def create_content(title: str, author: str, content: str, ctime: str):
    contents = []
    # 判断文章的文件是否为空
    if os.path.getsize(contents_file) != 0:
        # 先读后写
        with open(contents_file, "rb") as io:
            contents = pickle.load(io)

    # 构建文章对象
    content = Content(title, author, content, ctime)
    # 将文章对象存入列表
    contents.append(content)

    # 将列表按照序列化方式写入文件
    with open(contents_file, "wb") as io:
        pickle.dump(contents, io)


# 读取所有的文章
def read_all():
    contents = []
    if os.path.getsize(contents_file) != 0:
        with open(contents_file, "rb") as io:
            contents = pickle.load(io)
    return contents


# 按标题查找文章
def query_by_title(title: str):
    # 读取所有的文章
    contents = read_all()
    # 查询到的数据列表
    query_titles = []
    # 文件的搜索变成了列表的搜索
    for i in contents:
        if i.title == title:
            query_titles.append(i)

    return query_titles


def del_by_obj(del_obj: Content):
    # 读取所有的文章
    contents = read_all()

    # 将要删除的对象从contents中移除
    for i in contents:
        if i == del_obj:
            contents.remove(i)
            break

    # 重写文件
    with open(contents_file, "wb") as io:
        pickle.dump(contents, io)


# 按作者搜索文章
def query_by_author(author: str):
    # 读取所有的文章
    contents = read_all()
    # 查询到的数据列表
    query_authors = []
    # 文件的搜索变成了列表的搜索
    for i in contents:
        if i.author == author:
            query_authors.append(i)

    return query_authors


# 更新文章到文件
def update_file(content: Content, new_title, new_author, new_content, new_ctime):
    # 读取所有的文章
    contents = read_all()

    # 从contents中找到原对象 替换新的属性值
    for i in contents:
        if i == content:
            i.title = new_title
            i.author = new_author
            i.content = new_content
            i.ctime = new_ctime

    # 重写文件
    with open(contents_file, "wb") as io:
        pickle.dump(contents, io)
