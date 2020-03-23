from flask import Flask, request

app = Flask(__name__)


@app.route("/")
def index():
    # return "首页"
    # return "<h1>请在本页面填入你的个人信息，本系统自动对你的安全性评估</h1>"
    return "<h1>这里是首页</h1>"


@app.route("/userinfo", methods=["GET", "POST"])
def userinfo():
    print(request.method)
    if request.method == "GET":
        # return "<h1>这里是个人信息页面</h1>"
        return "<h1>请在本页面填入你的个人信息，本系统自动对你的安全性评估</h1>"
    elif request.method == "POST":
        return "正在获取你的信息"


app.debug = True

if __name__ == '__main__':
    app.run()
