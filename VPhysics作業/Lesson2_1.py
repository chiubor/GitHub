# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *

#產生一個寬400像素，高400像素的3度空間以進行繪圖
scene = display(width=400, height=400,center=(0,0.06,0))
#產生一個扁長形方塊，當做是地板
floor = box(pos=(0,-0.005/2,0), length=0.3, height=0.005, width=0.1)
#產生一個正立方物體
cube = box(pos=(0, 0.05/2, 0), length=0.05, height=0.05, width=0.05)

#----------
# 參數設定
#----------

#速度
v = 0.03    #物體速度 = 0.03 (公尺/秒)
#時間間隔
dt = 0.001  #畫面更新的時間間隔，單位為秒
#經過時間
t = 0       #模擬所經過的時間，單位為秒，初始值為0

#-------------
#一維等速運動
#-------------
while cube.pos.x < 0.1:
    rate(1000)
    # 位置 += 速度 * 時間
    cube.pos.x += v * dt
    t = t + dt

while cube.pos.x > -0.1:
    rate(1000)
    cube.pos.x -= v * dt
    t = t + dt   

print t
