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

line = cylinder(radius = 0.01)
line.pos = ceiling.pos
line.axis = ball.pos - ceiling.pos
line.L = line.length
K = 100000.0

dt = 0.001

while True:
        rate(1000)
#        F = - K * (line.length-line.L) * line.axis.norm()
#        ball.a = vector(0,-g,0) + F/ball.m
        ball.a = -(K/ball.m)*(line.length-line.L) * line.axis.norm() + g
        ball.v += ball.a * dt
        ball.pos += ball.v * dt
        line.axis = ball.pos - line.pos
