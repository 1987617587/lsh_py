# author : Lsh
# date: 2019/12/24 9:49
# file_name:tree2

from turtle import *
from random import random, randint

screen = Screen()
width, height = 800, 600
screen.setup(width, height)
screen.title("模拟3D星空_海龟画图版_作者:李兴球")
screen.bgcolor("black")
screen.mode("logo")
screen.delay(0)
# 这里要设为0，否则很卡

t = Turtle(visible=False, shape='circle')
t.pencolor("white")
t.fillcolor("white")
t.penup()
t.setheading(-90)
t.goto(width / 2, randint(-height / 2, height / 2))

stars = []
for i in range(200):
    star = t.clone()
    s = random() / 3
    star.shapesize(s, s)
    star.speed(int(s * 10))
    star.setx(width / 2 + randint(1, width))
    star.sety(randint(-height / 2, height / 2))
    star.showturtle()
    stars.append(star)

while True:
    for star in stars:
        star.setx(star.xcor() - 3 * star.speed())
        if star.xcor() < -width / 2:
            star.hideturtle()
            star.setx(width / 2 + randint(1, width))
            star.sety(randint(-height / 2, height / 2))
            star.showturtle()
# ————————————————
# 版权声明：本文为CSDN博主「李兴球」的原创文章，遵循 CC 4.0 BY-SA 版权协议，转载请附上原文出处链接及本声明。
# 原文链接：https://blog.csdn.net/avskya/article/details/81125576
