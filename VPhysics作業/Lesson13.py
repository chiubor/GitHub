# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *
from visual.graph import *

#  1.  畫面設定
scene = display(width=600, height=400, background=(0.5,0.6,0.5), y=0)
arrow1 = arrow(display=scene, pos=(-1,0,0), axis=(2,0,0), shaftwidth=0.005)
arrow2 = arrow(display=scene, pos=(0,0,0), axis=(0,0.3,0), shaftwidth=0.005)

gd1 = gdisplay(x=600, y=0, title='v vs t', xtitle='t', ytitle='v', ymax=1, xmax=2, background=(0.3,0.3,0.3))
vt1 = gcurve(gdisplay=gd1, color=(0.5,0.5,0.5))
vt2 = gcurve(gdisplay=gd1, color=color.orange)

#  2.  物體設定
ball_iron = sphere(display=scene, radius=0.05, pos=(-0.2,0,0), color=(0.5, 0.5, 0.5), material=materials.rough)
ball_iron.m = 4
ball_iron.v = 0.25

ball_pingpong = sphere(display=scene, radius=0.02, pos=(0.1,0,0), color=color.orange)
ball_pingpong.m = 0.2
ball_pingpong.v = 0

#  3.  定義函數
def collide(v1,v2,m1,m2):
    v1f = v1*(m1-m2)/(m1+m2) + v2*2*m2/(m1+m2)
    v2f = v1*2*m1/(m2+m1) + v2*(m2-m1)/(m2+m1)
    return v1f, v2f

def collide2(ball1, ball2):
    return collide(ball1.v, ball2.v, ball1.m, ball2.m)  

#  4.  物體運動
dt = 0.001
t = 0
while t < 2:
    rate(200)
    t += dt
    ball_iron.pos.x = ball_iron.pos.x + ball_iron.v * dt
    vt1.plot(pos=(t, ball_iron.v))
    ball_pingpong.pos.x = ball_pingpong.pos.x + ball_pingpong.v * dt
    vt2.plot(pos=(t, ball_pingpong.v))

    if abs(ball_iron.pos-ball_pingpong.pos) < (ball_iron.radius+ball_pingpong.radius) and ball_iron.v > ball_pingpong.v:
#        ball_iron.v, ball_pingpong.v = collide(ball_iron.v,ball_pingpong.v,ball_iron.m,ball_pingpong.m)
        ball_iron.v, ball_pingpong.v = collide2(ball_iron, ball_pingpong)
