from main import render_template,app,request
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


@app.route("/list")
def list():
    # 内容需要查询数据库
    categorylist = [
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
    return render_template("categorylist.html", categories=categorylist, user=user)



@app.route('/books', methods=["GET", "POST"])
def index():
    if request.method == "GET":
        # return "<h1>GET</h1>"
        # 使用静态文件模板 并传参
        return render_template('booklist.html', booklist=["倚天屠龙记", "神雕侠侣", "天龙八部"], username="zzy")

    elif request.method == "POST":
        return "<h1>POST</h1>"

