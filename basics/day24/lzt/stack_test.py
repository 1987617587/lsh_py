# author:lzt
# date: 2019/12/5 9:53
# file_name: stack_test
# 导入栈的类
from queue import LifoQueue

# 创建一个栈:
bullets = LifoQueue()

# 如何进栈
bullets.put("第一颗子弹")
bullets.put("第二颗子弹")
bullets.put("第三颗子弹")
bullets.put("第四颗子弹")
bullets.put("第五颗子弹")
bullets.put("第六颗子弹")

# 判断栈空?
print(bullets.empty())

# 栈中的元素数
print(bullets.qsize())

# 查看栈中的所有数据
for i in bullets.queue:
    print(i)

print("**************************")

# 抠出坏弹
temp = LifoQueue()
while 1:
    # 从原弹夹中扣出子弹
    bullet = bullets.get()
    if bullet != "第四颗子弹":
        temp.put(bullet)
    else:
        break

# 还原弹夹
while not temp.empty():
    bullets.put(temp.get())

print("**************************")
# 所有子弹开始开火击发
while not bullets.empty():
    print(f"击发了{bullets.get()}")
