from visual import *
g = 9.8             			#重力加速度 9.8 m/s^2
L = 4.9             			#板長度
size = 0.1          			#球半徑 0.1m
th = 30 * pi / 180  		#板斜度 30度
dt = 0.001

scene = display(width=900, height=900, background=(0.5,0.5,0))
scene.center = (0,(L-2*size)*sin(th)/2,0)					#設定視窗中心點
scene.forward = (-2, 0, -1)							#設定視窗視角方向
board = box(length=L, height=0.001, width=1)				#畫斜板
board.pos = vector(-L*cos(th)/2 - size*sin(th) , L*sin(th)/2-size*cos(th), 0)	#斜板的中心
board.axis=vector(-L*cos(th), L*sin(th),0)					#斜板的方向	
#1
ball = sphere(radius = size, color = color.red)			#球
ball.pos = vector(-L*cos(th), L*sin(th), 0)        	 	#球初始位置 
ball.v = vector(0.0, 0.0, 0.0)                      			#球初速            
#2
t=0
while ball.pos.x < 0.0 :
    rate(1000)
    t = t+dt						#時間每次增加量
    a = vector(g * sin(th) * cos(th), - g * sin (th) * sin(th), 0)          #加速度
    ball.v += a * dt                                            
    ball.pos += ball.v * dt                                       
print "時間=",t
#3
