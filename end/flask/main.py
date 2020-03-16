from flask import Flask, request, render_template

# 创建实例
app = Flask(__name__)
# 开启调试模式，修改代码不需要重启
app.debug = True


@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        # return "请先登录"
        return render_template('login.html')
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        return render_template('booklist.html', booklist=["倚天屠龙记", "神雕侠侣", "天龙八部"], username=username)


# def hello_world():
#     # return '<h1>Hello, World!</h1>'
#     # 使用静态文件模板
#     return render_template('index.html')


@app.route('/about')
def about():
    return '这是关于页面'


@app.route('/books', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # return "<h1>GET</h1>"
        # 使用静态文件模板 并传参
        return render_template('booklist.html', booklist=["倚天屠龙记", "神雕侠侣", "天龙八部"], username="zzy")

    elif request.method == "POST":
        return "<h1>POST</h1>"


if __name__ == "__main__":
    # http: // 127.0.0.1: 5000 / 是默认的IP和端口
    app.run()
    # 如果要自定义端口则需要使用
    # app.run(host="0.0.0.0", port=19011)
