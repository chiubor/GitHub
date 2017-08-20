# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *
from visual.graph import *

# 1. 參數設定
# 木塊質量 0.5 kg
m = 0.5
# 彈簧的彈性係數 10 N/m
k = 10.0
# 時間間隔
dt = 0.001
# 經過時間
t = 0

# 2. 畫面設定
# 畫布
scene = display(width=1000, height=1000, background=(0.5,0.6,0.5))
# 位置圖
gd1 = gdisplay(x=800, y=0, xtitle='t(s)', ytitle='x(m)', ymax=1, xmax=20, ymin=-1)
tx = gcurve(gdisplay=gd1, color=color.yellow)
# 地板
floor = box(length=3, height=0.01, width=1, material=materials.silver)
# 牆面
wall = box(length=0.01, height=0.5, width=1, material=materials.silver)
# 木塊
square = box(length=0.2, height=0.2, width=0.2, material=materials.wood)
# 彈簧
spring = helix(radius=0.06, coils=15, thickness = 0.03)

# 設定地板位置
floor.pos = (0, 0, 0)
# 設定牆面位置
wall.pos = (-floor.length/2, wall.height/2, 0)
# 設定木塊位置
square.pos = (0, square.height/2, 0)
# 設定木塊初速
square.v = vector(2,0,0)
# 設定彈簧位置
spring.pos = (-floor.length/2, square.height/2,0)
# 設定彈簧軸線(長度)
spring.axis = square.pos-spring.pos-square.axis/2
# 取得彈簧原長
spring.L = spring.length

# 3. 運動部分
while True:
    rate(1000)
    #彈簧的加速度 a= ( k / m ) * 彈簧的伸長量 * 彈簧的反方向
    square.a = -(k/m)*(spring.length-spring.L) * spring.axis.norm()
    square.v = square.v + square.a * dt
    square.pos = square.pos + square.v * dt
    #求出彈簧的長度
    spring.axis = square.pos-spring.pos-square.axis/2

    # 畫出x軸位置圖
    t = t + dt
    tx.plot(pos=(t, square.pos.x))

