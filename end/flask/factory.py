"""
flask:应用工厂，负责应用相关所有的内容

"""
from flask import render_template, request, flash, Flask
from werkzeug.utils import redirect




def create_app():
    app = Flask(__name__)
    # 开启调试模式，修改代码不需要重启
    app.debug = True
    # 必须配置secret_key
    app.secret_key = "3\x83\xea\xeeeB?\xa9\x03Q\x83+\xa8\x11\x1bZ2iS\xe2?Q\xca"

    @app.route("/")
    def books():
        # 内容需要查询数据库
        books = [
            {
                "id": 101,
                "name": "哇哈哈"
            },
            {
                "id": 102,
                "name": "可口可乐"
            },
            {
                "id": 103,
                "name": "乐虎"
            },
        ]
        user = [
            {
                "name": "admin"
            }
        ]
        # return render_template("booklist.html", booklist=["雪山飞狐", "射雕英雄传", "少林寺传奇"])
        return render_template("index.html", books=books, user=user)

    @app.route('/', methods=["GET", "POST"])
    def login():
        if request.method == "GET":
            # return "请先登录"
            return render_template('login.html')
        if request.method == "POST":
            username = request.form.get("username")
            password = request.form.get("password")

            error = None
            if not username:
                error = "用户名必填"
            if not password:
                error = "密码必填"
            # 需要在本次请求中将信息写入session （前提必须配置secret_key）
            # flash("提示内容")
            # 下次请求中取获取、并且从session移除
            # get_flashed_messages()
            if error:
                flash(error, category=error)
                return redirect('/')
            return render_template('booklist.html', booklist=["倚天屠龙记", "神雕侠侣", "天龙八部"], username=username)

    @app.route('/regist', methods=["GET", "POST"])
    def regist():
        if request.method == "GET":
            # return "请先登录"
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
            if error:
                flash(error, category=error)
                return redirect('/regist')
            return redirect('/')

    @app.errorhandler(404)
    def page_not_found(error):
        return render_template("404.html")

    return app
