# pickle方式操作文件
import os
import pickle

# 定义文章保存路径和文件名
students_file = "students.objs"

# 判断文件是否存在
if not os.path.exists(students_file):
    os.close(os.open(students_file, os.O_CREAT))


# 预定义学员信息:（不需要）有录入学员信息功能

class Student:

    def __init__(self, name, stu_num, score, ctime) -> None:
        super().__init__()
        self.stu_num = stu_num
        self.name = name
        self.score = score
        self.ctime = ctime

    def __str__(self) -> str:
        return "%-6s%-6d%-6d " % (self.name, self.stu_num, self.score) + f"{self.ctime}"

    def __eq__(self, other):
        return self.name == other.name and self.stu_num == other.stu_num and \
               self.score == other.score and self.ctime == other.ctime

    def __gt__(self, other):
        return self.name > other.name and self.stu_num > other.stu_num and \
               self.score > other.score and self.ctime > other.ctime


# 追加新学员的功能
def create_student(name: str, stu_num: int, score: int, ctime: str):
    students = []
    # 判断学员信息的文件是否为空
    if os.path.getsize(students_file) != 0:
        # 先读后写
        with open(students_file, "rb") as io:
            students = pickle.load(io)

    # 构建学员对象
    student = Student(name, stu_num, score, ctime)
    # 将学员对象存入列表
    students.append(student)

    # 将列表按照序列化方式写入文件
    with open(students_file, "wb") as io:
        pickle.dump(students, io)


# 读取所有的学员信息
def read_all():
    students = []
    if os.path.getsize(students_file) != 0:
        with open(students_file, "rb") as io:
            students = pickle.load(io)
    return students


# 按学号查找学员
def query_by_stu_num(stu_num: int):
    # 读取所有的学员
    students = read_all()
    # 查询到的数据列表
    query_stu_nums = []
    # 文件的搜索变成了列表的搜索
    for i in students:
        if i.stu_num == stu_num:
            query_stu_nums.append(i)

    return query_stu_nums


def del_by_obj(del_obj: Student):
    # 读取所有的学员
    students = read_all()

    # 将要删除的对象从students(列表)中移除
    for i in students:
        if i == del_obj:
            students.remove(i)
            break

    # 重写文件
    with open(students_file, "wb") as io:
        pickle.dump(students, io)


# 按姓名搜索学员
def query_by_name(name: str):
    # 读取所有的学员
    students = read_all()
    # 查询到的数据列表
    query_names = []
    # 文件的搜索变成了列表的搜索
    for i in students:
        if i.name == name:
            query_names.append(i)

    return query_names


# 更新学员信息到文件
def update_file(student: Student, new_name, new_stu_num, new_score, new_ctime):
    # 读取所有的学员信息
    students = read_all()

    # 从students(列表)中找到原对象 替换新的属性值
    for i in students:
        if i == student:
            i.name = new_name
            i.stu_num = new_stu_num
            i.score = new_score
            i.ctime = new_ctime

    # 重写文件
    with open(students_file, "wb") as io:
        pickle.dump(students, io)
