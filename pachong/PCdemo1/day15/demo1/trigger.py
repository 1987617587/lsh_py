import time

from tasks import add

print('===')
# 把一个执行的任务放入任务队列
result = add.delay(4,4) # 注意这里不是直接调用add(4,4)


while not result.ready():# ready()如果任务执行完返回True否则返回False
    time.sleep(1)

print(f'task done:{result.get()}')# get()获取任务执行的结果
