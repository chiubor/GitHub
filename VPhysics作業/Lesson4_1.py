# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *

# 重力加速度
g = vector(0, -9.8, 0)

# 1. 參數設定
#加速度
a = -9.8    #加速度值,在 x、z 方向為 0,在 y 方向為 g=-9.8 公尺/秒^2
#速度
vx = 5      #球的 x 方向速度(公尺/秒)
vy = 0      #球的 y 方向速度(公尺/秒)
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
floor = box(pos=(0,0,0), length=30, height=0.005, width=5)
#左牆
leftWall = box(pos =(-floor.length/2, h/2 ,0), length=floor.height, height=h, width=floor.width)
#右牆
rightWall = box(pos =(floor.length/2, h/2 ,0), length=floor.height, height=h, width=floor.width)

#球
ball = sphere(pos =(0, h ,0), radius=0.2, color=color.blue, make_trail= True)

# 3. 描述物體的運動

len = (floor.length - ball.radius)/2

while True:
    rate(1000)
    # 速度 = 速度 + 加速度 * 時間間隔
    vy += a * dt
    # 位置 = 位置 + 速度 * 時間間隔
    ball.pos.x += vx * dt
    ball.pos.y += vy * dt

    if ball.pos.y < ball.radius and vy < 0:
        vy = -vy
    if abs(ball.pos.x) > len:
        vx = -vx
