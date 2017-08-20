# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *
from visual.graph import *

# 1. 參數設定
# 重力加速度
g = -9.8
# 時間間隔
dt = 0.0001
# 經過時間
t=0

# 2. 畫面設定
# 畫布
scene = display(width=600, height=600, background=(0.5,0.6,0.5), center=(0,2,0), range=5)
# 地板
#floor = box(pos=(0,-0.2,0), length=5, height=0.1, width=5, material=materials.wood)
floor = box(pos=(0,-0.05,0), length=5, height=0.1, width=5, material=materials.wood)
# 兩球高度時間圖
gd = gdisplay(x=600, y=0, title='y vs t', xtitle='t', ytitle='y', ymax=13, xmax=10, background=(0.3,0.3,0.3))
yt1 = gcurve(gdisplay=gd, color=color.cyan)
yt2 = gcurve(gdisplay=gd, color=color.red)
yt3 = gcurve(gdisplay=gd, color=color.yellow)

# 3. 球的設定
ball1 = sphere(radius=0.05, color=color.cyan, v=0, m=0.2)
ball2 = sphere(radius=0.1,  color=color.red, v=0, m=0.6)
ball3 = sphere(radius=0.15,  color=color.yellow, v=0, m=1.0)

ball3.pos = (0,2,0)
ball2.pos=(0,2+ball2.radius+ball3.radius+0.05,0)
ball1.pos=(0,2+ball1.radius+ball2.radius*2+ball3.radius+0.05,0)

# 4. 函數定義
def collide(v1,v2,m1,m2):
    v1f = v1*(m1-m2)/(m1+m2) + v2*2*m2/(m1+m2)
    v2f = v1*2*m1/(m2+m1) + v2*(m2-m1)/(m2+m1)
    return v1f, v2f

# 5. 運動部分
while t<=10:
    rate(2000)
    t = t + dt
    ball1.v = ball1.v + g * dt
    ball1.pos.y = ball1.pos.y + ball1.v * dt
#    if ball1.pos.y <= 0:
    if ball1.pos.y <= ball3.radius*2+ball2.radius*2+ball1.radius:
        ball1.v = -ball1.v
    yt1.plot( pos = (t, ball1.pos.y))

    ball2.v = ball2.v + g * dt
    ball2.pos.y = ball2.pos.y + ball2.v * dt
#    if ball2.pos.y <= 0:
    if ball2.pos.y <= ball3.radius*2+ball2.radius:
        ball2.v = -ball2.v
    yt2.plot( pos = (t, ball2.pos.y))

    ball3.v = ball3.v + g * dt
    ball3.pos.y = ball3.pos.y + ball3.v * dt
#    if ball3.pos.y <= 0:
    if ball3.pos.y <= ball3.radius:
        ball3.v = -ball3.v
    yt3.plot( pos = (t, ball3.pos.y))

    # 上兩球碰撞
    if abs(ball1.pos-ball2.pos) <= ball1.radius + ball2.radius :
        ball1.v, ball2.v = collide(m1=ball1.m, v1=ball1.v, v2=ball2.v, m2=ball2.m)

    # 下兩球碰撞
    if abs(ball2.pos-ball3.pos) <= ball2.radius + ball3.radius :
        ball2.v, ball3.v = collide(m1=ball2.m, v1=ball2.v, v2=ball3.v, m2=ball3.m)

