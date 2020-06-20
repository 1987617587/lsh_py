from celery import Celery
# 使用第二个redis数据库作为我们的任务队列
uri = 'redis://@127.0.0.1:6379/2'
# 有密码
# uri = 'redis://:123456@127.0.0.1:6379/2'
# broker指定任务队列
# backend 指定任务执行结果的存储
app = Celery('tasks',broker=uri,backend=uri)

# 定义认为函数
# 装饰器 @app.task 实际上是将一个正常的函数修饰成了一个 celery task 对象
@app.task
def add(x,y):
    return x+y