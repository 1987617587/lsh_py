from flask import Blueprint, render_template, session, request
from werkzeug.utils import redirect

from models import *
from .utils import checklogin

# 新建用户模块蓝图
admin_bp = Blueprint("admin", __name__)


# @admin_bp.route("/admin", methods=["GET"])
# def admin():
#     """
#     查看用户是否登录
#     登录admin账户进入本页面 其他用户去主页
#     未登录先去登录 然后进入相应页面
#     :return:相应页面
#     """
#     # user = request.cookies.get("user")
#     user = session.get("user")
#     if user:
#         print("登陆成功")
#
#         # return "管理员页面"
#         cs = Category.query.all()
#         bs = Book.query.all()
#
#         return render_template('admin/admin.html', cs=cs, bs=bs)
#
#     else:
#         return redirect("/login?next=/admin")

# 使用装饰器检测是否登录
@admin_bp.route("/admin", methods=["GET"])
@checklogin
def admin():
    cs = Category.query.all()
    bs = Book.query.all()
    return render_template('admin/admin.html', cs=cs, bs=bs)


@admin_bp.route("/admin/<resource_type>/add", methods=["GET", "POST"])
@checklogin
def add(resource_type):
    if request.method == "GET":
        fields = []
        # if resource_type == "category":
        #     ps = dir(Category)
        #     for p in ps:
        #         if (not p.startswith("__")) and (not p.startswith("_")) and (
        #                 p not in ["metadata", "query", "query_class", "id", "books"]):
        #             fields.append(p)
        # if resource_type == "book":
        #     # ps = dir(Book)
        #     ps = dir(Category)
        #
        #     for p in ps:
        #         if (not p.startswith("__")) and (not p.startswith("_")) and (
        #                 p not in ["metadata", "query", "query_class", "id", "books"]):
        #             fields.append(p)
        # 使用字符串映射类名
        resource = globals()[resource_type.capitalize()]
        ps = dir(resource)
        for p in ps:
            if (not p.startswith("__")) and (not p.startswith("_")) and (
                    p not in ["metadata", "query", "query_class", "id", "books"]):
                fields.append(p)
        return render_template("admin/add.html", fs=fields)

    else:

        resource = globals()[resource_type.capitalize()]
        print(resource)
        r = resource()
        r.name = request.form["addname"]
        # r.cid = 3
        db.session.add(r)
        db.session.commit()
        return redirect("/admin")


@admin_bp.route("/admin/<resource_type>/del/<id>", methods=["GET", "POST"])
@checklogin
def delete(resource_type, id):
    if request.method == "GET":
        if resource_type == "category":
            c = Category.query.filter_by(id=id).first()
            db.session.delete(c)
            db.session.commit()

        if resource_type == "book":
            b = Book.query.filter_by(id=id).first()
            db.session.delete(b)
            db.session.commit()

        return redirect("/admin")
    # return resource_type
