# 13、需要利用12题创建的类
# 有一个文件"students.txt"负责存储学员成绩（包括学生号，姓名，三门课成绩）（10分）
# 1.	载入该文件信息
# 2.	查询出是否包含名字为”Task13”的学生，若有，修改三门成绩为:66 77 88
# 3.	从键盘输入追加的学员数据（包括学生号，姓名，三门课成绩），计算出平均成绩，
# 将原有的数据和计算出的平均分数更新到"students.txt"文件中，平均成绩存储在最后一行。
import os
import pickle
from functools import wraps

from exam2 import base3, base5


# 建立装饰器，要求先登录
def check_login(func):
    @wraps(func)
    def wrapper():
        if base3.Student.login_num is not None:
            func()
        else:
            print("*" * 12 + "您还未登录，请先登录！" + "*" * 12)

    return wrapper


# 解第一题


students_file = "students.txt"
#  判断文件是否存在
if not os.path.exists(students_file):
    os.close(os.open(students_file, os.O_CREAT))
# 写入文件
with open(students_file, "wb") as io:
    pickle.dump(base3.arr1, io)


# 增加学员
@check_login
def create_student():
    # 判断学员信息的文件是否为空
    if os.path.getsize(students_file) != 0:
        # 先读后写
        with open(students_file, "rb") as io:
            students = pickle.load(io)

    # 构建学员对象
    try:
        stu_num = input("请输入学号：")
        name = input("请输入姓名：")
        c_score = int(input("请输入新的语文成绩："))
        m_score = int(input("请输入新的数学成绩："))
        e_score = int(input("请输入新的英语成绩："))
        student = base3.Student(stu_num, "一班", name, c_score, m_score, e_score)
        # 将学员对象存入列表
        students.append(student)
    except:
        print("增加失败！")
    # 将列表按照序列化方式写入文件
    with open(students_file, "wb") as io:
        pickle.dump(students, io)


# 读取所有的学员信息
@check_login
def read_all():
    students = []
    if os.path.getsize(students_file) != 0:
        with open(students_file, "rb") as io:
            students = pickle.load(io)
    return students


# 按姓名搜索学员
@check_login
def query_by_name():
    # 读取所有的学员
    students = read_all()
    # 查询到的数据列表
    query_names = []
    name = input("请输入要查询的学员姓名：")
    # 文件的搜索变成了列表的搜索
    for i in students:
        if i.name == name:
            query_names.append(i)

    return query_names


# 更新学员信息到文件
@check_login
def update_file():
    # 读取所有的学员信息
    students = read_all()
    # 从students(列表)中找到原对象 替换新的属性值
    name = input("请输入要修改的学员姓名：")
    for i in students:
        if i.name == name:
            try:
                i.c_score = int(input("请输入新的语文成绩："))
                i.m_score = int(input("请输入新的数学成绩："))
                i.e_score = int(input("请输入新的英语成绩："))
            except:
                print("输入有误")
    # 重写文件
    with open(students_file, "wb") as io:
        pickle.dump(students, io)


# 求出平均成绩增加到文件末尾
@check_login
def get_ever_score():
    # 读取所有的学员信息
    students = read_all()
    for i in students:
        students.append((i.c_score + i.e_score + i.m_score) / 3)
    # 重写文件
    with open(students_file, "wb") as io:
        pickle.dump(students, io)


if __name__ == '__main__':
    # 解第二题
    # 开始查找姓名"Task13"学员
    stu_arr = query_by_name()
    # 修改成绩
    update_file()
    # 解第三题
    # 增加学员：
    create_student()
    # 求出平均成绩增加到文件末尾
    get_ever_score()
