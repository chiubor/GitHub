# -*- coding: cp950 -*-
from visual import *
q = 1.6 * 10 ** -19     #質子電量(C) 
m = 1.67 * 10 ** -27    #質子質量(kg)
B = (0, 1, 0)           #外加磁場(T)

scene = display(width=800, height=600, x = 300, y =0,  background=(0.5,0.5,0))  #設畫面
p = sphere(radius=1E-11,color=color.yellow, make_trail=True)     #畫質子, 且留下軌跡
pointer = arrow(pos=(-5E-10,0,0),axis=(0,4E-10,0))              #畫磁場箭頭

p.pos = vector(0.0,0.0,0.0)             #質子初位置
p.v = vector(2*10**-2, 10**-3, 0)       #質子初速度
            
dt = 1E-12
while true:
    rate(100000)

    F =  q * cross(p.v , B)             # F = q v x B

    p.v = p.v + F / m * dt                   # a = F/m
    p.pos = p.pos + p.v * dt
    




