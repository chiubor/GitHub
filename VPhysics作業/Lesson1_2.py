# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *

#產生一個寬400像素，高400像素的3度空間以進行繪圖
scene = display(width=400, height=400, center=(0,0.06,0))
#產生一個扁長形方塊，當做是地板
floor = box(pos=(0,-0.005/2,0), length=0.3, height=0.005, width=0.1)

#產生一個正立方物體
cube = box(pos=(0, 0.05/2, 0), length=0.05, height=0.05, width=0.05)

#邊界設定
right = (floor.length - cube.length)/2
bottom = (floor.width - cube.width)/2
left = -right
top = -bottom

#讓物體運動
cube.pos.x = left
cube.pos.z = top

while True:
    while cube.pos.x < right:
        rate(100)
        cube.pos.x += 0.001

    while cube.pos.z < bottom:
        rate(100)
        cube.pos.z += 0.001
        
    while cube.pos.x > left:
        rate(100)
        cube.pos.x -= 0.001

    while cube.pos.z > top:
        rate(100)
        cube.pos.z -= 0.001    
