# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *

# 重力加速度
g = vector(0, -9.8, 0)

scene = display(center=vector(0,-1.0,0), background=(0.5,0.5,0))
ceiling = box(length=1, width=1, height = 0.01, color=color.blue)
ball = sphere(radius=0.1, color=color.red, make_trail=True)
ball.pos = vector(1,-1, 0)
ball.m = 0.5
ball.v = vector(0,0,0)

line1 = cylinder(pos=ceiling.pos, radius=0.01)
line1.axis = ball.pos-ceiling.pos
line1.L = line1.length

#釘子座標
nail = vector(0,-0.6,0)

line2 = cylinder(pos=nail, radius=0.01)
line2.axis = vector(0,0,0)
line2.L = line1.length - abs(nail)

K = 100000.0
dt = 0.001

line = line1

while True:
        rate(1000)
        if ball.pos.x < 0 and line != line2:
                line1.axis = nail-ceiling.pos
                line2.axis = ball.pos-nail
                line = line2
        elif ball.pos.x >= 0 and line != line1:
                line1.axis = ball.pos-ceiling.pos
                line2.axis = vector(0,0,0)
                line = line1

        ball.a = -(K/ball.m)*(line.length-line.L) * line.axis.norm() + g
        ball.v += ball.a * dt
        ball.pos += ball.v * dt
        line.axis = ball.pos - line.pos

