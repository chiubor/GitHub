from visual import *

g = 9.8             #重力加速度 9.8 m/s^2
size = 0.05         #球半徑 0.05 m
r = 0.5             #彈簧原長 0.5m
k = 10              #彈簧力常數 10 N/m
m = 0.2             #球質量 0.2 kg

scene = display(width=800, height=800, center=(0, -r*0.6, 0), background=(0.5,0.5,0))  #設定畫面
ceiling = box(length=0.8, height=0.005, width=0.8, color=color.blue)                    #畫天花板
ball = sphere(radius = size,  color=color.red)                              #畫球
spring = helix(radius=0.02, thickness =0.01)                                #畫彈簧,不動端在(0,0,0)

ball.pos0 = vector(0, -r, 0) 					#球的初位置，即彈簧運動端的初位置
ball.pos = vector(0, -r , 0)        					#球在時間＝０時的位置
ball.v = vector(0, 0, 0)            					#球初速

ball_v_arrow = arrow(shaftwidth = 0.01)
ball_a_arrow = arrow(shaftwidth = 0.01)

dt = 0.001   
while True:
    rate(100)
    spring.axis = ball.pos - spring.pos 		#彈簧的全長＝彈簧不動端的位置向量到球現在的位置向量

    ball.a = vector(0, - g - k * (ball.pos.y - ball.pos0.y )/m , 0)
						#球的加速度的y分量 = - g - k*(彈簧伸長量)/m

    ball.v +=   ball.a*dt
    ball.pos += ball.v*dt

    ball_v_arrow.pos = ball.pos + vector(size, 0, 0)
    ball_v_arrow.axis = ball.v / 5.0

    ball_a_arrow.pos = ball.pos - vector(size, 0, 0)
    ball_a_arrow.axis = ball.a / 50.0
