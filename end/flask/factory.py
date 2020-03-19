"""
flask:应用工厂，负责应用相关所有的内容

"""
import sqlite3

from flask import render_template, request, flash
from werkzeug.utils import redirect

# 引入模块
from flask import Flask

# from views.book import books_bp
# from views.other import get404_bp
# from views.user import user_bp
from models import db
from views import *


def creat_app():
    # 实例化WSGI应用
    app = Flask(__name__)
    # 开启调试模式，修改代码不需要重启
    app.debug = True
    # 必须配置secret_key
    app.secret_key = "3\x83\xea\xeeeB?\xa9\x03Q\x83+\xa8\x11\x1bZ2iS\xe2?Q\xca"

    # 404针对整个项目，不能加入蓝图
    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html")

    # @app.route("/active/<int:id>", methods=["GET"])
    # def activeuser(id):
    #     # if request.method == "GET":
    #     print(id)
    #     # with sqlite3.connect("demo5.db") as con:
    #     #     cur = con.cursor()
    #     #     cur.execute("update user set is_active = 1 where id = ?", (id,))
    #     #     con.commit()
    #     return redirect("/login")

    @app.template_filter(name="myupper")
    def myupper(value):
        return value.upper()

    # 邮箱配置
    # 网易的

    app.config["MAIL_SERVER"] = "smtp.163.com"
    app.config["MAIL_PORT"] = 25

    app.config["MAIL_USERNAME"] = "18336068360@163.com"
    app.config["MAIL_PASSWORD"] = "UMGMFZEQRXCDSFAN"
    app.config['MAIL_DEFAULT_SENDER'] = '确认加入神秘组织<18336068360@163.com>'
    # qq的
    # app.config["MAIL_SERVER"] = "smtp.qq.com"
    # # 端口号465或587
    # app.config["MAIL_PORT"] = 587
    # app.config["MAIL_USE_SSL "] = True
    # app.config["MAIL_USE_TLS "] = False
    # app.config["MAIL_DEBUG "] = True
    #
    # app.config["MAIL_USERNAME"] = "1987617587@qq.com"
    # app.config["MAIL_PASSWORD"] = "plvhsqynyvexbdfe"
    # app.config['MAIL_DEFAULT_SENDER'] = '老张大讲堂<1987617587@qq.com>'
    # 扩展工厂 关联邮件
    mail.init_app(app)

    # 注册蓝图
    app.register_blueprint(user_bp)
    app.register_blueprint(books_bp)
    app.register_blueprint(get404_bp)
    app.register_blueprint(admin_bp)

    # @app.before_first_request
    # def first_request_do_something():
    #     print("这是第一次请求，创建数据库")
    #     try:
    #         con = sqlite3.connect("flask_demo.db")
    #         cur = con.cursor()
    #         cur.execute("DROP TABLE IF EXISTS user;")
    #         cur.execute(
    #             "CREATE TABLE user (id INTEGER PRIMARY KEY AUTOINCREMENT,"
    #             "username TEXT UNIQUE NOT NULL,password TEXT NOT NULL,"
    #             "created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP, "
    #             "is_admin INTEGER DEFAULT 0, is_active INTEGER DEFAULT 0 )")
    #         con.commit()
    #         cur.close()
    #         con.close()
    #     except:
    #         print("出错了")
    #
    #     return "这是第一次请求"

    # 配置数据库
    app.config['SQLALCHEMY_ECHO'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_demo.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    db.app = app

    return app
