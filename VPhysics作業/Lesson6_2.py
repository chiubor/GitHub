# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *

# 1. 參數設定
#球的半徑
size = 0.2  #球的半徑，單位為公尺
#加速度
g = vector(0,-9.8,0)    #加速度值,在 x、z 方向為 0,在 y 方向為重力加速度 -9.8 公尺/秒^2
#時間間隔
dt = 0.001  #畫面更新的時間間隔,單位為秒
#經過時間
t = 0       #模擬所經過的時間 ,單位為秒,初始值為0

# 2. 畫面設定
#畫布
scene = display(center = (15, 5, 0), background=(0.5,0.6, 0.5))
#參考地板
floor = box(pos=(15,-0.05,0), length=30, height=0.1, width=5)
#球
ball = sphere(pos=(0, 0, 0), radius=size, color=color.blue, make_trail= True)

# 3.初始條件
ball.v = vector(5, 10, 0)

v_arrow = arrow(pos = ball.pos, axis=ball.v, shaftwidth=0.1)

# 4. 描述物體的運動

while t < 5:
    rate(1000)
    # 速度 = 速度 + 加速度 * 時間間隔
    ball.v += g * dt
    # 位置 = 位置 + 速度 * 時間間隔
    ball.pos += ball.v * dt


    # 判斷球是否碰到地面
    if ball.pos.y <= ball.radius:
        ball.v.y = abs(ball.v.y)

    v_arrow.pos = ball.pos
    v_arrow.axis = ball.v/5


    #計算時間
    t = t + dt
