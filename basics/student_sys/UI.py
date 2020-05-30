# author:lzt
# date: 2019/12/9 14:36
# file_name: UI
# 负责和用户交互：1.获取用户的输入 2.向用户展示数据

# 模拟学生成绩管理系统
# 1.账号注册，登陆验证，班级管理
# 2.填写学员信息 和 成绩
# 3.查询所有学员成绩
# 4.查询其中一位成绩
# 5.修改学员成绩
# 6.删除学员
# 7.排序显示
# 8.退出系统
# 项目的启动文件！！！
import datetime
import sys
from functools import wraps

from blog_sys.check_login import stu_num_repeat
from student_sys import user_manager, class_manager

login_num = None


def check_login(func):
    @wraps(func)
    def wrapper(cls):
        if login_num is not None:
            func(cls)
        else:
            print("*" * 12 + "您还未登录，请先登录！" + "*" * 12)

    return wrapper


class UI:
    # 类函数

    # 欢迎界面
    @staticmethod
    def welcome():
        print("""
############################################
          欢迎来到学生成绩管理系统
############################################        
        """)
        UI.oparator()

    # 主操作界面
    @staticmethod
    def oparator():
        print("""
************** 请选择操作项目 **************
             1.账号注册，登陆验证
             2.班级管理填写学员信息
             3.查询所有学员成绩
             4.查询其中一位成绩
             5.修改学员成绩
             6.删除学员
             7.排序显示
             8.退出系统""")
        print("********************************************")
        choice = input("-->请输入要操作的选项(1-8):")
        if choice == "1":
            UI.login()
        elif choice == "2":
            UI.create_student()
        elif choice == "3":
            UI.show_all()
        elif choice == "4":
            UI.query()
        elif choice == "5":
            UI.modify_content()
        elif choice == "6":
            UI.del_content()
        elif choice == "7":
            UI.sort()
        elif choice == "8":
            UI.exit()
        else:
            UI.oparator()
        UI.oparator()
        pass

    # 各个操作界面
    @classmethod
    def login(cls):
        global login_num
        if login_num is None:
            # 获取用户输入的用户名和密码
            name = input("用户名:")
            pwd = input("密  码:")
            # 用user_manager中的方法和文件中的所有的用户进行匹配
            user = user_manager.query_by_name_pwd(name, pwd)
            if user is not None:
                print("登录成功！正在返回主页！")
                login_num = 1
            else:
                print("登录失败 若没有用户 请先注册！")
                UI.register()
        else:
            print("*" * 12 + "已登录，请勿重复登录！" + "*" * 12)

    @classmethod
    def register(cls):
        if login_num is None:
            # 获取用户注册的信息
            name = input("请输入注册的用户名:")
            # 检测用户名是否存在
            if user_manager.query_by_name(name):
                print("用户名已存在！")
                UI.register()
                return
            while 1:
                pwd1 = input("注册密码:")
                pwd2 = input("重复密码:")
                if pwd1 == pwd2:
                    break
                print("两次输入不一致！")
            # 保存用户注册的信息到文件:
            user_manager.write_json(name, pwd1)
            print("注册成功 正在前往登录界面！")
            UI.login()
        else:
            print("*" * 12 + "已登录，无需再次注册！" + "*" * 12)

    @classmethod
    @check_login
    def create_student(cls):
        # 填写学员信息 和 成绩
        name = input("学生姓名:")
        try:
            while 1:  # 学员信息中学号不能重复！
                stu_num = int(input("学生学号:"))
                if stu_num_repeat(stu_num):
                    break
                else:
                    print("学号已存在，请核对后，再次输入！")
            score = int(input("学生成绩:"))
            ctime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # 将学员信息 和 成绩保存起来
            class_manager.create_student(name, stu_num, score, ctime)
            print("信息录入成功！正在返回主界面！")
        except:
            print("信息格式错误！请返回主界面重试！")

    @classmethod
    @check_login
    def del_content(cls):
        # 删除学员
        try:
            del_stu_num = int(input("要删除的学员学号:"))
            # 判断学员是否存在 或者列出多个学员 供选择
            query = class_manager.query_by_stu_num(del_stu_num)
            if len(query) == 0:
                print("找不到这样的学员！")
            else:
                print("请选择一位学员来删除：")
                print("序号.姓名  学号  成绩  创建时间")
                for index, i in enumerate(query, 1):
                    print(f"{index}.{i}")
                try:
                    num = int(input("请输入要删除的序号:"))
                    if num < 1 or num > len(query):
                        print("输入有误 无法删除 返回主界面")
                        return
                    # 删除学员
                    class_manager.del_by_obj(query[num - 1])
                    print("删除成功！正在返回主页！")
                except:
                    print("输入有误 返回主界面！")
        except:
            print("输入有误 返回主界面！")

    @classmethod
    @check_login
    def query(cls):
        # 请用户选择按学员姓名查询还是学员学号查询
        name_stu_num = input("1.姓名 其他.学号")
        if name_stu_num == "1":
            # 按学员姓名查询用户输入
            name = input("请输入学员的名字:")
            # 查询学员的成绩:
            # 显示成绩:
            query = class_manager.query_by_name(name)
            if len(query) == 0:
                print("未找到该学员的成绩 返回主界面！")
            else:
                print("姓名   学号   成绩   创建时间")
                for i in query:
                    print(i)
        else:
            try:
                # 按学号查询用户输入
                stu_num = int(input("请输入学员的学号:"))
                # 查询学员的成绩:
                # 显示成绩:
                query = class_manager.query_by_stu_num(stu_num)
                if len(query) != 0:
                    print("姓名   学号   成绩   创建时间")
                    for i in query:
                        print(i)
                else:
                    print("无学员信息显示！")
            except:
                print("输入有误 返回主界面！")

    @classmethod
    @check_login
    def modify_content(cls):
        try:
            # 输入要修改的学员学号
            m_stu_num = int(input("要修改的学员学号:"))
            # 查询该学员
            query = class_manager.query_by_stu_num(m_stu_num)
            if len(query) == 0:
                print("没有这样的学员！")
                return
            print("请选择一位学员来修改：")
            print("序号.姓名  学号  成绩  创建时间")
            for index, i in enumerate(query, 1):
                print(f"{index}.{i}")
            try:
                num = int(input("请输入要修改的序号:"))
                if num < 1 or num > len(query):
                    print("输入有误 无法修改 返回主界面")
                    return
                # 若查到 修改学员信息内容
                modify_content = query[num - 1]
                # 询问用户要修改什么？
                name = input("学员的新姓名:")
                stu_num = input("学员的新学号:")
                try:
                    score = int(input("学员的新成绩:"))
                    ctime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    # 更新文章
                    # 老对象和新内容
                    class_manager.update_file(modify_content, name, stu_num, score, ctime)
                except:
                    print("输入有误 无法修改 返回主界面")
            except:
                print("输入有误 返回主界面！")
        except:
            print("输入有误 返回主界面！")

    @classmethod
    @check_login
    def show_all(cls):
        # 查询所有的学员成绩:
        # 显示所有的学员成绩：
        if class_manager.read_all():
            print("姓名   学号   成绩   创建时间")
            for content in class_manager.read_all():
                print(content)
            pass
        else:
            print("暂无学生信息 返回主界面！")

    @classmethod
    @check_login
    def sort(cls):
        # 将所有学员信息按成绩排序（从小到大）
        if len(class_manager.read_all()) != 0:
            score_sort_list = class_manager.read_all()
            # score_sort_list.sort()
            num = input("请选择排序类型：1.姓名 2.学号 3.成绩 4.创建时间 (1-4):")
            if num == "1":
                score_sort_list.sort(key=lambda s: s.name)
            if num == "2":
                score_sort_list.sort(key=lambda s: int(s.stu_num))
            if num == "3":
                score_sort_list.sort(key=lambda s: s.score)
            if num == "4":
                score_sort_list.sort(key=lambda s: s.ctime)
            # score_sort_list.sort(key=lambda s: s.score)
            print("序号.姓名  学号  成绩  创建时间")
            for index, i in enumerate(score_sort_list, 1):
                print(f"{index}.{i}")
        else:
            print("暂无学生信息 返回主界面！")

    @classmethod
    def exit(cls):
        exit_ok = input("确定退出吗?y-退出 其他-回到主界面:")
        if exit_ok.upper() == "Y":
            print("已安全退出！")
            sys.exit(0)
        UI.oparator()
        pass
