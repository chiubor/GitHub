# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *

# 重力加速度
g = vector(0, -9.8, 0)

scene = display(center=vector(0,-1.0,0), background=(0.5,0.5,0))
ceiling = box(length=1, width=1, height = 0.01, color=color.blue)
ball1 = sphere(radius=0.1, color=color.red, make_trail=True)
ball2 = sphere(radius=0.1, color=color.red, make_trail=True)

ball1.pos = vector(1,-1, 0)
ball1.m = 0.5
ball1.v = vector(0,0,0)

line1 = cylinder(radius = 0.01)
line1.pos = ceiling.pos + (ball1.radius, 0, 0)
line1.axis = ball1.pos - line1.pos
line1.L = line1.length

ball2.pos = vector(-ball1.radius, -line1.L, 0)
ball2.m = 0.5
ball2.v = vector(0,0,0)

line2 = cylinder(radius = 0.01)
line2.pos = ceiling.pos - (ball1.radius, 0, 0)
line2.axis = ball2.pos - line2.pos
line2.L = line2.length


# 函數定義
def collide(v1,v2,m1,m2):
    v1f = v1*(m1-m2)/(m1+m2) + v2*2*m2/(m1+m2)
    v2f = v1*2*m1/(m2+m1) + v2*(m2-m1)/(m2+m1)
    return v1f, v2f

K = 100000.0

dt = 0.001

balls = [[ball1, line1], [ball2, line2]]

while True:
    rate(1000)

    for ball, line in balls:
        ball.a = -(K/ball.m)*(line.length-line.L) * line.axis.norm() + g
        ball.v += ball.a * dt
        ball.pos += ball.v * dt
        line.axis = ball.pos - line.pos

    # 兩球碰撞
    if abs(ball1.pos-ball2.pos) <= ball1.radius + ball2.radius :
        ball1.v, ball2.v = collide(m1=ball1.m, v1=ball1.v, v2=ball2.v, m2=ball2.m)
        
