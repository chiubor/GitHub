# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *

# 1. 參數設定
#加速度
a = vector(0, -9.8, 0)    #加速度值,在 x、z 方向為 0,在 y 方向為 g=-9.8 公尺/秒^2
#速度
v = vector(0, 0, 0)    #速度值,在 x、y、z 方向為 0
#高度
h = 10.0    #球的初始高度，單位為公尺
#時間間隔
dt = 0.001  #畫面更新的時間間隔,單位為秒
#經過時間
t = 0       #模擬所經過的時間 ,單位為秒,初始值為0

# 2. 畫面設定
#畫布
scene = display(center = (0, h/2, 0), background=(0.5,0.6, 0))
#參考地板
floor = box(pos=(0,0,0), length=15, height=0.005, width=5)
#球
ball = sphere(pos=(0, h, 0), radius=0.2, color=color.blue)
#速度箭頭
v_arrow = arrow(pos = ball.pos, axis=v, shaftwidth=0.1)

# 3. 描述物體的運動
while ball.pos.y > 0.2:
        rate(1000)
        # 速度 = 速度 + 加速度 * 時間間隔
        v = v + a * dt
        # 位置 = 位置 + 速度 * 時間間隔
        ball.pos= ball.pos+ v* dt
        # 更新速度箭頭資料
        v_arrow.pos = ball.pos
        v_arrow.axis = v/5
