"""
# author Liu shi hao
# date: 2019/12/5 9:47
# file_name: stsck_test

"""
from queue import LifoQueue
s = LifoQueue(6)
for i in range(6):
    s.put(f"第{i+1}颗子弹")

for j in s.queue:
    print(j)

s1 = LifoQueue(5)

while not s.empty():
    n = s.get()
    if n != "第4颗子弹":
        s1.put(n)


for i in range(5):
    s.put(s1.get())

for k in s.queue:
    print(k)





















































































