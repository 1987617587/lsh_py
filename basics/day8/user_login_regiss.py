"""
# author Liu shi hao
# date: 2019/11/15 11:13
# file_name: user_login_regiss
# 8.
# 定义一个普通用户类
# 普通用户类具备的属性：用户名、密码、权限
# 普通用户类具备的方法：登录、注册
#
# 注意：请详细测试该类
"""


class Users:

    def __init__(self, user_name, password, pri) -> None:
        super().__init__()
        self.user_name = user_name
        self.password = password
        self.pri = pri

    def login(self, user_name, password):
        return self.user_name == user_name and self.password == password

    def register(self, user_name, password, pri):
        self.user_name = user_name
        self.password = password
        self.pri = pri


# 准备数据库中的对象列表
users = \
    [
        Users("asd", "121", "admin"),
        Users("user1", "121", "user")
    ]

# 模拟前端验证
# 模拟登录
for j in range(3):
    user_name = input("用户名：")
    password = input("密 码：")
    # 匹配数据库中对象信息
    user_login = None
    for i in range(len(users)):
        if users[i].login(user_name, password):
            print("登录成功！")
            user_login = users[i]
            break
    else:
        print(f"用户名或密码输入有误，请重新输入，您还有{2 - j}次机会。") if j != 2 else print("您三次输入都有误，请与管理员联系")

    if user_login is not None:
        break
# 模拟前端注册
# 模拟注册
register_user = Users(None, None, None)
user_name = input("注册用户名：")
while 1:
    password = input("注册密码：")
    re_password = input("请重复密码：")
    if password != re_password:
        print("两次输入不一致，请重新设定密码！")
        continue
    break
# 管理员注册验证
pri = input("请选择权限(1,管理员  2,用户)：")
i = 0

if pri == "1":
    while i < 3:
        in_admin_psw = input("请输入管理员密码：")
        if in_admin_psw == "666666":
            pri = "admin"
            print("注册管理员成功，正在返回登录！")
            break
        else:
            i += 1
            if i == 3:
                print("注册管理员失败！")
                pri = "user"
                break
            print(f"管理员密码输入错误！您还有{3 - i}次机会！")
else:
    pri = "user"
    print("注册成功，正在返回登录！")

# 产生用户对象
register_user.register(user_name, password, pri)
# 注册成功的对象存入数据库
users.append(register_user)
# 遍历数据库，验证注册是否成功
for i in range(len(users)):
    print(f"用户名:{users[i].user_name} 密码:{users[i].password} 权限:{users[i].pri}")
