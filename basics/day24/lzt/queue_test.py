# author:lzt
# date: 2019/12/5 9:07
# file_name: queue_test
# 导入的队列的模块和类
from queue import Queue

# 产生一个队列
qu = Queue()

# 元素入队 进队
qu.put("第一个人")
qu.put("第二个人")
qu.put("第三个人")

# 队伍空不空?
print(qu.empty())

# 队伍的长度
print(qu.qsize())

# 迭代查看队列的所有元素
# for i in qu:
#     print(i)
# print(qu.queue)
# for i in qu.queue:
#     print(i)

# try:
#     # 所有人依次出队：
#     # print(qu.get())
#     # print(qu.get())
#     # print(qu.get())
#     # print(qu.get_nowait())
#     while not qu.empty():
#         print(qu.get())
# except:
#     print("队伍中没有更多的数据了！")


# 构建模拟圆环数据的队列
qu2 = Queue()
mod = 13
# 模拟一些数据放入:
for i in range(5):
    qu2.put(f"第{i + 1}个人")

# 模拟出队和入队
# 计数器
count = 0
while qu2.qsize() != 1:
    # 出队报数
    data = qu2.get()
    count += 1

    # 判断报的数字是否为mod或被mod整除
    if count % mod == 0:
        print(f"{data}out")
    else:
        # 再次入队
        qu2.put(data)

print(f"{qu2.get()}Win")
