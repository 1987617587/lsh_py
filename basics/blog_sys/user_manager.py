# author:lzt
# date: 2019/12/9 14:37
# file_name: user_manager

# json user

# 若用户文件不存在 需要创造文件
import json
import os

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
