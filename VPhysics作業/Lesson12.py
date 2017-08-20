# -*- coding: utf8 -*-
# 匯入視覺化套件
from visual import *

#  1. 參數設定
#物質密度 單位: kg/m**3
density_bricks = 400.0
density_marble = 900.0
density_earth = 2600.0
#球半徑 0.05m
size = 0.05
#地板長
L = 1.00
#時間間隔
dt = 0.001
#體積
V = (4/3)*pi*(size)**3
#初始動量 kg*m/s
P = 0.1

#  2. 畫面設定
scene = display(width=800, height=800, background=(0.5,0.6,0.5))
bottom = box(pos=(0,-size,0), length=2*L, height=0.001, width=2)
wall = box(pos=(L,-size/2,0), length=0.01, height=size, width=2)

#  3. 球的設定
ball_bricks = sphere(pos=(-L,0,-0.40), radius=size, material=materials.bricks)
ball_marble = sphere(pos=(-L,0,0), radius=size, material=materials.marble)
ball_earth = sphere(pos=(-L,0,0.40), radius=size, material=materials.earth)

balls = [ball_bricks, ball_marble, ball_earth]

#質量
ball_bricks.m = V*density_bricks
ball_marble.m = V*density_marble
ball_earth.m = V*density_earth

#速度
for ball in balls:
    ball.v = P / ball.m

#  4. 運動
while True:
    rate(1000)
    for ball in balls:
        ball.pos.x = ball.pos.x + ball.v * dt
        ball.rotate(axis=(0,0,1), angle = -ball.v*dt/size)
        if ball.pos.x >= L-size:
            ball.v = 0
