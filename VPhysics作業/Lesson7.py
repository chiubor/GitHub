# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *

#  1. 畫面設定
# 畫布
scene = display(center=(0, 0.3, 0.2), width=1000, height=1000, background=(0.5,0.6,0.5))
# 桌面
table = cylinder(pos=(0,-0.03,0), axis=(0,-0.01,0), radius=0.7, material=materials.wood)
# 圓心
center = cylinder(pos=(0, -0.03, 0), axis = (0, 0.03, 0), radius = 0.007)
# 球
ball = sphere(pos=(-0.5,0,0), radius=0.03, color=color.blue)

#  2. 設定參數、初始值
ball.v = vector(0, 0, 0.5)
r = abs(ball.pos)

print "速度 = ", abs(ball.v)
print "時間週期 = ", 2*pi*r / abs(ball.v)

# 時間間隔
dt = 0.001

# 設定箭頭
ball.a = -(abs(ball.v)**2 / r) * (ball.pos/r)
a_arrow = arrow(pos = ball.pos, axis=ball.a, shaftwidth=0.01)
v_arrow = arrow(pos = ball.pos, axis=ball.v, shaftwidth=0.01)

#  3. 運動部分
while True:
    rate(1000)

    # 更新球的資料
    ball.a = -(abs(ball.v)**2 / r) * (ball.pos/r)
    ball.v += ball.a*dt
    ball.pos += ball.v*dt
    
    # 更新箭頭資料
    a_arrow.pos = ball.pos
    a_arrow.axis = ball.a

    v_arrow.pos = ball.pos
    v_arrow.axis = ball.v
