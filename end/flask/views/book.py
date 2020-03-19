from flask import render_template, request, flash, Blueprint
from werkzeug.utils import redirect
from models import *

# 新建用户模块蓝图
books_bp = Blueprint("book", __name__)


@books_bp.route('/')
def index():
    # c = Category()
    # c.name = "武侠"
    # db.session.add(c)
    #
    # c1 = Category()
    # c1.name = "科幻"
    # db.session.add(c1)
    #
    # c2 = Category()
    # c2.name = "玄幻"
    # db.session.add(c2)
    #
    # c3 = Category()
    # c3.name = "言情"
    # db.session.add(c3)
    #
    # db.session.commit()

    cs = Category.query.all()
    return render_template("categories.html", cs=cs)


@books_bp.route("/categories", methods=["GET", "POST"])
def categories():
    return "分类"


@books_bp.route("/categories/<id>", methods=["GET", "POST"])
def category(id):
    c = Category.query.filter_by(id=id).first()

    if c:
        # 表关联查询
        # bs = Book.query.filter_by(cid=c.id).all()
        # bs[0].cid

        # 关系字段查询
        bs = c.books
        print(bs[0].category.id, bs[0].category.name)
        return render_template("category.html", bs=bs)
    return "输入不合法"
