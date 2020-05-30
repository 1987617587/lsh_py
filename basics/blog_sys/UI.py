# author:lzt
# date: 2019/12/9 14:36
# file_name: UI
# 负责和用户交互：1.获取用户的输入 2.向用户展示数据
import datetime
import sys
from functools import wraps
from blog_sys import user_manager, blog_manager


# def check_login(func):
#     @wraps(func)
#     def wrapper(cls):
#         if UI.login_num is not None:
#             func(cls)
#         else:
#             print("*"*12+"您还未登录，请先登录！"+"*"*12)
#
#     return wrapper
from blog_sys.check_login import check_login


class UI:
    login_num = None

    # 类函数

    # 欢迎界面
    @staticmethod
    def welcome():
        print("""
############################################
         欢迎来到奇酷的博客系统
############################################        
        """)
        UI.oparator()

    # 主操作界面
    @staticmethod
    def oparator():
        print("""
***** 您已进入主操作界面，请选择操作项目 *****
                1.登录
                2.注册
                3.编写文章
                4.删除文章
                5.查询文章(作者或标题)
                6.修改文章
                7.显示所有文章
                8.退出系统
**********************************************
        """)
        choice = input("-->请输入要操作的选项(1-8):")
        if choice == "1":
            UI.login()
        elif choice == "2":
            UI.register()
        elif choice == "3":
            UI.create_content()
        elif choice == "4":
            UI.del_content()
        elif choice == "5":
            UI.query()
        elif choice == "6":
            UI.modify_content()
        elif choice == "7":
            UI.show_all()
        elif choice == "8":
            UI.exit()
        else:
            UI.oparator()
        UI.oparator()
        pass

    # 各个操作界面
    @classmethod
    def login(cls):
        if UI.login_num is None:
            # 获取用户输入的用户名和密码
            name = input("用户名:")
            pwd = input("密  码:")
            # 用user_manager中的方法和文件中的所有的用户进行匹配
            user = user_manager.query_by_name_pwd(name, pwd)
            if user is not None:
                print("登录成功！")
                UI.login_num = 1
            else:
                print("登录失败 若没有用户 请先注册！")
        else:
            print("*" * 12 + "已登录，请勿重复登录！" + "*" * 12)

    @classmethod
    def register(cls):
        if UI.login_num is None:
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
            print("注册成功 返回登录页面！")
            UI.login()
        else:
            print("*" * 12 + "已登录，无需再次注册！" + "*" * 12)

    @classmethod
    @check_login
    def create_content(cls):
        # 编写文章
        title = input("文章的标题:")
        author = input("文章的作者:")
        content = input("文章的内容:")
        ctime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        # 将新文章保存起来
        blog_manager.create_content(title, author, content, ctime)
        pass

    @classmethod
    @check_login
    def del_content(cls):
        # 删除文章
        del_title = input("要删除的文章标题:")
        # 判断文章是否存在 或者列出多个文章 供选择
        query = blog_manager.query_by_title(del_title)
        if len(query) == 0:
            print("找不到这样的文章！")
        else:
            print("请选择一篇来删除：")
            for index, i in enumerate(query, 1):
                print(f"{index}.{i}")
            try:
                num = int(input("请输入要删除的序号:"))
                if num < 1 or num > len(query):
                    print("输入有误 无法删除 返回主界面")
                    return
                # 删除文章
                blog_manager.del_by_obj(query[num - 1])
                print("删除成功 返回主界面！")
            except:
                print("输入有误 返回主界面！")

        pass

    @classmethod
    @check_login
    def query(cls):
        # 请用户选择按作者查询还是标题查询
        title_author = input("1.作者 其他.标题")
        if title_author == "1":
            # 按作者查询用户输入
            author = input("请输入作者的名字:")
            # 查询作者的文章:
            # 显示文章
            query = blog_manager.query_by_author(author)
            if len(query) == 0:
                print("未找到该作者的文章 返回主界面！")
            else:
                for i in query:
                    print(i)
        else:
            # 按标题查询用户输入
            title = input("请输入标题的名字:")
            # 查询标题的文章:
            # 显示文章
            query = blog_manager.query_by_title(title)
            if len(query) != 0:
                print("标题 作者 内容 创建时间")
                for i in query:
                    print(i)
            else:
                print("无文章显示 返回主界面！")
        pass

    @classmethod
    @check_login
    def modify_content(cls):
        # 输入要修改的文章标题
        m_title = input("要修改的文章标题:")
        # 查询该文章
        query = blog_manager.query_by_title(m_title)
        if len(query) == 0:
            print("没有这样的文章！")
            return
        print("请选择一篇来修改：")
        for index, i in enumerate(query, 1):
            print(f"{index}.{i}")
        try:
            num = int(input("请输入要修改的序号:"))
            if num < 1 or num > len(query):
                print("输入有误 无法修改 返回主界面")
                return
            # 若查到 修改文章内容
            modify_content = query[num - 1]
            # 询问用户要修改什么？
            title = input("文章的新标题:")
            author = input("文章的新作者:")
            content = input("文章的新内容:")
            ctime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            # 更新文章
            # 老对象和新内容
            blog_manager.update_file(modify_content, title, author, content, ctime)
            print("修改完成 返回主界面！")
        except:
            print("输入有误 返回主界面！")
        pass

    @classmethod
    @check_login
    def show_all(cls):
        # 查询所有的文章:
        # 显示所有的文章：
        if blog_manager.read_all():
            print("标题 作者 内容 创建时间")
            for content in blog_manager.read_all():
                print(content)
            pass
        else:
            print("暂无文章 返回主界面！")

    @classmethod
    def exit(cls):
        exit_ok = input("-->确定退出吗?y-退出 其他-回到主界面:")
        if exit_ok.upper() == "Y":
            print("已安全退出！")
            sys.exit(0)
        UI.oparator()
        pass
