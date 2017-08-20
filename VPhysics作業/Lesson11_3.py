# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *

#  1. 參數設定
#球半徑 0.05 m
size = 0.05
#地板長
L = 1.0
#時間間隔
dt = 0.001

#  2. 畫面設定
scene = display(width=800, height=800, background=(0.5,0.6,0.5))
bottom = box(pos=(0,-size,0), length=2*L, height=0.001, width=2)
wall = box(pos=(L,-size/2,0), length=0.01, height=size, width=2)

#3. 球的設定
ball_marble = sphere(pos=(-L,0,0), radius=size, material=materials.marble)
ball_marble.v = 0.5

#  4. 運動
while True:
    rate(1000)
    ball_marble.pos.x += ball_marble.v * dt
    ball_marble.rotate(axis=(0,0,1), angle=-ball_marble.v*dt/size)
    if ball_marble.pos.x >= L-size :
        ball_marble.v = 0
