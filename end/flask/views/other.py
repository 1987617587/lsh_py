from flask import Blueprint, render_template

get404_bp = Blueprint("other", __name__)

# 蓝图注册404暂时不可用
@get404_bp.errorhandler(404)
def page_not_found(error):
    return render_template("404.html")
