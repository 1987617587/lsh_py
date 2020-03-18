from factory import creat_app

if __name__ == "__main__":
    # http: // 127.0.0.1: 5000 / 是默认的IP和端口
    creat_app().run()
    # 如果要自定义端口则需要使用
    # app.run(host="0.0.0.0", port=19011)
