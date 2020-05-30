# author : Lsh
# date: 2019/12/24 15:03
# file_name:shengdan

import turtle as T
import random
import time

n = 100.0

T.speed("fastest")
T.screensize(bg='seashell')
T.left(90)
T.forward(3*n)
T.color("orange", "yellow")
T.begin_fill()
T.left(126)

for i in range(5):
    T.forward(n/5)
    T.right(144)
    T.forward(n/5)
    T.left(72)
T.end_fill()
T.right(126)

T.color("dark green")
T.backward(n*4.8)
def tree(d, s):
    if d <= 0: return
    T.forward(s)
    tree(d-1, s*.8)
    T.right(120)
    tree(d-3, s*.5)
    T.right(120)
    tree(d-3, s*.5)
    T.right(120)
    T.backward(s)
tree(15, n)
T.backward(n/2)

for i in range(200):
    a = 200 - 400 * random.random()
    b = 10 - 20 * random.random()
    T.up()
    T.forward(b)
    T.left(90)
    T.forward(a)
    T.down()
    if random.randint(0, 1) == 0:
            T.color('tomato')
    else:
        T.color('wheat')
    T.circle(2)
    T.up()
    T.backward(a)
    T.right(90)
    T.backward(b)

time.sleep(60)