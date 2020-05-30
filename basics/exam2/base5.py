#
#
# 14.编写装饰器装饰12、13的功能：要求必须登录才可操作，并追加一个登录函数，登录后才可以继续操作。（10分）

# 来个管理者
# 若用户文件不存在 需要创造文件
import json
import os
from functools import wraps
from exam2 import base4

user_file = "user.ini"

# 定义json文件的格式
# {"users":[{"name":name,"pwd":pwd},{},{}]}

if not os.path.exists(user_file):
    os.close(os.open(user_file, os.O_CREAT))


# 因为有注册 所有不需要预定义一些用户！！！
# 根据前端需要创建函数
def query_by_name_pwd(name: str, pwd: str):
    if os.path.getsize(user_file) == 0:
        return None
    # 读取所有的用户
    # 通过迭代查询
    # 如果查询到 返回user
    with open(user_file, "r", encoding="utf-8") as json_io:
        users = json.load(json_io)

    for user in users.get("users"):
        if user.get("name") == name and user.get("pwd") == pwd:
            return name, pwd
    # 未匹配任何用户
    return None


# 检索用户名
def query_by_name(name: str):
    if os.path.getsize(user_file) == 0:
        return False

    with open(user_file, "r", encoding="utf-8") as json_io:
        users = json.load(json_io)

    for user in users.get("users"):
        if user.get("name") == name:
            return True

    return False


def write_json(name: str, pwd: str):
    if os.path.getsize(user_file) == 0:
        with open(user_file, "w", encoding="utf-8") as json_io:
            dict_str = {"users": [{"name": name, "pwd": pwd}]}
            json.dump(dict_str, json_io)
    else:
        # 先读取所有 追加后 写出到文件
        with open(user_file, "r", encoding="utf-8") as json_io:
            users = json.load(json_io)

        # 向users追加
        users.get("users").append({"name": name, "pwd": pwd})

        # 文件写回
        with open(user_file, "w", encoding="utf-8") as json_io:
            json.dump(users, json_io)


base4.base3.Student.login_num = None


# 建立装饰器，要求先登录
def check_login(func):
    @wraps(func)
    def wrapper():
        if base4.base3.Student.login_num is not None:
            func()
        else:
            print("*" * 12 + "您还未登录，请先登录！" + "*" * 12)

    return wrapper


def login():
    global login_num
    if base4.base3.Student.login_num is None:
        # 获取用户输入的用户名和密码
        name = input("用户名:")
        pwd = input("密  码:")
        # 用user_manager中的方法和文件中的所有的用户进行匹配
        user = query_by_name_pwd(name, pwd)
        if user is not None:
            print("登录成功！正在返回主页！")
            base4.base3.Student.login_num = 1
        else:
            print("登录失败 若没有用户 请先注册！")
            register()
    else:
        print("*" * 12 + "已登录，请勿重复登录！" + "*" * 12)


def register():
    if base4.base3.Student.login_num is None:
        # 获取用户注册的信息
        name = input("请输入注册的用户名:")
        # 检测用户名是否存在
        if query_by_name(name):
            print("用户名已存在！")
            register()
            return
        while 1:
            pwd1 = input("注册密码:")
            pwd2 = input("重复密码:")
            if pwd1 == pwd2:
                break
            print("两次输入不一致！")
        # 保存用户注册的信息到文件:
        write_json(name, pwd1)
        print("注册成功 正在前往登录界面！")
        login()
    else:
        print("*" * 12 + "已登录，无需再次注册！" + "*" * 12)


if __name__ == '__main__':
    # 开始登陆操作
    # register()
    login()
