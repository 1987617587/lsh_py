"""
# author Liu shi hao
# date: 2019/11/20 15:34
# file_name: blog_UI

"""


class UI:
    @staticmethod
    def welcome():
        print("""
        ###########################
            欢迎来到奇酷博客系统
        ###########################
        """)

    @staticmethod
    def login():
        input("请输入用户名：")
        input("请输入密码：")

    @staticmethod
    def exit():
        input("确定退出？（y/n）")

    @staticmethod
    def ops():
        print("""
        1.编写文章
        2.发布文章
        3.修改文章
        """)
UI.welcome()
UI.login()
UI.exit()
UI.ops()