# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *

#  1. 參數設定
#球半徑 0.05 m
size = 0.5
#時間間隔
dt = 0.001

#  2. 畫面設定
scene = display(width=800, height=800, background=(0.5,0.6,0.5))
# x軸箭頭
x_axis = arrow(axis=(1, 0, 0), shaftwidth=0.01)
# y軸箭頭
y_axis = arrow(axis=(0, 1, 0), shaftwidth=0.01)
# z軸箭頭
z_axis = arrow(axis=(0, 0, 1), shaftwidth=0.01)


#3. 球的設定
earth = sphere(pos=(0,0,0), radius=size, material=materials.earth)
marble = sphere(pos=(1,0,0), radius=size, material=materials.marble)
bricks = sphere(pos=(-1,0,0), radius=size, material=materials.bricks)
wood = sphere(pos=(-2,0,0), radius=size, material=materials.wood)
rough = sphere(pos=(2,0,0), radius=size, material=materials.rough)

balls = [earth, marble, bricks, wood, rough]

#  4. 運動
while True:
    rate(1000)
    for ball in balls:
        ball.rotate(axis=(0,0,1), angle=-2*dt)
