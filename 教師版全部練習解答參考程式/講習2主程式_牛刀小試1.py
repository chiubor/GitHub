﻿from visual import *

g = 9.8             #重力加速度 9.8 m/s^2
size = 0.05         #球半徑 0.05 m
r = 0.5             #彈簧原長 0.5m
k = 10              #彈簧力常數 10 N/m
m = 0.2             #球質量 0.2 kg

scene = display(width=800, height=800, background=(0.5,0.5,0))  #設定畫面
floor = box(length=1.5, height=0.005, width=1.5, color=color.blue)                    #畫地板
ball = sphere(radius = size,  color=color.red)                              #畫球
spring = helix(radius=0.02, thickness =0.01)                                #畫彈簧,不動端在(0,0,0)

spring.pos = vector(0, size, 0)
ball.pos0 = vector(r, size, 0) 					#球的初位置，即彈簧運動端的初位置
ball.pos = vector(r, size , 0)        					#球在時間＝０時的位置
ball.v = vector(1.5, 0, 0)            					#球初速

dt = 0.001   
while True:
    rate(1000)
    spring.axis = ball.pos - spring.pos 		#彈簧的全長＝彈簧不動端的位置向量到球現在的位置向量

    ball.a = vector( - k * (ball.pos.x - ball.pos0.x )/m, 0 , 0)
						#球的加速度的x分量 = - k*(彈簧伸長量)/m

    ball.v +=   ball.a*dt
    ball.pos += ball.v*dt
