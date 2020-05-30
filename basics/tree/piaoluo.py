# author : Lsh
# date: 2019/12/24 14:50
# file_name:piaoluo
import time
import turtle as T
from random import *
from math import *

def tree(n,l):
    T.pd()#下笔
    #阴影效果
    t = cos(radians(T.heading()+45))/8+0.25
    T.pencolor(t,t,t)
    T.pensize(n/3)
    T.forward(l)#画树枝

    if n>0:
        b = random()*15+10 #右分支偏转角度
        c = random()*15+10 #左分支偏转角度
        d = l*(random()*0.25+0.7) #下一个分支的长度
        #右转一定角度,画右分支
        T.right(b)
        tree(n-1,d)
        #左转一定角度，画左分支
        T.left(b+c)
        tree(n-1,d)
        #转回来
        T.right(c)
    else:
        #画叶子
        T.right(90)
        n=cos(radians(T.heading()-45))/4+0.5
        T.pencolor(n,n*0.8,n*0.8)
        T.circle(3)
        T.left(90)
        #添加0.3倍的飘落叶子
        if(random()>0.7):
            T.pu()
            #飘落
            t = T.heading()
            an = -40 +random()*40
            T.setheading(an)
            dis = int(800*random()*0.5 + 400*random()*0.3 + 200*random()*0.2)
            T.forward(dis)
            T.setheading(t)
            #画叶子
            T.pd()
            T.right(90)
            n = cos(radians(T.heading()-45))/4+0.5
            T.pencolor(n*0.5+0.5,0.4+n*0.4,0.4+n*0.4)
            T.circle(2)
            T.left(90)
            T.pu()
            #返回
            t=T.heading()
            T.setheading(an)
            T.backward(dis)
            T.setheading(t)
    T.pu()
    T.backward(l)#退回
    # time.sleep(0.01)


T.bgcolor(0.5,0.5,0.5)#背景色
T.ht()#隐藏turtle
T.speed(0)#速度 1-10渐进，0 最快
T.tracer(0,0)
T.pu()#抬笔
T.backward(100)
T.left(90)#左转90度
T.pu()#抬笔
T.backward(300)#后退300
tree(12,100)#递归7层


T.done()
