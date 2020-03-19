"""
视图工具模块
"""
# 扩展flask模块 定义邮件模块
from flask_mail import Mail

mail = Mail()

from functools import wraps

from flask import session, redirect, request


# 定义检测用户是否登录的函数
def checklogin(f):
    @wraps(f)
    def check1(*args, **kwargs):
        user = session.get("user")
        if user:
            return f(*args, **kwargs)
        else:
            # return redirect("/login")
            return redirect("/login?next=" + request.path)

    return check1
