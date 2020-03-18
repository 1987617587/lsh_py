from flask import render_template, request, flash, Blueprint
from werkzeug.utils import redirect
# 新建用户模块蓝图
books_bp = Blueprint("book", __name__)


@books_bp.route("/", methods=["GET", "POST"])
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
