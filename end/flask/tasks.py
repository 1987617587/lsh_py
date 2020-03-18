import os
import time

from celery import Celery
# 实例
from flask_mail import Message
from flask import current_app
from factory import creat_app

from views import mail

cel = Celery("tasks", broker="redis://127.0.0.1:6379/13", backend="redis://127.0.0.1:6379/13")
os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')


# 构建任务
@cel.task()
def work1():
    print("开始执行任务1")
    time.sleep(5)
    print("执行任务1完成，耗时5秒")
    return 1000


@cel.task()
def sendmail(username, serstr):

    # with current_app.app_context():
    with creat_app().app_context():
        print("准备发送")
        msg = Message(subject="神秘组织激活邮件", recipients=[username])
        # msg.html = "<a href='http://127.0.0.1:5000/active/" + str(r2[0]) + "'>点击激活</a>"
        msg.html = "<a href='http://127.0.0.1:5000/active/%s'>点击激活</a>" % (serstr,)
        mail.send(msg)
