import sqlite3
from itsdangerous import TimedJSONWebSignatureSerializer, SignatureExpired, BadSignature

from flask import Blueprint, request, current_app
from flask import render_template, request, flash
from flask_mail import Message
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash, check_password_hash

# 新建用户模块蓝图
from .utils import mail

user_bp = Blueprint("user", __name__)


@user_bp.route("/regist", methods=["GET", "POST"])
def regist():
    if request.method == "GET":
        # return "请先登录"
        flash({

        })
        return render_template('regist.html')
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("password2")
        error = None
        if not username:
            error = "用户名必填"
        elif not password:
            error = "密码必填"
        elif not password2:
            error = "重复密码必填"
        elif password != password2:
            error = "密码不一致"
        else:
            with sqlite3.connect("flask_demo.db") as con:
                cur = con.cursor()
                cur.execute("select * from user where username = ?", (username,))
                r = cur.fetchall()
                print(r)
                if len(r) == 0:
                    print("可以创建")
                    try:
                        # 密码加密
                        security_password = generate_password_hash(password)
                        cur.execute("insert into user (username,password) values (?,?)", (username, security_password))
                        cur.execute("select * from user where username = ?", (username,))
                        r2 = cur.fetchone()
                        print(r2[0])
                        # 发送邮件
                        # 邮箱加密 密钥使用自动产生的密钥
                        print(current_app.secret_key)
                        seria_util = TimedJSONWebSignatureSerializer(current_app.secret_key, expires_in=3600)
                        serstr = seria_util.dumps({"id": r2[0]}).decode("utf-8")

                        # msg = Message(subject="神秘组织激活邮件", recipients=[username])
                        # # msg.html = "<a href='http://127.0.0.1:5000/active/" + str(r2[0]) + "'>点击激活</a>"
                        # msg.html = "<a href='http://127.0.0.1:5000/active/%s'>点击激活</a>" % (serstr,)
                        # mail.send(msg)
                        from tasks import sendmail
                        sendmail.delay(username, serstr)
                        # 发送邮件成功再提交
                        con.commit()
                    # 邮箱发送失败，不写入数据库
                    except Exception as e:
                        print(e)
                        con.rollback()
                        return "出现异常"

                    return redirect('/login')
                error = "用户名已存在"
        if error:
            # flash(error, category=error)
            flash({
                "error": error,
                "username": username
            })
            return redirect('/regist')


@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        flash({

        })
        # return "请先登录"
        return render_template('login.html')
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        error = None
        if not username:
            error = "用户名必填"
        elif not password:
            error = "密码必填"
        else:
            with sqlite3.connect("flask_demo.db") as con:
                cur = con.cursor()
                cur.execute("select * from user where username = ?", (username,))
                r = cur.fetchone()
                if r:
                    print(r, r[2])
                    # 校验密码
                    if check_password_hash(r[2], password):
                        print("找到用户")
                        if r[5] == 0:
                            error = "用户未激活，不能直接登录,请前往邮箱激活"
                            flash({
                                "error": error,
                                "username": username,
                                "password": password,
                            })
                            return redirect('/login')

                        return redirect('/')

                error = "用户名或密码错误"
        # 需要在本次请求中将信息写入session （前提必须配置secret_key）
        # flash("提示内容")
        # 下次请求中取获取、并且从session移除
        # get_flashed_messages()

        if error:
            # flash(error, category=error)
            flash({
                "error": error,
                "username": username,
                "password": password,
            })
            return redirect('/login')
        # return render_template('booklist.html', booklist=["倚天屠龙记", "神雕侠侣", "天龙八部"], username=username)
        # return redirect('/')


@user_bp.route("/active/<serstr>", methods=["GET"])
def activeuser(serstr):
    # 解密
    try:
        seria_util = TimedJSONWebSignatureSerializer(current_app.secret_key)
        obj = seria_util.loads(serstr)
        print(obj["id"])
        id = obj["id"]
        print(id)
        with sqlite3.connect("flask_demo.db") as con:
            cur = con.cursor()
            cur.execute("update user set is_active = 1 where id = ?", (id,))
            con.commit()
        return redirect("/login")

    except SignatureExpired as e:
        print(e, "过期了")
    except BadSignature as e:
        print(e, "密钥错误")
